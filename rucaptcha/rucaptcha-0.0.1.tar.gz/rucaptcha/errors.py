__all__ = [
    "RucaptchaError",
    "ConfigurationError",
    "ApiError",
    "ResultNotReady",
    "ResultTimeout",
]


class RucaptchaError(Exception):
    pass


class ConfigurationError(Exception):
    pass


class ApiError(Exception):
    def __init__(self, error_code, error_description=None):
        self.error_code = error_code
        self.error_description = error_description
        if error_description:
            msg = "{}: {}".format(error_code, error_description)
        else:
            msg = error_code
        super().__init__(msg)


class ResultNotReady(ApiError):
    pass


class ResultTimeout(RucaptchaError):
    pass
