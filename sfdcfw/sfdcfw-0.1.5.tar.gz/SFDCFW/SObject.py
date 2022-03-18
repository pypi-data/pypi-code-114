"""
SFDCFW.Rest.SObject
~~~~~~~~~~~~~~~~~~~
"""

import json
from urllib.parse import urlparse

import requests

from SFDCFW.Constant import SFDC_API_V

class SObject:
    """SObject class."""

    def __init__(self, access):
        """Constructor

        Args:
            access (tuple): The Salesforce session ID / access token and
                server URL / instance URL tuple
        """

        # Unpack the tuple for session ID / access token and server URL / instance URL
        self.id_token, self.base_url = access
        
        # Parse the URL
        u = urlparse(self.base_url)
        self.base_url = f'{u.scheme}://{u.netloc}'

        # Create REST header
        self.header = {
            'Authorization': f'Bearer {self.id_token}',
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


    def create(self, payload):
        """Create SObject.

        Args:
            payload (dict): The required data for the SObject.

        Returns:
            A string for the unique identifier (ID) of the SObject.
        """
        
        # Create the request URL
        request_url = f'{self.base_url}/services/data/v{SFDC_API_V}/sobjects/{self.label}'

        # Send the request
        r = requests.post(url=request_url,
                          headers=self.header,
                          data=payload)

        # Check the status code
        if r.status_code == 201:
            # Parse the unique identifier (ID) of the SObject
            sobject_id = json.loads(r.text)['id']
            # Return the unique identifier (ID) of the SObject
            return sobject_id

        # There was an error
        return None


    def read(self, id=None):
        """Read SObject.

        Args:
            id (str): The unique identifier (ID) of the SObject.

        Returns:
            A string formatted JSON for the request.
        """

        if id is not None:
            # Create the request URL with ID
            request_url = f'{self.base_url}/services/data/v{SFDC_API_V}/sobjects/{self.label}/{id}'
        else:
            # Create the request URL without ID
            request_url = f'{self.base_url}/services/data/v{SFDC_API_V}/sobjects/{self.label}'

        # Send the request
        r = requests.get(url=request_url,
                         headers=self.header)

        # Check the status code
        if r.status_code == 200:
            # Return the response text (message body)
            return r.text

        # There was an error
        return None


    def update(self, id, payload):
        """Update SObject.

        Args:
            id (str): The ID of the SObject.
            payload (dict): The updated data for the SObject.

        Returns:
            A HTTP Status Code (or None) of the response.
        """

        # Create the request URL
        request_url = f'{self.base_url}/services/data/v{SFDC_API_V}/sobjects/{self.label}/{id}'

        # Send the request
        r = requests.patch(url=request_url,
                           headers=self.header,
                           data=payload)

        # Check the status code
        if r.status_code == 204:
            # Return the status code
            return r.status_code

        # There was an error
        return None


    def delete(self, id):
        """Delete SObject.

        Args:
            id (str): The ID of the SObject.

        Returns:
            A HTTP Status Code (or None) of the response.
        """

        # Create the request URL
        request_url = f'{self.base_url}/services/data/v{SFDC_API_V}/sobjects/{self.label}/{id}'

        # Send the request
        r = requests.delete(url=request_url,
                            headers=self.header)

        # Check the status code
        if r.status_code == 204:
            # Return the status code
            return r.status_code

        # There was an error
        return None


    # def query(self, query):
    #     """Execute SOQL (Salesforce Object Query Language) Query

    #     Args:
    #         query (str): The SOQL (Salesforce Object Query Language) query

    #     Returns:
    #         A string formatted JSON for the query response
    #     """

    #     # Create the request URL
    #     request_url = "/query/?q=" + query

    #     # Send the request
    #     r = self.send(HTTP_GET, request_url, None)

    #     return r.text


    # def query_more(self, next_record_url):
    #     """Query Next Record Batch

    #     Args:
    #         next_record_url (str): The URL for the next batch of records

    #     Returns:
    #         A string formatted JSON for the query response
    #     """

    #     # Send the request
    #     r = self.send(HTTP_GET, next_record_url, None)

    #     return r.text