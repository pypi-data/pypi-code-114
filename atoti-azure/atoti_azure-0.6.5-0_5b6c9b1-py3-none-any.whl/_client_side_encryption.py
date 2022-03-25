from atoti_core import deprecated

from .client_side_encryption import AzureKeyPair


def create_azure_key_pair(
    *, key_id: str, private_key: str, public_key: str
) -> AzureKeyPair:
    deprecated("`create_azure_key_pair()` is deprecated, use `AzureKeyPair()` instead.")
    return AzureKeyPair(key_id=key_id, private_key=private_key, public_key=public_key)
