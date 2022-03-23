import os
import platform

platform_system = platform.system()
is_windows = os.name == 'nt' or (platform_system.lower() == 'windows' or platform_system.lower().find('cygwin') >= 0)

# disable Kivy's argument parser, must be set before kivy is imported
os.environ["KIVY_NO_ARGS"]= "1"
if is_windows:
    print(f" * Windows detected ({platform_system}), using KIVY OpenGL workaround")
    os.environ["KIVY_GL_BACKEND"]= "angle_sdl2"

import kivy
kivy.require("1.8.0")

if is_windows:
    from kivy import Config
    Config.set("graphics", "multisamples", "0")


from witaker.clipboardserver.gui.clipboard_server_app import ClipboardServerApp
from witaker.clipboardserver.gui.clipboard_server_main import clipboard_server_gui_main
