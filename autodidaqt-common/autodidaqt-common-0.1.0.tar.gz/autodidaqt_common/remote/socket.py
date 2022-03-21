from typing import Any, List, Optional, Union

import asyncio
from dataclasses import dataclass, field

from loguru import logger
from pynng import Socket
from pynng.exceptions import NotSupported, TryAgain
from pynng.nng import Context

from autodidaqt_common.remote.middleware import Middleware

SocketOrContext = Union[Socket, Context]

__all__ = ["AsyncUnbufferedSocket", "AsyncBufferedSocket"]


@dataclass
class AsyncUnbufferedSocket:
    socket: SocketOrContext
    middleware: List[Middleware] = field(default_factory=list)

    def prep_message_outbound(self, message):
        for m in self.middleware:
            message = m.run_outbound(message)

        return message

    def prep_message_inbound(self, message):
        for m in self.middleware[::-1]:
            message = m.run_inbound(message)

        return message

    async def asend(self, message):
        message = self.prep_message_outbound(message)
        return await self.socket.asend(message)

    def send(self, message):
        message = self.prep_message_outbound(message)
        return self.socket.send(message)

    async def arecv(self):
        message = await self.socket.arecv()
        message = self.prep_message_inbound(message)
        return message

    def recv(self, block=True):
        message = self.socket.recv(block=block)
        message = self.prep_message_inbound(message)
        return message


@dataclass
class AsyncBufferedSocket:
    socket: Socket
    middleware: List[Middleware] = field(default_factory=list)

    outbound: AsyncUnbufferedSocket = field(init=False)
    inbound: AsyncUnbufferedSocket = field(init=False)
    pending_outbound_message: Optional[str] = field(init=False)
    outbound_messages: asyncio.Queue = field(init=False)
    inbound_messages: asyncio.Queue = field(init=False)
    use_contexts: bool = field(init=False)

    def __post_init__(self):
        self.pending_outbound_message = None
        self.outbound_messages = asyncio.Queue()
        self.inbound_messages = asyncio.Queue()

        try:
            self.outbound = AsyncUnbufferedSocket(self.socket.new_context(), self.middleware)
            self.inbound = AsyncUnbufferedSocket(self.socket.new_context(), self.middleware)

            self.use_contexts = True
            asyncio.ensure_future(self.send_task())
        except NotSupported:
            self.outbound = AsyncUnbufferedSocket(self.socket, self.middleware)
            self.use_contexts = False
            asyncio.ensure_future(self.shared_task())

    async def send_pending_outbound_message(self):
        if self.pending_outbound_message:
            try:
                self.outbound.send(self.pending_outbound_message)
                logger.trace("Sending previously pulled message")
                self.pending_outbound_message = None
            except TryAgain:
                pass

        await asyncio.sleep(-1)

    async def pop_outbound_message(self):
        if self.pending_outbound_message is None:
            try:
                self.pending_outbound_message = self.outbound_messages.get_nowait()
                logger.trace("Pulling message from queue for outbound")
                self.outbound_messages.task_done()
            except asyncio.QueueEmpty:
                pass

        await asyncio.sleep(-1)

    async def look_for_message_to_recv(self):
        try:
            message = self.outbound.recv(block=False)
            logger.info("Receiving message")
            await self.inbound_messages.put(message)
        except TryAgain:
            pass

        await asyncio.sleep(-1)

    async def shared_task(self):
        while True:
            await self.send_pending_outbound_message()
            await self.pop_outbound_message()
            await self.look_for_message_to_recv()

            await asyncio.sleep(0.01)

    async def send_task(self):
        while True:
            message = await self.outbound_messages.get()
            self.outbound_messages.task_done()
            await self.outbound.asend(message)

    def recv(self) -> Any:
        if self.use_contexts:
            return self.inbound.recv()
        else:
            message = self.inbound_messages.get_nowait()
            self.inbound_messages.task_done()
            return message

    async def arecv(self) -> Any:
        if self.use_contexts:
            return await self.inbound.arecv()
        else:
            message = await self.inbound_messages.get()
            self.inbound_messages.task_done()
            return message

    def send(self, message: Any):
        self.outbound_messages.put_nowait(message)

    async def asend(self, message: Any):
        await self.outbound_messages.put(message)
