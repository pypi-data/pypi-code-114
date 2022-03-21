"""Command line interface for Glowing Pancake"""
from pathlib import Path
import typing as t

import rich
import typer

import glopan

VERSION_STR = glopan.__version__
CONTEXT_SETTINGS = {'help_option_names': ['-h', '--help']}

# Initialize Typers
# Main
main = typer.Typer(
    add_completion=False,
    context_settings=CONTEXT_SETTINGS,
    no_args_is_help=True,
    help=f'✨🥞✨ v{VERSION_STR}.',
)

config_typer = typer.Typer(
    name='config',
    context_settings=CONTEXT_SETTINGS,
    no_args_is_help=True,
    help='Set, list or reset the configuration',
)

main.add_typer(config_typer)


@main.command(
    no_args_is_help=True,
)
def convert(
    filename: t.Optional[str] = typer.Argument(
        None, help='The file to convert.'
    ),
    from_format: t.Optional[str] = typer.Option(
        None, '--fromformat', '-ff', help='The format to convert from'
    ),
    to_format: str = typer.Option(
        ..., '--toformat', '-tf', help='The format to convert to'
    ),
):
    """Convert a file to a given format. Provide either the name of a file to
    convert or the format to convert from. If only the format to convert from
    is given, all the files of the given format will be converted.
    """
    if from_format is None and filename is not None:
        from_format = filename[filename.index('.') + 1 :]
    elif from_format is None and filename is None:
        typer.echo(
            'Please provide the name of the file to convert and/or a format to'
            ' convert from.'
        )
        raise typer.Exit()
    if isinstance(from_format, str):
        converter = from_format.lower() + '_to_' + to_format.lower()
    converter_function = getattr(glopan, converter, None)
    if converter_function is not None and isinstance(from_format, str):
        if filename is None:
            filenames = [
                str(this_filename)
                for this_filename in Path().cwd().iterdir()
                if str(this_filename).lower().endswith(from_format)
            ]
            for this_filename in filenames:
                converter_function(this_filename)
        else:
            if Path(filename).exists():
                converter_function(filename)
            else:
                typer.echo(f'The file {filename} does not exist.')
                raise typer.Exit()
    else:
        typer.echo(
            'No available function to convert from '
            f'{from_format} to {to_format}.'
        )
        raise typer.Exit()


@main.command(
    no_args_is_help=True,
)
def combine(
    filenames: t.List[str] = typer.Argument(
        None, help='The files to combine.'
    ),
    file_format: t.Optional[str] = typer.Option(
        None, '--format', '-f', help='Combine all files of this format'
    ),
    outfile: t.Optional[str] = typer.Option(
        None, '--outfile', '-o', help='The name of the combined file'
    ),
):
    """Combine several files to one. Provide either a list of the files to
    combine, or the format of the files to combine.
    """
    if len(filenames) > 0:
        files_to_combine = filenames
        first_file = filenames[0]
        file_format = first_file[first_file.index('.') :].replace('.', '')
    elif len(filenames) == 0 and file_format is not None:
        file_format = file_format.replace('.', '')
        files_to_combine = [
            str(this_file)
            for this_file in Path.cwd().iterdir()
            if str(this_file).lower().endswith(file_format)
        ]
    else:
        typer.echo('Provide at least the format of the files to combine.')
        raise typer.Exit()
    combiner_function = None
    if file_format is not None:
        combiner = 'combine_' + file_format + 's'
        combiner_function = getattr(glopan, combiner, None)

    if outfile is None and file_format is not None:
        outfile = str(
            Path(files_to_combine[0]).parent / ('compilation.' + file_format)
        )

    if combiner_function is not None:
        if files_to_combine and outfile is not None:
            combiner_function(files_to_combine, outfile)
    else:
        typer.echo(f'No available function to combine {file_format} files')
        raise typer.Exit()


# Config commands
@config_typer.command(
    'set',
    no_args_is_help=True,
)
def set_config(
    key: str = typer.Argument(..., help='The key to set'),
    value: str = typer.Argument(..., help='The value of the key to set'),
):
    """Set the value of a configuration key."""
    glopan.config.set(key, value)


@config_typer.command()
def reset():
    """Reset the configuration to an empty state."""
    glopan.config.reset()


@config_typer.command('list')
def list_config():
    """List the current configuration."""
    rich.print(glopan.config.config)
