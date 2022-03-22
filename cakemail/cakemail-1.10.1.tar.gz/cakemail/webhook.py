from cakemail_openapi import WebhookApi
from cakemail.wrapper import WrappedApi


class Webhook(WrappedApi):
    archive: WebhookApi.archive_webhook
    create: WebhookApi.create_webhook
    get: WebhookApi.get_webhook
    list: WebhookApi.list_webhooks
    update: WebhookApi.patch_webhook
    unarchive: WebhookApi.unarchive_webhook

    def __init__(self, superclass):
        super().__init__(
            superclass=superclass,
            namemap={
                'archive': 'archive_webhook',
                'create': 'create_webhook',
                'get': 'get_webhook',
                'list': 'list_webhooks',
                'update': 'patch_webhook',
                'unarchive': 'unarchive_webhook',
            }
        )
