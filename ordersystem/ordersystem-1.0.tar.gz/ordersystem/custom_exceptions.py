class OrderIncompleteException(Exception):
    def __init__(self, item):
        self.message = f"Unable to process: {item} is missing"
        self.status_code = 400
        super().__init__(self.message)

class TooManyItemsException(Exception):
    def __init__(self, item):
        self.message = (f"Unable to process: {item} cannot be ordered more than once")
        self.status_code = 400
        super().__init__(self.message)

class UnknownItemException(Exception):
    def __init__(self, item):
        self.message = f"Unable to process: {str(item)} is not on the menu"
        self.status_code = 400
        super().__init__(self.message)