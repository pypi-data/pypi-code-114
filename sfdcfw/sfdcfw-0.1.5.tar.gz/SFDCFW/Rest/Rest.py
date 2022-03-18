"""
SFDCFW.Rest.Rest
~~~~~~~~~~~~~~~~
"""

import json
from urllib.parse import urlparse


class Rest(object):
    """REST (REpresentational State Transfer) class."""

    def __init__(self, access):
        """Constructor

        Args:
            access (tuple): The Salesforce session ID / access token and
                server URL / instance URL tuple
        """

        # Unpack the tuple for session ID / access token and server URL / instance URL
        id_token, base_url = access
        
        # Parse the URL
        u = urlparse(base_url)
        self.base_url = f'{u.scheme}://{u.netloc}'

        # Create REST header
        self.header = {
            'Authorization': f'Bearer {id_token}',
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'application/json'
        }

    def __getattr__(self, label):
        """Get Attribute Passed In.

        Args:
            label (str): The attribute passed in.

        Returns:
            A instance of the SObject class.
        """
        # Set the name / label
        self.label = label

        # Return the self instance
        return self