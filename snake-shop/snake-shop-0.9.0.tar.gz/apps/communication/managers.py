from oscar.apps.communication import managers
from custom.site_manager import BaseSiteManager


class CommunicationTypeManager(managers.CommunicationTypeManager, \
                               BaseSiteManager):
    pass
