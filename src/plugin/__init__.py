from aqt import mw
from aqt.qt import QAction, QMessageBox


def on_sync_clicked():
    try:
        1 / 0
    except Exception as e:
        QMessageBox.information(mw, "同步成功", str(e))


def main():
    action = QAction("AnyToAnki Sync", mw)
    action.triggered.connect(on_sync_clicked)
    mw.form.menuTools.addAction(action)


main()
