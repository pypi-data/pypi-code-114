# pylint: skip-file
import pytest

from ..messagehandlersprovider import MessageHandlersProvider
from .conftest import TestCommand
from .conftest import TestEvent


class TestMessageHandlersProvider:

    def test_parse_command(self, command):
        data = command.as_message().dict(by_alias=True)
        provider = MessageHandlersProvider()
        provider.register(TestCommand, None)
        message = provider.parse(data)
        assert message.api_version == 'v1'
        assert message.kind == 'TestCommand'

    def test_parse_event(self, event):
        data = event.as_message().dict(by_alias=True)
        provider = MessageHandlersProvider()
        provider.register(TestEvent, None)
        message = provider.parse(data)
        assert message.api_version == 'v1'
        assert message.kind == 'TestEvent'

    def test_invalid_raises_exception_on_parse(self, command):
        provider = MessageHandlersProvider()
        with pytest.raises(provider.UnknownMessageType):
            provider.parse({})

    def test_unknown_raises_exception_on_parse(self, command):
        provider = MessageHandlersProvider()
        with pytest.raises(provider.UnknownMessageType):
            provider.parse(command.as_message().dict(by_alias=True))

    def test_register_single_command(self, command):
        provider = MessageHandlersProvider()
        provider.register(TestCommand, 'foo')

        message = command.as_message()
        handlers = provider.get(message)
        assert handlers == ['foo']

    def test_register_multiple_command(self, command):
        provider = MessageHandlersProvider()
        provider.register(TestCommand, 'foo')
        provider.register(TestCommand, 'bar')

        message = command.as_message()
        handlers = provider.get(message)
        assert handlers == ['foo', 'bar']
