"""AWS profile switcher"""
import configparser
import os
import sys
from pathlib import Path

from InquirerPy import prompt

__version__ = "0.2.2"


DEFAULT_PROFILE = "default"
AWS_PATH = ".aws"
AWS_CONFIG = "config"
AWS_CONFIG_FILE = "AWS_CONFIG_FILE"
AWS_PROFILE = "AWS_PROFILE"
AWSPS_FILE = ".awsswitch"


def get_profile() -> str:
    """Get aws profile."""
    if aws_profile := os.getenv(AWS_PROFILE):
        return aws_profile

    return DEFAULT_PROFILE


def get_path() -> Path:
    """Get aws config path."""
    if aws_path_env := os.getenv(AWS_CONFIG_FILE):
        return Path(aws_path_env).parent

    return Path.home() / AWS_PATH


def profile_reader(path: Path) -> list:
    """Read AWS profile."""
    config = configparser.ConfigParser()
    config.read(path / AWS_CONFIG)
    return sorted(
        " ".join(section.split(" ")[1:]) if "profile " in section else section
        for section in config.sections()
    )


def set_profile(profile: str) -> None:
    """Write profile to file."""
    with open(Path.home() / AWSPS_FILE, "w", encoding="utf-8") as file_out:
        file_out.write(profile)


def print_help(msg: str):
    """Print help message."""
    text = (
        msg,
        "Refer to this guide for help on setting up a new AWS profile:",
        "https://docs.aws.amazon.com/cli/"
        "latest/userguide/cli-chap-getting-started.html",
    )
    print(
        "\n".join(text),
        file=sys.stderr,
    )


def app() -> None:
    """AWS profile switcher."""
    print("AWS profile switcher")

    aws_config_path = get_path()

    if not aws_config_path.exists() or not aws_config_path.is_dir():
        print_help("No AWS config path found.")
        return

    if not (aws_config_path / AWS_CONFIG).exists():
        print_help("AWS config path does not exist.")
        return

    questions = [
        {
            "type": "list",
            "message": "Choose a profile",
            "choices": profile_reader(aws_config_path),
            "default": os.getenv(AWS_PROFILE) or DEFAULT_PROFILE,
        },
    ]
    result = prompt(questions)
    set_profile(str(result[0]))


if __name__ == "__main__":
    app()
