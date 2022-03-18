r"""
**Async** version of iDAC SDK
"""

import platform
from idac_sdk._version import __version__ as version

system = platform.platform()
python = platform.python_implementation() + " " + platform.python_version()

DEFAULT_WAIT_TIMEOUT = 10 * 60  # 10 minutes
DEFAULT_WAIT_INTERVAL = 30  # 30 seconds
DEFAULT_USER_AGENT = f"iDAC SDK/{version} ({system}; {python})"
