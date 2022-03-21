class IGIUserFriendlyException(Exception):
    """
    Base class for IGI custom excpetions with message suitable for end user.
    """
    pass


class IGIAggregateException(IGIUserFriendlyException):
    """
    Construct with args for the exceptions to be combined.
    """
    pass


class IGINoSupportedSheetsException(IGIUserFriendlyException):
    """
    Construct with args for the exceptions to be combined.
    """
    pass


def create_aggregate_ex(*exs: Exception) -> IGIAggregateException:
    msg = ", ".join(set(str(ex) for ex in exs))
    return IGIAggregateException(msg)
