import typer

from ingeniictl.cli.infra.main import app as infra_app

app = typer.Typer()
app.add_typer(infra_app, name="infra")
