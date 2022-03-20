from pydantic import BaseSettings, Extra, SecretStr


class DatabaseConfig(BaseSettings):
    host: SecretStr
    port: int
    user: SecretStr
    password: SecretStr

    class Config:
        extra = Extra.ignore


class PostgresConfig(DatabaseConfig):
    port: int = 5432
    database: str = 'postgres'
