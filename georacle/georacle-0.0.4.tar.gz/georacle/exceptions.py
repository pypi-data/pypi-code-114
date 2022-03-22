class APIError(Exception):
    """Generic API Error"""

    pass


class RateLimitError(APIError):
    """Client Rate Limited"""

    pass


class APIKeyError(APIError):
    """Authentication Error"""

    pass


class EmptyResponseError(APIError):
    """Empty API Response"""

    pass


class EncodingError(APIError):
    """Invalid Encoding"""

    pass


class BoundingBoxError(Exception):
    """Invalid Bounding Box Definition"""

    pass
