# -*- coding: utf-8 -*-

"""
Tanzanite utility functions.
"""


# pylint: disable=consider-using-f-string


# Standard imports
import argparse
import logging
import os
import platform
# >> Issue: [B404:blacklist] Consider possible security implications associated
#           with the subprocess module.
#    Severity: Low   Confidence: High
#    CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
#    Location: tanzanite/utils/__init__.py:16:0
#    More Info: https://bandit.readthedocs.io/en/1.7.4/blacklists/blacklist_imports.html#b404-import-subprocess  # noqa
import subprocess  # nosec B404
import sys
import webbrowser

from contextlib import contextmanager
from pathlib import Path
from pydantic import (  # pylint: disable=no-name-in-module
    AnyHttpUrl,
)

# External imports
# TODO(dittrich): https://github.com/Mckinsey666/bullet/issues/2
# Workaround until bullet has fix for Windows missing 'termios'.
try:
    from bullet import (
        Password,
        Input,
        colors,
    )
except ModuleNotFoundError:
    pass

# Local imports
from tanzanite import (
    DEFAULT_API_VER,
    LOCALHOST,
    SERVER_NAME,
    SERVER_PORT,
    TANZANITE_BASE_DIR,
    __version__
)


BROWSER = os.getenv('BROWSER', None)
# Use syslog for logging?
# TODO(dittrich): Make this configurable, since it can fail on Mac OS X
SYSLOG = False
USERNAME_PROMPT = 'Username (use email address)'


class CustomFormatter(
    argparse.RawDescriptionHelpFormatter,
    argparse.ArgumentDefaultsHelpFormatter,
):
    """
    Custom class to control arparse help output formatting.
    """


# TODO(dittrich): Generalize this as soon as possible for other browsers.
_platform = platform.system()
if _platform == 'Darwin':
    chrome_path = r'open -a /Applications/Google\ Chrome.app %s'
elif _platform == "Linux":
    chrome_path = '/usr/bin/google-chrome %s'
elif _platform == "Windows":
    chrome_path = (
        r'C:/Program Files\ (x86)/Google'
        '/Chrome/Application/chrome.exe %s'
    )

logger = logging.getLogger(__name__)


def check_update(
    parsed_args: argparse.Namespace,
    updates: dict,
    arg_to_attribute: dict,
):
    """
    Check to see if any command line arguments map to attributes that can
    be changed. If they differ, change them.

    Returns a boolean reflecting whether any changes were made.
    """
    changed = False
    parsed_args_dict = {
        item: parsed_args.__dict__.get(item)
        for item in dir(parsed_args)
        if (
            item in arg_to_attribute
            and parsed_args.__dict__.get(item) is not None
        )
    }
    for arg_str, arg_val in parsed_args_dict.items():
        attribute_str = arg_to_attribute.get(arg_str)
        attribute_val = updates.get(attribute_str)
        if attribute_val in [None, arg_val]:
            continue
        updates[attribute_str] = arg_val
        changed = True
    return changed


def elapsed(start, end):
    """Return elapsed time string."""
    assert isinstance(start, float)
    assert isinstance(end, float)
    assert start >= 0.0
    assert start <= end
    hours, rem = divmod(end - start, 3600)
    minutes, seconds = divmod(rem, 60)
    return "{:0>2}:{:0>2}:{:05.2f}".format(
        int(hours), int(minutes), seconds)


def get_shell_login(username=None):
    """Return a shortened *nix-like login name."""
    if username is None or '@' not in username:
        return None
    login_portion = username.split('@')[0]
    return login_portion


def add_browser_options(parser):
    """Add web browser options."""
    parser.add_argument(
        '--browser',
        action='store',
        dest='browser',
        # default=BROWSER,
        default=None,
        help='Browser to use for viewing'
    )
    parser.add_argument(
        '--force',
        action='store_true',
        dest='force',
        default=False,
        help='Open the browser even if process has no TTY'
    )
    return parser


# Moved prompt_for_login_creds() to `tanzanite.core.security`


def prompt_for_input(prompt: str = None) -> str:
    """
    Uses Bullet to prompt user for string input.
    """
    if prompt is None:
        prompt = "Enter a value"
    cli = Input(
        default=' ',
        prompt=f"{str(prompt).capitalize()}: ",
        word_color=colors.foreground["yellow"],
        strip=True,
    )
    response = cli.launch()
    return response


def prompt_for_password(prompt: str = None) -> str:
    """
    Uses Bullet to prompt user for a password.
    """
    if prompt is None:
        prompt = "Password: "
    cli = Password(
        prompt=prompt,
        hidden="*",
        word_color=colors.foreground["yellow"]
    )
    password = cli.launch()
    return password


def get_base_url(
    proto=None,
    host=SERVER_NAME,
    port=SERVER_PORT,
):
    """
    Return the base URL for accessing general Tanzanite server paths.
    """
    if proto is None:
        proto = "http" if host in LOCALHOST else "https"
    if port not in [None, '80']:
        host = ":".join([host, port])
    return f"{proto}://{host}"


