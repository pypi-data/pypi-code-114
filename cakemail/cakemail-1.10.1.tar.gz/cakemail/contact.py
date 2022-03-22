from cakemail_openapi import ContactApi
from cakemail.wrapper import WrappedApi


class Contact(WrappedApi):
    create: ContactApi.create_contact
    delete: ContactApi.delete_contact
    delete_contacts_export: ContactApi.delete_contacts_export
    download_contacts_export: ContactApi.download_contacts_export
    export_contacts: ContactApi.export_contacts
    get: ContactApi.get_contact
    get_contacts_export: ContactApi.get_contacts_export
    import_contacts: ContactApi.import_contacts
    list_contacts_exports: ContactApi.list_contacts_exports
    list: ContactApi.list_contacts_of_list
    list_from_segments: ContactApi.list_contacts_of_segment
    update: ContactApi.patch_contact
    unsubscribe: ContactApi.unsubscribe_contact

    def __init__(self, superclass):
        super().__init__(
            superclass=superclass,
            namemap={
                'create': 'create_contact',
                'delete': 'delete_contact',
                'delete_contacts_export': 'delete_contacts_export',
                'download_contacts_export': 'download_contacts_export',
                'export_contacts': 'export_contacts',
                'get': 'get_contact',
                'get_contacts_export': 'get_contacts_export',
                'import_contacts': 'import_contacts',
                'list_contacts_exports': 'list_contacts_exports',
                'list': 'list_contacts_of_list',
                'list_from_segments': 'list_contacts_of_segment',
                'update': 'patch_contact',
                'unsubscribe': 'unsubscribe_contact',
            }
        )
