import os
import pathlib

from grid5000 import Grid5000

import IPython

CONF_PATH = os.path.join(os.environ.get("HOME"), ".python-grid5000.yaml")

MOTD = r"""
                 __  __
    ____  __  __/ /_/ /_  ____  ____
   / __ \/ / / / __/ __ \/ __ \/ __ \
  / /_/ / /_/ / /_/ / / / /_/ / / / /
 / .___/\__, /\__/_/ /_/\____/_/ /_/
/_/_________/ _     ___  __________  ____  ____
  / ____/____(_)___/ ( )/ ____/ __ \/ __ \/ __ \
 / / __/ ___/ / __  /|//___ \/ / / / / / / / / /
/ /_/ / /  / / /_/ /  ____/ / /_/ / /_/ / /_/ /
\____/_/  /_/\__,_/  /_____/\____/\____/\____/


* Configuration loaded from %s
* A new client (variable gk) has been created for the user %s
* Start exploring the API through the gk variable
  # Example: Get all available sites
  $) gk.sites.list()

"""


def main():

    path = pathlib.Path(CONF_PATH)
    if not path.exists():
        print("Configuration file %s is missing" % CONF_PATH)
        return
    gk = Grid5000.from_yaml(CONF_PATH)
    motd = MOTD % (CONF_PATH, gk.username)
    IPython.embed(header=motd)


def auth(user: str):
    from getpass import getpass

    path = pathlib.Path(CONF_PATH)

    password = getpass("Grid'5000 password: ")
    path.write_text("\n".join([f"username: {user}", f"password: {password}"]))
    print(f"{CONF_PATH} created successfully")
    path.chmod(0o600)


def cli_auth():
    import argparse

    parser = argparse.ArgumentParser(description=f"Check or create {CONF_PATH}")
    parser.add_argument("--user", "-u", help="Username on Grid'5000", required=True)
    args = parser.parse_args()

    path = pathlib.Path(CONF_PATH)
    if path.exists():
        print(f"{CONF_PATH} file already exists, not overwriting")
        return
    auth(args.user)
