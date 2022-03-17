"""
Autogenerated using `pop-create-idem <https://gitlab.com/saltstack/pop/pop-create-idem>`__

hub.exec.boto3.client.ec2.create_transit_gateway
hub.exec.boto3.client.ec2.delete_transit_gateway
hub.exec.boto3.client.ec2.describe_transit_gateways
hub.exec.boto3.client.ec2.modify_transit_gateway
"""
import copy
from typing import Any
from typing import Dict
from typing import List

__contracts__ = ["resource"]
TREQ = {
    "present": {
        "require": ["aws.ec2.subnet.present"],
        "require": ["aws.ec2.transit_gateway.present"],
    },
}


async def present(
    hub,
    ctx,
    name: str,
    transit_gateway: str,
    vpc_id: str,
    subnet_ids: List,
    resource_id: str = None,
    options: dict = None,
    tags: List = None,
) -> Dict[str, Any]:
    r"""
    **Autogenerated function**

    Attaches the specified VPC to the specified transit gateway. If you attach a VPC with a CIDR range that overlaps
    the CIDR range of a VPC that is already attached, the new VPC CIDR range is not propagated to the default
    propagation route table. To send VPC traffic to an attached transit gateway, add a route to the VPC route table
    using CreateRoute.

    Args:
        name(Text): Name of the resource.
        transit_gateway(Text): The ID of the transit gateway.
        vpc_id(Text): The ID of the VPC.
        subnet_ids(List): The IDs of one or more subnets. You can specify only one subnet per Availability Zone.
                       You must specify at least one subnet, but we recommend that you specify two subnets for better availability.
                       The transit gateway uses one IP address from each specified subnet.
             * (Text)
        resource_id(Text, optional): AWS Transit gateway VPC attachment id to identify the resource
        options(dictionary, optional): The VPC attachment options.
             *  DnsSupport (Text) -- Enable or disable DNS support. Enabled by default.,
             *  Ipv6Support (Text) -- Enable or disable IPv6 support. The default is disable.,
             *  ApplianceModeSupport (Text) -- Enable or disable support for appliance mode. If enabled, a traffic flow between a source and destination uses the same Availability Zone for the VPC attachment for the lifetime of that flow. The default is disable .
        tags(List, optional): The tags to apply to the VPC attachment.
            * Key (Text) -- The key of the tag. Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with aws: .
            * Value (Text) -- The value of the tag. Tag values are case-sensitive and accept a maximum of 255 Unicode characters.

    Request Syntax:
        [transit-gateway-resource-id]:
          aws.ec2.transit_gateway_vpc_attachment.present:
            - name: 'string'
            - resource_id: 'string'
            - transit_gateway: 'string'
            - vpc_id: 'string'
            - subnet_ids:
               - 'string'
            - options:
                ApplianceModeSupport: 'string'
                DnsSupport: 'string'
                Ipv6Support: 'string'
            - tags:
                - Key: 'string'
                  Value: 'string'
    Returns:
        Dict[str, Any]

    Examples:

        .. code-block:: sls

            tgw-attach-0871e9c72becf0710:
                aws.ec2.transit_gateway_vpc_attachment.present:
                - name: tgw-attach-0871e9c72becf0710
                - resource_id: tgw-attach-0871e9c72becf0710
                - transit_gateway: tgw-02994a8dda824c337
                - vpc_id: vpc-0afa0d5fe3fc2785c
                - subnet_ids:
                   - subnet-07f91b9ebd252be49
                - options:
                    ApplianceModeSupport: disable
                    DnsSupport: enable
                    Ipv6Support: disable
                - tags:
                    - Key: Name
                      Value: test-transit-gateway-attachment

    """
    result = dict(comment=(), old_state=None, new_state=None, name=name, result=True)
    before = None
    resource_updated = False
    if resource_id:
        before = await hub.exec.aws.ec2.transit_gateway_vpc_attachment.get_transit_gateway_vpc_attachment_by_id(
            ctx, resource_id
        )
    if before and before["ret"]:
        result[
            "old_state"
        ] = hub.tool.aws.ec2.conversion_utils.convert_raw_tg_vpc_attachment(
            before["ret"], name
        )

    try:
        if before and before["ret"]:
            plan_state = copy.deepcopy(result["old_state"])
            if subnet_ids is not None:
                update_ret = await hub.exec.aws.ec2.transit_gateway_vpc_attachment.update_transit_gateway_vpc_attachment(
                    ctx=ctx,
                    transit_gateway_vpc_attachment_id=resource_id,
                    old_subnets=before["ret"].get("SubnetIds"),
                    new_subnets=subnet_ids,
                    old_options=before["ret"].get("Options"),
                    new_options=options,
                )
                result["comment"] = result["comment"] + update_ret["comment"]
                result["result"] = update_ret["result"]
                resource_updated = resource_updated or update_ret["result"]
                if ctx.get("test", False) and update_ret["ret"]:
                    if subnet_ids:
                        plan_state["subnet_ids"] = update_ret["ret"].get("subnet_ids")
                    if options:
                        plan_state["options"] = update_ret["ret"].get("options")
            if result["result"] and (tags is not None):
                # Update tags
                update_ret = await hub.exec.aws.ec2.tag.update_tags(
                    ctx=ctx,
                    resource_id=resource_id,
                    old_tags=before.get("Tags"),
                    new_tags=tags,
                )
                if not update_ret["result"]:
                    result["comment"] = result["comment"] + update_ret["comment"]
                    result["result"] = update_ret["result"]
                resource_updated = resource_updated or update_ret["result"]
                if ctx.get("test", False) and update_ret["ret"]:
                    plan_state["tags"] = tags

            if result["result"]:
                result["comment"] = result["comment"] + (
                    f"'Updated transit gateway {name}'",
                )

        else:
            if ctx.get("test", False):
                result["new_state"] = hub.tool.aws.test_state_utils.generate_test_state(
                    enforced_state={},
                    desired_state={
                        "name": name,
                        "transit_gateway": transit_gateway,
                        "vpc_id": vpc_id,
                        "subnet_ids": subnet_ids,
                        "options": options,
                        "tags": tags,
                    },
                )
                result["comment"] = result["comment"] + (
                    f"Would create aws.ec2.transit_gateway_vpc_attachment {name}",
                )
                return result
            ret = await hub.exec.boto3.client.ec2.create_transit_gateway_vpc_attachment(
                ctx,
                TransitGatewayId=transit_gateway,
                VpcId=vpc_id,
                SubnetIds=subnet_ids,
                Options=options,
                TagSpecifications=[
                    {"ResourceType": "transit-gateway-attachment", "Tags": tags}
                ]
                if tags
                else None,
            )

            if not ret["result"]:
                result["comment"] = result["comment"] + ret["comment"]
                result["result"] = ret["result"]
                return result

            result["comment"] = result["comment"] + (f"Created '{name}'",)
            resource_updated = resource_updated or ret["result"]
            resource_id = ret["ret"]["TransitGatewayVpcAttachment"][
                "TransitGatewayAttachmentId"
            ]

    except hub.tool.boto3.exception.ClientError as e:
        result["result"] = False
        result["comment"] = result["comment"] + (f"{e.__class__.__name__}: {e}",)

    try:
        if ctx.get("test", False):
            result["new_state"] = plan_state
        elif resource_updated:
            after = await hub.exec.aws.ec2.transit_gateway_vpc_attachment.get_transit_gateway_vpc_attachment_by_id(
                ctx, resource_id
            )
            result[
                "new_state"
            ] = hub.tool.aws.ec2.conversion_utils.convert_raw_tg_vpc_attachment(
                after["ret"], name
            )
        else:
            result["new_state"] = copy.deepcopy(result["old_state"])
    except Exception as e:
        result["comment"] = result["comment"] + (str(e),)
        result["result"] = False
    return result


