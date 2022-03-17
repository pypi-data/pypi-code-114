from click.testing import CliRunner
from pathlib import Path
from texproject.command import cli
from texproject.filesystem import template_linker
import pytest
import shlex


def _verbose_invoke(runner, args):
    print(shlex.join(["tpr"] + args))
    return runner.invoke(cli, args)


def _run_cmd_seq(runner, *args_list, expect_fail=False):
    results = (_verbose_invoke(runner, args) for args in args_list)
    if expect_fail:
        assert all(res.exit_code != 0 for res in results)
    else:
        assert all(res.exit_code == 0 for res in results)


@pytest.fixture
def fs_runner():
    print(f"Set up new environment.")
    runner = CliRunner()
    with runner.isolated_filesystem():
        yield runner


@pytest.mark.slow
@pytest.mark.parametrize("tname", template_linker.list_names())
def test_all_templates(fs_runner, tname):
    _run_cmd_seq(fs_runner, ["init", tname], ["validate"])


def test_archive(fs_runner):
    _run_cmd_seq(
        fs_runner,
        ["init", "preprint"],
        ["archive", "out.zip"],
        ["archive", "--mode", "arxiv", "out.tar"],
        ["archive", "--mode", "nohidden", "no_hidden.tar"],
    )
    import tarfile

    with tarfile.open("out.tar") as tf:
        path_list = [Path(name) for name in tf.getnames()]
        for path in [
            Path("texproject/macros/local-arxiv-typesetting.sty"),
            Path("000README.XXX"),
        ]:
            assert path in path_list

        assert Path("texproject/macros/local-typesetting.sty") not in path_list

    with tarfile.open("no_hidden.tar") as tf:
        path_list = [Path(name) for name in tf.getnames()]
        for path in [
            Path("texproject/macros"),
        ]:
            assert path in path_list


def test_import(fs_runner):
    _run_cmd_seq(fs_runner, ["init", "preprint"], ["import", "--macro", "tikz"])
    cit_path = Path("test.bib")
    bibtext = "example text"
    cit_path.write_text(bibtext)
    _run_cmd_seq(
        fs_runner,
        ["import", "--citation-path", str(cit_path)],
        ["import", "--style", "palatino"],
        ["import", "--gitignore"],
        ["import", "--pre-commit"],
    )
    assert Path(".texproject/citations/local-test.bib").read_text() == bibtext
    assert len(Path(".gitignore").read_text()) > 0
    assert len(Path(".git/hooks/pre-commit").read_text()) > 0


def test_git_init(fs_runner):
    _run_cmd_seq(
        fs_runner,
        ["init", "plain"],
        [
            "-n",
            "git",
            "init",
            "--repo-name",
            "test_repo",
            "--repo-description",
            "some description",
            "--no-wiki",
            "--issues",
            "--repo-visibility",
            "private",
        ],
    )


def test_git_files(fs_runner):
    _run_cmd_seq(
        fs_runner,
        ["init", "plain"],
        [
            "git",
            "init-files",
        ],
    )
    assert len(Path(".gitignore").read_text()) > 0
    assert len(Path(".github/workflows/build_latex.yml").read_text()) > 0
    assert len(Path(".git/hooks/pre-commit").read_text()) > 0


def test_git_archive(fs_runner):
    _run_cmd_seq(
        fs_runner,
        ["init", "plain"],
        ["-n", "git", "init-archive", "--repo-name", "test"],
    )


def test_template(fs_runner):
    _run_cmd_seq(
        fs_runner,
        ["init", "plain"],
        ["template", "add", "--macro", "tikz"],
        ["template", "add", "--citation", "example"],
        ["template", "remove", "--macro", "tikz"],
    )
    assert len(Path(".texproject/citations/local-example.bib").read_text()) > 0
    Path(".texproject/macros/local-tikz.sty").unlink()
    _run_cmd_seq(
        fs_runner,
        ["template", "refresh"],
    )
    assert not Path(".texproject/macros/local-tikz.sty").exists()
    _run_cmd_seq(fs_runner, ["template", "remove", "--macro", "tikz"], expect_fail=True)


def test_clean(fs_runner):
    _run_cmd_seq(fs_runner, ["init", "preprint"], ["import", "--macro", "tikz"])
    assert Path(".texproject/macros/local-tikz.sty").exists()
    _run_cmd_seq(fs_runner, ["util", "clean"])
    assert not Path(".texproject/macros/local-tikz.sty").exists()


def test_list(fs_runner):
    _run_cmd_seq(
        fs_runner,
        ["list", "macro"],
        ["list", "citation"],
        ["list", "style"],
        ["list", "template"],
    )


def test_init_fail(fs_runner):
    _run_cmd_seq(fs_runner, ["init", "plain"])
    _run_cmd_seq(fs_runner, ["init", "preprint"], expect_fail=True)


def test_show(fs_runner):
    _run_cmd_seq(
        fs_runner,
        ["init", "plain"],
        ["show", "--macro", "typesetting"],
        ["show", "--citation", "main"],
        ["show", "--macro", "typesetting", "--diff"],
        ["show", "--style", "palatino", "--diff"],
    )
