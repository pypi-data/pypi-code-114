# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import json
import boto3
import botocore


def get_boto3_session(role_arn=None, tags_str=None):
    """
    Create boto session which allow cross account cluster access by pass remote role_arn.
    The tags(as json object) are passed as session tags only when assumable role is specified.

    :param role_arn: IAM role arn to assume if not none.
    :param tags_str: Session tags to attach while assuming the specified role.
    :return: boto3 session.
    """
    if not role_arn:
        if tags_str:
            raise ValueError(
                "Error while creating boto session. Cannot attach session tags "
                "if no assumable IAM role ARN is specified."
            )
        return boto3.session.Session()
    else:
        sts_client = boto3.client("sts")
        try:
            params = {"RoleArn": role_arn, "RoleSessionName": "SageMakerStudioUser"}

            if tags_str:
                # Accommodate tag key/value containing space.
                tags = json.loads(tags_str.replace("'", ""))
                if len(tags) > 0:
                    params["Tags"] = [{"Key": key, "Value": tags[key]} for key in tags]

            assume_role_object = sts_client.assume_role(**params)
        except botocore.exceptions.ClientError as ce:
            raise ValueError(
                f"Unable to assume role(arn: {role_arn}). Ensure permissions are setup correctly"
                f' Error: {ce.response["Error"]}'
            ) from None
        return boto3.Session(
            aws_access_key_id=assume_role_object["Credentials"]["AccessKeyId"],
            aws_secret_access_key=assume_role_object["Credentials"]["SecretAccessKey"],
            aws_session_token=assume_role_object["Credentials"]["SessionToken"],
        )
