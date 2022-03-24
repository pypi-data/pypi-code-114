"""Unit tests for the Parser abstract class."""

# pylint: disable=abstract-class-instantiated
# pylint: disable=too-few-public-methods

import pytest

from pyvconf import Parser


class TestParser:
    """Encapsulates the unit tests for the Parser class."""

    @staticmethod
    def test_instantiation_fails() -> None:
        """Test can't instantiate abstract base class."""
        with pytest.raises(TypeError) as excinfo:
            Parser()  # type: ignore
        assert "Can't instantiate abstract class" in str(excinfo.value)

