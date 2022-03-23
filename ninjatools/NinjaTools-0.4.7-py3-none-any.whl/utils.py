import subprocess
import sys
from datetime import datetime
from math import sqrt
from time import perf_counter, sleep

import pkg_resources
import psutil
import pyperclip
import win32gui
import win32process

from ninja_tools.bbox import BBOX


class Utilities:
    ##########################
    # Import functions
    ##########################
    @staticmethod
    def try_import(package, installer=None):
        def check(_):
            return _ in [_.project_name for _ in pkg_resources.working_set]

        if not check(package):
            installer = package if not installer else installer
            install = subprocess.Popen([sys.executable, "-m", "pip", "install", installer])
            install.wait()

    ##########################
    # Clipboard Functions
    ##########################
    @staticmethod
    def put_on_clipboard(_):
        pyperclip.copy(_)

    @staticmethod
    def get_from_clipboard():
        return pyperclip.paste()

    ##########################
    # Math Functions
    ##########################
    @staticmethod
    def safe_div(x, y):
        return 0 if y == 0 else x / y

    def safe_div_round(self, x, y, decimals=2):
        return round(self.safe_div(x, y), decimals)

    @staticmethod
    def safe_div_int(x, y):
        return int(0 if y == 0 else x / y)

    @staticmethod
    def get_distance(p0, p1):
        return sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)

    ##########################
    # Process Functions
    ##########################
    @staticmethod
    def get_handle_from_title(window):
        return win32gui.FindWindow(None, window)

    @staticmethod
    def get_handle_from_pid(pid):
        def callback(hwnd, _):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)

            if found_pid == pid:
                _.append(hwnd)
            return True

        handle = []
        win32gui.EnumWindows(callback, handle)
        return handle

    @staticmethod
    def get_process_name_from_pid(pid):
        return psutil.Process(pid).name()

    def get_pid_from_title(self, window):
        handle = self.get_handle_from_title(window)
        _, found_pid = win32process.GetWindowThreadProcessId(handle)
        return found_pid

    @staticmethod
    def get_current_window_title():
        return win32gui.GetWindowText(win32gui.GetForegroundWindow())

    def is_current_window_title(self, window_name: str):
        return window_name == self.get_current_window_title()

    @staticmethod
    def _get_rect(type_, handle):
        if type_ == "WINDOW":
            return win32gui.GetWindowRect(handle)
        elif type_ == "CLIENT":
            return win32gui.GetClientRect(handle)
        else:
            raise 'Either type == WINDOW or CLIENT only!'

    def get_window_rect_from_handle(self, handle, bbox: bool = True):
        rect = self._get_rect("WINDOW", handle)
        return BBOX(rect) if bbox else rect

    def get_window_rect_from_pid(self, pid, bbox: bool = True):
        handle = self.get_handle_from_pid(pid)
        rect = self._get_rect("WINDOW", handle)
        return BBOX(rect) if bbox else rect

    def get_client_rect_from_handle(self, handle, bbox: bool = True):
        rect = self._get_rect("CLIENT", handle)
        return BBOX(rect) if bbox else rect

    def get_client_rect_from_pid(self, pid, bbox: bool = True):
        handle = self.get_handle_from_pid(pid)
        rect = self._get_rect("CLIENT", handle)
        return BBOX(rect) if bbox else rect

    ##########################
    # Utility Functions
    ##########################
    @staticmethod
    def pause(milliseconds: int):
        sleep(milliseconds * 0.001)

    @staticmethod
    def make_hash(d):
        __ = ''
        for _ in d:
            __ += str(d[_])
        return hash(__)

    @staticmethod
    def timestamp():
        (dt, micro) = datetime.utcnow().strftime('%Y%m%d-%H%M%S.%f').split('.')
        dt = "%s.%03d" % (dt, int(micro) * 0.001)
        return dt

    @staticmethod
    def datetime():
        return datetime.utcnow()

    @staticmethod
    def perf():
        return perf_counter()

    ##########################
    # I/O
    ##########################
    @staticmethod
    def write_to_file(filename, text, method: str = "a", add_new_line: bool = True):
        with open(filename, method) as file:
            if add_new_line:
                file.write(text + "\n")
            else:
                file.write(text)

    @staticmethod
    def read_file(filename, method="r"):
        return open(filename, method).read()

    @staticmethod
    def read_lines(filename, method="r"):
        return open(filename, method, encoding="utf8").readlines()

    ##########################
    # Assorted
    ##########################
    @staticmethod
    def cv2_show(cv2, image, window_name=None, delay=1, stop_key='q'):
        cv2.imshow(window_name, image)
        if cv2.waitKey(delay) & 0xFF == ord(stop_key):
            cv2.destroyAllWindows()
