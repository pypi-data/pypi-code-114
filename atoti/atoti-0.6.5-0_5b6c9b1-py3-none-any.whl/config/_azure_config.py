from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Optional

from atoti_core import keyword_only_dataclass

from ._config import Config, pop_optional_sub_config
from .key_pair import KeyPair


@keyword_only_dataclass
@dataclass(frozen=True)
class AzureKeyPair(KeyPair):
    """The key pair to use for client side encryption.

    Warning:

        Each encrypted blob must have the metadata attribute ``unencrypted_content_length`` with the unencrypted file size.
        If this is not set, an :guilabel:`Issue while downloading` error will occur.

    Example:

        >>> config = {
        ...     "azure": {
        ...         "client_side_encryption": {
        ...             "key_pair": {
        ...                 "key_id": "some key ID",
        ...                 "public_key": "some public key",
        ...                 "private_key": "some private key",
        ...             }
        ...         }
        ...     }
        ... }

        .. doctest::
            :hide:

            >>> validate_config(config)

    """

    key_id: str
    """The ID of the key used to encrypt the blob."""


@keyword_only_dataclass
@dataclass(frozen=True)
class AzureClientSideEncryptionConfig(Config):
    """The client side encryption configuration to use when loading data from Azure."""

    key_pair: AzureKeyPair

    @classmethod
    def _from_mapping(
        cls, mapping: Mapping[str, Any]
    ) -> AzureClientSideEncryptionConfig:
        data = dict(mapping)
        return cls(
            key_pair=AzureKeyPair._from_mapping(data.pop("key_pair")),
            **data,
        )


@keyword_only_dataclass
@dataclass(frozen=True)
class AzureConfig(Config):
    """The Azure configuration.

    Note:
        This requires the :mod:`atoti-azure <atoti_azure>` plugin.

    """

    client_side_encryption: Optional[AzureClientSideEncryptionConfig] = None

    @classmethod
    def _from_mapping(cls, mapping: Mapping[str, Any]) -> AzureConfig:
        data = dict(mapping)
        return cls(
            client_side_encryption=pop_optional_sub_config(
                data,
                attribute_name="client_side_encryption",
                sub_config_class=AzureClientSideEncryptionConfig,
            ),
            **data,
        )
