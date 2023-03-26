
# 导入必要的模块
from aqt import mw  # 从 aqt 模块导入 mw 对象，用于访问 Anki 主窗口
from aqt.qt import *  # 导入 PyQt 库，用于创建用户界面

# 定义一个处理“同步”按钮点击事件的函数
def on_sync_clicked():
    QMessageBox.information(mw, "同步成功", "同步成功！")
    # 弹出消息框，显示“同步成功”的消息。mw 作为父窗口显示消息框，确保消息框显示在 Anki 应用程序中。

def init():
    action = QAction("同步", mw)
    action.triggered.connect(on_sync_clicked)
    mw.form.menuTools.addAction(action)
    
    

