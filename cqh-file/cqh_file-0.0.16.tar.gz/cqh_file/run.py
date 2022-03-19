import string
import cqh_file
import click

#ctypes.windll.user32.MessageBoxW(0, msg, title, 1)


@click.group()
def cli():
    pass




@click.command()
@click.option("--port", default=8081)
@click.option("--dir")
@click.option("--timeout", default=60)
def serve(port, dir, timeout):
    click.echo("port:{}".format(port))
    click.echo("dir:{}, timeout:{}".format(dir, timeout))
    from cqh_file import __version__
    click.echo("version:{}".format(__version__))
    from cqh_file.serve import create_app

    create_app(port=port, dir=dir, timeout=timeout)

def parse_time(v):
    if v[-1].isdigit():
        return int(v)
    value, unit = v[:-1], v[-1]
    value = int(value)
    unit_d = {
        "s": 1,
        "m": 60,
        "h": 3600,
        "d": 3600*24
    }
    return unit_d[unit]* value

@click.command()
@click.option("--url")
@click.option("--dir", multiple=True)
@click.option("--sleep", default="300s")
@click.option("--delete", default=1)
def client(url, dir, sleep, delete):
    click.echo("url:{}, dir:{}, sleep:{}, delete:{}".format(url,dir, sleep, delete))
    sleep = parse_time(sleep)
    
    from cqh_file import __version__
    click.echo("version:{}".format(__version__))
    from cqh_file.client import ClientLoop
    loop = ClientLoop(url=url, dir=dir, sleep=sleep, 
    delete=delete)
    loop.loop()

cli.add_command(serve)
cli.add_command(client)


if __name__ == "__main__":
    cli()
