# pylint: skip-file
import pytest

import aorta


class TestCommand(aorta.Command):
    foo: int


class TestEvent(aorta.Event):
    foo: int


class TestCommandHandler(aorta.CommandHandler):

    async def handle(self):
        pass


class TestEventListener(aorta.EventListener):

    async def handle(self):
        pass


@pytest.fixture
def command():
    return TestCommand(foo=1)


@pytest.fixture
def command_handler(command):
    return TestCommandHandler(
        message=command.as_message()
    )


@pytest.fixture
def event_listener(event):
    return TestEventListener(
        message=event.as_message()
    )


@pytest.fixture
def event():
    return TestEvent(foo=1)


@pytest.fixture
def publisher():
    return aorta.MessagePublisher(
        transport=aorta.transport.NullTransport()
    )
