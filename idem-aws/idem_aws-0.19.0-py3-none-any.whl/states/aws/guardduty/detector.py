"""
Autogenerated using `pop-create-idem <https://gitlab.com/saltstack/pop/pop-create-idem>`__

hub.exec.boto3.client.guardduty.create_detector
hub.exec.boto3.client.guardduty.untag_resource
hub.exec.boto3.client.guardduty.tag_resource
hub.exec.boto3.client.guardduty.get_detector
hub.exec.boto3.client.guardduty.list_detectors
hub.exec.boto3.client.guardduty.delete_detector
hub.exec.boto3.client.guardduty.update_detector
"""
import copy
from typing import Any
from typing import Dict

__contracts__ = ["resource"]


async def present(
    hub,
    ctx,
    name: str,
    enable: bool = True,
    resource_id: str = None,
    client_token: str = None,
    finding_publishing_frequency: str = None,
    data_sources: Dict = None,
    tags: Dict = None,
) -> Dict[str, Any]:
    r"""
    **Autogenerated function**

    Creates a single Amazon GuardDuty detector.
    A detector is a resource that represents the GuardDuty service.
    To start using GuardDuty, you must create a detector in each Region where you enable the service.
    You can have only one detector per account per Region.
    All data sources are enabled in a new detector by default.

    Args:
        name(Text): An Idem name of the resource.
        resource_id(Text): AWS DETECTOR id to identify the resource
        enable(bool, Default: True): A Boolean value that specifies whether the detector is to be enabled.
        client_token(Text, Optional): The idempotency token for the create request.
                                     This field is auto_populated if not provided.
        finding_publishing_frequency(Text, Optional): A value that specifies how frequently updated findings are exported
        data_sources(Dict, Optional): Describes which data sources will be enabled for the detector.
        tags(Dict, Optional): The tags to be added to a new detector resource.

    Request Syntax:
        [detector-resource-id]:
          aws.guaardduty.detector.present:
          - enable: True
          - client_token: 'string'
          - finding_publishing_frequency: 'string'
          - data_sources: dict
          - tags:
            - string: 'string'

    Returns:
        Dict[str, Any]

    Examples:

        .. code-block:: sls

            cebf7ced6562d943d61f76a915e32563:
                aws.guardduty.detector.present:
                    - enable: True
                    - finding_publishing_frequency: ONE_HOUR
                    - data_sources:
                        S3Logs:
                            Enable: true
                    - tags:
                        detector: my_detector

    """
    result = dict(comment=(), old_state=None, new_state=None, name=name, result=True)
    before = None
    resource_updated = False
    if resource_id:
        before = await hub.exec.boto3.client.guardduty.get_detector(
            ctx, DetectorId=resource_id
        )

    if not before:
        if ctx.get("test", False):
            result["new_state"] = hub.tool.aws.test_state_utils.generate_test_state(
                enforced_state={},
                desired_state={
                    "name": name,
                    "enable": enable,
                    "finding_publishing_frequency": finding_publishing_frequency,
                    "data_sources": data_sources,
                    "tags": tags,
                },
            )
            result["comment"] = (f"Would create aws.guardduty.detector {name}",)
            return result
        try:
            ret = await hub.exec.boto3.client.guardduty.create_detector(
                ctx,
                Enable=enable,
                ClientToken=client_token,
                FindingPublishingFrequency=finding_publishing_frequency,
                DataSources=data_sources,
                Tags=tags,
            )
            result["result"] = ret["result"]
            if not result["result"]:
                result["comment"] = ret["comment"]
                return result
            result["comment"] = result["comment"] + (f"Created '{name}'",)
            resource_id = ret["ret"]["DetectorId"]
        except hub.tool.boto3.exception.ClientError as e:
            result["comment"] = result["comment"] + (f"{e.__class__.__name__}: {e}",)
            result["result"] = False
            return result

    else:
        try:
            account_details = await hub.exec.boto3.client.sts.get_caller_identity(ctx)
            account_id = account_details["ret"]["Account"]
            region_name = ctx["acct"]["region_name"]
            detector_arn = (
                "arn:aws:guardduty:"
                + region_name
                + ":"
                + account_id
                + ":detector/"
                + resource_id
            )
            result[
                "old_state"
            ] = await hub.tool.aws.guardduty.conversion_utils.convert_raw_detector_to_present(
                ctx, raw_resource=before, idem_resource_name=name
            )
            plan_state = copy.deepcopy(result["old_state"])
            update_ret = await hub.exec.aws.guardduty.detector.update_detector(
                ctx,
                before=before,
                detector_id=resource_id,
                finding_publishing_frequency=finding_publishing_frequency,
                data_sources=data_sources,
            )
            result["comment"] = result["comment"] + update_ret["comment"]
            result["result"] = update_ret["result"]
            resource_updated = resource_updated or bool(update_ret["ret"])
            if update_ret["ret"] and ctx.get("test", False):
                if "finding_publishing_frequency" in update_ret["ret"]:
                    plan_state["finding_publishing_frequency"] = update_ret["ret"][
                        "finding_publishing_frequency"
                    ]
                if "data_sources" in update_ret["ret"]:
                    plan_state["data_sources"] = update_ret["ret"]["data_sources"]

            if (tags is not None) and (result["old_state"].get("tags", {}) != tags):
                update_tags_ret = (
                    await hub.exec.aws.guardduty.detector.update_detector_tags(
                        ctx=ctx,
                        resource_arn=detector_arn,
                        old_tags=result["old_state"].get("tags", {}),
                        new_tags=tags,
                    )
                )
                if not result["result"]:
                    result["comment"] = update_tags_ret["comment"]
                    result["result"] = False
                    return result
                result["comment"] = result["comment"] + update_tags_ret["comment"]
                result["result"] = result["result"] and update_tags_ret["result"]
                resource_updated = resource_updated or bool(update_tags_ret["ret"])
                if ctx.get("test", False) and update_tags_ret["ret"] is not None:
                    plan_state["tags"] = update_tags_ret["ret"].get("tags")
            if not resource_updated:
                result["comment"] = result["comment"] + (f"{name} already exists",)
        except hub.tool.boto3.exception.ClientError as e:
            result["comment"] = result["comment"] + (f"{e.__class__.__name__}: {e}",)
            result["result"] = False
            return result

    try:
        if ctx.get("test", False):
            result["new_state"] = plan_state
        elif (not before) or resource_updated:
            after = await hub.exec.boto3.client.guardduty.get_detector(
                ctx, DetectorId=resource_id
            )
            result[
                "new_state"
            ] = await hub.tool.aws.guardduty.conversion_utils.convert_raw_detector_to_present(
                ctx, raw_resource=after, idem_resource_name=name
            )
        else:
            result["new_state"] = copy.deepcopy(result["old_state"])
    except Exception as e:
        result["comment"] = result["comment"] + (str(e),)
        result["result"] = False
    return result


