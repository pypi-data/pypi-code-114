from .alert_type_enum import ALERT_TYPE

class Alert:
    def __init__(self, message: str = "", type:ALERT_TYPE=ALERT_TYPE.SUCCESS):
        self.alert_type = type
        self.alert_msg = message

    def to_dict(self):
        tmp_dict = {"alert_type": self.alert_type.value, "alert_msg": self.alert_msg}
        return tmp_dict