import os
from pydantic import BaseConfig


class Config(BaseConfig):
    SW_HOST: str = os.getenv("SW_HOST")
    SW_USER: str = os.getenv("SW_USER")
    SW_PASS: str = os.getenv("SW_PASS")


def load_config():
    return Config()
