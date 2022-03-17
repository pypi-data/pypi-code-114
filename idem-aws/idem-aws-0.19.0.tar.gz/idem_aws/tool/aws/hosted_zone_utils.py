from collections import OrderedDict
from typing import Any
from typing import Dict
from typing import List


def convert_raw_hosted_zone_to_present(
    hub,
    raw_resource: Dict[str, Any],
    idem_resource_name: str = None,
    tags: List = None,
) -> Dict[str, Any]:

    """
    Given an object state from aws, this function creates a translated resource object in response.

    Args:
        hub: required for functions in hub
        raw_resource (Dict): The dictionary object from where the raw state of resource needs to be translated.
        idem_resource_name (Text): The idem of the idem resource
        tags (List): The tags.
                * Key (Text) -- The key of the tag. Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with aws: .
                * Value (Text) -- The value of the tag. Tag values are case-sensitive and accept a maximum of 255 Unicode characters.


    Returns: Dict[str, Any]
    """

    hosted_zone = raw_resource["ret"].get("HostedZone")
    vpcs = raw_resource["ret"].get("VPCs")
    delegation_set = raw_resource["ret"].get("DelegationSet")
    resource_id = hosted_zone.get("Id")
    resource_parameters = OrderedDict(
        {
            "Name": "hosted_zone_name",
            "CallerReference": "caller_reference",
            "Id": "resource_id",
        }
    )
    resource_translated = {"name": idem_resource_name, "resource_id": resource_id}
    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in hosted_zone:
            resource_translated[parameter_present] = hosted_zone.get(parameter_raw)
    resource_translated["config"] = hosted_zone.get("Config").copy()
    if vpcs is not None:
        resource_translated["vpcs"] = vpcs
    if delegation_set is not None:
        resource_translated["delegation_set"] = delegation_set.copy()
    resource_translated["tags"] = tags

    return resource_translated
