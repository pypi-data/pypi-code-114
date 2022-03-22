from cakemail_openapi import SystemEmailApi
from cakemail.wrapper import WrappedApi


class SystemEmail(WrappedApi):
    update: SystemEmailApi.patch_system_emails
    set: SystemEmailApi.set_system_emails
    show: SystemEmailApi.show_system_emails

    def __init__(self, superclass):
        super().__init__(
            superclass=superclass,
            namemap={
                'update': 'patch_system_emails',
                'set': 'set_system_emails',
                'show': 'show_system_emails',
            }
        )
