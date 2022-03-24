

class HttpApiBaseException(Exception):
    def __init__(self, status_code):
        self.status_code = status_code
        super().__init__()

    def __str__(self):
        return str(self.status_code)



class Api4xxException(HttpApiBaseException):
    pass


class Api5xxException(HttpApiBaseException):
    pass


class Api404Exception(Api4xxException):
    def __init__(self):
        super().__init__(status_code=404)


class Api401Exception(Api4xxException):
    def __init__(self):
        super().__init__(status_code=401)


class Api500Exception(Api5xxException):
    def __init__(self):
        super().__init__(status_code=500)



def raise_the_desired_error(exception):
    if exception.response.status_code == 404:
        raise Api404Exception()
    elif exception.response.status_code == 500:
        raise Api500Exception()
    elif exception.response.status_code == 401:
        raise Api401Exception()

    raise HttpApiBaseException(status_code=exception.response.status_code)
