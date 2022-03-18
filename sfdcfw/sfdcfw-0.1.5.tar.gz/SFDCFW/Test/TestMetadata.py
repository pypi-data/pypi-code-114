"""
SFDCFW.Test.TestMetadata
~~~~~~~~~~~~~~~~~~~~~~~~
"""

import json
import os
import unittest

from SFDCFW.Access import Access
from SFDCFW.Metadata import Metadata
from SFDCFW.Constant import TEST_DATA


def setUpModule():
    """Set Up Module"""
    pass


def tearDownModule():
    """Tear Down Module"""
    pass

class TestMetadata(unittest.TestCase):
    """Test Metadata."""

    @classmethod
    def setUpClass(cls):
        """Prepare test set up class.

        Get the Test Data from JSON (JavaScript Object Notation) file.
        """

        # Get the current directory of the file
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # Get the path of the Test Data file
        cls.test_data_file = os.path.join(current_directory, TEST_DATA)

        # Open the file for reading
        with open(cls.test_data_file, 'r') as f:
            cls.data = json.load(f)

        # Get the hostname from the Test Data
        cls.domain = cls.data['domain']

        # Get the WSDL (Web Service Definition Language) file path
        cls.enterprise_wsdl = os.path.join(current_directory, cls.data['enterprise_wsdl'])
        cls.metadata_wsdl = os.path.join(current_directory, cls.data["metadata_wsdl"])

        # Get the SOAP Access user data for success login
        soap_access_user_success = cls.data['user']['soap_access_user_success']

        # Create an instance of Access object and login
        cls.access = Access(username=soap_access_user_success['username'],
                            password=soap_access_user_success['password'],
                            security_token=soap_access_user_success['security_token'],
                            domain=cls.domain,
                            wsdl=cls.enterprise_wsdl,
                            metadata=True).login()


    def test_metadata_general(self):
        metadata = Metadata(access=self.access,
                            wsdl=self.metadata_wsdl)