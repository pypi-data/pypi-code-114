from battlenet_client.constants import Region


class WoWRegion(Region):

    class Id:
        """Defines the Region IDs for World of Warcraft"""

        #: Region ID for North America
        US = 1

        #: Region ID for Taiwan
        TW = 4

        #: Region ID for Europe
        EU = 3

        #: Region ID for Korea
        KR = 2

        #: Region ID for China
        CN = 5

    class Release:
        """Defines the Release Names for World of Warcraft/World of Warcraft Classic"""

        #: Release name for the original World of Warcraft (v 1.0)
        VANILLA = 'classic1x'

        #: Release name for The Burning Crusade expansion (v 2.0)
        BURNING_CRUSADE = 'classic'

        #: Release name for the current expansion
        RETAIL = 'retail'
