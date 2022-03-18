import json
import time
import sys

from SFDCFW.Rest.Rest import Rest

import pandas as pd

from SFDCFW.Constant import SFDC_API_V
from SFDCFW.Constant import HTTP_GET
from SFDCFW.Constant import HTTP_POST
from SFDCFW.Constant import HTTP_PATCH
from SFDCFW.Constant import HTTP_PUT

class Bulk(Rest):
    """Bulk API.
    """

    def create_job(self, operation, object_type):
        """Create a Bulk job

        Args:
            operation (str): The operation of the Bulk job
            object_type (str): The object type (API name) for the Bulk job

        Returns:
            A string formatted JSON for the HTTP response object
        """

        # Create the request relative URL
        relative_url = "/jobs/ingest"

        # Update the header
        self._header["Content-Type"] = "application/json"

        # Create payload
        payload = {
            "operation": operation,
            "object": object_type,
            "contentType": "CSV"
        }

        # Send the request
        r = self.send(HTTP_POST, relative_url, json.dumps(payload))

        return r.text


    def add_data(self, id, data):
        """Add data to the job

        Args:
            id (str): The ID of the Bulk job
            data (str): The data for the Bulk job, must be in CSV format

        Returns:
            A string of the response status code
        """

        # Create the data request relative URL
        relative_url = "/jobs/ingest/" + id + "/batches"

        # Update the header
        self._header["Content-Type"] = "text/csv"
        self._header["Accept"] = "application/json"

        # Send the data request
        r = self.send(HTTP_PUT, relative_url, data)

        # Return the response status code
        return r.status_code


    def close_job(self, id):
        """Close the job

        Args:
            id (str): The ID of the Bulk job

        Returns:
            A string formatted JSON for the HTTP response object
        """

        # Create the job request relative URL
        relative_url = "/jobs/ingest/" + id

        # Update the header
        self._header["Content-Type"] = "application/json"
        self._header.pop("Accept", None)

        # Create payload
        job_payload = {
            "state": "UploadComplete"
        }

        # Send the job request
        r = self.send(HTTP_PATCH, relative_url, json.dumps(job_payload))

        return r.text


    def check_status(self, id):
        """Check the status of the job

        Args:
            id (str): The ID of the Bulk job

        Returns:
            A string formatted JSON for the HTTP response object
        """

        # Create the job request relative URL
        relative_url = "/jobs/ingest/" + id

        # Update the header
        self._header.pop("Content-Type", None)
        self._header.pop("Accept", None)

        # Send the job request
        r = self.send(HTTP_GET, relative_url, None)

        return r.text


    def get_result(self, id):
        """Get the job result

        Args:
            id (str): The ID of the Bulk job

        Returns:
            A string formatted JSON for the HTTP response object
        """
        pass


    def create(self, object_type, data):
        """Create

        Args:
            data (str): The data to be created in CSV format (newline per entry)

        Returns:
            A string formatted JSON for the HTTP response object
        """

        # The specified operation for Bulk job
        operation = "insert"

        # Create the Bulk job
        bulk_job = self.create_job(operation, object_type)

        # Parse the Bulk job ID
        bulk_job_id = json.loads(bulk_job)["id"]
        # Create the data request relative URL
        data_relative_url = "/jobs/ingest/" + bulk_job_id + "/batches"
        # Addition to header
        self._header["Content-Type"] = "text/csv"
        self._header["Accept"] = "application/json"
        # Send the data request
        _ = self.send(HTTP_PUT, data_relative_url, data)

        # Create the job request relative URL
        job_relative_url = "/jobs/ingest/" + bulk_job_id
        # Update the header
        self._header["Content-Type"] = "application/json"
        # Create the job payload
        job_payload = {
            "state": "UploadComplete"
        }
        # Send the job request 
        job_r = self.send(HTTP_PATCH, job_relative_url, json.dumps(job_payload))

        return job_r.text


    def update(self, object_type, data, batch_limit=1000):
        """Update

        Args:
            object_type (str): The object type (API name) for the Bulk job
            data (list): A list of dictionary with the data to update, each
                dictionary should have the same "key"
                [
                    { "email": "alice@company.com.invalid" },
                    { "email": "bob@company.com.invalid" }
                ]

            batch_limit (int): The record size (count) of the Bulk job

        Returns:
            A string formatted JSON for the HTTP response object
        """

        print("Object Type: {}".format(object_type))
        print("Data: {}".format(data))

        # It is easier to extract data with pandas DataFrame
        # Create the DataFrame from data
        df = pd.DataFrame.from_dict(data)

        # The specified operation for Bulk job
        operation = "update"

        # Get the size of the object data
        object_data_size = len(data)
        # Calculate the number of Bulk job needed
        bulk_job_size = (object_data_size + (-object_data_size) % batch_limit) // batch_limit

        # Create a list for the Bulk job ID
        # This will be for each Bulk job
        bulk_job_id_list = []
        # Loop through and create the payload list for Bulk job
        for i in range(0, bulk_job_size):
            # Calculate the head (start) and tail (end) of each Bulk payload
            payload_head = i * batch_limit
            payload_tail = payload_head + batch_limit - 1

            # Create the Bulk job
            bulk_job_r = self.create_job(operation, object_type)

            # Parse the Bulk job ID
            bulk_job_id = json.loads(bulk_job_r)["id"]
            # Add the Bulk job ID to list
            bulk_job_id_list.append(bulk_job_id)

            # Add the data to the job and get the response
            add_data_r = self.add_data(bulk_job_id, df[payload_head : payload_tail].to_csv(index=False))

            if add_data_r == 201:
                # Upload successful, close the job
                _ = self.close_job(bulk_job_id)
            else:
                # Failure, something went wrong
                print("Failure, Status Code: {}".format(add_data_r))


    def empty_batch(self, object_type, condition=None, batch_limit=1000):
        """Empty

        Args:
            object_type (str): The object type (API name) for the Bulk job
            condition (str): The WHERE clause
            batch_limit (int): The record size (count) of the Bulk job
        """

        # Query all the data from the object
        # Query
        if condition:
            query = "SELECT Id FROM " + object_type + " WHERE " + condition
        else:
            query = "SELECT Id FROM " + object_type
        # Retrieve the object data
        object_data = self.query(query)
        # JSONify the object data
        object_data = json.loads(object_data)

        # Get the record count of the object data
        object_data_size = object_data["totalSize"]
        # Compare record count vs. batch limit, take the smaller of the two
        object_data_count = object_data_size if object_data_size < batch_limit else batch_limit

        # Create a list for the payload
        # This will be for each Bulk job
        payload_list = []
        # Loop through and create the payload list batch
        for i in range(0, object_data_size, batch_limit):
            # Build a string with the object data for the delete request body
            payload = "Id\n"
            # Loop through and build the payload
            for record in object_data["records"][i : i + object_data_count - 1]:
                payload += record["Id"] + "\n"

            # Add the payload batch to list
            payload_list.append(payload)

        # The specified operation for Bulk job
        operation = "delete"

        # Create a list for the Bulk job ID
        bulk_job_id_list = []
        # Loop through the payload batch and create the Bulk jobs
        for payload in payload_list:
            bulk_job_r = self.create_job(operation, object_type)

            # Parse the Bulk job ID
            bulk_job_id = json.loads(bulk_job_r)["id"]
            # Add the Bulk job ID to list
            bulk_job_id_list.append(bulk_job_id)

        # Align the Bulk job ID to the payload
        bulk_job_id_payload_list = zip(bulk_job_id_list, payload_list)

        # Loop through and add data (payload) to job (bulk_job_id)
        for bulk_job in bulk_job_id_payload_list:
            # Unpack the tuple
            bulk_job_id, payload = bulk_job
            # Add the data to the job and get the response
            add_data_r = self.add_data(bulk_job_id, payload)

            if add_data_r == 201:
                # Upload successful, close the job
                _ = self.close_job(bulk_job_id)
            else:
                # Failure, something went wrong
                print("Failure, Status Code: {}".format(add_data_r))


    def empty(self, object_type, condition=None, batch_size=1000):
        """Empty

        Args:
            object_type (str): The object type (API name) for the Bulk job
            condition (str): The WHERE clause
            batch_size (int): The record size of the Bulk job
        """

        # Query all the data from the object
        # Query
        if condition:
            query = "SELECT Id FROM " + object_type + " WHERE " + condition
        else:
            query = "SELECT Id FROM " + object_type
        # Retrieve the object data
        object_data = self.query(query)
        # JSONify the object data
        object_data = json.loads(object_data)

        # Build a string with the object data for the delete request body
        payload = "Id\n"
        for record in object_data["records"]:
            payload += record["Id"] + "\n"

        # The specified operation for Bulk job
        operation = "delete"

        # Create the Bulk job and get the response
        bulk_job_r = self.create_job(operation, object_type)

        # Parse the Bulk job ID
        bulk_job_id = json.loads(bulk_job_r)["id"]
        # Add the data to the job and get the response
        add_data_r = self.add_data(bulk_job_id, payload)

        if add_data_r == 201:
            # Upload successful, close the job
            _ = self.close_job(bulk_job_id)
        else:
            # Failure, something went wrong
            print("Failure, Status Code: {}".format(add_data_r))

        # Check the state of the job
        check_status_r = self.check_status(bulk_job_id)

        # Get the current state
        current_state = json.loads(check_status_r)["state"]

        # See if the job is done (need to use equality compare)
        while current_state != "JobComplete":
            # If job is not done, wait and check again
            print("Job State: {}".format(current_state))
            print("Waiting 10 Seconds...")
            time.sleep(10)
            check_status_r = self.check_status(bulk_job_id)
            current_state = json.loads(check_status_r)["state"]

        return check_status_r