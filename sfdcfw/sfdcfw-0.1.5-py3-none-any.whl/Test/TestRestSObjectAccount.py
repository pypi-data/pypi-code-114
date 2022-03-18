"""
SFDCFW.Test.TestRestSObjectAccount
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import json
import os
import random
import string
import unittest

from SFDCFW.Access import Access
from SFDCFW.SObject import SObject
from SFDCFW.Constant import TEST_DATA


def setUpModule():
    """Set Up Module"""
    pass


def tearDownModule():
    """Tear Down Module"""
    pass


class TestRestSObjectCreateAccount(unittest.TestCase):
    """
    Test the SObject module using REST (REpresentational State Transfer)
    with Create Account.
    """

    @classmethod
    def setUpClass(cls):
        """Prepare test setup class.

        Get the data from JSON (JavaScript Object Notation) file and
        login. Initialize any prerequisite.
        """

        # Get the current directory of the file
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # Get the path of the Test Data file
        cls.test_data_file = os.path.join(current_directory, TEST_DATA)

        # Open the file for reading
        with open(cls.test_data_file, 'r') as f:
            cls.data = json.load(f)

        # Get the domain
        domain = cls.data['domain']

        # Get the REST Access user data for success login
        rest_access_user_success = cls.data['user']['access_user_success']

        # Create an instance of Access object and login
        access = Access(username=rest_access_user_success['username'],
                        password=rest_access_user_success['password'],
                        security_token=rest_access_user_success['security_token'],
                        client_id=rest_access_user_success['consumer_key'],
                        client_secret=rest_access_user_success['consumer_secret'],
                        domain=domain).login()

        # Create an instance of SObject
        cls.sobject = SObject(access)


    def test_rest_sobject_create_account_success(self):
        """Test a success of REST (REpresentational State Transfer) SObject create Account.

        Generated Account Name to make a request for create. Should
        result in response with status code 204 No Content.
        """

        # Create the payload
        payload = {
            # Generate a random Account Name
            'Name': f'Account-{random.randrange(10000, 99999)}'
        }

        # Make a request to create the Account
        # Get the return unique identifier (ID)
        # The payload need to be serialized to JSON formatted str (json.dumps)
        account_id = self.sobject.Account.create(json.dumps(payload))

        # Variable `self.data` come from `cls.data`
        # Create the dictionary for Account data
        self.data['account'] = {}
        self.data['account']['rest_create_account_success'] = {}
        # Create or update the Account ID in the Test Data
        self.data['account']['rest_create_account_success']['id'] = account_id

        # Write the new Test Data to file
        with open(self.test_data_file, 'w') as f:
            json.dump(self.data, f)

        # Test to ensure Account ID is a string
        self.assertEqual(type(account_id), str)


    def test_rest_sobject_create_account_failure(self):
        """Test a failure of REST (REpresentational State Transfer) SObject create Account.

        Generated a random Account Description to make a request for
        create. Should result in response with status code 400 Bad
        Request.
        """

        # Create the payload
        payload = {
            # Generate a random Account Description
            'Description': f'Description-{random.randrange(10000, 99999)}'
        }

        # Make a request to create the Account
        # Get the return unique identifier (ID)
        # The payload need to be serialized to JSON formatted str (json.dumps)
        account_id = self.sobject.Account.create(json.dumps(payload))

        # Test to ensure Account ID is None
        self.assertEqual(account_id, None)


    @classmethod
    def tearDownClass(cls):
        """Prepare test teardown class.

        Clean up Test Data
        """

        # Check if Account data exist
        if 'account' in cls.data:
            # Get the REST create Account success data
            rest_create_account_success_id = cls.data['account']['rest_create_account_success']['id']

            # Make a request to delete the Account
            rest_create_account_success = cls.sobject.Account.delete(rest_create_account_success_id)

            # Check if the delete was successful
            if rest_create_account_success == 204:
                # Delete the Account entry from the Test Data
                del cls.data['account']

            # Write the new Test Data to file
            with open(cls.test_data_file, 'w') as f:
                json.dump(cls.data, f)


class TestRestSObjectReadAccount(unittest.TestCase):
    """
    Test the SObject module using REST (REpresentational State Transfer)
    with Read Account.
    """

    @classmethod
    def setUpClass(cls):
        """Prepare test setup class.

        Get the data from JSON (JavaScript Object Notation) file and
        login.
        """

        # Get the current directory of the file
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # Get the path of the Test Data file
        cls.test_data_file = os.path.join(current_directory, TEST_DATA)

        # Open the file for reading
        with open(cls.test_data_file, 'r') as f:
            cls.data = json.load(f)

        # Get the domain
        domain = cls.data['domain']

        # Get the REST Access user data for success login
        rest_access_user_success = cls.data['user']['access_user_success']

        # Create an instance of Access object and login
        access = Access(username=rest_access_user_success['username'],
                        password=rest_access_user_success['password'],
                        security_token=rest_access_user_success['security_token'],
                        client_id=rest_access_user_success['consumer_key'],
                        client_secret=rest_access_user_success['consumer_secret'],
                        domain=domain).login()

        # Create an instance of SObject
        cls.sobject = SObject(access)

        # Create the payload
        payload = {
            # Generate a random Account Name
            'Name': f'Account-{random.randrange(10000, 99999)}'
        }

        # Make a request to create the Account
        # Get the return unique identifier (ID)
        # The payload need to be serialized to JSON formatted str (json.dumps)
        cls.account_id = cls.sobject.Account.create(json.dumps(payload))


    def test_rest_sobject_read_account_success(self):
        """Test a success for read Account.

        Make a request for read Account. Should result in response with
        a string and status code 200 OK.
        """

        # Make a request to read the Account
        # Get the return Account data
        account_data = self.sobject.Account.read(self.account_id)

        # Test to ensure Account data is a string
        self.assertEqual(type(account_data), str)


    def test_rest_sobject_read_account_failure(self):
        """Test a failure for read Account.

        Generate a fake random Account unique identifier (ID) and make
        a request for read Account. Should result in response with
        None (status code 404 Not Found).
        """

        # Generate a random Account unique identifier (ID)
        # The Account unique identifier (ID) will have invalid length
        account_id = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))

        # Make a request to read the Account
        # Get the return Account data
        account_data = self.sobject.Account.read(account_id)

        # Test to ensure Account data is None
        self.assertIsNone(account_data)


    @classmethod
    def tearDownClass(cls):
        """Prepare test teardown class.

        Clean up Test Data
        """

        # Make a request to delete the Account
        _ = cls.sobject.Account.delete(cls.account_id)


class TestRestSObjectUpdateAccount(unittest.TestCase):
    """
    Test the SObject module using REST (REpresentational State Transfer)
    with Update Account.
    """

    @classmethod
    def setUpClass(cls):
        """Prepare test setup class.

        Get the data from JSON (JavaScript Object Notation) file and
        login.
        """

        # Get the current directory of the file
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # Get the path of the Test Data file
        cls.test_data_file = os.path.join(current_directory, TEST_DATA)

        # Open the file for reading
        with open(cls.test_data_file, 'r') as f:
            cls.data = json.load(f)

        # Get the domain
        domain = cls.data['domain']

        # Get the REST Access user data for success login
        rest_access_user_success = cls.data['user']['access_user_success']

        # Create an instance of Access object and login
        access = Access(username=rest_access_user_success['username'],
                        password=rest_access_user_success['password'],
                        security_token=rest_access_user_success['security_token'],
                        client_id=rest_access_user_success['consumer_key'],
                        client_secret=rest_access_user_success['consumer_secret'],
                        domain=domain).login()

        # Create an instance of SObject
        cls.sobject = SObject(access)

        # Create the payload
        payload = {
            # Generate a random Account Name
            'Name': f'Account-{random.randrange(10000, 99999)}'
        }

        # Make a request to create the Account
        # Get the return unique identifier (ID)
        # The payload need to be serialized to JSON formatted str (json.dumps)
        cls.account_id = cls.sobject.Account.create(json.dumps(payload))


    def test_rest_sobject_update_account_success(self):
        """Test a success for update Account.

        Generated Account Name to make a request for update. Should
        result in response with status code 204 No Content.
        """

        # Create the payload
        payload = {
            # Generate a random Account Name
            'Name': f'Account-{random.randrange(10000, 99999)}'
        }

        # Make a request to update the Account
        account = self.sobject.Account.update(self.account_id, json.dumps(payload))

        # Test to ensure HTTP status code is 204 No Content
        self.assertEqual(account, 204)


    def test_rest_sobject_update_account_failure(self):
        """Test a failure for update Account.

        Generate Account Name to make a request for update. Should
        result in response with status code 204 No Content.
        """

        # Generate a random Account unique identifier (ID)
        # The Account unique identifier (ID) will have invalid length
        account_id = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))

        # Create the payload
        payload = {
            # Generate a random Account Name
            'Name': f'Account-{random.randrange(10000, 99999)}'
        }

        # Make a request to update the Account
        account = self.sobject.Account.update(account_id, json.dumps(payload))

        # Test to ensure HTTP status code is not 204 No Content
        self.assertNotEqual(account, 204)


    @classmethod
    def tearDownClass(cls):
        """Prepare test teardown class.

        Clean up Test Data
        """

        # Make a request to delete the Account
        _ = cls.sobject.Account.delete(cls.account_id)


class TestRestSObjectDeleteAccount(unittest.TestCase):
    """
    Test the SObject module using REST (REpresentational State Transfer)
    with Delete Account.
    """

    @classmethod
    def setUpClass(cls):
        """Prepare test setup class.

        Get the data from JSON (JavaScript Object Notation) file and
        login.
        """

        # Get the current directory of the file
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # Get the path of the Test Data file
        cls.test_data_file = os.path.join(current_directory, TEST_DATA)

        # Open the file for reading
        with open(cls.test_data_file, 'r') as f:
            cls.data = json.load(f)

        # Get the domain
        domain = cls.data['domain']

        # Get the REST Access user data for success login
        rest_access_user_success = cls.data['user']['access_user_success']

        # Create an instance of Access object and login
        access = Access(username=rest_access_user_success['username'],
                        password=rest_access_user_success['password'],
                        security_token=rest_access_user_success['security_token'],
                        client_id=rest_access_user_success['consumer_key'],
                        client_secret=rest_access_user_success['consumer_secret'],
                        domain=domain).login()

        # Create an instance of SObject
        cls.sobject = SObject(access)

        # Create the payload
        payload = {
            # Generate a random Account Name
            'Name': f'Account-{random.randrange(10000, 99999)}'
        }

        # Make a request to create the Account
        # Get the return unique identifier (ID)
        # The payload need to be serialized to JSON formatted str (json.dumps)
        cls.account_id = cls.sobject.Account.create(json.dumps(payload))


    def test_rest_sobject_delete_account_success(self):
        """Test a success for delete Account.

        Get the unique identifier (ID) of the Account from the Test Data
        to make a request for delete. Should result in response with
        status code 204 No Content.
        """

        # Make a request to delete the Account
        account = self.sobject.Account.delete(self.account_id)

        # Test to ensure HTTP status code is 204 No Content
        self.assertEqual(account, 204)


    def test_rest_sobject_delete_account_failure(self):
        """Test a failure for delete Account.

        Generate a random unique identifier (ID) of the Account to make
        a request for update. Should result in response with status
        code 204 No Content.
        """

        # Generate a random Account unique identifier (ID)
        # The Account unique identifier (ID) will have invalid length
        account_id = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))

        # Make a request to delete the Account
        account = self.sobject.Account.delete(account_id)

        # Test to ensure HTTP status code is not 204 No Content
        self.assertNotEqual(account, 204)


    @classmethod
    def tearDownClass(cls):
        """Prepare test teardown class.

        Clean up Test Data
        """

        # Make a request to delete the Account
        _ = cls.sobject.Account.delete(cls.account_id)


def suite():
    """Test Suite"""

    # Create the Unit Test Suite
    suite = unittest.TestSuite()

    # Add the Unit Test
    suite.addTest(TestRestSObjectCreateAccount())
    suite.addTest(TestRestSObjectReadAccount())
    suite.addTest(TestRestSObjectUpdateAccount())
    suite.addTest(TestRestSObjectDeleteAccount())

    # Return the Test Suite
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())