# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AuditLogConfigLogType',
    'EndpointNetworkType',
]


class AuditLogConfigLogType(str, Enum):
    """
    The log type that this config enables.
    """
    LOG_TYPE_UNSPECIFIED = "LOG_TYPE_UNSPECIFIED"
    """
    Default case. Should never be this.
    """
    ADMIN_READ = "ADMIN_READ"
    """
    Admin reads. Example: CloudIAM getIamPolicy
    """
    DATA_WRITE = "DATA_WRITE"
    """
    Data writes. Example: CloudSQL Users create
    """
    DATA_READ = "DATA_READ"
    """
    Data reads. Example: CloudSQL Users list
    """


class EndpointNetworkType(str, Enum):
    """
    Type of the network where the endpoint is located. Applicable only to source endpoint, as destination network type can be inferred from the source.
    """
    NETWORK_TYPE_UNSPECIFIED = "NETWORK_TYPE_UNSPECIFIED"
    """
    Default type if unspecified.
    """
    GCP_NETWORK = "GCP_NETWORK"
    """
    A network hosted within Google Cloud Platform. To receive more detailed output, specify the URI for the source or destination network.
    """
    NON_GCP_NETWORK = "NON_GCP_NETWORK"
    """
    A network hosted outside of Google Cloud Platform. This can be an on-premises network, or a network hosted by another cloud provider.
    """
