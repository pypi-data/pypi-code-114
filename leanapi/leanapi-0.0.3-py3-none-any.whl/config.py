# -*- coding: utf-8 -*-
import secrets

from typing import Optional, Dict, Any, List, Union
from pydantic import (
    BaseSettings,
    Field, EmailStr, validator, AnyHttpUrl, HttpUrl,
)


class ApiConfig(BaseSettings):
    BACKEND_CORS_ORIGINS: List[str] = ["*"]
    BASE_URL: str = "/base"
    NAME: str = "LEAN API"
    DESCRIPTION: str = ""
    VERSION: str = "0.0.0"

    @classmethod
    def load(cls):
        return cls()
