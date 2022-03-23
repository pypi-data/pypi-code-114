from hashlib import algorithms_available


class InvalidSeparator(Exception):
    """Exception raised for errors in the input value of separator attribute of StringSigner class.

    Args:
        message: explanation of the error
    """

    def __init__(self, message=None):
        self.message = (
            message
            or "The separator can't be neither alphanumeric nor '-' or '_' or '='."
        )
        super().__init__(self.message)


class InvalidAlgorithm(Exception):
    """Exception raised for errors in the input value of hash_algorithm attribute of StringSigner class.

    Args:
        message: explanation of the error
    """

    def __init__(self, message=None):
        self.message = message or "The hash_algorithm must be one of the following: "
        self.message += ", ".join(algorithms_available) + "."
        super().__init__(self.message)


class InvalidSaltLength(Exception):
    """Exception raised for errors in the input value of salt_length attribute of StringSigner class.

    Args:
        salt_length: input salt_length which caused the error
        message: explanation of the error
    """

    def __init__(self, message=None):
        self.message = message or "The salt_length need to be greater than zero."
        super().__init__(self.message)


class InvalidSignedString(Exception):
    """Exception raised for errors in the input value of signed_string into unsign method of StringSigner class.

    Args:
        message: explanation of the error
    """

    def __init__(self, message=None):
        self.message = message or "The signed_string need to be str."
        super().__init__(self.message)


class InvalidSignature(Exception):
    """Exception raised for errors in the signature validation of StringSigner class.

    Args:
        message: explanation of the error
    """

    def __init__(self, message=None):
        self.message = message or "The message signature doesn't match."
        super().__init__(self.message)


class InvalidSignatureStructure(Exception):
    """Exception raised for errors in the signature validation of StringSigner class.

    Args:
        message: explanation of the error
    """

    def __init__(self, message=None):
        self.message = message or "Wrong signature structure."
        super().__init__(self.message)


class InvalidSecretKey(Exception):
    """Exception raised for errors in the input value of secret_key attribute of StringSigner class.

    Args:
        message: explanation of the error
    """

    def __init__(self, message=None):
        self.message = message or "The secret_key must be a string and cannot be empty."
        super().__init__(self.message)


class InvalidSignatureType(Exception):
    """Exception raised for errors in the signature validation into _encode_signature method of StringSigner class.

    Args:
        message: explanation of the error
    """

    def __init__(self, message=None):
        self.message = message or "The signature must be in bytes format."
        super().__init__(self.message)


class InvalidString(Exception):
    """Exception raised for errors in the input value of _string into sign method of StringSigner class.

    Args:
        message: explanation of the error
    """

    def __init__(self, message=None):
        self.message = message or "The _string need to be a str."
        super().__init__(self.message)
