from email import header
from pathlib import Path
from typing import Optional, List
from trk import ( ERRORS, __app_name__, __version__, config, database, trk
)

import pandas as pd
from tabulate import tabulate


import typer


app = typer.Typer()



def get_tracker() -> trk.Tracker:
    if config.CONFIG_FILE_PATH.exists():
        db_path = database.get_database_path(config.CONFIG_FILE_PATH)
    else:
        typer.secho(
            'Config file not found. Please, run "trk init"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    if db_path.exists():
        return trk.Tracker(db_path)
    else:
        typer.secho(
            'Database not found. Please, run "trk init"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

def _version_callback(value: bool) -> None:
    if value:
        typer.echo("A time tracking cli tool created by Nick McMillan")
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return

@app.command()
def init(
    db_path: str = typer.Option(
        str(database.DEFAULT_DB_FILE_PATH),
        "--db-path",
        "-db",
        prompt="time tracker database location?",
    ),
) -> None:
    """Initialize the to-do database."""
    app_init_error = config.init_app(db_path)
    if app_init_error:
        typer.secho(
            f'Creating config file failed with "{ERRORS[app_init_error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    db_init_error = database.init_database(Path(db_path))
    if db_init_error:
        typer.secho(
            f'Creating database failed with "{ERRORS[db_init_error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    else:
        typer.secho(f"The time tracker database is {db_path}", fg=typer.colors.GREEN)
    


@app.command()
def start(event: str = typer.Argument(...), 
    start_time: str =  typer.Option(None, "--time", "-t", help = "Add a manual start time instead of current time."),
    project: str = typer.Option(None, "--project", "-p", help = "Add a project tag"),
    client: str = typer.Option(None,"--client", "-c", help = "Add a client tag")) -> None:
    ''' Start recording a task'''

    tracker = get_tracker()
    str_time, error = tracker.start(event, start_time, project, client)

    if error is None:

        message_start = typer.style("Started the task: ", fg = typer.colors.GREEN)
        message_event = typer.style(event, fg = typer.colors.BRIGHT_WHITE, bold = True)      
        first_line =  message_start + message_event 

        # time
        time_1 = typer.style("time: ",  fg = typer.colors.BRIGHT_YELLOW)
        time_2 = typer.style(str_time,  fg = typer.colors.WHITE)

        # project
        project_1 = typer.style("project: ",  fg = typer.colors.BRIGHT_YELLOW)
        project_2 = typer.style(project,  fg = typer.colors.WHITE)
        

        # client
        client_1 = typer.style("client: ",  fg = typer.colors.BRIGHT_YELLOW)
        client_2 = typer.style(client,  fg = typer.colors.WHITE)

        
        typer.echo("\n" + first_line)
        typer.echo("\t" + time_1 + time_2)
        typer.echo("\t" + project_1 + project_2 )
        typer.echo("\t" + client_1 + client_2 + "\n")

    else:
        message = typer.style(error, fg = typer.colors.BRIGHT_RED )
        typer.echo(message)
    
   
@app.command()
def stop(end_time: str =  typer.Option(None, "--time", "-t", help = "Add a manual end time instead of current time.")):
    """End recording a task"""
    tracker = get_tracker()
    task, project, client, str_start, str_end, str_minutes = tracker.stop(end_time)

    message_start = typer.style("Ended the task: ", fg = typer.colors.GREEN)
    message_event = typer.style(task, fg = typer.colors.BRIGHT_WHITE, bold = True)      
    first_line =  message_start + message_event 

    # time
    time_label = typer.style("time: ",  fg = typer.colors.BRIGHT_YELLOW)
    between = typer.style(" --> ", fg = typer.colors.BRIGHT_RED)
    start_time_1 = typer.style(str_start,  fg = typer.colors.WHITE)
    end_time_1 = typer.style(str_end,  fg = typer.colors.WHITE)

    # duration
    minutes = typer.style("minutes: ",  fg = typer.colors.BRIGHT_YELLOW)
    number = typer.style(str_minutes,  fg = typer.colors.WHITE)


    # project
    project_1 = typer.style("project: ",  fg = typer.colors.BRIGHT_YELLOW)
    project_2 = typer.style(project,  fg = typer.colors.WHITE)
    

    # client
    client_1 = typer.style("client: ",  fg = typer.colors.BRIGHT_YELLOW)
    client_2 = typer.style(client,  fg = typer.colors.WHITE)

    
    typer.echo("\n" + first_line)
    typer.echo("\t" + time_label + start_time_1 + between + end_time_1)
    typer.echo("\t" + minutes + number)
    typer.echo("\t" + project_1 + project_2 )
    typer.echo("\t" + client_1 + client_2 + "\n")



@app.command()
def add(event: str = typer.Argument(...), 
    start_time: str =  typer.Option(None, "--from", "-f", help = "Add a manual start time instead of current time."),
    end_time: str =  typer.Option(None, "--to", "-t", help = "Add a manual end time instead of current time."),
    project: str = typer.Option(None, "--project", "-p", help = "Add a project tag"),
    client: str = typer.Option(None,"--client", "-c", help = "Add a client tag")):
    """Add a task that was not tracked live"""

    tracker = get_tracker()
    task, project, client, str_start, str_end, str_minutes = tracker.add(event, start_time, end_time, project, client)

    message_start = typer.style("Manually added the task: ", fg = typer.colors.GREEN)
    message_event = typer.style(task, fg = typer.colors.BRIGHT_WHITE, bold = True)      
    first_line =  message_start + message_event 

    # time
    time_label = typer.style("time: ",  fg = typer.colors.BRIGHT_YELLOW)
    between = typer.style(" --> ", fg = typer.colors.BRIGHT_RED)
    start_time_1 = typer.style(str_start,  fg = typer.colors.WHITE)
    end_time_1 = typer.style(str_end,  fg = typer.colors.WHITE)

    # duration
    minutes = typer.style("minutes: ",  fg = typer.colors.BRIGHT_YELLOW)
    number = typer.style(str_minutes,  fg = typer.colors.WHITE)


    # project
    project_1 = typer.style("project: ",  fg = typer.colors.BRIGHT_YELLOW)
    project_2 = typer.style(project,  fg = typer.colors.WHITE)
    

    # client
    client_1 = typer.style("client: ",  fg = typer.colors.BRIGHT_YELLOW)
    client_2 = typer.style(client,  fg = typer.colors.WHITE)

    
    typer.echo("\n" + first_line)
    typer.echo("\t" + time_label + start_time_1 + between + end_time_1)
    typer.echo("\t" + minutes + number)
    typer.echo("\t" + project_1 + project_2 )
    typer.echo("\t" + client_1 + client_2 + "\n")


@app.command()
def list(column_name: str):
    """Get unique values of the project or client """
    tracker = get_tracker()
    values = tracker.list_unique(column_name)
    typer.echo(tabulate(values, showindex= False, headers = "keys"))

@app.command()
def summary(column_names: List[str]):
    """Return a summary table"""
    tracker = get_tracker()
    ls_column_names = []
    for i in column_names:
        ls_column_names.append(i)
    #typer.echo(type(ls_column_names))
    summary = tracker.summary(ls_column_names)
    typer.echo("\n")
    typer.echo(tabulate(summary, showindex= False, headers = "keys" ))
    typer.echo("\n")

