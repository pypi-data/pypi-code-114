"""
Read-only viewing of Jupyter notebooks in the web browser.
"""
from __future__ import annotations

import logging
from pathlib import Path

import typer
from rich.logging import RichHandler

__version__ = "0.0.1"

logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True, markup=True, show_path=False)],
)
# TODO: find a way to have `nbv` before logging level in the output

log = logging.getLogger("rich")

app = typer.Typer(name="nbv")


def _open_in_web_browser(
    notebook: str, *, theme: str = "light", template: str = "lab", debug: bool = False
):
    """Convert notebook to HTML with nbconvert and open in default web browser."""
    import subprocess
    import tempfile
    import webbrowser

    p0 = Path(notebook)

    tf = tempfile.NamedTemporaryFile(prefix=f"notebook={p0.name}_", suffix=".html", delete=False)
    tf.close()
    p = Path(tf.name)

    # TODO: theme/template options
    # [x] default templates: lab (default), classic, basic
    # [x] default themes: light (default), dark
    # other templates: toc ?
    # other themes: https://github.com/dunovank/jupyter-themes ?
    # fmt: off
    cmd = [
        "jupyter-nbconvert", str(p0),
        "--to", "html",
        "--theme", theme,
        "--template", template,
        "--output", p.as_posix(),
    ]
    # fmt: on
    log.info(f"Invoking '{' '.join(cmd)}'")
    cp = subprocess.run(cmd, capture_output=not debug)
    if cp.returncode != 0:
        if cp.stderr is not None:
            suff = ":\n...\n" + "\n".join(cp.stderr.decode().splitlines()[-3:])
        else:
            suff = "."
        raise Exception(f"Command '{' '.join(cmd)}' failed{suff}")

    # TODO: browser option using https://docs.python.org/3/library/webbrowser.html#webbrowser.get
    log.info(f"Opening '{p.as_posix()}' in default web browser")
    webbrowser.open(p, new=2, autoraise=True)


def _try(fn, *args, **kwargs):
    try:
        fn(*args, **kwargs)
    except Exception as e:
        msg = f"Invoking `{fn.__name__}` failed"
        if kwargs.get("debug", False):
            log.exception(msg)
        else:
            log.error(f"{msg} with message: [bold]{e}[/]")
        return True
    else:
        return False


@app.command(no_args_is_help=True, help="View Jupyter notebook in web browser.")
def main(
    notebook: str = typer.Argument(..., help="Notebook file to open."),
    theme: str = typer.Option("light", help="HTML theme to use."),
    template: str = typer.Option("lab", help="HTML template to use."),
    debug: bool = typer.Option(False, "--debug/", help="Enable info/debug messages."),
) -> int:
    log.setLevel(logging.DEBUG if debug else logging.WARNING)

    p = Path(notebook)
    if not p.suffix == ".ipynb":
        log.error("Only '.ipynb' files are supported.")
        return 2

    if not p.is_file():
        log.error(f"File {p.as_posix()!r} does not exist.")
        return 2

    if theme == "dark" and template in {"basic", "classic"}:
        typer.echo(
            "Note that theme 'dark' is only applied with template 'lab' (the default template)."
        )

    err = _try(_open_in_web_browser, p, theme=theme, template=template, debug=debug)

    return int(err)


if __name__ == "__main__":
    app()
