"""Common development tasks via Nox automation."""

import nox


@nox.session(python=["3.7", "3.8", "3.9", "3.10"])
def test(session):
    """Unit testing."""
    session.install("--editable", ".")
    session.install("pytest")

    session.run("pytest")


@nox.session
def qa(session):
    """Quality assurance."""
    session.install("--editable", ".")
    session.install("flake8", "flake8-docstrings", "mypy")

    # Exit peacefully even when errors found.
    # We still want mypy to run afterwards.
    session.run("flake8", "--exit-zero", "src", "tests")
    session.run("mypy", "src")


@nox.session
def format(session):
    """Code formatting."""
    session.install("--editable", ".")
    session.install("black", "isort")

    session.run("black", "src", "tests")
    session.run("isort", "src", "tests")


class BuildType:
    """Options for building documentation."""

    BUILD = "build"
    REBUILD = "rebuild"


class DocTestMode:
    """Options for running doctest tests."""

    TEST = "test_doctest"
    IGNORE = "ignore_doctest"


@nox.session
@nox.parametrize(
    "doctest_mode",
    [DocTestMode.TEST, DocTestMode.IGNORE],
    ids=[DocTestMode.TEST, DocTestMode.IGNORE],
)
@nox.parametrize(
    "build_type",
    [BuildType.BUILD, BuildType.REBUILD],
    ids=[BuildType.BUILD, BuildType.REBUILD],
)
def doc(session, build_type, doctest_mode):
    """Generate documentation and test documentation examples."""
    session.install("--editable", ".")
    session.install("sphinx", "furo", "myst-parser")

    DP_FROM = "docs/source"
    DP_TO = "docs/build"

    CMD_DOCTEST = ("sphinx-build", "-M", "doctest")
    CMD_HTML_BUILD = ("sphinx-build", "-M", "html")

    if build_type == BuildType.BUILD:
        session.run(*(CMD_HTML_BUILD + (DP_FROM, DP_TO)))
    elif build_type == BuildType.REBUILD:
        session.run(*(CMD_HTML_BUILD + (DP_FROM, DP_TO, "-E")))
    else:
        raise NotImplementedError

    if doctest_mode == DocTestMode.TEST and build_type == BuildType.BUILD:
        session.run(*(CMD_DOCTEST + (DP_FROM, DP_TO)))
    if doctest_mode == DocTestMode.TEST and build_type == BuildType.REBUILD:
        session.run(*(CMD_DOCTEST + (DP_FROM, DP_TO, "-E")))
    elif doctest_mode == DocTestMode.IGNORE:
        pass
    else:
        raise NotImplementedError

    pass
