__author__ = "Sebastian Stigler"
__copyright__ = "Copyright 2022, Sebastian Stigler"
__credits__ = []
__license__ = "MIT"
__version__ = "1.4.0"
__maintainer__ = "Sebastian Stigler"
__email__ = "sebastian.stigler@hs-aalen.de"
__status__ = "Production"

from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class Info:
    author: str = __author__
    copyright: str = __copyright__
    credits: List[str] = field(default_factory=lambda: __credits__)
    license: str = __license__
    version: str = __version__
    maintainer: str = __maintainer__
    email: str = __email__
    status: str = __status__