def get_api_base_url(
    proto=None,
    host=SERVER_NAME,
    port=SERVER_PORT,
    api_ver=DEFAULT_API_VER
) -> AnyHttpUrl:
    """
    Return the base URL for accessing Tanzanite API endpoints.
    """
    base_url = get_base_url(
        proto=proto,
        host=host,
        port=port
    )
    return f"{base_url}/api/{api_ver}"


def get_version(default=__version__) -> str:
    """
    Return the version number produced by `poetry version` for consistency.
    """
    dev_version = Path(TANZANITE_BASE_DIR).parent / 'VERSION.dev'
    if dev_version.exists():
        return dev_version.read_text().strip()
    return default


def open_browser(url=None, browser=None, force=False):
    """
    Open web browser to page.
    """
    if not sys.stdin.isatty() and not force:
        raise RuntimeError(
            "[-] use --force to open browser when stdin is not a TTY"
        )
    if url is None:
        url = get_base_url()
        # raise RuntimeError("[-] no url specified")
    in_browser = f" in {browser}" if browser is not None else ""
    logger.info('[+] opening URL %s%s', url, in_browser)
    if browser is not None:
        webbrowser.get(browser).open_new_tab(url)
    else:
        webbrowser.open(url, new=1)


@contextmanager
def set_directory(path: Path):
    """
    Sets the cwd within the context

    https://dev.to/teckert/changing-directory-with-a-python-context-manager-2bj8

    Args:
        path (Path): The path to the cwd

    Yields:
        None
    """

    origin = Path().absolute()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(origin)


# >> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check
#           for execution of untrusted input.
#    Severity: Low   Confidence: High
#    CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
#    Location: tanzanite/utils/__init__.py:268:24
#    More Info: https://bandit.readthedocs.io/en/1.7.4/plugins/b603_subprocess_without_shell_equals_true.html  # noqa
def run(*args, **kwargs) -> subprocess.CompletedProcess:
    completed_process = subprocess.run(  # nosec B603
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        **kwargs,
    )
    if completed_process.returncode != 0:
        raise RuntimeError(
            'subprocess failed: '
            f"return_code={completed_process.returncode}"
            f"stdout={completed_process.stdout.decode()}"
        )
    return completed_process


# TODO(dittrich): Import from psec (once circular import issue fixed)
# class Timer(object):
#     """
#     Timer object usable as a context manager, or for manual timing.
#     Based on code from http://coreygoldberg.blogspot.com/
#                        2012/06/python-timer-class-context-manager-for.html

#     As a context manager, do::
#         from timer import Timer

#         url = 'https://github.com/timeline.json'
#         with Timer() as t:
#             r = requests.get(url)
#         print 'fetched %r in %.2f millisecs' % (url, t.elapsed*1000)

#     """

#     def __init__(self, task_description='elapsed time', verbose=False):
#         self.verbose = verbose
#         self.task_description = task_description
#         self.laps = OrderedDict()

#     def __enter__(self):
#         """Record initial time."""
#         self.start(lap="__enter__")
#         if self.verbose:
#             sys.stdout.write(f'{self.task_description}...')
#             sys.stdout.flush()
#         return self

#     def __exit__(self, *args):
#         """Record final time."""
#         self.stop()
#         backspace = '\b\b\b'
#         if self.verbose:
#             sys.stdout.flush()
#             if self.elapsed_raw() < 1.0:
#                 sys.stdout.write(backspace + ':' + '{:.2f}ms\n'.format(
#                     self.elapsed_raw() * 1000))
#             else:
#                 sys.stdout.write(backspace + ': ' + '{}\n'.format(
#                     self.elapsed()))
#             sys.stdout.flush()

#     def start(self, lap=None):
#         """Record starting time."""
#         t = time.time()
#         first = None if len(self.laps) == 0 \
#             else self.laps.iteritems().next()[0]
#         if first is None:
#             self.laps["__enter__"] = t
#         if lap is not None:
#             self.laps[lap] = t
#         return t

#     def lap(self, lap="__lap__"):
#         """
#         Records a lap time.
#         If no lap label is specified, a single 'last lap' counter will be
#         (re)used. To keep track of more laps, provide labels yourself.
#         """
#         t = time.time()
#         self.laps[lap] = t
#         return t

#     def stop(self):
#         """Record stop time."""
#         return self.lap(lap="__exit__")

#     def get_lap(self, lap="__exit__"):
#         """Get the timer for label specified by 'lap'"""
#         return self.lap.get(lap)

#     def elapsed_raw(self, start="__enter__", end="__exit__"):
#         """Return the elapsed time as a raw value."""
#         return self.laps.get(end) - self.laps.get(start)

#     def elapsed(self, start="__enter__", end="__exit__"):
#         """
#         Return a formatted string with elapsed time between 'start'
#         and 'end' kwargs (if specified) in HH:MM:SS.SS format.
#         """
#         hours, rem = divmod(self.elapsed_raw(start, end), 3600)
#         minutes, seconds = divmod(rem, 60)
#         return "{:0>2}:{:0>2}:{:05.2f}".format(
#             int(hours), int(minutes), seconds)


# vim: set ts=4 sw=4 tw=0 et :
