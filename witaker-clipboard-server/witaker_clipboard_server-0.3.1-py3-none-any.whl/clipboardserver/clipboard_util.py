import multiprocessing
import xerox
from colorama import Fore

class AuthorizedClipboardUtilException(Exception):
    def __init__(self, message):
        super().__init__(message)

class AuthorizedClipboardUtil:

    def __init__(self, session_key):
        self.session_key = session_key
        self.queue = multiprocessing.Queue()

    def copy_text_to_clipboard(self, auth_key, text):
        if (auth_key == self.session_key):
            xerox.copy(text)
            self.queue.put(text)
        else:
            raise AuthorizedClipboardUtilException(f"Cannot copy text '{text}' to clipboard; auth key '{auth_key}' is invalid")


    def paste_text_from_clipboard(self, auth_key):
        if (auth_key == self.session_key):
            return xerox.paste()
        else:
            raise AuthorizedClipboardUtilException(f"Cannot paste text from clipboard; auth key '{auth_key}' is invalid")


    def auth_key_matches(self, auth_key):
        return auth_key == self.session_key


def get_auth_marker(server_port, auth_key):
    return f"witaker:clipboard-server[port={server_port};auth-key='{auth_key}']"

def get_auth_marker_color(server_port, auth_key):
    return get_auth_marker(f"{Fore.CYAN}{server_port}{Fore.RESET}", f"{Fore.GREEN}{auth_key}{Fore.RESET}")
