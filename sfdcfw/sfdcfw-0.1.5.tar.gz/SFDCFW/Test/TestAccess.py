"""
SFDCFW.Test.TestAccess
~~~~~~~~~~~~~~~~~~~~~~
"""

import json
import os
import unittest

from SFDCFW.Access import Access
from SFDCFW.Constant import TEST_DATA


def setUpModule():
    """Set Up Module"""
    pass


def tearDownModule():
    """Tear Down Module"""
    pass


class TestRestAccess(unittest.TestCase):
    """Test the Access module with REST (REpresentational State Transfer)."""

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


    def test_login_rest_success(self):
        """Test a success of REST (REpresentational State Transfer) login method.

        Get the success username and password (rest_access_user_success)
        data from the Test Data file and login. Should result in login
        method returning a tuple of the access token and instance URL.
        """

        # Get the REST Access user data for success login
        rest_access_user_success = self.data['user']['access_user_success']

        # Create an instance of Access object and login
        access = Access(username=rest_access_user_success['username'],
                        password=rest_access_user_success['password'],
                        security_token=rest_access_user_success['security_token'],
                        client_id=rest_access_user_success['consumer_key'],
                        client_secret=rest_access_user_success['consumer_secret'],
                        domain=self.domain).login()

        # Test to ensure `access` is a tuple
        self.assertEqual(type(access), tuple)


    def test_login_rest_failure(self):
        """Test a failure of REST (REpresentational State Transfer) login method.

        Get the failure username and password (rest_access_user_failure)
        data from the Test Data file and login. Should result in login
        method returning a a `None` value.
        """

        # Get the REST Access user data for failure login
        rest_access_user_failure = self.data['user']['access_user_failure']

        # Create an instance of Access object and login
        access = Access(username=rest_access_user_failure['username'],
                        password=rest_access_user_failure['password'],
                        security_token=rest_access_user_failure['security_token'],
                        client_id=rest_access_user_failure['consumer_key'],
                        client_secret=rest_access_user_failure['consumer_secret'],
                        domain=self.domain).login()

        # Test to ensure `access` is `None`
        self.assertIsNone(access)


class TestSoapAccess(unittest.TestCase):
    """Test the Access module with SOAP (Simple Object Access Protocol)."""

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
        # cls.metadata_wsdl = os.path.join(current_directory, cls.data["metadata_wsdl"])


    def test_soap_login_success(self):
        """Test a success of SOAP (Simple Object Access Protocol) login method.

        Get the success username and password (soap_access_user_success)
        data from the Test Data file and login. Should result in login
        method returning a tuple of the session ID and (metadata) server
        URL.
        """

        # Get the SOAP Access user data for success login
        soap_access_user_success = self.data['user']['access_user_success']

        # Create an instance of Access object and login
        access = Access(username=soap_access_user_success['username'],
                        password=soap_access_user_success['password'],
                        security_token=soap_access_user_success['security_token'],
                        domain=self.domain,
                        wsdl=self.enterprise_wsdl,
                        metadata=True).login()

        # Test to ensure `access` is a tuple
        self.assertEqual(type(access), tuple)


    def test_soap_login_failure(self):
        """Test a failure of SOAP (Simple Object Access Protocol) login method.

        Get the failure username and password (soap_access_user_failure)
        data from the Test Data file and login. Should result in login
        method returning a `None` value.
        """

        # Get the SOAP Access user data for failure login
        soap_access_user_failure = self.data['user']['access_user_failure']

        # Create an instance of Access object and login
        access = Access(username=soap_access_user_failure['username'],
                        password=soap_access_user_failure['password'],
                        security_token=soap_access_user_failure['security_token'],
                        domain=self.domain,
                        wsdl=self.enterprise_wsdl,
                        metadata=True).login()

        # Test to ensure `access` is `None`
        self.assertIsNone(access)


def suite():
    """Test Suite"""

    # Create the Unit Test Suite
    suite = unittest.TestSuite()

    # Add the Unit Test
    suite.addTest(TestRestAccess)
    suite.addTest(TestSoapAccess)

    # Return the Test Suite
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())