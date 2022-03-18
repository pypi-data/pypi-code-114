import csv
#
from SFDCFW.Soap.Metadata import Metadata

class CustomField(Metadata):
    """Custom Field.
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

    def toggle_lookup_filter_parallel(self, active, thread=20, process=10):
        """(De)Activate Lookup Filter(s) Parallel.

        Args:
            active (bool): A flag determine whether to activate or deactivate
                the Lookup Filter(s).
            thread (int): The number of thread to use
            process (int): The number of process to use

        Returns:
            A complex list of dictionary for result of the Lookup Filter(s)
                (de)activation.
        """

        # Create the query
        query = [{"type": "CustomField"}]

        # Get the list of Custom Field(s)
        custom_field_list = self.metadata.list_metadata(query)

        # Parse a list of full name from the Custom Field(s) result
        full_name_result = [custom_field["fullName"] for custom_field in custom_field_list]

        # Get the detail read result information from the full name
        read_result = self.metadata.read_metadata_thread(query[0]["type"], full_name_result, thread=thread)

        # Slice out the Custom Field(s) result that have Lookup Filter(s)
        # Look for those that are (in)active
        if active:
            lookup_filter_list = [record for record in read_result if record["fullName"] and record["lookupFilter"] and not record["lookupFilter"]["active"]]
        else:
            lookup_filter_list = [record for record in read_result if record["fullName"] and record["lookupFilter"] and record["lookupFilter"]["active"]]

        # Loop through the result and update the active status
        for record in lookup_filter_list:
            record["lookupFilter"]["active"] = active

        a = {
            'fullName': 'AcctPlan_White_Space__c.Account_BU__c',
            'businessOwnerGroup': None,
            'businessOwnerUser': None,
            'businessStatus': None,
            'caseSensitive': None,
            'customDataType': None,
            'defaultValue': None,
            'deleteConstraint': 'Restrict',
            'deprecated': None,
            'description': 'Account/BU that this White Space record is related to.',
            'displayFormat': None,
            'encryptionScheme': None,
            'escapeMarkup': None,
            'externalDeveloperName': None,
            'externalId': False,
            'fieldManageability': None,
            'formula': None,
            'formulaTreatBlanksAs': None,
            'inlineHelpText': 'Search for Account/BU entered on the Account/BU Tab',
            'isAIPredictionField': None,
            'isConvertLeadDisabled': None,
            'isFilteringDisabled': None,
            'isNameField': None,
            'isSortingDisabled': None,
            'label': 'Account/BU',
            'length': None,
            'lookupFilter': {
                'active': False,
                'booleanFilter': None,
                'description': None,
                'errorMessage': None,
                'filterItems': [
                    {
                        'field': 'Account_BU__c.AcctPlan_ParentPlan__c',
                        'operation': 'equals',
                        'value': None,
                        'valueField': '$Source.Account_Plan__c'
                    }
                ],
                'infoMessage': None,
                'isOptional': False
            },
            'maskChar': None,
            'maskType': None,
            'metadataRelationshipControllingField': None,
            'populateExistingRows': None,
            'precision': None,
            'referenceTargetField': None,
            'referenceTo': 'Account_BU__c',
            'relationshipLabel': 'Account Plan White Space',
            'relationshipName': 'AcctPlan_White_Space',
            'relationshipOrder': None,
            'reparentableMasterDetail': None,
            'required': True,
            'restrictedAdminField': None,
            'scale': None,
            'securityClassification': None,
            'startingNumber': None,
            'stripMarkup': None,
            'summarizedField': None,
            'summaryFilterItems': [],
            'summaryForeignKey': None,
            'summaryOperation': None,
            'trackFeedHistory': None,
            'trackHistory': True,
            'trackTrending': False,
            'translateData': None,
            'type': 'Lookup',
            'unique': None,
            'valueSet': None,
            'visibleLines': None,
            'writeRequiresMasterRead': None
        }

        b = { k: v for k, v in a.items() if v is not None }

        # # Update the metadata
        update_result = self.metadata.update_metadata_thread([b])

        # Return the update result
        return update_result