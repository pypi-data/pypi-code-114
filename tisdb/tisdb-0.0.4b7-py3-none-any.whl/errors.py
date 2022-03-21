# -*- coding: utf-8 -*-


class BaseInfo(object):
    """Returning result info

    Args:
        object ([type]): [description]
    """

    SUBCODE: int = 10200
    STATUS: str = u"ok"

    def __init__(self, message="", subcode=SUBCODE, status=STATUS, **kwargs):
        super().__init__()
        self.status = status or self.STATUS
        self.subcode = subcode or self.SUBCODE
        self.info = kwargs.get("info", {})
        self.info["message"] = message


class BaseError(Exception):
    """Raised when a error occur.

    Args:
        Exception ([type]): [description]
    """

    SUBCODE = 10501
    STATUS = u"TISDB Error"

    def __init__(self, message="", subcode=SUBCODE, status=STATUS, *args, **kwargs):
        self.status = status or self.STATUS
        self.subcode = subcode or self.SUBCODE
        self.error = kwargs.get("error", {})
        self.info = kwargs.get("info", {})
        Exception.__init__(self, message, *args)


class FakeError(BaseError):
    """Fake error for some situation to step in error handler"""

    SUBCODE = 10209
    STATUS = u"TISDB Fake Error"


class ParamError(BaseError):
    """Params error"""

    SUBCODE = 10422
    STATUS = u"TISDB Invalid Parameter Error"
