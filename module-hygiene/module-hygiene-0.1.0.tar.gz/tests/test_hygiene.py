import pytest

__author__ = "Joe Carpinelli"
__copyright__ = "Joe Carpinelli"
__license__ = "MIT"


def test_cleanup():
    """API Tests"""
    from hygiene import cleanup
    x = 1
    __export__ = [""]
    cleanup()
    assert "x" not in locals()
    assert "cleanup" not in locals()