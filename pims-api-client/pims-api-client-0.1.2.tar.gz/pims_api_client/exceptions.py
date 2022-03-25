import httpx


class HttpBaseException(Exception):
    def __init__(self, original_exception, message=None):
        self.message = message
        self.original_exception = original_exception
        super().__init__()

    def __str__(self):
        return self.message


class HttpConnectionFailed(HttpBaseException):
    pass


class HttpRequestError(HttpBaseException):
    pass


class HttpApiBaseException(HttpBaseException):
    def __init__(self, original_exception, message=None):
        self.status_code = original_exception.response.status_code
        super().__init__(original_exception=original_exception, message=message)

    def __str__(self):
        return str(self.status_code)


class Api4xxException(HttpApiBaseException):
    pass


class Api5xxException(HttpApiBaseException):
    pass


class Api404Exception(Api4xxException):
    pass


class Api401Exception(Api4xxException):
    pass


class Api500Exception(Api5xxException):
    pass



def raise_the_desired_api_error(exception):
    if exception.response.status_code == 404:
        raise Api404Exception(exception, message="404 не найдено")
    elif exception.response.status_code == 401:
        raise Api401Exception(exception, message="срок действия токена истек")
    elif exception.response.status_code == 500:
        raise Api500Exception(exception)
