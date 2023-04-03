from aqt import mw
from aqt.qt import QAction

action = QAction("AnyToAnki Sync", mw)
# action.triggered.connect(on_sync_clicked)
mw.form.menuTools.addAction(action)
