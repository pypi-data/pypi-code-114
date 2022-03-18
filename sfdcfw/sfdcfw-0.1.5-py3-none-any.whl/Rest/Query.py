"""
SFDCFW.Query
~~~~~~~~~~~~
"""

import json
import requests

from SFDCFW.Constant import SFDC_API_V
from SFDCFW.Rest.Rest import Rest


class Query(Rest):
    """Query class."""
    
    def query(self, query, more=False):
        """Execute SOQL (Salesforce Object Query Language) Query

        Retrieve query results, or more query results if the initial
        results are too large.

        Args:
            query (str): The SOQL (Salesforce Object Query Language) query
            more (bool): Whether to retrieve more query result

        Returns:
            A string formatted JSON for the query response
        """

        # Format the query
        if more:
            # If retrieving more query result
            # The `query` parameter is an identifier
            format_query = query
        else:
            # Replace ` ` with `+` valid query
            format_query = query.replace(' ', '+')

        # Create the request URL
        request_url = f'{self.base_url}/services/data/v{SFDC_API_V}/query/?q={format_query}'

        # Send the request
        r = requests.get(url=request_url,
                         headers=self.header)

        # Check the status code
        if r.status_code == 200:
            # Return the response text (message body)
            return r.text

        # There was an error
        return None

    
    def explain(self, query):
        """Get Performance Feedback

        Retrieve performance feedback on query (without executing),
        report, or list view.
        """
        pass