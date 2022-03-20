import json

import pytest
from aio_pika import IncomingMessage
from aio_pika.message import DeliveredMessage
from pamqp.header import ContentHeader
from pamqp.specification import Basic

from siphon import RabbitConfig


@pytest.fixture()
def config() -> RabbitConfig:
    config = RabbitConfig()
    return config


@pytest.fixture()
def mock_message() -> IncomingMessage:
    message = DeliveredMessage(
        channel=None,
        delivery=Basic.Deliver(),
        header=ContentHeader(),
        body=json.dumps({'message': 'this is a mock message'}).encode(),
    )
    return IncomingMessage(message)
