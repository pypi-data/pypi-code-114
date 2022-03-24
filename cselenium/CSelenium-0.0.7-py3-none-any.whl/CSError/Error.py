'''

    自定义异常
'''

class Error(Exception):
    pass


class DriverError(Error):
    def __init__(self,err_info:str):
        self.__err_info = err_info

    def __str__(self):
        return repr(self.__err_info)



