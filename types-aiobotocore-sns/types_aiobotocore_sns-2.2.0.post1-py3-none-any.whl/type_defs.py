"""
Type annotations for sns service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_sns.type_defs import AddPermissionInputRequestTypeDef

    data: AddPermissionInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    LanguageCodeStringType,
    NumberCapabilityType,
    RouteTypeType,
    SMSSandboxPhoneNumberVerificationStatusType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddPermissionInputRequestTypeDef",
    "AddPermissionInputTopicAddPermissionTypeDef",
    "BatchResultErrorEntryTypeDef",
    "CheckIfPhoneNumberIsOptedOutInputRequestTypeDef",
    "CheckIfPhoneNumberIsOptedOutResponseTypeDef",
    "ConfirmSubscriptionInputRequestTypeDef",
    "ConfirmSubscriptionInputTopicConfirmSubscriptionTypeDef",
    "ConfirmSubscriptionResponseTypeDef",
    "CreateEndpointResponseTypeDef",
    "CreatePlatformApplicationInputRequestTypeDef",
    "CreatePlatformApplicationInputServiceResourceCreatePlatformApplicationTypeDef",
    "CreatePlatformApplicationResponseTypeDef",
    "CreatePlatformEndpointInputPlatformApplicationCreatePlatformEndpointTypeDef",
    "CreatePlatformEndpointInputRequestTypeDef",
    "CreateSMSSandboxPhoneNumberInputRequestTypeDef",
    "CreateTopicInputRequestTypeDef",
    "CreateTopicInputServiceResourceCreateTopicTypeDef",
    "CreateTopicResponseTypeDef",
    "DeleteEndpointInputRequestTypeDef",
    "DeletePlatformApplicationInputRequestTypeDef",
    "DeleteSMSSandboxPhoneNumberInputRequestTypeDef",
    "DeleteTopicInputRequestTypeDef",
    "EndpointTypeDef",
    "GetEndpointAttributesInputRequestTypeDef",
    "GetEndpointAttributesResponseTypeDef",
    "GetPlatformApplicationAttributesInputRequestTypeDef",
    "GetPlatformApplicationAttributesResponseTypeDef",
    "GetSMSAttributesInputRequestTypeDef",
    "GetSMSAttributesResponseTypeDef",
    "GetSMSSandboxAccountStatusResultTypeDef",
    "GetSubscriptionAttributesInputRequestTypeDef",
    "GetSubscriptionAttributesResponseTypeDef",
    "GetTopicAttributesInputRequestTypeDef",
    "GetTopicAttributesResponseTypeDef",
    "ListEndpointsByPlatformApplicationInputRequestTypeDef",
    "ListEndpointsByPlatformApplicationResponseTypeDef",
    "ListOriginationNumbersRequestRequestTypeDef",
    "ListOriginationNumbersResultTypeDef",
    "ListPhoneNumbersOptedOutInputRequestTypeDef",
    "ListPhoneNumbersOptedOutResponseTypeDef",
    "ListPlatformApplicationsInputRequestTypeDef",
    "ListPlatformApplicationsResponseTypeDef",
    "ListSMSSandboxPhoneNumbersInputRequestTypeDef",
    "ListSMSSandboxPhoneNumbersResultTypeDef",
    "ListSubscriptionsByTopicInputRequestTypeDef",
    "ListSubscriptionsByTopicResponseTypeDef",
    "ListSubscriptionsInputRequestTypeDef",
    "ListSubscriptionsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTopicsInputRequestTypeDef",
    "ListTopicsResponseTypeDef",
    "MessageAttributeValueTypeDef",
    "OptInPhoneNumberInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "PhoneNumberInformationTypeDef",
    "PlatformApplicationTypeDef",
    "PublishBatchInputRequestTypeDef",
    "PublishBatchRequestEntryTypeDef",
    "PublishBatchResponseTypeDef",
    "PublishBatchResultEntryTypeDef",
    "PublishInputPlatformEndpointPublishTypeDef",
    "PublishInputRequestTypeDef",
    "PublishInputTopicPublishTypeDef",
    "PublishResponseTypeDef",
    "RemovePermissionInputRequestTypeDef",
    "RemovePermissionInputTopicRemovePermissionTypeDef",
    "ResponseMetadataTypeDef",
    "SMSSandboxPhoneNumberTypeDef",
    "ServiceResourcePlatformApplicationRequestTypeDef",
    "ServiceResourcePlatformEndpointRequestTypeDef",
    "ServiceResourceSubscriptionRequestTypeDef",
    "ServiceResourceTopicRequestTypeDef",
    "SetEndpointAttributesInputPlatformEndpointSetAttributesTypeDef",
    "SetEndpointAttributesInputRequestTypeDef",
    "SetPlatformApplicationAttributesInputPlatformApplicationSetAttributesTypeDef",
    "SetPlatformApplicationAttributesInputRequestTypeDef",
    "SetSMSAttributesInputRequestTypeDef",
    "SetSubscriptionAttributesInputRequestTypeDef",
    "SetSubscriptionAttributesInputSubscriptionSetAttributesTypeDef",
    "SetTopicAttributesInputRequestTypeDef",
    "SetTopicAttributesInputTopicSetAttributesTypeDef",
    "SubscribeInputRequestTypeDef",
    "SubscribeInputTopicSubscribeTypeDef",
    "SubscribeResponseTypeDef",
    "SubscriptionTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TopicTypeDef",
    "UnsubscribeInputRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "VerifySMSSandboxPhoneNumberInputRequestTypeDef",
)

AddPermissionInputRequestTypeDef = TypedDict(
    "AddPermissionInputRequestTypeDef",
    {
        "TopicArn": str,
        "Label": str,
        "AWSAccountId": Sequence[str],
        "ActionName": Sequence[str],
    },
)

AddPermissionInputTopicAddPermissionTypeDef = TypedDict(
    "AddPermissionInputTopicAddPermissionTypeDef",
    {
        "Label": str,
        "AWSAccountId": Sequence[str],
        "ActionName": Sequence[str],
    },
)

BatchResultErrorEntryTypeDef = TypedDict(
    "BatchResultErrorEntryTypeDef",
    {
        "Id": str,
        "Code": str,
        "SenderFault": bool,
        "Message": NotRequired[str],
    },
)

CheckIfPhoneNumberIsOptedOutInputRequestTypeDef = TypedDict(
    "CheckIfPhoneNumberIsOptedOutInputRequestTypeDef",
    {
        "phoneNumber": str,
    },
)

CheckIfPhoneNumberIsOptedOutResponseTypeDef = TypedDict(
    "CheckIfPhoneNumberIsOptedOutResponseTypeDef",
    {
        "isOptedOut": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfirmSubscriptionInputRequestTypeDef = TypedDict(
    "ConfirmSubscriptionInputRequestTypeDef",
    {
        "TopicArn": str,
        "Token": str,
        "AuthenticateOnUnsubscribe": NotRequired[str],
    },
)

ConfirmSubscriptionInputTopicConfirmSubscriptionTypeDef = TypedDict(
    "ConfirmSubscriptionInputTopicConfirmSubscriptionTypeDef",
    {
        "Token": str,
        "AuthenticateOnUnsubscribe": NotRequired[str],
    },
)

ConfirmSubscriptionResponseTypeDef = TypedDict(
    "ConfirmSubscriptionResponseTypeDef",
    {
        "SubscriptionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEndpointResponseTypeDef = TypedDict(
    "CreateEndpointResponseTypeDef",
    {
        "EndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePlatformApplicationInputRequestTypeDef = TypedDict(
    "CreatePlatformApplicationInputRequestTypeDef",
    {
        "Name": str,
        "Platform": str,
        "Attributes": Mapping[str, str],
    },
)

CreatePlatformApplicationInputServiceResourceCreatePlatformApplicationTypeDef = TypedDict(
    "CreatePlatformApplicationInputServiceResourceCreatePlatformApplicationTypeDef",
    {
        "Name": str,
        "Platform": str,
        "Attributes": Mapping[str, str],
    },
)

CreatePlatformApplicationResponseTypeDef = TypedDict(
    "CreatePlatformApplicationResponseTypeDef",
    {
        "PlatformApplicationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePlatformEndpointInputPlatformApplicationCreatePlatformEndpointTypeDef = TypedDict(
    "CreatePlatformEndpointInputPlatformApplicationCreatePlatformEndpointTypeDef",
    {
        "Token": str,
        "CustomUserData": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, str]],
    },
)

CreatePlatformEndpointInputRequestTypeDef = TypedDict(
    "CreatePlatformEndpointInputRequestTypeDef",
    {
        "PlatformApplicationArn": str,
        "Token": str,
        "CustomUserData": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, str]],
    },
)

CreateSMSSandboxPhoneNumberInputRequestTypeDef = TypedDict(
    "CreateSMSSandboxPhoneNumberInputRequestTypeDef",
    {
        "PhoneNumber": str,
        "LanguageCode": NotRequired[LanguageCodeStringType],
    },
)

CreateTopicInputRequestTypeDef = TypedDict(
    "CreateTopicInputRequestTypeDef",
    {
        "Name": str,
        "Attributes": NotRequired[Mapping[str, str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateTopicInputServiceResourceCreateTopicTypeDef = TypedDict(
    "CreateTopicInputServiceResourceCreateTopicTypeDef",
    {
        "Name": str,
        "Attributes": NotRequired[Mapping[str, str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateTopicResponseTypeDef = TypedDict(
    "CreateTopicResponseTypeDef",
    {
        "TopicArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEndpointInputRequestTypeDef = TypedDict(
    "DeleteEndpointInputRequestTypeDef",
    {
        "EndpointArn": str,
    },
)

DeletePlatformApplicationInputRequestTypeDef = TypedDict(
    "DeletePlatformApplicationInputRequestTypeDef",
    {
        "PlatformApplicationArn": str,
    },
)

DeleteSMSSandboxPhoneNumberInputRequestTypeDef = TypedDict(
    "DeleteSMSSandboxPhoneNumberInputRequestTypeDef",
    {
        "PhoneNumber": str,
    },
)

DeleteTopicInputRequestTypeDef = TypedDict(
    "DeleteTopicInputRequestTypeDef",
    {
        "TopicArn": str,
    },
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "EndpointArn": NotRequired[str],
        "Attributes": NotRequired[Dict[str, str]],
    },
)

GetEndpointAttributesInputRequestTypeDef = TypedDict(
    "GetEndpointAttributesInputRequestTypeDef",
    {
        "EndpointArn": str,
    },
)

GetEndpointAttributesResponseTypeDef = TypedDict(
    "GetEndpointAttributesResponseTypeDef",
    {
        "Attributes": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPlatformApplicationAttributesInputRequestTypeDef = TypedDict(
    "GetPlatformApplicationAttributesInputRequestTypeDef",
    {
        "PlatformApplicationArn": str,
    },
)

GetPlatformApplicationAttributesResponseTypeDef = TypedDict(
    "GetPlatformApplicationAttributesResponseTypeDef",
    {
        "Attributes": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSMSAttributesInputRequestTypeDef = TypedDict(
    "GetSMSAttributesInputRequestTypeDef",
    {
        "attributes": NotRequired[Sequence[str]],
    },
)

GetSMSAttributesResponseTypeDef = TypedDict(
    "GetSMSAttributesResponseTypeDef",
    {
        "attributes": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSMSSandboxAccountStatusResultTypeDef = TypedDict(
    "GetSMSSandboxAccountStatusResultTypeDef",
    {
        "IsInSandbox": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSubscriptionAttributesInputRequestTypeDef = TypedDict(
    "GetSubscriptionAttributesInputRequestTypeDef",
    {
        "SubscriptionArn": str,
    },
)

GetSubscriptionAttributesResponseTypeDef = TypedDict(
    "GetSubscriptionAttributesResponseTypeDef",
    {
        "Attributes": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTopicAttributesInputRequestTypeDef = TypedDict(
    "GetTopicAttributesInputRequestTypeDef",
    {
        "TopicArn": str,
    },
)

GetTopicAttributesResponseTypeDef = TypedDict(
    "GetTopicAttributesResponseTypeDef",
    {
        "Attributes": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEndpointsByPlatformApplicationInputRequestTypeDef = TypedDict(
    "ListEndpointsByPlatformApplicationInputRequestTypeDef",
    {
        "PlatformApplicationArn": str,
        "NextToken": NotRequired[str],
    },
)

ListEndpointsByPlatformApplicationResponseTypeDef = TypedDict(
    "ListEndpointsByPlatformApplicationResponseTypeDef",
    {
        "Endpoints": List["EndpointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOriginationNumbersRequestRequestTypeDef = TypedDict(
    "ListOriginationNumbersRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListOriginationNumbersResultTypeDef = TypedDict(
    "ListOriginationNumbersResultTypeDef",
    {
        "NextToken": str,
        "PhoneNumbers": List["PhoneNumberInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPhoneNumbersOptedOutInputRequestTypeDef = TypedDict(
    "ListPhoneNumbersOptedOutInputRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)

ListPhoneNumbersOptedOutResponseTypeDef = TypedDict(
    "ListPhoneNumbersOptedOutResponseTypeDef",
    {
        "phoneNumbers": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPlatformApplicationsInputRequestTypeDef = TypedDict(
    "ListPlatformApplicationsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)

ListPlatformApplicationsResponseTypeDef = TypedDict(
    "ListPlatformApplicationsResponseTypeDef",
    {
        "PlatformApplications": List["PlatformApplicationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSMSSandboxPhoneNumbersInputRequestTypeDef = TypedDict(
    "ListSMSSandboxPhoneNumbersInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListSMSSandboxPhoneNumbersResultTypeDef = TypedDict(
    "ListSMSSandboxPhoneNumbersResultTypeDef",
    {
        "PhoneNumbers": List["SMSSandboxPhoneNumberTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSubscriptionsByTopicInputRequestTypeDef = TypedDict(
    "ListSubscriptionsByTopicInputRequestTypeDef",
    {
        "TopicArn": str,
        "NextToken": NotRequired[str],
    },
)

ListSubscriptionsByTopicResponseTypeDef = TypedDict(
    "ListSubscriptionsByTopicResponseTypeDef",
    {
        "Subscriptions": List["SubscriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSubscriptionsInputRequestTypeDef = TypedDict(
    "ListSubscriptionsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)

ListSubscriptionsResponseTypeDef = TypedDict(
    "ListSubscriptionsResponseTypeDef",
    {
        "Subscriptions": List["SubscriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTopicsInputRequestTypeDef = TypedDict(
    "ListTopicsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)

ListTopicsResponseTypeDef = TypedDict(
    "ListTopicsResponseTypeDef",
    {
        "Topics": List["TopicTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MessageAttributeValueTypeDef = TypedDict(
    "MessageAttributeValueTypeDef",
    {
        "DataType": str,
        "StringValue": NotRequired[str],
        "BinaryValue": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
    },
)

OptInPhoneNumberInputRequestTypeDef = TypedDict(
    "OptInPhoneNumberInputRequestTypeDef",
    {
        "phoneNumber": str,
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)

PhoneNumberInformationTypeDef = TypedDict(
    "PhoneNumberInformationTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "PhoneNumber": NotRequired[str],
        "Status": NotRequired[str],
        "Iso2CountryCode": NotRequired[str],
        "RouteType": NotRequired[RouteTypeType],
        "NumberCapabilities": NotRequired[List[NumberCapabilityType]],
    },
)

PlatformApplicationTypeDef = TypedDict(
    "PlatformApplicationTypeDef",
    {
        "PlatformApplicationArn": NotRequired[str],
        "Attributes": NotRequired[Dict[str, str]],
    },
)

PublishBatchInputRequestTypeDef = TypedDict(
    "PublishBatchInputRequestTypeDef",
    {
        "TopicArn": str,
        "PublishBatchRequestEntries": Sequence["PublishBatchRequestEntryTypeDef"],
    },
)

PublishBatchRequestEntryTypeDef = TypedDict(
    "PublishBatchRequestEntryTypeDef",
    {
        "Id": str,
        "Message": str,
        "Subject": NotRequired[str],
        "MessageStructure": NotRequired[str],
        "MessageAttributes": NotRequired[Mapping[str, "MessageAttributeValueTypeDef"]],
        "MessageDeduplicationId": NotRequired[str],
        "MessageGroupId": NotRequired[str],
    },
)

PublishBatchResponseTypeDef = TypedDict(
    "PublishBatchResponseTypeDef",
    {
        "Successful": List["PublishBatchResultEntryTypeDef"],
        "Failed": List["BatchResultErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PublishBatchResultEntryTypeDef = TypedDict(
    "PublishBatchResultEntryTypeDef",
    {
        "Id": NotRequired[str],
        "MessageId": NotRequired[str],
        "SequenceNumber": NotRequired[str],
    },
)

PublishInputPlatformEndpointPublishTypeDef = TypedDict(
    "PublishInputPlatformEndpointPublishTypeDef",
    {
        "Message": str,
        "TopicArn": NotRequired[str],
        "PhoneNumber": NotRequired[str],
        "Subject": NotRequired[str],
        "MessageStructure": NotRequired[str],
        "MessageAttributes": NotRequired[Mapping[str, "MessageAttributeValueTypeDef"]],
        "MessageDeduplicationId": NotRequired[str],
        "MessageGroupId": NotRequired[str],
    },
)

PublishInputRequestTypeDef = TypedDict(
    "PublishInputRequestTypeDef",
    {
        "Message": str,
        "TopicArn": NotRequired[str],
        "TargetArn": NotRequired[str],
        "PhoneNumber": NotRequired[str],
        "Subject": NotRequired[str],
        "MessageStructure": NotRequired[str],
        "MessageAttributes": NotRequired[Mapping[str, "MessageAttributeValueTypeDef"]],
        "MessageDeduplicationId": NotRequired[str],
        "MessageGroupId": NotRequired[str],
    },
)

PublishInputTopicPublishTypeDef = TypedDict(
    "PublishInputTopicPublishTypeDef",
    {
        "Message": str,
        "TargetArn": NotRequired[str],
        "PhoneNumber": NotRequired[str],
        "Subject": NotRequired[str],
        "MessageStructure": NotRequired[str],
        "MessageAttributes": NotRequired[Mapping[str, "MessageAttributeValueTypeDef"]],
        "MessageDeduplicationId": NotRequired[str],
        "MessageGroupId": NotRequired[str],
    },
)

PublishResponseTypeDef = TypedDict(
    "PublishResponseTypeDef",
    {
        "MessageId": str,
        "SequenceNumber": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemovePermissionInputRequestTypeDef = TypedDict(
    "RemovePermissionInputRequestTypeDef",
    {
        "TopicArn": str,
        "Label": str,
    },
)

RemovePermissionInputTopicRemovePermissionTypeDef = TypedDict(
    "RemovePermissionInputTopicRemovePermissionTypeDef",
    {
        "Label": str,
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)

SMSSandboxPhoneNumberTypeDef = TypedDict(
    "SMSSandboxPhoneNumberTypeDef",
    {
        "PhoneNumber": NotRequired[str],
        "Status": NotRequired[SMSSandboxPhoneNumberVerificationStatusType],
    },
)

ServiceResourcePlatformApplicationRequestTypeDef = TypedDict(
    "ServiceResourcePlatformApplicationRequestTypeDef",
    {
        "arn": str,
    },
)

ServiceResourcePlatformEndpointRequestTypeDef = TypedDict(
    "ServiceResourcePlatformEndpointRequestTypeDef",
    {
        "arn": str,
    },
)

ServiceResourceSubscriptionRequestTypeDef = TypedDict(
    "ServiceResourceSubscriptionRequestTypeDef",
    {
        "arn": str,
    },
)

ServiceResourceTopicRequestTypeDef = TypedDict(
    "ServiceResourceTopicRequestTypeDef",
    {
        "arn": str,
    },
)

SetEndpointAttributesInputPlatformEndpointSetAttributesTypeDef = TypedDict(
    "SetEndpointAttributesInputPlatformEndpointSetAttributesTypeDef",
    {
        "Attributes": Mapping[str, str],
    },
)

SetEndpointAttributesInputRequestTypeDef = TypedDict(
    "SetEndpointAttributesInputRequestTypeDef",
    {
        "EndpointArn": str,
        "Attributes": Mapping[str, str],
    },
)

SetPlatformApplicationAttributesInputPlatformApplicationSetAttributesTypeDef = TypedDict(
    "SetPlatformApplicationAttributesInputPlatformApplicationSetAttributesTypeDef",
    {
        "Attributes": Mapping[str, str],
    },
)

SetPlatformApplicationAttributesInputRequestTypeDef = TypedDict(
    "SetPlatformApplicationAttributesInputRequestTypeDef",
    {
        "PlatformApplicationArn": str,
        "Attributes": Mapping[str, str],
    },
)

SetSMSAttributesInputRequestTypeDef = TypedDict(
    "SetSMSAttributesInputRequestTypeDef",
    {
        "attributes": Mapping[str, str],
    },
)

SetSubscriptionAttributesInputRequestTypeDef = TypedDict(
    "SetSubscriptionAttributesInputRequestTypeDef",
    {
        "SubscriptionArn": str,
        "AttributeName": str,
        "AttributeValue": NotRequired[str],
    },
)

SetSubscriptionAttributesInputSubscriptionSetAttributesTypeDef = TypedDict(
    "SetSubscriptionAttributesInputSubscriptionSetAttributesTypeDef",
    {
        "AttributeName": str,
        "AttributeValue": NotRequired[str],
    },
)

SetTopicAttributesInputRequestTypeDef = TypedDict(
    "SetTopicAttributesInputRequestTypeDef",
    {
        "TopicArn": str,
        "AttributeName": str,
        "AttributeValue": NotRequired[str],
    },
)

SetTopicAttributesInputTopicSetAttributesTypeDef = TypedDict(
    "SetTopicAttributesInputTopicSetAttributesTypeDef",
    {
        "AttributeName": str,
        "AttributeValue": NotRequired[str],
    },
)

SubscribeInputRequestTypeDef = TypedDict(
    "SubscribeInputRequestTypeDef",
    {
        "TopicArn": str,
        "Protocol": str,
        "Endpoint": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, str]],
        "ReturnSubscriptionArn": NotRequired[bool],
    },
)

SubscribeInputTopicSubscribeTypeDef = TypedDict(
    "SubscribeInputTopicSubscribeTypeDef",
    {
        "Protocol": str,
        "Endpoint": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, str]],
        "ReturnSubscriptionArn": NotRequired[bool],
    },
)

SubscribeResponseTypeDef = TypedDict(
    "SubscribeResponseTypeDef",
    {
        "SubscriptionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "SubscriptionArn": NotRequired[str],
        "Owner": NotRequired[str],
        "Protocol": NotRequired[str],
        "Endpoint": NotRequired[str],
        "TopicArn": NotRequired[str],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TopicTypeDef = TypedDict(
    "TopicTypeDef",
    {
        "TopicArn": NotRequired[str],
    },
)

UnsubscribeInputRequestTypeDef = TypedDict(
    "UnsubscribeInputRequestTypeDef",
    {
        "SubscriptionArn": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

VerifySMSSandboxPhoneNumberInputRequestTypeDef = TypedDict(
    "VerifySMSSandboxPhoneNumberInputRequestTypeDef",
    {
        "PhoneNumber": str,
        "OneTimePassword": str,
    },
)
