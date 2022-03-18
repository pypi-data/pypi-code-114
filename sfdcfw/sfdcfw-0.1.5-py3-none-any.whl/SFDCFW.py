"""
SFDCFW.SFDCFW
~~~~~~~~~~~~~
"""

from urllib.parse import urlparse

from SFDCFW.Access import Access
from SFDCFW.Rest.SObject import SObject

from SFDCFW.Constant import SFDC_API_V


class SFDCFW(SObject):
    """Salesforce.com FrameWork."""

    def __init__(self,
                 username=None,
                 password=None,
                 security_token=None,
                 client_id=None,
                 client_secret=None,
                 version=SFDC_API_V,
                 domain='login',
                 wsdl=None,
                 metadata=False):
        """Constructor

        Args:
            username (str): The Salesforce user Username
            password (str): The Salesforce user Password
            security_token (str): The Salesforce user Security Token
            client_id (str): The Salesforce Connected App Consumer Key
            client_secret (str): The Salesforce Connected App Consumer Secret
            version (str): The Salesforce version of the Application Programming Interface
            domain (str): The common Salesforce domain for connection (login or test)
            wsdl (str): The path to the WSDL (Web Services Description Language) file
            metadata (bool): Whether or not this is for metadata
        """

        # Create an instance of Access object and login
        access = Access(username=username,
                        password=password,
                        security_token=security_token,
                        client_id=client_id,
                        client_secret=client_secret,
                        version=version,
                        domain=domain,
                        wsdl=wsdl,
                        metadata=metadata).login()

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