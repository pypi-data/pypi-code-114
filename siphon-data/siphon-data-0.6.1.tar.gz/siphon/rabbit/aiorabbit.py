import asyncio
from typing import Callable, Coroutine, Union

import aio_pika as rabbit
from aiostream import stream

from siphon.logger import logger
from siphon.rabbit.config import RabbitConfig


class AioRabbitConsumer:
    name: str = 'aio-worker-consumer'
    channel: rabbit.Channel
    exchange: rabbit.Exchange
    queue: rabbit.Queue
    connection: rabbit.Connection

    def __init__(self, config: RabbitConfig):
        self.config = config

    async def _rabbit_startup(self):
        await self.get_rabbit_channel()
        await self.get_exchange()
        await self.get_queue()

    async def _rabbit_shutdown(self) -> None:
        logger.debug(f'{self.name} closing rabbit channel..')
        await self.channel.close()
        logger.debug(f'{self.name} closing rabbit connection..')
        await self.connection.close()
        logger.info(f'{self.name} connections to rabbit are closed')

    async def on_startup(self) -> None:
        """This method can be overridden with any startup steps that you want to perform

        Returns: None
        """
        pass

    async def on_shutdown(self) -> None:
        """Anything setup as part of start up can be closed here when the worker shuts down

        Returns: None
        """
        pass

    async def transform(self, message: rabbit.IncomingMessage) -> Union[Callable, Coroutine]:
        """Main transformation logic
        When we receive a message from the queue(s) we're bound to, the payload
        from rabbit is passed to this method. This is where you should implement the main
        logic of your pipeline. Any pipelines should subclass AioWorker and implement this
        method
        Args:
            message: A RabbitMQ message that contains metadata about the message and the data

        Returns: A Callable that will be called when a message is received

        """
        raise NotImplementedError(
            'A transform must be implemented for this worker to process messages'
        )

    async def on_message(self, message: rabbit.IncomingMessage) -> None:
        """
        The process that we run when a message is received on a queue. We implement this as a
        wrapper for our _transform so we can handle errors and not fail our entire worker in the
        event one message can't be processed. We also make sure the message gets acknowledged in
        either a successful message being processed or an error.
        Args:
            message: a rabbit.IncomingMessage object

        Returns: None

        """
        try:
            async with message.process():
                await self.transform(message.body)
                logger.debug('message processing finished successfully')
        # we catch all Exceptions so the worker doesn't crash in cases where we cant process
        # a message from the queue. E.g due to a data error, decryption error etc
        except Exception as err:
            logger.error(f'pipeline failed with error: {err}')

    async def get_rabbit_channel(self) -> None:
        """Get Channel
        Connect to rabbit using values from the environment and create a channel

        Returns: None
        """
        logger.debug(f'connecting to rabbit at {self.config.host}')
        self.connection = await rabbit.connect_robust(
            host=self.config.host,
            port=self.config.port,
            login=self.config.user,
            password=self.config.password.get_secret_value(),
            virtualhost=self.config.vhost,
        )

        self.channel = await self.connection.channel()

    async def get_exchange(self):
        """Get Exchange
        Get an exchange and declare with some defaults

        Returns: None
        """
        logger.debug(
            f'declaring exchange {self.config.exchange} ' f'with type {self.config.exchange_type}'
        )
        self.exchange = await self.channel.declare_exchange(
            name=self.config.exchange,
            type=rabbit.ExchangeType[self.config.exchange_type.upper()],
            durable=True,
        )

    async def get_queue(self):
        """Get Queue
        Get a queue and bind it to the exchange we've previously declared
        Returns: None

        """
        logger.debug(f'declaring queue {self.config.queue}')
        self.queue = await self.channel.declare_queue(self.config.queue, durable=True)

        logger.debug(f'binding queue {self.config.queue} to {self.config.exchange}')
        await self.queue.bind(exchange=self.exchange, routing_key=self.config.routing_key)

    async def __call__(self, *args, **kwargs):
        """
        This is a worker that will create an exchange, queue and bind them together as well as run
        forever. In the event of any errors in processing they will be acknowledged and the worked
        will continue to wait for new messages.

        Returns: None

        """
        try:
            await self._rabbit_startup()
            await self.on_startup()
            async with stream.iterate(self.queue.iterator()).stream() as streamer:
                logger.info('ready for messages')
                async for message in streamer:
                    logger.debug(
                        'received message',
                        consumer_tag=message.consumer_tag,
                        content_type=message.content_type,
                        body_size=message.body_size,
                    )
                    asyncio.create_task(self.on_message(message))

        except Exception as err:
            logger.error(f'{self.name} worker failed with error: {err.__class__.__name__}. {err}')
            exit(code=1)
        finally:
            await self.on_shutdown()
            await self._rabbit_shutdown()
