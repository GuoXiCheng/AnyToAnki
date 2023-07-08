# from aqt import mw
# from aqt.qt import QAction, QMessageBox
# import json, os


# def create_note_type():
#     path = os.path.join(os.path.dirname(__file__), "note-type/default.json")
#     with open(path, "r") as f:
#         json_str = f.read()

#     json_obj = json.loads(json_str)
#     model_name = json_obj["model_name"]
#     model_fields = json_obj["model_fields"]
#     model_templates = json_obj["model_templates"]

#     note_type = mw.col.models.new(model_name)
#     for field in model_fields:
#         mw.col.models.addField(note_type, mw.col.models.newField(**field))
#     for template in model_templates:
#         temp = mw.col.models.newTemplate(template["name"])
#         temp["qfmt"] = template["qfmt"]
#         temp["afmt"] = template["afmt"]
#         mw.col.models.addTemplate(note_type, temp)

#     mw.col.models.add(note_type)


# def on_sync_clicked():
#     try:
#         create_note_type()
#         QMessageBox.information(mw, "同步成功", "同步笔记成功!")
#     except Exception as e:
#         QMessageBox.information(mw, "同步失败", str(e))


# def main():
#     action = QAction("AnyToAnki Sync", mw)
#     action.triggered.connect(on_sync_clicked)
#     mw.form.menuTools.addAction(action)


# main()


import json
import os

from .utils import read_from_file


try:
    from aqt import mw
    from aqt.qt import QAction, QMessageBox

    def add_note_with_template(deck_name: str, note_type_name: str):
        # 获取默认牌组
        deck = mw.col.decks.byName(deck_name)

        # 打开一个笔记模板
        note_type = mw.col.models.byName(note_type_name)

        # 设置当前笔记模板
        mw.col.models.set_current(note_type)

        # 从笔记模板创建笔记
        note = mw.col.newNote()

        # 设置笔记内容
        note.fields[0] = "Front"  
        note.fields[1] = "Back"   
        
        # 将笔记添加到牌组
        mw.col.add_note(note, deck_id=deck['id'])



    def update_or_create_note_type():
        path = os.path.join(
            os.path.dirname(__file__), "note-type/choice-question/config.json"
        )
        json_config = json.loads(read_from_file(path))
        model_name = json_config["model_name"]
        model_fields = json_config["model_fields"]

        note_type = mw.col.models.by_name(model_name)

        qfmt_template = read_from_file("note-type/choice-question/front.html")
        afmt_template = read_from_file("note-type/choice-question/backend.html")
        css_template = read_from_file("note-type/choice-question/style.css")

        if note_type is None:
            note_type = mw.col.models.new(model_name)
            for field in model_fields:
                mw.col.models.addField(note_type, mw.col.models.newField(**field))

            temp = mw.col.models.newTemplate(model_name)
            temp["qfmt"] = qfmt_template
            temp["afmt"] = afmt_template
            mw.col.models.addTemplate(note_type, temp)
            mw.col.models.add(note_type)

        note_type["css"] = css_template

        tmpl = note_type["tmpls"][0]
        tmpl["qfmt"] = qfmt_template
        tmpl["afmt"] = afmt_template
        mw.col.models.save(note_type)
        

    def on_sync_clicked():
        try:
            update_or_create_note_type()
            QMessageBox.information(mw, "同步成功", f"同步笔记成功!")
        except Exception as e:
            QMessageBox.information(mw, "同步失败", str(e))

    action = QAction("AnyToAnki Sync", mw)
    action.triggered.connect(on_sync_clicked)
    mw.form.menuTools.addAction(action)
except:
    print("失败")
