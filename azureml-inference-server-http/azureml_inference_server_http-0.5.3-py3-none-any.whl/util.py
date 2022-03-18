from pathlib import Path


def get_version():
    with open(Path(__file__).resolve().parent.joinpath("VERSION")) as f:
        return f.readline().strip()
