"""
Autogenerated using `pop-create-idem <https://gitlab.com/saltstack/pop/pop-create-idem>`__

hub.exec.boto3.client.iam.delete_user_policy
hub.exec.boto3.client.iam.get_user_policy
hub.exec.boto3.client.iam.list_user_policies
hub.exec.boto3.client.iam.put_user_policy
resource = hub.tool.boto3.resource.create(ctx, "iam", "UserPolicy", name)
hub.tool.boto3.resource.exec(resource, delete, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, put, *args, **kwargs)
"""
import asyncio
import copy
import json
from typing import Any
from typing import Dict

__contracts__ = ["resource"]


async def present(
    hub, ctx, name: str, user_name: str, policy_document: Dict or str
) -> Dict[str, Any]:
    r"""
    **Autogenerated function**

    Adds or updates an inline policy document that is embedded in the specified IAM user. An IAM user can also have
    a managed policy attached to it. To attach a managed policy to a user, use AttachUserPolicy. To create a new
    managed policy, use CreatePolicy. For information about policies, see Managed policies and inline policies in
    the IAM User Guide. For information about the maximum number of inline policies that you can embed in a user,
    see IAM and STS quotas in the IAM User Guide.  Because policy documents can be large, you should use POST rather
    than GET when calling PutUserPolicy. For general information about using the Query API with IAM, see Making
    query requests in the IAM User Guide.

    Args:
        name(Text): The name of the AWS IAM user policy.
        user_name(Text): The UserPolicy's user_name identifier
        policy_document(dictionary): The policy document. IAM stores policies in JSON format. However, resources that were created using CloudFormation templates can be formatted in YAML. CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.

    Request Syntax:
        [iam-user-policy-name]:
          aws.iam.user_policy.present:
          - user_name: 'string'
          - policy_document: 'dict or string'

    Returns:
        Dict[str, Any]

    Examples:

        .. code-block:: sls

            idem-test-user-policy:
              aws.iam.user_policy.present:
                - user_name: idem-test-user
                - policy_document: '{"Version": "2012-10-17", "Statement": {"Effect": "Allow", "Action": ["cloudwatch:ListMetrics", "cloudwatch:GetMetricStatistics"], "Resource":"*"}}'

    """

    result = dict(comment="", old_state=None, new_state=None, name=name, result=True)
    resource = hub.tool.boto3.resource.create(
        ctx, "iam", "UserPolicy", user_name=user_name, name=name
    )
    before = await hub.tool.boto3.resource.describe(resource)
    if ctx.get("test", False):
        if before:
            result["comment"] = f"Would update aws.iam.user_policy {name}"
        else:
            result["comment"] = f"Would create aws.iam.user_policy {name}"
        return result

    if before:
        before.pop("ResponseMetadata", None)
        result["old_state"] = before
        result["comment"] = f"'{name}' already exists"
    else:
        try:
            # Standardise on the json format of policy
            if isinstance(policy_document, str) and len(policy_document) > 0:
                policy_document = json.loads(policy_document)
            policy_document = json.dumps(policy_document, separators=(", ", ": "))

            ret = await hub.exec.boto3.client.iam.put_user_policy(
                ctx,
                UserName=user_name,
                PolicyName=name,
                PolicyDocument=policy_document,
            )
            result["result"] = ret["result"]
            if not result["result"]:
                result["comment"] = ret["comment"]
                return result
            result["comment"] = f"Created '{name}'"
        except hub.tool.boto3.exception.ClientError as e:
            result["comment"] = f"{e.__class__.__name__}: {e}"
            result["result"] = False

    try:
        if not before:
            after = await hub.tool.boto3.resource.describe(resource)
            after.pop("ResponseMetadata", None)
            result["new_state"] = after
        else:
            result["new_state"] = copy.deepcopy(result["old_state"])
    except Exception as e:
        result["comment"] = str(e)
        result["result"] = False
    return result