async def absent(
    hub,
    ctx,
    name: str,
    resource_id: str,
) -> Dict[str, Any]:
    r"""
    **Autogenerated function**

    Deletes an Amazon GuardDuty detector that is specified by the detector ID.
    Args:
        resource_id(Text): The AWS ID of the detector.
        name(Text): A Idem name of the detector.

    Examples:

        .. code-block:: sls

            cebf7ced6562d943d61f76a915e32563:
              aws.guardduty.detector.absent:
                - name: value
    """

    result = dict(comment=(), old_state=None, new_state=None, name=name, result=True)
    before = await hub.exec.boto3.client.guardduty.get_detector(
        ctx, DetectorId=resource_id
    )

    if not before:
        result["comment"] = (f"'{name}' already absent",)
    elif ctx.get("test", False):
        result[
            "old_state"
        ] = await hub.tool.aws.guardduty.conversion_utils.convert_raw_detector_to_present(
            ctx, raw_resource=before, idem_resource_name=name
        )
        result["comment"] = (f"Would delete aws.guardduty.detector",)
        return result
    else:
        result[
            "old_state"
        ] = await hub.tool.aws.guardduty.conversion_utils.convert_raw_detector_to_present(
            ctx, raw_resource=before, idem_resource_name=name
        )
        try:
            ret = await hub.exec.boto3.client.guardduty.delete_detector(
                ctx, DetectorId=resource_id
            )
            result["result"] = ret["result"]
            if not result["result"]:
                result["comment"] = ret["comment"]
                result["result"] = False
                return result
            result["comment"] = (f"Deleted '{name}'",)
        except hub.tool.boto3.exception.ClientError as e:
            result["comment"] = (f"{e.__class__.__name__}: {e}",)

    return result


async def describe(hub, ctx) -> Dict[str, Dict[str, Any]]:
    r"""
    **Autogenerated function**

    Describe the resource in a way that can be recreated/managed with the corresponding "present" function

    Lists detectorIds of all the existing Amazon GuardDuty detector resources.
    Retrieves an Amazon GuardDuty detector specified by the detectorId.


    Returns:
        Dict[str, Any]

    Examples:

        .. code-block:: bash

            $ idem describe aws.guardduty.detector
    """

    result = {}
    ret = await hub.exec.boto3.client.guardduty.list_detectors(ctx)

    if not ret["ret"]["DetectorIds"]:
        hub.log.debug(f"Could not list detector {ret['comment']}")
        return {}

    for resource_id in ret["ret"]["DetectorIds"]:
        detector_id = resource_id
        detector = await hub.exec.boto3.client.guardduty.get_detector(
            ctx, DetectorId=resource_id
        )

        resource_translated = await hub.tool.aws.guardduty.conversion_utils.convert_raw_detector_to_present(
            ctx, raw_resource=detector, idem_resource_name=detector_id
        )

        result[detector_id] = {
            "aws.guardduty.detector.present": [
                {parameter_key: parameter_value}
                for parameter_key, parameter_value in resource_translated.items()
            ]
        }
    return result
