from typing import Any, Dict
import jwt
from dotenv import dotenv_values


class JWTSingleton:
    """JWTSingleton manages the JWT encoding and decoding state for the entire application.
    """

    algorithm : str = "HS256"
    key : str

    @classmethod
    def encode(cls, value : Any)->str:
        return jwt.encode(value, JWTSingleton.key, JWTSingleton.algorithm).decode('utf-8')

    @classmethod
    def decode(cls, value : str)->Dict[str, Any]:
        return jwt.decode(value, JWTSingleton.key)


class JWTController:
    """JWTCOntroller can be used to interact with the JWT singleton.
    """

    def __init__(self, env_key : str):
        key = dotenv_values()[env_key]
        if not key:
            raise ValueError("JWTController did not find an environment variable matching the specified key.")
        JWTSingleton.key = key

    def encode(self, value : Any)->str:
        return JWTSingleton.encode(value)

    def decode(self, value : str)->Dict[str, Any]:
        return JWTSingleton.decode(value)
