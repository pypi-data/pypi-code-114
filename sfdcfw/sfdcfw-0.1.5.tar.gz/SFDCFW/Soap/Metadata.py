"""
Metadata API

Metadata Coverage

.. _Metadata Coverage:
   https://developer.salesforce.com/docs/metadata-coverage/54
"""

import threading
import sys
# import xml.etree.ElementTree as ET
import requests

from zeep import Client, Settings

from SFDCFW.Constant import SFDC_API_V

class Metadata:
    """Metadata class."""

    def __init__(self, access, wsdl):
        """Constructor

        Args:
            access (tuple): The Salesforce session ID / access token and
                server URL / instance URL tuple
            wsdl (str): The path to the WSDL file
        """

        # Unpack the tuple for session ID / access token and server URL / instance URL
        self.id_token, self.url = access

        # Create client with setting of disable strict mode, use recovery mode
        setting = Settings(strict=False)
        client = Client(wsdl, settings=setting)
        # Create the service with custom binding and URL
        binding = "{http://soap.sforce.com/2006/04/metadata}MetadataBinding"
        self.service = client.create_service(binding, self.url)

        # Create the SOAP header (this is different than the HTTP header)
        self.soap_header = {
            "SessionHeader": {
                "sessionId": self.id_token
            }
        }


    def list_metadata(self, query):
        """List Metadata

        Args:
            query (list): A complex list of dictionary specify components
                [
                    { "folder": "Report", "type": "ReportName" },
                    { "type": "WorkflowRule" }
                ]

        Returns:
            A complex list of dictionary for the requested metadata
            component(s)
        """

        return self.service.listMetadata(queries=query,
                                         asOfVersion=SFDC_API_V,
                                         _soapheaders=self.soap_header)


    def read_metadata(self, metadata_type, full_name, thread=32):
        """Read Metadata

        Args:
            metadata_type (str): The type of the metadata
            full_name (list): A complex list of string for the full
                name(s) of the metadata component

        Returns:
            A complex list of dictionary for the requested metadata
            component(s)
        """

        # Create a new list to store all the read result
        read_result_all = []
        # Get the size of the full name list
        full_name_size = len(full_name)
        # Limit for the metadata API function
        record_limit = 10

        # Loop through the full name list 10 records at a time
        for i in range(0, full_name_size, record_limit):
            # Make request(s) to read metadata, 10 at a time
            read_result = self.service.readMetadata(type=metadata_type,
                                                    fullNames=full_name[ i : i + record_limit ],
                                                    _soapheaders=self.soap_header)
            # Add the current read result to all the read result
            read_result_all.extend(read_result)

        return read_result_all


    def read_metadata_thread(self, metadata_type, full_name, thread=10):
        """Read Metadata

        Args:
            metadata_type (str): The type of the metadata
            full_name (list): A complex list of string for the full
                name(s) of the metadata component
            thread (int): The number of thread to use

        Returns:
            A complex list of dictionary for the requested metadata
            component(s)
        """

        def _read_metadata_thread(self, metadata_type, full_name):
            """Read Metadata Thread Function

            Args:
                metadata_type (str): The type of the metadata
                full_name (list): A complex list of string for the full
                    name(s) of the metadata component
            """
            # Make request(s) to read metadata, 10 at a time
            read_result = self.service.readMetadata(type=metadata_type,
                                                    fullNames=full_name,
                                                    _soapheaders=self.soap_header)

            # Add the current read result to all the read result
            read_result_all.extend(read_result)

        # Create a new list to store all the read result
        read_result_all = []
        # Get the size of the full name list
        full_name_size = len(full_name)
        # Limit for the metadata API function
        record_limit = 10

        # Round the thread to multiple of 10
        # thread_size = thread + (-thread) % 10
        thread_size = thread
        # Calculate the thread batch size based on metadata API limit
        thread_batch_size = (full_name_size + (-full_name_size) % record_limit) // record_limit
        # Check which is smaller, thread batch size or thread size
        # Take the smaller of the two
        thread_count = thread_batch_size if thread_batch_size < thread_size else thread_size
        # Create a thread list
        t_list = []

        # Loop through the full name list
        for i in range(0, thread_batch_size, thread_size):
            # Account for last iteration, maximum thread (thread_size) not needed
            if thread_batch_size - i < thread_size:
                # Use only maximum thread needed
                thread_count = thread_batch_size - i

            # Loop through and execute the thread
            for j in range(thread_count):
                # Calculate full name start and end range
                full_name_start = (j + i) * record_limit
                # Calculate the precise end range for last iteration...
                # Because I can...
                if full_name_start + record_limit > full_name_size:
                    full_name_end = full_name_start + thread_count
                else:
                    full_name_end = full_name_start + record_limit

                # Create the thread
                t = threading.Thread(target=_read_metadata_thread,
                                     args=(self, metadata_type, full_name[ full_name_start : full_name_end ],))
                # Add it to a thread list
                t_list.append(t)
                # Start the thread
                t.start()

            # Wait for all threads to finish
            for t in t_list:
                t.join()

        return read_result_all


    def update_metadata(self, metadata):
        """Update Metadata

        Args:
            metadata (list): A complex list of dictionary for metadata
                component to update

        Returns:
            A complex list of dictionary for result of the metadata
            component update
        """

        # Create a new list to store all the update result
        update_result_all = []
        # Get the size of the metadata list
        metadata_size = len(metadata)
        # Limit for the metadata API function
        record_limit = 10

        # Loop through the metadata list 10 records at a time
        for i in range(0, metadata_size, record_limit):
            # Make request(s) to update metadata, 10 at a time
            update_result = self.service.updateMetadata(metadata=metadata[ i : i + record_limit ],
                                                        _soapheaders=self.soap_header)
            # Add the current update result to all the update result
            update_result_all.extend(update_result)

        return update_result_all

    def update_metadata_thread(self, metadata, thread=10):
        """Update Metadata

        Args:
            metadata (list): A complex list of dictionary for metadata
                component to update
            thread (int): The number of thread to use

        Returns:
            A complex list of dictionary for result of the metadata
                component update
        """

        def _update_metadata_thread(self, metadata):
            """Update Metadata

            Args:
                metadata (list): A complex list of dictionary for
                    metadata component to update

            Returns:
                A complex list of dictionary for result of the metadata
                    component update
            """

            # Make request(s) to update metadata, 10 at a time
            update_result = self.service.updateMetadata(metadata=metadata,
                                                        _soapheaders=self.soap_header)

            # Add the current update result to all the update result
            update_result_all.extend(update_result)

        # Create a new list to store all the update result
        update_result_all = []
        # Get the size of the metadata list
        metadata_size = len(metadata)
        # Limit for the metadata API function
        record_limit = 10

        # Thread size
        thread_size = thread
        # Calculate the thread batch size based on metadata API limit
        thread_batch_size = (metadata_size + (-metadata_size) % record_limit) // record_limit
        # Check which is smaller, thread batch size or thread size
        # Take the smaller of the two
        thread_count = thread_batch_size if thread_batch_size < thread_size else thread_size
        # Create a thread list
        t_list = []

        # Loop through the metadata list
        for i in range(0, thread_batch_size, thread_size):

            # Account for last iteration, maximum thread (thread_size) not needed
            if thread_batch_size - i < thread_size:
                # Use only maximum thread needed
                thread_count = thread_batch_size - i
            
            for j in range(thread_count):
                # Calculate metadata start and end range
                metadata_start = (j + i) * record_limit
                metadata_end = metadata_start + record_limit
                # Create the thread
                t = threading.Thread(target=_update_metadata_thread,
                                     args=(self, metadata[ metadata_start : metadata_end ],))
                # Add it to a thread list
                t_list.append(t)
                # Start the thread
                t.start()

            # Wait for all threads to finish
            for t in t_list:
                t.join()

        return update_result_all