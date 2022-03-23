"""Prep __main__ entry."""
# pylint: disable=invalid-name
from pathlib import Path
from typing import List, Optional

import environs
import logzero
import typer
from icecream import ic
from icecream import install as ic_install
from textwrap import dedent
from logzero import logger

import fast_scores  # noqa: F401, W0611
import cmat2aset  # noqa: F401

from ezbee import __version__, ezbee
from ezbee.loadtext import loadtext

# set env LOGLEVEL to 10/debug/DEBUG to turn on debug
try:
    _ = environs.Env().log_level("LOGLEVEL")
# except environs.EnvValidationError:
except (environs.EnvError, environs.EnvValidationError):
    _ = None
except Exception:
    _ = None

# logzero.loglevel(_ or 10)
logzero.loglevel(_ or 20)

# logger.debug(" debug: %s", __file__)
# logger.info(" info: %s", __file__)

ic_install()
ic.configureOutput(
    includeContext=True,
    # outputFunction=logger.info,
    outputFunction=logger.debug,
)
ic.enable()

app = typer.Typer(
    name="ezbee",
    add_completion=False,
    help="en-zh-bee aligner",
)

esp_min_samples_expl = dedent(
    """
    Larger esp or smaller min_samples will result in more aligned pairs but also more false positives (pairs falsely identified as candidates). On the other hand, smaller esp or larger min_samples values tend to miss ‘good’ pairs."""
).strip()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{app.info.name} v.{__version__}")
        raise typer.Exit()


@app.command()
def main(
    files: List[str] = typer.Argument(
        ...,
        metavar="file1 [file2]...",
        help="files (absolute or relative paths) to be aligned",
    ),
    eps: float = typer.Option(10, help="epsilon"),
    min_samples: int = typer.Option(
        6, help="eps, min samples: " + esp_min_samples_expl
    ),
    need_sep: bool = typer.Option(
        False,
        "--need-sep",
        "-s",
        is_flag=True,
        help="whether the files are mixed english and chinese and hence need to be separated",
    ),
    version: Optional[bool] = typer.Option(  # pylint: disable=(unused-argument
        None,
        "--version",
        "-v",
        "-V",
        help="Show version info and exit.",
        callback=_version_callback,
        is_eager=True,
    ),
):
    """Align en-zh texts.

    e.g.

    * ezbee file1 file2

    * ezbee file1 -s

    * ezbee file1 file2 -s
    """
    if not files:
        typer.echo("Provide at least one file")
        raise typer.Exit()

    if len(files) == 1 and not need_sep:
        typer.echo(
            "If you only provide one file, you'll also have to specify -s or --need-sep."
        )
        typer.echo("Try again...")
        raise typer.Exit()

    for file_ in files:
        if not Path(file_).is_file():
            typer.echo(f" [{file_}] is not a file or does not exit.")
            raise typer.Exit()

    # paired
    if len(files) == 2:
        try:
            text1 = loadtext(files[0])
        except Exception as e:
            logger.error(e)
            raise
        try:
            text2 = loadtext(files[1])
        except Exception as e:
            logger.error(e)
            raise
    else:  # assume mixed english/chinese, separate
        text1 = []
        text2 = []
        for file in files:
            text = loadtext(file)
            # TODO
        del text

    text1 = Path(files[0]).read_text(encoding="utf8").splitlines()
    text2 = Path(files[1]).read_text(encoding="utf8").splitlines()

    try:
        _ = ezbee(
            text1,
            text2,
            eps=eps,
            min_samples=min_samples,
        )
        typer.echo("ezbee....")
        raise typer.Exit()
    except Exception as e:
        typer.echo(e)
        raise typer.Exit()


if __name__ == "__main__":
    app()
