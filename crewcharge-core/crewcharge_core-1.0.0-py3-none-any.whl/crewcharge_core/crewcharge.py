import sys
import hashlib
import requests
import json

if sys.version_info < (3, 6):
    import sha3

crewcharge_end_point = "http://localhost:80"

def gen_hash(project_key, user_id):
    """
        The function to generates a uid_hashed for Crewcharge APIs (to comply with GDPR)
  
        Parameters:
            project_key: project_key is the unique project key of your Crewcharge project. Found at https://app.crewcharge.com/projects (and click on your project).

            user_id: user_id is your customer's user id inside your database. In case you don't have an id, pass their email.
          
        Returns:
            String: A hashed uid along with project key prefix_ encoded in SHA3-512.
    """
    try: 
        # create a sha3 hash object
        hash_sha3_512 = hashlib.new("sha3_512", str.encode(str(user_id)))
        # To test go to https://emn178.github.io/online-tools/sha3_512.html
        hash_digest = hash_sha3_512.hexdigest()
        hashed_uid = project_key + "_" + hash_digest
        return hashed_uid
    except Exception as er:
        print(er)
        return user_id


def attach_user_attributes(api_key, uid_hashed, attributes, privacy_preferences, test_user):
    """
        The function attaches a new user with Crewcharge or modifies the existing user preferences.

        Parameters:
            api_key (String) - Your API key within Crewcharge.
            
            uid_hashed (String) - Identifier of the user that needs to be a one-way hash. This must start with your Project key and be generated using genHash function

            attributes (Dictionary) - Contains information about the user.
            You can attach any attributes, but the needed ones are {@see recommended_user_attributes}

            privacy_preferences (Dictionary) - Refers to modifying user's preferences with collecting data on analytics, email, feedback, sms, etc. Valid values are {@see valid_privacy_preferences}

            test_user (Boolean) - Refers to whether the user must be attached as a test user within Crewcharge.

            For example,
            if you store { "id" : 1, "name": "Alice", "email": "alice@gmail.com" }

            DO NOT PASS 1, as the uid_hash, instead hash 1 and send it over.
            [GDPR Rules]
    """

    try: 
        attach_attributes_end_point = crewcharge_end_point + "/api/v1/attach_user_attributes"

        headers = {
        'api-key': api_key,
        'Content-Type': 'application/json',
        } 

        json_attributes_object = json.dumps(attributes, indent = 4) 
        json_privacy_preferences_object = json.dumps(privacy_preferences, indent = 4)

        payload = {
            "uid_hashed": uid_hashed,
            "attributes": json_attributes_object,
            "privacy_preferences": json_privacy_preferences_object,
            "test_user": test_user
        }

        response = requests.request("POST", attach_attributes_end_point, headers=headers, data=payload)

        return response.json()

    except ValueError as ve:
        return ("Invalid JSON returned")
    except requests.RequestException as reqEx:
        return (reqEx)

def log_trigger(analytics_tag, uid_hashed, trigger_key):
    """
        The function attaches a new user with Crewcharge or modifies the existing user preferences.

        Parameters:
            trigger_key (String) - the key you want to track (Obtain this from your Crewcharge Console).
            
            analytics_tag (String) - is your tag obtained for this project.

            uid_hashed (String) - Identifier of the user that needs to be a one-way hash. This must start with your Project key and be generated using genHash function
    """

    try: 
        log_trigger_end_point = crewcharge_end_point + "/api/v1/log"

        headers = {
        'Content-Type': 'application/json',
        } 

        payload = {
            "uid_hashed": uid_hashed,
            "analytics_tag": analytics_tag,
            "trigger_key": trigger_key
        }

        response = requests.post(url=log_trigger_end_point, headers=headers, json=payload)

        return response.json()

    except ValueError as ve:
        return ("Invalid JSON returned")
    except requests.RequestException as reqEx:
        return (reqEx)


recommended_user_attributes = {
    "pii_name": "pii_name",
    "pii_email": "pii_email",
    "pii_image": "pii_image",
    "locale": "locale"
}

## Please note, all values are in booleans.
valid_privacy_preferences = {
    "analytics": {
        "pii": "false"
    }, "feedback": {
        "email": "false",
        "push": "false",
        "sms": "false",
        "in_app": "true"
    }, "marketing": {
        "email": "false",
        "push": "false",
        "sms": "false",
        "in_app": "true",
    },
}
