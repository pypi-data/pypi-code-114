import re

import typer

app = typer.Typer()


def validate_mac(value: str) -> str:
    if len(value) not in [4,12]:
        raise typer.BadParameter("Please enter the full or last 4 characters of the MAC address")
    mac = re.match(fr"^[a-fA-F0-9]{{{len(value)}}}$", value)
    if not mac:
        raise typer.BadParameter(f"Invalid MAC: {value}")    
    return "-".join([value[i:i+2] for i in range(0, len(value), 2)])


@app.command()
def mac(mac: str = typer.Option(..., callback=validate_mac, help="Full or last 4 characters of the MAC address")):
    """
    Find Desktop/Phone by MAC Address
    """
    typer.echo(mac)
