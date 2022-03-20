import json

import pytest
from aio_pika import (Channel, Connection, Exchange, Queue, RobustExchange,
                      RobustQueue)

from siphon import AioQueue, AioRabbitConsumer, RabbitConfig


@pytest.mark.asyncio
async def test_worker_setup(config):
    worker = AioRabbitConsumer(config)

    await worker._rabbit_startup()
    assert isinstance(worker.connection, Connection)
    assert isinstance(worker.channel, Channel)
    assert isinstance(worker.queue, Queue)
    assert isinstance(worker.exchange, Exchange)
    await worker._rabbit_shutdown()


@pytest.mark.asyncio
async def test_worker_connection(config):
    worker = AioRabbitConsumer(config)

    await worker.get_rabbit_channel()
    assert worker.connection.is_closed is False
    assert worker.channel.is_closed is False
    await worker._rabbit_shutdown()
    assert worker.connection.is_closed is True


@pytest.mark.asyncio
async def test_worker_queue(config):
    worker = AioRabbitConsumer(config)

    await worker.get_rabbit_channel()
    await worker.get_exchange()
    await worker.get_queue()
    assert isinstance(worker.queue, RobustQueue)
    await worker._rabbit_shutdown()


@pytest.mark.asyncio
async def test_worker_exchange(config):
    worker = AioRabbitConsumer(config)

    await worker.get_rabbit_channel()
    await worker.get_exchange()
    assert isinstance(worker.exchange, RobustExchange)
    await worker._rabbit_shutdown()


@pytest.mark.asyncio
async def test_worker_message(config, mock_message):
    q = AioQueue()
    worker = AioRabbitConsumer(config)
    worker.transform = lambda x: q.put_nowait(x)
    await worker.on_message(mock_message)
    assert mock_message.processed is True
    out = await q.get()
    assert json.loads(out) == json.loads(mock_message.body.decode())


@pytest.mark.asyncio
async def test_failed_worker():
    config = RabbitConfig(
        protocol='amqp',
        host='nohost',
        port=5432,
        vhost='/',
        user='guest',
        password='wrong',
        routing_key='routing',
        exchange='exchange',
        exchange_type='fanout',
        queue='queue',
    )
    worker = AioRabbitConsumer(config)
    with pytest.raises(ConnectionError):
        await worker.get_rabbit_channel()
