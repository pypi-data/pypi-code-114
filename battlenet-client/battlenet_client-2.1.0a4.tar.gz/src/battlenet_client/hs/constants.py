from battlenet_client.constants import Region


class HSRegion(Region):

    class Id:
        """Defines the Region IDs for Hearthstone"""

        #: Region ID for North America
        US = 1

        #: Region ID for Europe
        EU = 2

        #: Region ID for Korea and Taiwan
        APAC = 3

        #: Region ID for China
        CN = 5
