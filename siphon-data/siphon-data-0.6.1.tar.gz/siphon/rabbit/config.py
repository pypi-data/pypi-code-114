from typing import Optional

from pydantic import BaseSettings, SecretStr


class RabbitConfig(BaseSettings):
    protocol: str = 'amqp'
    host: str
    port: int = 5672
    vhost: str
    user: str
    password: SecretStr
    routing_key: Optional[str]
    exchange: str
    exchange_type: str
    queue: str

    class Config:
        case_sensitive = False
        allow_mutation = False
        env_prefix = 'RABBIT_'
