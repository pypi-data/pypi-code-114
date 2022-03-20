import secrets
import signal

from witaker.clipboardserver import app, AuthorizedClipboardUtil
from witaker.clipboardserver.gui import ClipboardServerApp

def signal_handler(signal, frame):
    print(" CTRL + C detected, exiting ... ")
    exit(1)

def clipboard_server_gui_main():
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    import kivy
    kivy.require('1.8.0')


    secret_auth_key = secrets.token_hex()
    print(f" * Initializing with secret_auth_key: {secret_auth_key}")
    clipboard_util = AuthorizedClipboardUtil(secret_auth_key)
   
    app.config['clipboard_util'] = clipboard_util

    gui = ClipboardServerApp()
    gui.set_queue(clipboard_util.queue)
    gui.set_secret_auth_key(secret_auth_key)
    gui.set_clipboard_util(clipboard_util)
    gui.set_server_app(app)
    gui.run()
    return 0
