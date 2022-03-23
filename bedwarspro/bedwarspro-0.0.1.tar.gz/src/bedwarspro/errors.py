class BedwarsProException(Exception):
    """Base exception. This can be used to catch all errors from this library """


class APIError(BedwarsProException):
    """ Raised for errors """

    def __init__(self, message):
        self.text = message
        super().__init__(self.text)
