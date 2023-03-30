
# 导入必要的模块
from aqt import mw  # 从 aqt 模块导入 mw 对象，用于访问 Anki 主窗口
from aqt.qt import *  # 导入 PyQt 库，用于创建用户界面
from anki.notes import Note
from aqt.deckbrowser import DeckBrowser
 
def create_note_type():
    model_name = "MyModel"
    model_fields = [
        {"name": "Front"},
        {"name": "Back"},
        {"name": "Option1"},
        {"name": "Option2"},
        {"name": "Option3"},
        {"name": "Option4"},
        {"name": "Answer"},
    ]
    model_templates = [
        {
            "name": "MyModel",
            "qfmt": "{{Front}}<br>{{Option1}}<br>{{Option2}}<br>{{Option3}}<br>{{Option4}}",
            "afmt": "{{Front}}<br>{{Answer}}"
        }
    ]

    note_type = mw.col.models.new(model_name)
    for field in model_fields:
        mw.col.models.addField(note_type, mw.col.models.newField(**field))
    for template in model_templates:
        temp = mw.col.models.newTemplate(template["name"])
        temp["qfmt"] = template["qfmt"]
        temp["afmt"] = template["afmt"]
        mw.col.models.addTemplate(note_type, temp)

    mw.col.models.add(note_type)

def create_deck():
    # 获取当前打开集合
    collection = mw.col

    # 创建新的牌组
    deck_name = "My Deck"
    model_name = "Basic"

    # 获取笔记类型对象
    note_type = collection.models.byName(model_name)

    deck = collection.decks.id(deck_name)

    foundNoteId = collection.find_notes("\"deck:My Deck\" \"Front:Front content\"")
    if len(foundNoteId) == 1:
        foundNote = collection.getNote(foundNoteId[0])
        foundNote["Front"] = "New Front Note Content"
        foundNote.flush()
    else:
        # 创建新的笔记对象
        note = Note(col=collection, model=note_type)
        note["Front"] = "Front content"
        note["Back"] = "Back content"

        # 添加新的笔记到牌组中
        collection.add_note(note, deck)

    # 保存集合
    collection.save()

    # 刷新牌组页面
    deck_browser = DeckBrowser(mw)
    deck_browser.refresh()


# 定义一个处理“同步”按钮点击事件的函数
def on_sync_clicked():
    # result = create_deck()
    result = create_note_type()
    QMessageBox.information(mw, "同步成功", "同步成功！" + str(result))
    # 弹出消息框，显示“同步成功”的消息。mw 作为父窗口显示消息框，确保消息框显示在 Anki 应用程序中。

def init():
    action = QAction("AnyToAnki Sync", mw)
    action.triggered.connect(on_sync_clicked)
    mw.form.menuTools.addAction(action)
    
    

