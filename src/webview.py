from aqt import mw
from aqt.qt import *
from aqt import gui_hooks

def on_webview_will_set_content(web_content, context):
    if context["event"].lower() != "copy":
        return
    selected_text = context["selected_text"]
    if not selected_text:
        return
    web_content.html = selected_text.upper()

gui_hooks.webview_will_set_content.append(on_webview_will_set_content)

mw.addon_manager.register(__name__)
