class ApiV5Error(ValueError):
    """Any problems get thrown as ApiV5Error exceptions with the relevant info inside"""

    def __init__(self, result, data=None):
        """
        Init ApiV5Error
        :params result : requests result
        :params data: custom data
        """
        super(ApiV5Error, self).__init__(result and getattr(result, "reason", None))

        self.result = result
        self.data = data
        self.error_message = (getattr(result, "reason", "ApiV5Error Error"),)
        self.status_code = (getattr(result, "status_code", ""),)
        self.method = (getattr(result.request, "method", ""),)
        self.url = (getattr(result.request, "url", ""),)
        self.path_url = (getattr(result.request, "path_url", ""),)
        self.headers = (getattr(result.request, "headers", ""),)
        self.body = (getattr(result.request, "body", ""),)
        self.reason = (getattr(result, "content", ""),)
        self.tdata = str(data)

    def __str__(self):
        return str(self.__dict__)


class ApiV5NoConfig(Exception):
    """no client_id or client_secret were passed to the client"""


class ApiV5IncorrectMethod(Exception):
    """ "Incorrect Method: only POST,GET,PATCH,PUT,DELETE authorized."""


class ApiV5Timeout(Exception):
    """socket timeouts, sslerror, and 504"""


class ApiV5AuthenticationError(Exception):
    """Unable to get an token"""


class ApiV5ConnectionError(Exception):
    """Connection Error, example: error with domain"""


class Apiv5ExceptionError(Exception):
    """Generic exception error"""


class Apiv5ValueError(Exception):
    """Value Error"""


class ApiV5BadRequest(ApiV5Error):
    """most 40X results and 501 results"""


class ApiV5NotFound(ApiV5Error):
    """404 and 410 results"""


class ApiV5Unauthorized(ApiV5Error):
    """401 Unauthorized errors"""


class ApiV5Conflict(ApiV5Error):
    """409 conflict errors"""


class ApiV5ServerError(ApiV5Error):
    """most 500 errors"""


class ApiV5RateLimited(ApiV5Error):
    """exception for when we're rate limited"""


class ApiV5Forbidden(ApiV5Error):
    """403 Forbidden"""
