
class ApiBaseException(Exception):

    def __init__(self, original_exception, message = None):
        self.message = message
        self.original_exception = original_exception
        super().__init__(self.message or "ApiBaseException")

    def __str__(self):
        return self.message or self.original_exception.message
