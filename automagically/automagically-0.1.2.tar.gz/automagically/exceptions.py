class AutomagicallyError(Exception):
    def __init__(self, message, error_code, status_code, support_id, method, url):
        self.message = message
        self.error_code = error_code
        self.status_code = status_code
        self.support_id = support_id
        self.method = method
        self.url = url


class AutomagicallyAuthenticationError(Exception):
    pass


class AutomagicallyPermissionError(Exception):
    pass


class AutomagicallyServicesTransactionLimitError(Exception):
    pass


class DeserializeException(Exception):
    def __init__(self, value: str) -> None:
        self.value = value
        super().__init__(f"Could not deserializer json value: {value}")
