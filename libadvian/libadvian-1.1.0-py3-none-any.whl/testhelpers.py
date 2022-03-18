"""Some common helpers for testing"""
from typing import Generator
import platform
import tempfile

import pytest


@pytest.fixture
def nice_tmpdir() -> Generator[str, None, None]:
    """Return sane tmp path on OSX too"""
    tempdir = "/tmp" if platform.system() == "Darwin" else tempfile.gettempdir()  # nosec
    with tempfile.TemporaryDirectory(dir=tempdir) as tmpdir:
        yield str(tmpdir)
