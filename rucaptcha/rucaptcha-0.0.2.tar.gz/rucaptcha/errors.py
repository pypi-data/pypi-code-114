__all__ = [
    "RucaptchaError",
    "ConfigurationError",
    "ApiError",
    "ResultNotReady",
    "ResultTimeout",
    "ZeroBalance",
    "ServiceIsBusy",
    "ServiceUnexpectedError",
]


class RucaptchaError(Exception):
    pass


class ConfigurationError(RucaptchaError):
    pass


class ResultTimeout(RucaptchaError):
    pass


class ServiceUnexpectedError(RucaptchaError):
    pass


class ApiError(RucaptchaError):
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


class ZeroBalance(ApiError):
    pass


class ServiceIsBusy(ApiError):
    pass
