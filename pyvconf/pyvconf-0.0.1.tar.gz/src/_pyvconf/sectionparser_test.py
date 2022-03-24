"""Unit tests for the SectionParser abstract class."""

# pylint: disable=abstract-class-instantiated
# pylint: disable=too-few-public-methods

import pytest

from pyvconf import SectionParser


class TestSectionParser:
    """Encapsulates the unit tests for the SectionParser class."""

    @staticmethod
    def test_instantiation_fails() -> None:
        """Test can't instantiate abstract base class."""
        with pytest.raises(TypeError) as excinfo:
            SectionParser()  # type: ignore
        assert "Can't instantiate abstract class" in str(excinfo.value)

