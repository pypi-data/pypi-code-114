class SsoException(Exception):
    """
    自定义的SSO异常
    """

    def __init__(self, code):
        """
        使用指定的错误码引发异常
        :param code: 引发此异常的错误码
        """
        self.code = code

    def __str__(self):
        return '<ErrorCodes.%s: %s>' % (self.code.name, hex(self.code.value))

    def __repr__(self):
        return self.__str__()