async def absent(hub, ctx, name: str, resource_id: str) -> Dict[str, Any]:
    r"""
    **Autogenerated function**

    Deletes the specified VPC attachment.

    Args:
        name(Text): Name of the resource.
        resource_id(Text): AWS Transit gateway VPC attachment ID to identify the resource

    Returns:
        Dict[str, Any]

    Examples:

        .. code-block:: sls

            aws.ec2.transit_gateway_vpc_attachment.absent:
                - name: tgw-attach-0871e9c72becf0710
                - resource_id: tgw-attach-0871e9c72becf0710
    """

    result = dict(comment=(), old_state=None, new_state=None, name=name, result=True)
    before = await hub.exec.aws.ec2.transit_gateway_vpc_attachment.get_transit_gateway_vpc_attachment_by_id(
        ctx, resource_id
    )
    if not before or not before["ret"]:
        result["comment"] = (f"'{name}' already absent",)
        return result
    before = before["ret"]
    result[
        "old_state"
    ] = hub.tool.aws.ec2.conversion_utils.convert_raw_tg_vpc_attachment(before, name)
    if before["State"] and (
        before["State"] == "deleted" or before["State"] == "deleting"
    ):
        result["comment"] = result["comment"] + (
            f"'{name}' is already {before['State']}",
        )
    elif ctx.get("test", False):
        result["comment"] = result["comment"] + (
            f"Would delete aws.ec2.transit_gateway_vpc_attachment {name}",
        )
        return result
    else:
        try:
            ret = await hub.exec.boto3.client.ec2.delete_transit_gateway_vpc_attachment(
                ctx, TransitGatewayAttachmentId=resource_id
            )
            if not ret["result"]:
                result["comment"] = result["comment"] + ret["comment"]
                result["result"] = ret["result"]
                return result
            result["comment"] = result["comment"] + (f"Deleted '{name}'",)
        except hub.tool.boto3.exception.ClientError as e:
            result["comment"] = result["comment"] + (f"{e.__class__.__name__}: {e}",)
    return result


async def describe(hub, ctx) -> Dict[str, Dict[str, Any]]:
    r"""
    **Autogenerated function**

    Describe the resource in a way that can be recreated/managed with the corresponding "present" function


    Describes one or more VPC attachments. By default, all VPC attachments are described. Alternatively, you can
    filter the results.


    Returns:
        Dict[str, Any]

    Examples:

        .. code-block:: bash

            $ idem describe aws.ec2.transit_gateway_vpc_attachment
    """

    result = {}

    ret = await hub.exec.boto3.client.ec2.describe_transit_gateway_vpc_attachments(ctx)
    if not ret["result"]:
        hub.log.debug(
            f"Could not describe transit_gateway_vpc_attachments {ret['comment']}"
        )
        return {}
    for transit_gateway_vpc_attachment in ret["ret"]["TransitGatewayVpcAttachments"]:
        resource_id = transit_gateway_vpc_attachment.get("TransitGatewayAttachmentId")
        translated_resource = (
            hub.tool.aws.ec2.conversion_utils.convert_raw_tg_vpc_attachment(
                transit_gateway_vpc_attachment, resource_id
            )
        )
        result[resource_id] = {
            "aws.ec2.transit_gateway_vpc_attachment.present": [
                {parameter_key: parameter_value}
                for parameter_key, parameter_value in translated_resource.items()
            ]
        }

    return result
