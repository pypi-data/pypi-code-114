"""
SFDCFW.Access
~~~~~~~~~~~~~
"""

import requests
# import xml.etree.ElementTree as ET
from zeep import Client, Settings, exceptions

# try:
#     # Python 3+
#     from html import escape
# except ImportError:
#     # Python Older
#     from cgi import escape

from SFDCFW.Constant import SFDC_API_V


class Access:
    """Access."""

    def __init__(self,
                 username,
                 password,
                 security_token,
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

        self.username = username
        self.password = password
        self.security_token = security_token
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None
        self.soap_url = f'https://{domain}.salesforce.com/services/Soap/u/{version}'
        self.rest_url = f'https://{domain}.salesforce.com/services/oauth2/token'
        self.wsdl = wsdl
        self.metadata = metadata


    def login(self):
        """Login

        Returns:
            A tuple containing the session ID / access token and
            (metadata) server URL / instance URL based on credential
        """

        # Check if username, password, security token, client ID, client secret is provided
        if all(credential is not None for credential in [self.username,
                                                         self.password,
                                                         self.security_token,
                                                         self.client_id,
                                                         self.client_secret]):
            # If username, password, security token, client ID, client secret is provided, login with REST
            return self.login_rest(username=self.username,
                                   password=self.password,
                                   security_token=self.security_token,
                                   client_id=self.client_id,
                                   client_secret=self.client_secret,
                                   url=self.rest_url)

        # Check if username, password is provide
        elif all(credential is not None for credential in [self.username,
                                                           self.password,
                                                           self.security_token]):
            # If username, password is provided, login with SOAP
            return self.login_soap(username=self.username,
                                   password=self.password,
                                   security_token=self.security_token,
                                   url=self.soap_url,
                                   wsdl=self.wsdl,
                                   metadata=self.metadata)
        
        # There is an error
        return None
    

    def login_rest(self,
                   username,
                   password,
                   security_token,
                   client_id=None,
                   client_secret=None,
                   url=None):
        """Login via REST (REpresentational State Transfer)

        Args:
            username (str): The Salesforce user username
            password (str): The Salesforce user password
            security_token (str): The Salesforce user Security Token
            client_id (str): The Salesforce Connected App Consumer Key
            client_secret (str): The Salesforce Connected App Consumer Secret
            url (str): The Salesforce REST API URL used for login

        Returns:
            A string for the Salesforce bearer token if call was
            successful, or None otherwise
        """

        # Create header
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        # Create payload
        payload = {
            'grant_type': 'password',
            'username': username,
            'password': password + security_token,
            'client_id': client_id,
            'client_secret': client_secret
        }

        # Make the request and get the response
        r = requests.post(url, headers=header, data=payload)

        if r.status_code == 200:
            # Parse the access token and instance URL
            access_token = r.json()['access_token']
            instance_url = r.json()['instance_url']
            return (access_token, instance_url)

        # Return None for now if error
        return None


    def login_soap(self,
                   username,
                   password,
                   security_token,
                   url=None,
                   wsdl=None,
                   metadata=False):
        """Login via SOAP (Simple Object Access Protocol)

        Args:
            username (str): The Salesforce user username
            password (str): The Salesforce user password
            security_token (str): The Salesforce user Security Token
            url (str): The Salesforce SOAP API URL used for login
            wsdl (str): The path to the WSDL (Web Services Description Language) file
            metadata (bool): Whether or not to get the metadata server URL

        Returns:
            A tuple containing the session ID and (metadata) server URL
        """

        # Create client with setting of disable strict mode, use recovery mode
        setting = Settings(strict=False)
        client = Client(wsdl, settings=setting)

        try:
            # Attempt to make the request for the response
            r = client.service.login(username, password + security_token)
        except exceptions.Fault:
            # Return None for now if exception
            return None

        # Check to see if the client service succeeded
        if r is not None:
            # Get the sessionId
            session_id = r['sessionId']

            if metadata:
                # Get the `metadataServerUrl` if requested
                metadata_server_url = r['metadataServerUrl']

                # Return a tuple of the session ID and metadata server URL
                return (session_id, metadata_server_url)
            else:
                # Get the `serverUrl`
                server_url = r['serverUrl']

                # Return a tuple of the session ID and server URL
                return (session_id, server_url)

        # Return None for now if error
        return None