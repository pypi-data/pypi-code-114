import csv
from SFDCFW.Soap.Metadata import Metadata

class WorkflowRule:
    """Workflow Rule.
    """

    def __init__(self, access, wsdl):
        """Constructor.

        Args:
            access (tuple): The Salesforce session ID / access token and
                server URL / instance URL tuple.
            wsdl (str): The path to the WSDL file.
        """

        # Use the Metadata API
        self.metadata = Metadata(access, wsdl)

    def toggle_active(self, active, full_name=None):
        """(De)Activate specific Workflow Rule(s) for a given list of
           full name(s).

        Args:
            active (bool): A flag determine whether to activate or
                deactivate the Workflow Rule(s).
            full_name (list): A list of string(s) for the full name of
                the Workflow Rule to (de)activate. Will (de)activate all
                Workflow Rule(s) if no full name is passed.

        Returns:
            A complex list of dictionary for result of the Workflow
                Rule(s) (de)activation.
        """

        # Create the query
        query = [ { "type": "WorkflowRule" } ]

        # Get the list of Workflow Rule(s)
        workflow_rule_list = self.metadata.list_metadata(query)

        if full_name is not None:
            # Find full_name in workflow_rule_list
            # Loop through list of Workflow Rule(s) (workflow_rule_list) and find the requested (full_name) element
            workflow_rule_result = [workflow_rule for workflow_rule in workflow_rule_list if workflow_rule["fullName"] in full_name]
        else:
            workflow_rule_result = workflow_rule_list

        # Parse a list of full name from the Workflow Rule(s) result
        full_name_result = [workflow_rule["fullName"] for workflow_rule in workflow_rule_result]

        # Get the detail read result information from the full name
        read_result = self.metadata.read_metadata_thread(query[0]["type"], full_name_result)

        # Slice out the Workflow Rule(s) result that are (in)active
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
        update_result = self.metadata.update_metadata_thread(read_result)

        # Return the update result
        return update_result