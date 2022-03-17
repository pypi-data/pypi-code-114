import hashlib
import json
from datetime import datetime, timezone


def wrap_str(v):
    if isinstance(v, bool):
        return str(v).lower()
    return str(v)


def validate_checksum(
        request: dict,
        checksum: str,
        shared_secret: str,
        salt: str = "",
        time_delta: int = 5,
        use_time_component: bool = True,
) -> bool:
    """
    Use this method to validate a dict with a given checksum

    :param request: The dictionary with all parameters
    :param checksum: The given checksum to validate
    :param shared_secret: Shared secret the request is hashed with
    :param salt: Additional salt to use. Defaults to empty str
    :param time_delta: Time delta (+ and -) the requests should be valid, in seconds
    :param use_time_component: If specified False, time is not used for the protocol

    :return: bool
    """
    if use_time_component:
        # Get current (utc) timestamp
        current_timestamp = int(datetime.now(timezone.utc).timestamp())

    # Build sorted list
    sorted_request = [key + wrap_str(request[key]) for key in sorted(request)]

    # Build static_str
    static_str = "".join([str(x) for x in sorted_request])

    # Append with shared_secret
    static_str += shared_secret

    if use_time_component:
        # Iterate over the last +- time_delta timestamps
        for i in range(-time_delta, time_delta):
            tmp_timestamp = current_timestamp + i

            # Append static_str with timestamp
            not_so_static_str = static_str + str(tmp_timestamp)

            # Add salt and hash with SHA512
            hashed = hashlib.sha512((salt + not_so_static_str).encode("utf-8")).hexdigest()
            if hashed == checksum:
                return True
    else:
        # Add salt and hash with SHA512
        hashed = hashlib.sha512((salt + static_str).encode("utf-8")).hexdigest()
        if hashed == checksum:
            return True
    return False


def get_checksum(
        request: dict,
        shared_secret: str,
        use_time_component: bool = True,
        salt: str = ""
) -> str:
    """
    Use this method to retrieve a checksum of a given dict

    :param request: The dictionary with all parameters
    :param shared_secret: Shared secret the request is hashed with
    :param salt: Additional salt to use. Defaults to empty str
    :param use_time_component: If specified False, time is not used for the protocol

    :return: Checksum str
    """
    if use_time_component:
        # Get current (utc) timestamp
        current_timestamp = int(datetime.now(timezone.utc).timestamp())

    # Build sorted list
    sorted_request = [key + wrap_str(request[key]) for key in sorted(request)]

    # Build static_str
    static_str = "".join([str(x) for x in sorted_request])

    # Append with shared_secret
    static_str += shared_secret

    if use_time_component:
        # Append with timestamp
        static_str += str(current_timestamp)

    # Add salt and hash with SHA512
    hashed = hashlib.sha512((salt + static_str).encode("utf-8")).hexdigest()

    return hashed
