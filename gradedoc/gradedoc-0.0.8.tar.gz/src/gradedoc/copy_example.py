from pathlib import Path
from shutil import copytree

CWD = Path.cwd()


def copy_example(path: Path = CWD):
    """Copy example configuration and AutoHotkey scripts to the current directory."""
    import gradedoc

    scripts = Path(gradedoc.__file__).parent / "example"
    copytree(scripts, path / scripts.name)
