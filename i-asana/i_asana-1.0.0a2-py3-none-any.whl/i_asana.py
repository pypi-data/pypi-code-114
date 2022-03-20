"""Class module to interface with Asana.
"""
import os

from aracnid_logger import Logger
import asana

# initialize logging
logger = Logger(__name__).get_logger()


class AsanaInterface:
    """Asana interface class.

    Environment Variables:
        ASANA_ACCESS_TOKEN: Access token for Asana.

    Attributes:
        client: Asana client.

    Exceptions:
        TBD
    """

    def __init__(self) -> None:
        """Initializes the interface.
        """
        # read environment variables
        asana_access_token = os.environ.get('ASANA_ACCESS_TOKEN')

        # initialize asana client
        self._client = asana.Client.access_token(asana_access_token)

    @property
    def client(self) -> asana.client.Client:
        """Returns the Asana Client object.

        Returns:
            Asana Client object.
        """
        return self._client
