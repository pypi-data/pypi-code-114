from collections import OrderedDict
from typing import Any
from typing import Dict

"""
Util functions to convert raw resource state from AWS Cloudwatch to present input format.
"""


async def convert_raw_log_group_to_present(
    hub, ctx, raw_resource: Dict[str, Any], idem_resource_name: str = None
) -> Dict[str, Any]:
    resource_id = raw_resource.get("logGroupName")
    resource_parameters = OrderedDict({"kmsKeyId": "kms_key_id"})
    resource_translated = {"name": idem_resource_name, "resource_id": resource_id}
    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource:
            resource_translated[parameter_present] = raw_resource.get(parameter_raw)
    if resource_id:
        # list_tags_log_group always returns true even if there is no tag
        tags = await hub.exec.boto3.client.logs.list_tags_log_group(
            ctx, logGroupName=resource_id
        )
        if tags["result"]:
            if tags["ret"]["tags"]:
                resource_translated["tags"] = dict(tags["ret"]["tags"])
    return resource_translated
