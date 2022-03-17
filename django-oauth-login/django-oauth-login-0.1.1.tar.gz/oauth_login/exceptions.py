class OAuthError(Exception):
    """Base class for OAuth errors"""

    pass


class OAuthStateMismatchError(OAuthError):
    pass


class OAuthCannotDisconnectError(OAuthError):
    pass


class OAuthUserAlreadyExistsError(OAuthError):
    pass
