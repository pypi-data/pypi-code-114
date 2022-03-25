class FullyQualifiedIdentifier(str):
    """
    String class with case-insensitive comparison operations

    Examples
    --------
    >>> original_id = FullyQualifiedIdentifier("org.silastandard/core/SiLAService/v1")
    >>> lowercase_id = FullyQualifiedIdentifier("org.silastandard/core/silaservice/v1")
    >>> original_id == lowercase_id
    True
    """

    def __eq__(self, other):
        if isinstance(other, str):
            return self.lower() == other.lower()

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return f"{self.__class__.__name__}({super().__repr__()})"

    def __hash__(self):
        return super().lower().__hash__()
