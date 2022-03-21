from .modal_type_enum import *

class Modal:
    def __init__(
        self, message: str = "", type: MODAL_TYPE = MODAL_TYPE.SUCCESS, headline: str = "Hinweis"
    ):
        self.modal_type = type
        self.modal_msg = message
        self.modal_headline = headline

    def to_dict(self):
        tmp_dict = {
            "modal_type": self.modal_type.value,
            "modal_msg": self.modal_msg,
            "modal_headline": self.modal_headline,
        }
        return tmp_dict