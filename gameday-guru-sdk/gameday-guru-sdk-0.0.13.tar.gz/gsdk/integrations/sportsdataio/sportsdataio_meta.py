from typing import Protocol
from dotenv import dotenv_values

class SportsDataIOMetalike(Protocol):
    key : str
    domain : str

class SportsDataIOSingleton(SportsDataIOMetalike):
    """JWTSingleton manages the JWT encoding and decoding state for the entire application.
    """

    key : str
    domain : str


class SportsDataIOmeta(SportsDataIOMetalike):

    key : str
    domain : str

    def __init__(self, env_key : str, env_domain : str):
        key = dotenv_values()[env_key]
        domain = dotenv_values()[env_domain]
        if not key or not domain:
            raise ValueError("JWTController did not find an environment variable matching the specified key.")
        SportsDataIOSingleton.key = key
        SportsDataIOSingleton.domain = domain
        self.key = key
        self.domain = domain


    def get_key(self)->str:
        return SportsDataIOSingleton.key

    def get_domain(self)->str:
        return SportsDataIOSingleton.domain

