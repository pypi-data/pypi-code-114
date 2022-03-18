import json

from SFDCFW.Rest.SObject import SObject
from SFDCFW.Constant.Constant import HTTP_GET

class User(SObject):
    """User API
    """

    def assign_profile(self, username, profile_name):
        """Assign Profile

        Args:
            username (str): The Salesforce username to assign
            profile_name: (str): The Salesforce Profile name to assign

        Returns:
            True or False for the success or failure of the update
        """

        # User query
        user_query = "SELECT Id FROM User WHERE Username='" + username + "' and IsActive=true"
        # Create the User request URL
        user_relative_url = "/query/?q=" + user_query
        # Send the request for the User
        r = self.send(HTTP_GET, user_relative_url, None)

        if r.status_code == 200:
            # JSONify the return User data
            user_data = json.loads(r.text)

        # Profile query
        profile_query = "SELECT Id,Name FROM Profile WHERE Name='" + profile_name + "'"
        # Create the Profile request URL
        profile_relative_url = "/query/?q=" + profile_query
        # Send the request for the Profile
        r = self.send(HTTP_GET, profile_relative_url, None)

        if r.status_code == 200:
            # JSONify the return Profile data
            profile_data = json.loads(r.text)

        # Update User
        # Get the User ID
        user_id = user_data["records"][0]["Id"]
        # Get the Profile ID
        profile_id = profile_data["records"][0]["Id"]

        # Create payload
        payload = {
            "ProfileId": profile_id
        }

        # Execute the update
        r = self.User.update(user_id, payload)

        if r.status_code == 204:
            return True
        else:
            return False

    
    def assign_permission_set(self, username, permission_set_name):
        """Assign Permission Set

        Args:
            username (str): The Salesforce username to assign
            permission_set_name: (str): The Salesforce Permission Set name
                (API Name) to assign

        Returns:
            True or False for the success or failure of the update
        """
        
        # User query
        user_query = "SELECT Id FROM User WHERE Username='" + username + "' and IsActive=true"
        # Create the User request URL
        user_relative_url = "/query/?q=" + user_query
        # Send the request for the User
        r = self.send(HTTP_GET, user_relative_url, None)

        if r.status_code == 200:
            # JSONify the return User data
            user_data = json.loads(r.text)

        # Permission query
        permission_set_query = "SELECT Id FROM PermissionSet WHERE Name='" + permission_set_name + "'"
        # Create the Permission Set request URL
        permission_set_relative_url = "/query/?q=" + permission_set_query
        # Send the request for the Permission Set
        r = self.send(HTTP_GET, permission_set_relative_url, None)

        if r.status_code == 200:
            # JSONify the return Permission Set data
            permission_set_data = json.loads(r.text)

        # Update Permission Set Assignment
        # Get the User ID
        user_id = user_data["records"][0]["Id"]
        # Get the Profile ID
        permission_set_id = permission_set_data["records"][0]["Id"]

        # Create payload
        payload = {
            "AssigneeId": user_id,
            "PermissionSetId": permission_set_id
        }

        # Execute the update
        r = self.PermissionSetAssignment.create(payload)

        # print("Status Code: {}".format(r.status_code))
        # print("Message: {}".format(r.text))

        if r.status_code == 201:
            return True
        else:
            return False