"""Unit tests for the IniParser class."""

import configparser
import logging
import os
import tempfile
from typing import Generator, Tuple

from _pytest.fixtures import SubRequest
import pytest

from pyvconf import IniParser

IniPath = str
SectionName = str
ItemName = str
ItemValue = str
Items = dict[ItemName, ItemValue]
IniDict = dict[SectionName, Items]
IniPathDictPair = Tuple[IniPath, IniDict]


class TestIniParser:
    """Encapsulates the unit tests for the IniParser class."""

    config_default = {
        "str_val": "1",
        "int_val": "1",
        "float_val": "1",
        "bool_val": "1",
    }
    config_section1 = {
        "str_val": "2",
        "float_val": "1.5",
    }

    @staticmethod
    @pytest.fixture(scope="class", autouse=True)
    def logger() -> Generator[logging.Logger, None, None]:
        """A debugging logger."""
        res = logging.getLogger(__name__)
        res.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(filename="pytest.log",
                                           encoding="utf-8")
        file_handler.setFormatter(logging.Formatter(
            "%(asctime)s %(levelname)s %(message)s"))
        res.addHandler(file_handler)
        res.debug("test started")
        yield res
        res.debug("test finished\n**********")

    @staticmethod
    @pytest.fixture(scope="class", params=[
        {
            "DEFAULT": {
                "str_val": "1",
                "int_val": "1",
                "float_val": "1",
                "bool_val": "1",
            },
            "section1": {
                "str_val": "2",
                "float_val": "1.5",
            },
        },
        {
            "DEFAULT": {
                "str_val": "2",
                "float_val": "1.5",
            },
            "section1": {
                "str_val": "1",
                "int_val": "1",
                "float_val": "1",
                "bool_val": "1",
            },
        },
        {
            "DEFAULT": {
                "str_val": "2",
                "float_val": "1.5",
            },
            "section1": {
                "str_val": "1",
                "int_val": "1",
                "float_val": "1",
                "bool_val": "1",
            },
            "section2": {
                "int_val": "1",
                "float_val": "1",
                "bool_val": "1",
            },
        },
    ])
    def ini_file(request: SubRequest,
                 logger: logging.Logger) -> Generator[IniPathDictPair,
                                                      None, None]:
        """Create an ini file and return its path."""
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as ini_fp:
            config = configparser.ConfigParser()
            for section, items in request.param.items():
                config[section] = items
            config.write(ini_fp)
        logger.debug(ini_fp.name)
        yield (ini_fp.name, request.param)
        os.remove(ini_fp.name)

    @staticmethod
    def test_parse(ini_file: IniPathDictPair, logger: logging.Logger) -> None:
        """Test parsing an INI file."""
        ini_path, ini_dict = ini_file
        parser = IniParser()
        parser.parse(ini_path)

        assert parser.sections.keys() == ini_dict.keys()

        default = ini_dict["DEFAULT"]
        for ini_section, ini_items in ini_dict.items():
            full_ini_items = {**default, **ini_items}
            parser_items = parser.sections[ini_section]
            logger.debug(ini_section)
            logger.debug("    ini_items     : %s", ini_items)
            logger.debug("    full_ini_items: %s", full_ini_items)
            logger.debug("    parser_items  : %s", dict(parser_items))
            assert parser_items == full_ini_items

