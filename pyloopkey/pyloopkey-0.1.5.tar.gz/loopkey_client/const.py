"""Constants to be used in loopkey client directory."""
import enum

# Constants
ACTION = "action"
PHONE = "phone"
PASS = "pass"
AUTHORIZATION = "authorization"
BUFFER = 5
DOOR_ID = "doorId"
NAME = "name"
SURNAME = "surname"
PASSCODE = "passcode"
VALUE = "value"
GATEWAY = "gateway"
PERMISSION_TYPE = "permissionType"
INTEGRATION = "loopkey"
CODE_DEFINITION = "code_definition"
STATE_UNAVAILABLE = "unavailable"
STATE_LOCKED = "locked"
STATE_UNLOCKED = "unlocked"
REQUEST_DATEFORMAT = "%Y-%m-%dT%H:%M"

# Loopkey environment variables
LOOPKEY_USERNAME = "LOOPKEY_USERNAME"
LOOPKEY_PHONE = "LOOPKEY_PHONE"
LOOPKEY_PASSWORD = "LOOPKEY_PASSWORD"

# Loopkey API_URLs
API_BASE_URL = "https://api.loopkey.com.br/"
API_LOGIN_URL = API_BASE_URL + "login"
API_SET_PASSCODE = API_BASE_URL + "permission/add/passcode"
API_REMOVE_PASSCODE = API_BASE_URL + "permission/remove"
API_GET_EVENTS = API_BASE_URL + "events/door"
API_REGULAR_DOOR = API_BASE_URL + "door/{}"

EVENTS = {
    "set": "permissionCreate",
    "unset": "permissionRemove",
    "unlock": "unlockCommand",
    "failed": "alarmUnlockDenied"
}

# Loopkey Corp endpoints
API_ACCESS_URL = API_BASE_URL + "access"
API_LIST_CORPS = API_BASE_URL + "corps"
API_CORP = API_BASE_URL + "corp/{}"
API_SITE = API_BASE_URL + "corp/site/{}"
API_ACCESS_GROUP = API_BASE_URL + "corp/site/accessGroup/{}"
API_DOOR = API_BASE_URL + "corp/site/door/{}"
API_GATEWAY = API_BASE_URL + "corp/site/gateway/{}"
API_BOOKING = API_BASE_URL + "corp/site/booking/{}"
API_USER = API_BASE_URL + "corp/user/{}"
API_CORP_DOOR_COMMANDS = API_BASE_URL + "corp/site/door/send/{}"
API_ROLE = API_BASE_URL + "corp/role/{}"


class Actions(enum.Enum):
    SET = "set"
    UNSET = "unset"
