"""
This program only controls the basic commands of the program's window.
Like starting, closing, and checking if it exists.
"""
from time import sleep
from pywinauto import keyboard, mouse
import win32clipboard
from subprocess import Popen
from pathlib import Path

from pkg_resources import resource_filename
from os import path

import requests


class Client:
    def __init__(self, url, key):
        self.url = url
        self.key = key
        self.resolved = False

    def authenticate(self):
        if not self.resolved:
            resp = requests.post(f"{self.url}/authenticate", params={"key": self.key})
            if resp.text != "success":
                raise Exception("Invalid url or key")
            self.resolved = True


class ApplicationDriver(Client):
    def __init__(self, url, key):
        Client.__init__(self, url, key)
        self.authenticate()
        self.__desktop = None
        self.__window = None
        self.pane = None
        self.ark_lnk_path = resource_filename(__name__, 'ark.lnk')
        self.ark_lnk = path.join(path.dirname(__file__), 'ark.lnk')

    def start(self):
        """ Starts the application by running the shortcut file. """
        if self.resolved:
            self.__assert_ark_link_exists()
            path = Path(self.ark_lnk_path)
            Popen(str(path), shell=True)
            self.__find_desktop_app()
            self.wait_exists()

    def __find_ark_pywinauto(self, desktop):
        self.__window = desktop.window(title="ARK: Survival Evolved")
        if self.resolved and self.exists():
            self.pane = self.__window['Pane2']
            self.window = self.__window
        else:
            raise LookupError("Application was unable to be located as a background process.")

    def __find_desktop_app(self):
        assert self.resolved, "You must authenticate the driver"
        from pywinauto import Desktop
        self.__desktop = Desktop(backend="uia")
        self.__find_ark_pywinauto(self.__desktop)  # also finds the ark app

    def __assert_ark_link_exists(self):
        assert self.resolved, "You must authenticate the driver"
        from pathlib import Path
        ark_path = Path(self.ark_lnk_path)
        if not ark_path.exists():
            raise FileNotFoundError("ark.lnk file is not found in the current directory")

    def exists(self, seconds=5):
        """ Checks if the program is currently running. Default times out at 5 seconds. """
        assert self.resolved, "You must authenticate the driver"
        return self.__window.exists(seconds)

    def close(self):
        """ Closes the application """
        assert self.resolved, "You must authenticate the driver"
        if self.exists():
            self.__window.close()

    def wait_exists(self):
        """ halts the program until the ark starts. """
        assert self.resolved, "You must authenticate the driver"
        self.__window.wait('exists')

    def wait_visible(self):
        """ halts the program until the ark is on screen (e.g. not minimized) """
        assert self.resolved, "You must authenticate the driver"
        self.__window.wait('visible')

    def wait_active(self):
        """ Halts the program until ark is the main focus """
        assert self.resolved, "You must authenticate the driver"
        self.__window.wait('active')

    def minimize(self):
        """ Minimizes the window. """
        assert self.resolved, "You must authenticate the driver"
        self.__window.minimize()

    def maximize(self):
        """ Maximizes the window. """
        assert self.resolved, "You must authenticate the driver"
        self.__window.maximize()

    def set_focus(self):
        """
        Makes this window the current focus/active window
        """
        assert self.resolved, "You must authenticate the driver"
        self.__window.set_focus()

    def __get_monitor_size(self):
        """ Returns width, height of monitor resolution """
        assert self.resolved, "You must authenticate the driver"
        from win32api import GetSystemMetrics
        return GetSystemMetrics(0), GetSystemMetrics(1)

    def __window_pane_offset(self):
        """
        Absolute differences between the whole window and the pane.
        :return: the absolute difference
        """
        assert self.resolved, "You must authenticate the driver"
        window_rect = self.__window.rectangle()
        pane_rect = self.pane.rectangle()
        top = abs(window_rect.top - pane_rect.top)
        left = abs(window_rect.left - pane_rect.left)
        bottom = abs(window_rect.bottom - pane_rect.bottom)
        right = abs(window_rect.right - pane_rect.right)
        return left, top, right, bottom

    def resize_pane(self, width=1016, height=563):
        """
        Resizes the window by desired pane size
        :param width: size in pixels
        :param height: size in pixels
        """
        assert self.resolved, "You must authenticate the driver"
        o_left, o_top, o_right, o_bottom = self.__window_pane_offset()
        self.resize_window(width + o_left + o_right, height + o_top + o_bottom)
        # TODO: assert it has been resized

    def move_window(self, left, top):
        """ Moves the window to a new position as the top left corner being the origin """
        assert self.resolved, "You must authenticate the driver"
        self.set_focus()
        dialog_rect = self.__window['Dialog'].rectangle()
        dialog_left = dialog_rect.left + (dialog_rect.width() // 2)
        dialog_top = dialog_rect.top + (dialog_rect.height() // 2)
        self.drag((dialog_left, dialog_top), (left, top))
        # TODO: assert the window has been moved (e.g. program interruption)

    def has_keyboard_focus(self):
        # will have to use AI to figure this out
        assert self.resolved, "You must authenticate the driver"

    def double_click_dialog(self):
        assert self.resolved, "You must authenticate the driver"
        self.__window['Dialog'].double_click_input()

    def send_keys(self, string):
        assert self.resolved, "You must authenticate the driver"
        self.set_focus()
        sleep(2)
        for c in string:
            if c == " ":
                keyboard.send_keys("{SPACE down}", pause=0.2)
                keyboard.send_keys("{SPACE up}", pause=0.2)
            elif c == "_":
                #keyboard.send_keys("{VK_SHIFT down}", pause=0.5)
                keyboard.send_keys("_", pause=0.5)
                #keyboard.send_keys("{VK_SHIFT up}", pause=0.5)
            else:
                keyboard.send_keys("{" + "{}".format(c) + " down}", pause=0.2)
                keyboard.send_keys("{" + "{}".format(c) + " up}", pause=0.2)

    def sides(self, pywin_obj):
        """ Gets the left, top, right, and bottom coordinates of a window/pane """
        assert self.resolved, "You must authenticate the driver"
        rect = pywin_obj.rectangle()
        return rect.left, rect.top, rect.right, rect.bottom

    def send_keys_tab(self):
        assert self.resolved, "You must authenticate the driver"
        rect = self.window.rectangle()
        return rect.width(), rect.height

    def send_keys_tabs(self):
        assert self.resolved, "You must authenticate the driver"
        rect = self.pane.rectangle()
        return rect.width(), rect.height()

    def send_key_tabs(self):
        assert self.resolved, "You must authenticate the driver"
        return self.__window.wrapper_object()

    def sends_keys_tabs(self):
        assert self.resolved, "You must authenticate the driver"
        return self.pane.wrapper_object()

    def sends_key_tab(self, pane_coords):
        assert self.resolved, "You must authenticate the driver"
        left, top, right, bottom = self.sides(self.pane)
        return left + pane_coords[0], top + pane_coords[1]

    def send_key_tab(self):
        assert self.resolved, "You must authenticate the driver"
        sleep(0.3)
        keyboard.send_keys("{TAB down}")
        sleep(0.5)
        keyboard.send_keys("{TAB up}")
        sleep(0.5)

    def send_keys_enter(self):
        assert self.resolved, "You must authenticate the driver"
        rect = self.window.rectangle()
        return rect.width(), rect.height

    def send_keys_enters(self):
        assert self.resolved, "You must authenticate the driver"
        rect = self.pane.rectangle()
        return rect.width(), rect.height()

    def send_key_enters(self):
        assert self.resolved, "You must authenticate the driver"
        return self.__window.wrapper_object()

    def sends_keys_enters(self):
        assert self.resolved, "You must authenticate the driver"
        return self.pane.wrapper_object()

    def sends_key_enter(self, pane_coords):
        assert self.resolved, "You must authenticate the driver"
        left, top, right, bottom = self.sides(self.pane)
        return left + pane_coords[0], top + pane_coords[1]

    def send_key_enter(self):
        assert self.resolved, "You must authenticate the driver"
        sleep(0.3)
        keyboard.send_keys("{ENTER down}")
        sleep(0.5)
        keyboard.send_keys("{ENTER up}")
        sleep(0.5)

    def send_keys_copy(self):
        assert self.resolved, "You must authenticate the driver"
        rect = self.window.rectangle()
        return rect.width(), rect.height

    def send_keys_copys(self):
        assert self.resolved, "You must authenticate the driver"
        rect = self.pane.rectangle()
        return rect.width(), rect.height()

    def send_key_copys(self):
        assert self.resolved, "You must authenticate the driver"
        return self.__window.wrapper_object()

    def sends_keys_copys(self):
        assert self.resolved, "You must authenticate the driver"
        return self.pane.wrapper_object()

    def sends_key_copy(self, pane_coords):
        assert self.resolved, "You must authenticate the driver"
        left, top, right, bottom = self.sides(self.pane)
        return left + pane_coords[0], top + pane_coords[1]

    def send_key_copy(self):
        assert self.resolved, "You must authenticate the driver"
        sleep(0.3)
        keyboard.send_keys("{VK_CONTROL down}", pause=0.5)
        sleep(0.3)
        keyboard.send_keys("{c down}", pause=0.5)
        sleep(0.3)
        keyboard.send_keys("{VK_CONTROL up}", pause=0.5)
        sleep(0.3)
        keyboard.send_keys("{c up}", pause=0.5)
        sleep(0.3)

    def send_keys_paste(self):
        assert self.resolved, "You must authenticate the driver"
        rect = self.window.rectangle()
        return rect.width(), rect.height

    def send_keys_pastes(self):
        assert self.resolved, "You must authenticate the driver"
        rect = self.pane.rectangle()
        return rect.width(), rect.height()

    def send_key_pastes(self):
        assert self.resolved, "You must authenticate the driver"
        return self.__window.wrapper_object()

    def sends_keys_pastes(self):
        assert self.resolved, "You must authenticate the driver"
        return self.pane.wrapper_object()

    def sends_key_paste(self, pane_coords):
        assert self.resolved, "You must authenticate the driver"
        left, top, right, bottom = self.sides(self.pane)
        return left + pane_coords[0], top + pane_coords[1]

    def send_key_paste(self):
        assert self.resolved, "You must authenticate the driver"
        sleep(0.3)
        keyboard.send_keys("{VK_CONTROL down}")
        sleep(0.3)
        keyboard.send_keys("{v down}")
        sleep(0.3)
        keyboard.send_keys("{VK_CONTROL up}")
        sleep(0.3)
        keyboard.send_keys("{v up}")
        sleep(0.3)

    def send_keys_ctrl_n(self):
        assert self.resolved, "You must authenticate the driver"
        rect = self.window.rectangle()
        return rect.width(), rect.height

    def send_keys_ctrl_ns(self):
        assert self.resolved, "You must authenticate the driver"
        rect = self.pane.rectangle()
        return rect.width(), rect.height()

    def send_key_ctrl_ns(self):
        assert self.resolved, "You must authenticate the driver"
        return self.__window.wrapper_object()

    def sends_keys_ctrl_n(self):
        assert self.resolved, "You must authenticate the driver"
        return self.pane.wrapper_object()

    def sends_key_ctrl_n(self, pane_coords):
        assert self.resolved, "You must authenticate the driver"
        left, top, right, bottom = self.sides(self.pane)
        return left + pane_coords[0], top + pane_coords[1]

    def send_key_ctrl_n(self):
        assert self.resolved, "You must authenticate the driver"
        keyboard.send_keys("{VK_CONTROL down}")
        sleep(0.3)
        keyboard.send_keys("{n down}")
        sleep(0.3)
        keyboard.send_keys("{VK_CONTROL up}")
        sleep(0.3)
        keyboard.send_keys("{n up}")
        sleep(0.3)

    def save_to_clipboard_texts(self):
        assert self.resolved, "You must authenticate the driver"
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()

    def save_to_clipboards_texts(self):
        assert self.resolved, "You must authenticate the driver"
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()

    def saves_to_clipboards_texts(self, string):
        assert self.resolved, "You must authenticate the driver"
        win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, string)

    def saves_to_clipboard_text(self, string):
        assert self.resolved, "You must authenticate the driver"
        win32clipboard.OpenClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, string)

    def saves_to_clipboards_text(self, string):
        assert self.resolved, "You must authenticate the driver"
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()

    def save_to_clipboard_text(self, string):
        assert self.resolved, "You must authenticate the driver"
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, string)
        # Alternate version if above fails
        # win32clipboard.SetClipboardText(string)
        win32clipboard.CloseClipboard()

    def get_from_clipboards(self):
        assert self.resolved, "You must authenticate the driver"
        win32clipboard.OpenClipboard()
        return win32clipboard.EmptyClipboard()

    def gets_from_clipboards(self):
        assert self.resolved, "You must authenticate the driver"
        win32clipboard.OpenClipboard()
        data = win32clipboard
        return data

    def get_from_clipboard(self):
        assert self.resolved, "You must authenticate the driver"
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return data

    def __del__(self):
        """ Close the application when the program finishes """
        assert self.resolved, "You must authenticate the driver"
        # self.close()

    def sides(self, pywin_obj):
        """ Gets the left, top, right, and bottom coordinates of a window/pane """
        assert self.resolved, "You must authenticate the driver"
        rect = pywin_obj.rectangle()
        return rect.left, rect.top, rect.right, rect.bottom

    def window_size(self):
        assert self.resolved, "You must authenticate the driver"
        rect = self.window.rectangle()
        return rect.width(), rect.height

    def pane_size(self):
        assert self.resolved, "You must authenticate the driver"
        rect = self.pane.rectangle()
        return rect.width(), rect.height()

    def window_wrapper(self):
        assert self.resolved, "You must authenticate the driver"
        return self.__window.wrapper_object()

    def pane_wrapper(self):
        assert self.resolved, "You must authenticate the driver"
        return self.pane.wrapper_object()

    def absolute_pane_coords(self, pane_coords):
        assert self.resolved, "You must authenticate the driver"
        left, top, right, bottom = self.sides(self.pane)
        return left + pane_coords[0], top + pane_coords[1]
