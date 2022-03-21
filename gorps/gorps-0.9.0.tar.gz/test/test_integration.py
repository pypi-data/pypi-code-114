import unittest
from unittest import mock
import os
import shlex
from io import StringIO, BytesIO
from contextlib import contextmanager
from typing import Union, Optional, IO, Any, Iterable
from collections.abc import Iterator, Callable, Mapping
import difflib
import logging
from xml.etree.ElementTree import canonicalize as etree_canonicalize
import sqlite3
import re

from gorps.__main__ import main
from gorps.exporters.templating import load_text_file
from gorps.exporters.openrecipes import unique_in_order
from . import BASE_DIR, outputs as out

README = load_text_file(os.path.join(BASE_DIR, "README.md"))


class IntegrationTest:
    """Base class for integration tests"""

    cmd: str
    check_readme: bool = True
    expected_outputs: Mapping[str, Union[str, bytes]]

    def test_readme(self) -> None:
        if not self.check_readme:
            return
        code_block = f"""
```sh
{self.cmd}
```
"""
        if not code_block in README:
            raise AssertionError("Code block not found in README.md")

    @staticmethod
    def setUp() -> None:
        os.chdir(os.path.join(os.path.dirname(__file__), ".."))

    def run_cmd(self, cmd: Optional[str] = None) -> None:
        if cmd is None:
            cmd = self.cmd
        main(
            shlex.split(cmd.replace(" \\\n", ""))[1:],
            log_level=logging.WARNING,
        )


class TestSVG(unittest.TestCase, IntegrationTest):
    cmd = "gorps export --template=examples/svg/template.svg -o /tmp/out.svg examples/recipes/"

    expected_outputs = {"/tmp/out-00.svg": out.svg}

    def test_command(self) -> None:
        with intercept_outputs() as outputs:
            self.run_cmd()
        assert_text_collection_equal(outputs, self.expected_outputs)


class TestXml(unittest.TestCase, IntegrationTest):
    cmd = """gorps export \\
  --template examples/menu-card/xml-fo/template.fo.xml \\
  --group-by 'tags["category"]' \\
  --group Starters \\
  --group "Main courses" \\
  --group Dessert \\
  --variable-file examples/menu-card/xml-fo/variables.json \\
  --title "Beans with Bacon a la Bud Spencer" \\
  --title "More Beans" \\
  -o /tmp/menucard.fo.xml \\
  examples/recipes/"""

    expected_outputs = {"/tmp/menucard.fo.xml": out.fo_xml}

    def test_command(self) -> None:
        with intercept_outputs() as outputs:
            self.run_cmd()
        assert_text_collection_equal(
            outputs, self.expected_outputs, canonicalize=xml_canonicalize
        )


class TestHtml(unittest.TestCase, IntegrationTest):
    cmd = """gorps export \\
  --template examples/html/template.html \\
  -o /tmp/beans.html \\
  examples/recipes/beans.yml"""

    expected_outputs = {"/tmp/beans.html": out.html_beans}

    def test_command(self) -> None:
        with intercept_outputs() as outputs:
            self.run_cmd()
        assert_text_collection_equal(outputs, self.expected_outputs)


class TestHtmlMenucard(unittest.TestCase, IntegrationTest):
    cmd = """gorps export \\
  --template examples/menu-card/html/menucard.template.html \\
  -V title="Beans & Beans" \\
  --filter-ingredient Salt \\
  --filter-ingredient Pepper \\
  --grouped-titles examples/menu-card/html/grouped_titles.json \\
  -o /tmp/menucard.html \\
  examples/recipes/"""
    expected_outputs = {"/tmp/menucard.html": out.html_menucard}

    def test_command(self) -> None:
        with intercept_outputs() as outputs:
            self.run_cmd()
        assert_text_collection_equal(outputs, self.expected_outputs)


class TestOpenrecipes(unittest.TestCase, IntegrationTest):
    cmd = """gorps export --fmt openrecipes -o /tmp/database.db examples/recipes"""

    expected_outputs = {":memory:": out.openrecipes_sql}

    def test_command(self) -> None:
        with dump_memory_db() as outputs:
            self.run_cmd(
                self.cmd.replace(
                    "/tmp/database.db", "file:memory?mode=memory&cache=shared"
                )
            )
        assert_text_collection_equal(outputs, self.expected_outputs)


class TestOpenrecipesXml(unittest.TestCase, IntegrationTest):
    cmd = """gorps export --fmt openrecipes-xml -o /tmp/out/ examples/recipes"""

    expected_outputs = out.openrecipes_xml

    def test_command(self) -> None:
        with intercept_outputs() as outputs:
            self.run_cmd()
        assert_text_collection_equal(
            outputs, self.expected_outputs, canonicalize=xml_canonicalize
        )


class TestMd(unittest.TestCase, IntegrationTest):
    cmd = "gorps export --fmt markdown -o /tmp/out/ examples/recipes/"

    expected_outputs = out.md

    def test_command(self) -> None:
        with intercept_outputs() as outputs:
            self.run_cmd()
        assert_text_collection_equal(outputs, self.expected_outputs)


