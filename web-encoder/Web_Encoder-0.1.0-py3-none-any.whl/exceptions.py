class InvalidStringType(ValueError):
    """Exception raised for errors in the input value of _string into _string_to_bytes method of WebEncoder class.

    Args:
        message: explanation of the error
    """

    def __init__(self, message=None):
        self.message = message or "The _string need to be str type."
        super().__init__(self.message)


class InvalidBytesType(ValueError):
    """Exception raised for errors in the input value of _bytes into methods of WebEncoder class.

    Args:
        message: explanation of the error
    """

    def __init__(self, message=None):
        self.message = message or "The _bytes need to be bytes type."
        super().__init__(self.message)


class InvalidDataType(ValueError):
    """Exception raised for errors in the input value of data into encode method of WebEncoder class.

    Args:
        message: explanation of the error
    """

    def __init__(self, message=None):
        self.message = message or "The data need to be str type."
        super().__init__(self.message)


class InvalidEncodedDataType(ValueError):
    """Exception raised for errors in the input value of encoded_data into decode method of WebEncoder class.

    Args:
        message: explanation of the error
    """

    def __init__(self, message=None):
        self.message = message or "The encoded_data need to be str type."
        super().__init__(self.message)


class DataDecodeError(Exception):
    """Exception raised for data decoding error in _bytes_to_string of WebEncoder class.

    Args:
        message: explanation of the error
    """

    def __init__(self, message=None):
        self.message = message or "Could not decode the message."
        super().__init__(self.message)


class CannotBeCompressed(Exception):
    """Exception raised for errors in the _compress_data method of WebEncoder class.

    Args:
        message: explanation of the error
    """

    def __init__(self, message=None):
        self.message = message or "The data cannot be compressed."
        super().__init__(self.message)


class CannotBeDecompressed(Exception):
    """Exception raised for errors in the _decompress_data method of WebEncoder class.

    Args:
        message: explanation of the error
    """

    def __init__(self, message=None):
        self.message = message or "The data cannot be decompressed."
        super().__init__(self.message)
