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