class TestSetImage(unittest.TestCase, IntegrationTest):
    cmd = "gorps set-image --pic=/tmp/1x1.png examples/recipes/more-beans.yml"

    expected_outputs = {"examples/recipes/more-beans.yml": out.yml}

    def test_command(self) -> None:
        with intercept_outputs(reads={"/tmp/1x1.png": out.png}) as outputs:
            self.run_cmd()
        assert_text_collection_equal(outputs, self.expected_outputs)


class TestExtractImage(unittest.TestCase, IntegrationTest):
    cmd = "gorps extract-image -o /tmp/1x1.png examples/recipes/more-beans.yml"

    expected_outputs = {"/tmp/1x1.png": out.png}

    def test_command(self) -> None:
        with intercept_outputs(
            reads={"examples/recipes/more-beans.yml": out.yml}
        ) as outputs:
            self.run_cmd()
        assert_text_collection_equal(outputs, self.expected_outputs)


def assert_text_collection_equal(
    actual: Mapping[str, Union[str, bytes]],
    expected: Mapping[str, Union[str, bytes]],
    canonicalize: Callable[[str], str] = lambda x: x,
) -> None:
    def generic_canonicalize(val: Union[str, bytes]) -> Union[str, bytes]:
        if isinstance(val, bytes):
            return val
        return canonicalize(val)

    if {key: generic_canonicalize(val) for key, val in actual.items()} == {
        key: generic_canonicalize(val) for key, val in expected.items()
    }:
        return
    raise AssertionError("\n" + "\n".join(diff_collection(actual, expected)))


def assert_text_equal(actual: str, expected: str, caption: str = "output") -> None:
    if actual == expected:
        return
    raise AssertionError(diff(actual, expected, caption))


def diff_collection(
    actual: Mapping[str, Union[str, bytes]], expected: Mapping[str, Union[str, bytes]]
) -> Iterable[str]:
    only_actual = frozenset(actual) - frozenset(expected)
    only_expected = frozenset(expected) - frozenset(actual)
    diffs = [
        diff(actual_text, expected[caption], caption)
        for caption, actual_text in actual.items()
        if caption in expected
    ]
    if only_actual:
        yield "Only in actual: " + ", ".join(only_actual)
    if only_expected:
        yield "Only in expected: " + ", ".join(only_expected)
    yield "\n".join(diffs)


def diff(actual: Union[str, bytes], expected: Union[str, bytes], caption: str) -> str:
    if isinstance(actual, bytes):
        actual = actual.decode()
    if isinstance(expected, bytes):
        expected = expected.decode()
    return "\n".join(
        difflib.unified_diff(
            expected.splitlines(),
            actual.splitlines(),
            fromfile=os.path.join("expected", caption.lstrip("/")),
            tofile=os.path.join("actual", caption.lstrip("/")),
            lineterm="\n",
        )
    )


def xml_canonicalize(body: str) -> str:
    return etree_canonicalize(body, strip_text=True)


@contextmanager
def intercept_outputs(
    reads: Optional[dict[str, Union[str, bytes]]] = None
) -> Iterator[dict[str, Union[str, bytes]]]:
    outputs: dict[str, Union[str, bytes]] = {}

    class BytesIOBuffer(BytesIO):
        def __init__(self, path: str):
            self.path = path
            super().__init__()

        def close(self) -> None:
            outputs[self.path] = self.getvalue()

    class StringIOBuffer(StringIO):
        def __init__(self, path: str):
            self.path = path
            super().__init__()

        def close(self) -> None:
            outputs[self.path] = self.getvalue()

    original_open = open

    def mock_open(
        path: str, mode: str = "r", encoding: Optional[str] = None, **kwargs: Any
    ) -> IO[Any]:
        if "r" in mode and reads is not None:
            contents = reads.get(path)
            if isinstance(contents, str):
                return StringIO(contents)
            if isinstance(contents, bytes):
                return BytesIO(contents)
        if mode == "w":
            return StringIOBuffer(path)
        if mode == "wb":
            return BytesIOBuffer(path)
        return original_open(path, mode, encoding=encoding, **kwargs)

    with mock.patch("builtins.open", mock_open):
        yield outputs


@contextmanager
def dump_memory_db() -> Iterator[dict[str, str]]:
    dump: dict[str, str] = {}
    connection = sqlite3.connect("file:memory?mode=memory&cache=shared")
    yield dump
    dump[":memory:"] = "\n".join(connection.iterdump())
    connection.close()


def canonicalize_sqldump(dump: str) -> str:
    expression = re.compile(r"X'[0-9A-Z]*'")
    random_ids = unique_in_order(expression.findall(dump))
    for deterministic_id, random_id in enumerate(random_ids):
        dump = dump.replace(random_id, f"X'{deterministic_id}'")
    return dump
