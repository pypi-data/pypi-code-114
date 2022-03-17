from collections import OrderedDict
from typing import Any
from typing import Dict
from typing import List

"""
Util functions to convert raw resource state from AWS EC2 to present input format.
"""


def convert_raw_db_subnet_group_to_present(
    hub, resource: Dict[str, Any], tags: List = None, idem_resource_name: str = None
) -> Dict[str, Any]:
    new_resource = {}
    db_subnet_group_id = resource.get("DBSubnetGroupName")
    describe_parameters = OrderedDict(
        {
            "DBSubnetGroupDescription": "db_subnet_group_description",
            "DBSubnetGroupArn": "db_subnet_group_arn",
        }
    )
    new_resource = {"name": db_subnet_group_id, "resource_id": db_subnet_group_id}
    for parameter_old_key, parameter_new_key in describe_parameters.items():
        if resource.get(parameter_old_key) is not None:
            new_resource[parameter_new_key] = resource.get(parameter_old_key)
    if resource.get("Subnets"):
        subnets = []
        for each_subnet in resource.get("Subnets"):
            subnets.append(each_subnet.get("SubnetIdentifier"))

        new_resource["subnets"] = subnets
    if tags:
        new_resource["tags"] = tags
    return new_resource
