import typer
from alma_hilse.lib.lo_timing import lftrr
from alma_hilse.lib.corr import drx
from alma_hilse import __version__
from typing import Optional

# Command-line application commands and subcommands based in Typer
app = typer.Typer(add_completion=False)
timing_app = typer.Typer(short_help="LFTRR/LORR related commands")
app.add_typer(timing_app, name="timing")
corr_app = typer.Typer(short_help="HILSE correlator related commands")
app.add_typer(corr_app, name="corr")

@app.callback()
def callback():
    """
    Collection of diagnostics and configuration commands for ALMA HILSE
    """

@corr_app.callback()
def corr_app_callback():
    """
    Obtain basic status of HILSE correlator device.

    Usage:

    \b
    alma-hilse corr xxxxx # XXXXXX

    """

@app.command(short_help='Show current version')
def version():
    print(__version__)

@timing_app.callback()
def timing_app_callback():
    """
    Obtain basic status of HILSE LFTRR device and issue resync command.

    Referring to the status, a stripped down version of the LORR status is presented,
    focusing only on variables relevant to HILSE.

    Usage:

    \b
    alma-hilse timing status # Display LFTRR status
    alma-hilse timing resync # Resync TE to central reference
    alma-hilse timing clear  # Clear TE and PLL error flags

    """

@timing_app.command("status", short_help='LFTRR healthcheck')
def status_lftrr():
    lftrr.status()

@timing_app.command("resync", short_help='Resync TE to central reference')
def resync_te():
    lftrr.resync_te()

@timing_app.command("clear", short_help='Clear TE and PLL error flags')
def clear_flags():
    lftrr.clear_flags()

@corr_app.command("status", short_help='DRX power and status check')
def status_drx():
    drx.get_drx_status()

def main():
    app()

if __name__ == "__main__":
    main()
