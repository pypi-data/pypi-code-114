from battlenet_client.constants import Region


class D3Region(Region):
    class Id:
        """Defines the Region IDs for Diablo III"""

        #: Region ID for North America
        US = 1

        #: Region ID for Europe
        EU = 2

        #: Region ID for Korea and Taiwan
        APAC = 3

        #: Region ID for China
        CN = 5
