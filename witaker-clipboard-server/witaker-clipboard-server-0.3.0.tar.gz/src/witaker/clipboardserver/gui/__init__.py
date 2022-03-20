import os
# disable Kivy's argument parser, must be set before kivy is imported
os.environ["KIVY_NO_ARGS"]= "1"

import kivy
kivy.require("1.8.0")


from witaker.clipboardserver.gui.clipboard_server_app import ClipboardServerApp
from witaker.clipboardserver.gui.clipboard_server_main import clipboard_server_gui_main
