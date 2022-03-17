# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ChangeStatus',
    'DnsKeySpecAlgorithm',
    'DnsKeySpecKeyType',
    'ManagedZoneDnsSecConfigNonExistence',
    'ManagedZoneDnsSecConfigState',
    'ManagedZoneForwardingConfigNameServerTargetForwardingPath',
    'ManagedZoneVisibility',
    'PolicyAlternativeNameServerConfigTargetNameServerForwardingPath',
    'ResponsePolicyRuleBehavior',
]


class ChangeStatus(str, Enum):
    """
    Status of the operation (output only). A status of "done" means that the request to update the authoritative servers has been sent, but the servers might not be updated yet.
    """
    PENDING = "PENDING"
    DONE = "DONE"


class DnsKeySpecAlgorithm(str, Enum):
    """
    String mnemonic specifying the DNSSEC algorithm of this key.
    """
    RSASHA1 = "RSASHA1"
    RSASHA256 = "RSASHA256"
    RSASHA512 = "RSASHA512"
    ECDSAP256SHA256 = "ECDSAP256SHA256"
    ECDSAP384SHA384 = "ECDSAP384SHA384"


class DnsKeySpecKeyType(str, Enum):
    """
    Specifies whether this is a key signing key (KSK) or a zone signing key (ZSK). Key signing keys have the Secure Entry Point flag set and, when active, are only used to sign resource record sets of type DNSKEY. Zone signing keys do not have the Secure Entry Point flag set and are used to sign all other types of resource record sets.
    """
    KEY_SIGNING = "KEY_SIGNING"
    ZONE_SIGNING = "ZONE_SIGNING"


class ManagedZoneDnsSecConfigNonExistence(str, Enum):
    """
    Specifies the mechanism for authenticated denial-of-existence responses. Can only be changed while the state is OFF.
    """
    NSEC = "NSEC"
    NSEC3 = "NSEC3"


class ManagedZoneDnsSecConfigState(str, Enum):
    """
    Specifies whether DNSSEC is enabled, and what mode it is in.
    """
    OFF = "OFF"
    """
    DNSSEC is disabled; the zone is not signed.
    """
    ON = "ON"
    """
    DNSSEC is enabled; the zone is signed and fully managed.
    """
    TRANSFER = "TRANSFER"
    """
    DNSSEC is enabled, but in a "transfer" mode.
    """


class ManagedZoneForwardingConfigNameServerTargetForwardingPath(str, Enum):
    """
    Forwarding path for this NameServerTarget. If unset or set to DEFAULT, Cloud DNS makes forwarding decisions based on IP address ranges; that is, RFC1918 addresses go to the VPC network, non-RFC1918 addresses go to the internet. When set to PRIVATE, Cloud DNS always sends queries through the VPC network for this target.
    """
    DEFAULT = "DEFAULT"
    """
    Cloud DNS makes forwarding decisions based on address ranges; that is, RFC1918 addresses forward to the target through the VPC and non-RFC1918 addresses forward to the target through the internet
    """
    PRIVATE = "PRIVATE"
    """
    Cloud DNS always forwards to this target through the VPC.
    """


class ManagedZoneVisibility(str, Enum):
    """
    The zone's visibility: public zones are exposed to the Internet, while private zones are visible only to Virtual Private Cloud resources.
    """
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"


class PolicyAlternativeNameServerConfigTargetNameServerForwardingPath(str, Enum):
    """
    Forwarding path for this TargetNameServer. If unset or set to DEFAULT, Cloud DNS makes forwarding decisions based on address ranges; that is, RFC1918 addresses go to the VPC network, non-RFC1918 addresses go to the internet. When set to PRIVATE, Cloud DNS always sends queries through the VPC network for this target.
    """
    DEFAULT = "DEFAULT"
    """
    Cloud DNS makes forwarding decision based on IP address ranges; that is, RFC1918 addresses forward to the target through the VPC and non-RFC1918 addresses forward to the target through the internet
    """
    PRIVATE = "PRIVATE"
    """
    Cloud DNS always forwards to this target through the VPC.
    """


class ResponsePolicyRuleBehavior(str, Enum):
    """
    Answer this query with a behavior rather than DNS data.
    """
    BEHAVIOR_UNSPECIFIED = "BEHAVIOR_UNSPECIFIED"
    BYPASS_RESPONSE_POLICY = "BYPASS_RESPONSE_POLICY"
    """
    Skip a less-specific ResponsePolicyRule and continue normal query logic. This can be used in conjunction with a wildcard to exempt a subset of the wildcard ResponsePolicyRule from the ResponsePolicy behavior and e.g., query the public internet instead. For instance, if these rules exist: *.example.com -> 1.2.3.4 foo.example.com -> PASSTHRU Then a query for 'foo.example.com' skips the wildcard.
    """
