import typer

from .login_helper import login_helper

app = typer.Typer()
app.add_typer(login_helper, name="login_helper")

if __name__ == "__main__":
    app()
