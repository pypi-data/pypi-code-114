"""
Validation Rule
"""

import csv
from SFDCFW.Soap.Metadata import Metadata

class ValidationRule(Metadata):
    """Validation Rule.
    """

    def __init__(self, access, wsdl):
        """Constructor.

        Args:
            access (tuple): The Salesforce session ID / access token and server
                URL / instance URL tuple.
            wsdl (str): The path to the WSDL file.
        """

        # Use the Metadata API
        self.metadata = Metadata(access, wsdl)


    def get(self, active=None, full_name=None):
        """
        """
        pass


    def toggle_active(self, active, full_name=None):
        """(De)Activate specific Validation Rule(s) for a given list of full name(s).

        Args:
            active (bool): A flag determine whether to activate or deactivate
                the Validation Rule(s).
            full_name (list): A list of string(s) for the full name of the
                Validation Rule to (de)activate. Will (de)activate all
                Validation Rule(s) if no full name is passed.

        Returns:
            A complex list of dictionary for result of the Validation Rule(s)
                (de)activation.
        """

        # Create the query
        query = [{"type": "ValidationRule"}]

        # Get the list of Valiation Rule(s)
        validation_rule_list = self.metadata.list_metadata(query)
        # print(validation_rule_list)

        if full_name is not None:
            # Find full_name in validation_rule_list
            # Loop through list of Validation Rule(s) (validation_rule_list) and find the requested (full_name) element
            validation_rule_result = [validation_rule for validation_rule in validation_rule_list if validation_rule["fullName"] in full_name]
        else:
            validation_rule_result = validation_rule_list

        # Parse a list of full name from the Validation Rule(s) result
        full_name_result = [validation_rule["fullName"] for validation_rule in validation_rule_result]

        # Get the detail read result information from the full name
        read_result = self.metadata.read_metadata(query[0]["type"], full_name_result)

        # Slice out the Validation Rule(s) result that are (in)active
        if active:
            read_result[:] = [record for record in read_result if not record["active"]]
        elif not active:
            read_result[:] = [record for record in read_result if record["active"]]

        # Loop through the result and update the active status
        for record in read_result:
            if active:
                record["active"] = True
            elif not active:
                record["active"] = False

        # Update the metadata
        update_result = self.metadata.update_metadata(read_result)

        # Return the update result
        return update_result