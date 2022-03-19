import exceptions


class ExistsSessionException(exceptions.Exception):

    def __init__(self, message):
        self.message = message