async def absent(hub, ctx, name: str, user_name: str) -> Dict[str, Any]:
    r"""
    **Autogenerated function**

    Deletes the specified inline policy that is embedded in the specified IAM user. A user can also have managed
    policies attached to it. To detach a managed policy from a user, use DetachUserPolicy. For more information
    about policies, refer to Managed policies and inline policies in the IAM User Guide.

    Args:
        name(Text): The name of the AWS IAM user policy.
        user_name(Text): The UserPolicy's user_name identifier

    Request Syntax:
        [iam-user-policy-name]:
          aws.iam.user_policy.present:
          - user_name: 'string'

    Returns:
        Dict[str, Any]

    Examples:

        .. code-block:: sls

            idem-test-user-policy:
              aws.iam.user_policy.absent:
                - user_name: idem-test-user
    """

    result = dict(comment="", old_state=None, new_state=None, name=name, result=True)
    resource = hub.tool.boto3.resource.create(
        ctx, "iam", "UserPolicy", user_name=user_name, name=name
    )
    before = await hub.tool.boto3.resource.describe(resource)

    if not before:
        result["comment"] = f"'{name}' already absent"
    elif ctx.get("test", False):
        result["comment"] = f"Would delete aws.iam.user_policy {name}"
        return result
    else:
        try:
            before.pop("ResponseMetadata", None)
            result["old_state"] = before
            ret = await hub.exec.boto3.client.iam.delete_user_policy(
                ctx, UserName=user_name, PolicyName=name
            )
            result["result"] = ret["result"]
            if not result["result"]:
                result["comment"] = ret["comment"]
                result["result"] = False
                return result
            result["comment"] = f"Deleted '{name}'"
        except hub.tool.boto3.exception.ClientError as e:
            result["result"] = False
            result["comment"] = f"{e.__class__.__name__}: {e}"

    return result


async def describe(hub, ctx) -> Dict[str, Dict[str, Any]]:
    r"""
    **Autogenerated function**

    Describe the resource in a way that can be recreated/managed with the corresponding "present" function


    Lists the names of the inline policies embedded in the specified IAM user. An IAM user can also have managed
    policies attached to it. To list the managed policies that are attached to a user, use ListAttachedUserPolicies.
    For more information about policies, see Managed policies and inline policies in the IAM User Guide. You can
    paginate the results using the MaxItems and Marker parameters. If there are no inline policies embedded with the
    specified user, the operation returns an empty list.


    Returns:
        Dict[str, Any]

    Examples:

        .. code-block:: bash

            $ idem describe aws_auto.iam.user_policy
    """

    result = {}
    # Fetch all users and then policies for each of them
    users = await hub.exec.boto3.client.iam.list_users(ctx)
    if not users["result"]:
        hub.log.debug(f"Could not describe users {users['comment']}")
        return {}

    for user in users["ret"]["Users"]:
        user_name = user.get("UserName")
        try:
            user_policies = await hub.exec.boto3.client.iam.list_user_policies(
                ctx, UserName=user_name
            )
            if not user_policies["result"]:
                hub.log.warning(
                    f"Could not fetch user policies for user {user_name} "
                    f"due to error {user_policies['comment']}. Skip this user and continue."
                )
                continue
        except hub.tool.boto3.exception.ClientError as e:
            hub.log.warning(
                f"Could not fetch user policies for user {user_name} due to error"
                f" {e.__class__.__name__}: {e}. Skip this user and continue."
            )
            continue
        if user_policies:
            if not user_policies["result"]:
                hub.log.warning(
                    f"Could not describe user_policy for user {user_name} due to error "
                    f"{user_policies['comment']}. Skip this user and continue."
                )
            else:
                for user_policy in asyncio.as_completed(
                    [
                        hub.exec.boto3.client.iam.get_user_policy(
                            ctx=ctx, UserName=user_name, PolicyName=user_policy_name
                        )
                        for user_policy_name in user_policies["ret"].get(
                            "PolicyNames", list()
                        )
                    ]
                ):
                    ret_user_policy = await user_policy
                    if not ret_user_policy["result"]:
                        hub.log.warning(
                            f"Could not get user_policy for user {user_name} due to error"
                            f" {ret_user_policy['comment']} . Skip this user policy and continue."
                        )
                    else:
                        resource = ret_user_policy["ret"]
                        resource_name = resource.get("PolicyName")
                        resource_translated = []
                        if resource.get("UserName"):
                            resource_translated.append(
                                {"user_name": resource.get("UserName")}
                            )
                        if resource.get("PolicyDocument"):
                            resource_translated.append(
                                {
                                    "policy_document": json.dumps(
                                        resource.get("PolicyDocument"),
                                        separators=(", ", ": "),
                                    )
                                }
                            )
                        # If different users have same policy name, describe will list only one of them since key used here is policy name.
                        result[resource_name] = {
                            "aws.iam.user_policy.present": resource_translated
                        }
    return result
