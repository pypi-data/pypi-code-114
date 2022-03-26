import re
from pathlib import Path


def get_version() -> str:
    pyproject_file = Path(Path(__file__).parent.parent.parent / "pyproject.toml")
    with open(pyproject_file, "r") as file:
        content = file.read()
    version = re.search("\s*version\s*=\s*[\"']\s*([.\w]{3,})\s*[\"']\s", content)[1]
    return version
