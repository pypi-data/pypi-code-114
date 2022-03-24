""" Utils for string validation for user input """
import re
import string
from dataclasses import dataclass
from typing import Optional


def validate_alphanumeric_dash_characters(text: str) -> bool:
    """ Validates lowercase alphanumeric with a dash """
    return re.match(r'[a-z\-]+', text) is not None  # type: ignore


@dataclass
class StringVerificationResult():
    """ Used to return the result of a string verification

    Overrides __len__ to be truthy based on validity
    Overrides __eq__ to cast when being compared to bools
    """
    valid: bool
    message: Optional[str]

    def __bool__(self) -> bool:
        return self.valid

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, bool):
            return bool(self) == __o
        return super().__eq__(__o)


def rfc_verification(
    text: str,
    length: int,
    special_characters: str,
    start_alnum_verification: bool = True,
    end_alnum_verification: bool = True,
) -> StringVerificationResult:
    """Does General RFC Verification with Parameters

    Args:
        text: The text to verify
        length: The maximum length allowed for the string
        special_characters: Regex Escaped Special Characters to allow

    Returns:
        Returns a truthy StringVerificationResult with possible error messages
    """
    if len(text) > length or len(text) == 0:
        return StringVerificationResult(
            False,
            f'Name must be less than {length} characters',
        )
    valid_characters = f'^[a-z0-9{special_characters}]*'

    if re.fullmatch(valid_characters, text) is None:
        return StringVerificationResult(
            False,
            f'Valid characters are only regex [{string.ascii_lowercase}{string.digits}{special_characters}]',
        )

    if start_alnum_verification and not text[0].isalnum():
        return StringVerificationResult(
            False,
            'The first character must be alphanumeric',
        )
    if end_alnum_verification and not text[-1].isalnum():
        return StringVerificationResult(
            False,
            'The last character must be alphanumeric',
        )

    return StringVerificationResult(True, None)


def validate_rfc1123_name(text: str) -> StringVerificationResult:
    """
    Ensures that secret names are valid based on k8s rfc1123 spec

        contain at most 63 characters
        contain only lowercase alphanumeric characters or '-'
        start with an alphanumeric character
        end with an alphanumeric character
    """
    return rfc_verification(text=text, length=63, special_characters=r'\-')


def validate_dns_subdomain_name(text: str) -> StringVerificationResult:
    """
    Ensures that secret names are valid based on k8s rfc1123 spec

        contain no more than 253 characters
        contain only lowercase alphanumeric characters, '-' or '.'
        start with an alphanumeric character
        end with an alphanumeric character
    """
    return rfc_verification(text=text, length=253, special_characters=r'\-\.')


def validate_secret_name(secret_name: str) -> bool:
    """
    Ensures that secret names are valid based on k8s spec

        contain no more than 253 characters
        contain only lowercase alphanumeric characters, '-' or '.'
        start with an alphanumeric character
        end with an alphanumeric character
    """
    verification_result = validate_dns_subdomain_name(text=secret_name)
    if not verification_result:
        print(verification_result.message)
        return False
    return True


def validate_secret_key(secret_key: str) -> bool:
    """
    Ensures that secret keys are valid based on k8s spec

        contain no more than 253 characters
        contain only alphanumeric characters, '-' or '.' or '_'
    """
    verification_result = rfc_verification(
        text=secret_key,
        length=253,
        special_characters=r'\-\._A-Z',
        start_alnum_verification=False,
        end_alnum_verification=False,
    )
    if not verification_result:
        print(verification_result.message)
        return False
    return True


def validate_simple_absolute_directory(path: str) -> bool:
    """
    Ensures that path is simple

        contain only alphanumeric characters, '-' or '.' or '_' or '/'
        starts with '/'
    """
    verification_result = rfc_verification(
        text=path,
        length=253,
        special_characters=r'\-\._/',
        start_alnum_verification=False,
        end_alnum_verification=False,
    )
    if not verification_result:
        print(verification_result.message)
        return False
    if path[0] != '/':
        print("Path must be absolute and start with '/'\n")
        return False

    return True


def validate_simple_absolute_filename(path: str) -> bool:
    """
    Ensures that path is simple

        contain only alphanumeric characters, '-' or '.' or '_' or '/'
        starts with '/'
    """
    verification_result = rfc_verification(
        text=path,
        length=253,
        special_characters=r'\-\._/',
        start_alnum_verification=False,
        end_alnum_verification=False,
    )
    if not verification_result:
        print(verification_result.message)
        return False
    if path[0] != '/':
        print("Path must be absolute and start with '/'\n")
        return False
    if path[-1] == '/':
        print('Must end with a valid filename')
        return False

    return True
