"""
Tooling API
"""

import json
from urllib.parse import urlencode

from SFDCFW.Rest.Rest import Rest
from SFDCFW.Constant.Constant import SFDC_API_V
from SFDCFW.Constant.Constant import HTTP_GET
from SFDCFW.Constant.Constant import HTTP_PATCH

class Tooling(Rest):
    """Tooling API.
    """

    def query(self, query):
        """Execute SOQL (Salesforce Object Query Language) Query

        Args:
            query (str): The SOQL (Salesforce Object Query Language) query

        Returns:
            A string formatted JSON for the query response
        """

        # Create the request URL
        request_url = "/tooling/query/?q=" + query

        # Send the request
        r = self.send(HTTP_GET, request_url, None)

        return r.text
    
    def execute_anonymous(self, anonymous_body):
        """Execute Anonymous

        Args:
            anonymous_body (str): The Apex code to be executed as an anonymous
                body

        Returns:
            A string formatted JSON for the HTTP response object
        """

        # Create the query string
        query = urlencode({'anonymousBody': anonymous_body})

        # Create the request URL
        request_url = "/tooling/executeAnonymous/?" + query

        # Send the request
        r = self.send(HTTP_GET, request_url, None)

        return r.text