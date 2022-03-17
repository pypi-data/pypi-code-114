# coding=utf-8
#####################################################
# THIS FILE IS AUTOMATICALLY GENERATED. DO NOT EDIT #
#####################################################
# noqa: E128,E201
from ...aio.asyncclient import AsyncBaseClient
from ...aio.asyncclient import createApiClient
from ...aio.asyncclient import config
from ...aio.asyncclient import createTemporaryCredentials
from ...aio.asyncclient import createSession
_defaultConfig = config


class AuthEvents(AsyncBaseClient):
    """
    The auth service is responsible for storing credentials, managing
    assignment of scopes, and validation of request signatures from other
    services.

    These exchanges provides notifications when credentials or roles are
    updated. This is mostly so that multiple instances of the auth service
    can purge their caches and synchronize state. But you are of course
    welcome to use these for other purposes, monitoring changes for example.
    """

    classOptions = {
        "exchangePrefix": "exchange/taskcluster-auth/v1/",
    }
    serviceName = 'auth'
    apiVersion = 'v1'

    def clientCreated(self, *args, **kwargs):
        """
        Client Created Messages

        Message that a new client has been created.

        This exchange takes the following keys:

         * reserved: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.
        """

        ref = {
            'exchange': 'client-created',
            'name': 'clientCreated',
            'routingKey': [
                {
                    'multipleWords': True,
                    'name': 'reserved',
                },
            ],
            'schema': 'v1/client-message.json#',
        }
        return self._makeTopicExchange(ref, *args, **kwargs)

    def clientUpdated(self, *args, **kwargs):
        """
        Client Updated Messages

        Message that a new client has been updated.

        This exchange takes the following keys:

         * reserved: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.
        """

        ref = {
            'exchange': 'client-updated',
            'name': 'clientUpdated',
            'routingKey': [
                {
                    'multipleWords': True,
                    'name': 'reserved',
                },
            ],
            'schema': 'v1/client-message.json#',
        }
        return self._makeTopicExchange(ref, *args, **kwargs)

    def clientDeleted(self, *args, **kwargs):
        """
        Client Deleted Messages

        Message that a new client has been deleted.

        This exchange takes the following keys:

         * reserved: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.
        """

        ref = {
            'exchange': 'client-deleted',
            'name': 'clientDeleted',
            'routingKey': [
                {
                    'multipleWords': True,
                    'name': 'reserved',
                },
            ],
            'schema': 'v1/client-message.json#',
        }
        return self._makeTopicExchange(ref, *args, **kwargs)

    def roleCreated(self, *args, **kwargs):
        """
        Role Created Messages

        Message that a new role has been created.

        This exchange takes the following keys:

         * reserved: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.
        """

        ref = {
            'exchange': 'role-created',
            'name': 'roleCreated',
            'routingKey': [
                {
                    'multipleWords': True,
                    'name': 'reserved',
                },
            ],
            'schema': 'v1/role-message.json#',
        }
        return self._makeTopicExchange(ref, *args, **kwargs)

    def roleUpdated(self, *args, **kwargs):
        """
        Role Updated Messages

        Message that a new role has been updated.

        This exchange takes the following keys:

         * reserved: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.
        """

        ref = {
            'exchange': 'role-updated',
            'name': 'roleUpdated',
            'routingKey': [
                {
                    'multipleWords': True,
                    'name': 'reserved',
                },
            ],
            'schema': 'v1/role-message.json#',
        }
        return self._makeTopicExchange(ref, *args, **kwargs)

    def roleDeleted(self, *args, **kwargs):
        """
        Role Deleted Messages

        Message that a new role has been deleted.

        This exchange takes the following keys:

         * reserved: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.
        """

        ref = {
            'exchange': 'role-deleted',
            'name': 'roleDeleted',
            'routingKey': [
                {
                    'multipleWords': True,
                    'name': 'reserved',
                },
            ],
            'schema': 'v1/role-message.json#',
        }
        return self._makeTopicExchange(ref, *args, **kwargs)

    funcinfo = {
    }


__all__ = ['createTemporaryCredentials', 'config', '_defaultConfig', 'createApiClient', 'createSession', 'AuthEvents']
