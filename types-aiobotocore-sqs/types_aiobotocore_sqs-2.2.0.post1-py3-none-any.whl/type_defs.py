"""
Type annotations for sqs service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_sqs.type_defs import AddPermissionRequestQueueAddPermissionTypeDef

    data: AddPermissionRequestQueueAddPermissionTypeDef = {...}
    ```
"""
import sys
from typing import IO, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import MessageSystemAttributeNameType, QueueAttributeNameType

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddPermissionRequestQueueAddPermissionTypeDef",
    "AddPermissionRequestRequestTypeDef",
    "BatchResultErrorEntryTypeDef",
    "ChangeMessageVisibilityBatchRequestEntryTypeDef",
    "ChangeMessageVisibilityBatchRequestQueueChangeMessageVisibilityBatchTypeDef",
    "ChangeMessageVisibilityBatchRequestRequestTypeDef",
    "ChangeMessageVisibilityBatchResultEntryTypeDef",
    "ChangeMessageVisibilityBatchResultTypeDef",
    "ChangeMessageVisibilityRequestMessageChangeVisibilityTypeDef",
    "ChangeMessageVisibilityRequestRequestTypeDef",
    "CreateQueueRequestRequestTypeDef",
    "CreateQueueRequestServiceResourceCreateQueueTypeDef",
    "CreateQueueResultTypeDef",
    "DeleteMessageBatchRequestEntryTypeDef",
    "DeleteMessageBatchRequestQueueDeleteMessagesTypeDef",
    "DeleteMessageBatchRequestRequestTypeDef",
    "DeleteMessageBatchResultEntryTypeDef",
    "DeleteMessageBatchResultTypeDef",
    "DeleteMessageRequestRequestTypeDef",
    "DeleteQueueRequestRequestTypeDef",
    "GetQueueAttributesRequestRequestTypeDef",
    "GetQueueAttributesResultTypeDef",
    "GetQueueUrlRequestRequestTypeDef",
    "GetQueueUrlRequestServiceResourceGetQueueByNameTypeDef",
    "GetQueueUrlResultTypeDef",
    "ListDeadLetterSourceQueuesRequestRequestTypeDef",
    "ListDeadLetterSourceQueuesResultTypeDef",
    "ListQueueTagsRequestRequestTypeDef",
    "ListQueueTagsResultTypeDef",
    "ListQueuesRequestRequestTypeDef",
    "ListQueuesResultTypeDef",
    "MessageAttributeValueTypeDef",
    "MessageSystemAttributeValueTypeDef",
    "MessageTypeDef",
    "PaginatorConfigTypeDef",
    "PurgeQueueRequestRequestTypeDef",
    "QueueMessageRequestTypeDef",
    "ReceiveMessageRequestQueueReceiveMessagesTypeDef",
    "ReceiveMessageRequestRequestTypeDef",
    "ReceiveMessageResultTypeDef",
    "RemovePermissionRequestQueueRemovePermissionTypeDef",
    "RemovePermissionRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SendMessageBatchRequestEntryTypeDef",
    "SendMessageBatchRequestQueueSendMessagesTypeDef",
    "SendMessageBatchRequestRequestTypeDef",
    "SendMessageBatchResultEntryTypeDef",
    "SendMessageBatchResultTypeDef",
    "SendMessageRequestQueueSendMessageTypeDef",
    "SendMessageRequestRequestTypeDef",
    "SendMessageResultTypeDef",
    "ServiceResourceMessageRequestTypeDef",
    "ServiceResourceQueueRequestTypeDef",
    "SetQueueAttributesRequestQueueSetAttributesTypeDef",
    "SetQueueAttributesRequestRequestTypeDef",
    "TagQueueRequestRequestTypeDef",
    "UntagQueueRequestRequestTypeDef",
)

AddPermissionRequestQueueAddPermissionTypeDef = TypedDict(
    "AddPermissionRequestQueueAddPermissionTypeDef",
    {
        "Label": str,
        "AWSAccountIds": Sequence[str],
        "Actions": Sequence[str],
    },
)

AddPermissionRequestRequestTypeDef = TypedDict(
    "AddPermissionRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "Label": str,
        "AWSAccountIds": Sequence[str],
        "Actions": Sequence[str],
    },
)

BatchResultErrorEntryTypeDef = TypedDict(
    "BatchResultErrorEntryTypeDef",
    {
        "Id": str,
        "SenderFault": bool,
        "Code": str,
        "Message": NotRequired[str],
    },
)

ChangeMessageVisibilityBatchRequestEntryTypeDef = TypedDict(
    "ChangeMessageVisibilityBatchRequestEntryTypeDef",
    {
        "Id": str,
        "ReceiptHandle": str,
        "VisibilityTimeout": NotRequired[int],
    },
)

ChangeMessageVisibilityBatchRequestQueueChangeMessageVisibilityBatchTypeDef = TypedDict(
    "ChangeMessageVisibilityBatchRequestQueueChangeMessageVisibilityBatchTypeDef",
    {
        "Entries": Sequence["ChangeMessageVisibilityBatchRequestEntryTypeDef"],
    },
)

ChangeMessageVisibilityBatchRequestRequestTypeDef = TypedDict(
    "ChangeMessageVisibilityBatchRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "Entries": Sequence["ChangeMessageVisibilityBatchRequestEntryTypeDef"],
    },
)

ChangeMessageVisibilityBatchResultEntryTypeDef = TypedDict(
    "ChangeMessageVisibilityBatchResultEntryTypeDef",
    {
        "Id": str,
    },
)

ChangeMessageVisibilityBatchResultTypeDef = TypedDict(
    "ChangeMessageVisibilityBatchResultTypeDef",
    {
        "Successful": List["ChangeMessageVisibilityBatchResultEntryTypeDef"],
        "Failed": List["BatchResultErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChangeMessageVisibilityRequestMessageChangeVisibilityTypeDef = TypedDict(
    "ChangeMessageVisibilityRequestMessageChangeVisibilityTypeDef",
    {
        "VisibilityTimeout": int,
    },
)

ChangeMessageVisibilityRequestRequestTypeDef = TypedDict(
    "ChangeMessageVisibilityRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "ReceiptHandle": str,
        "VisibilityTimeout": int,
    },
)

CreateQueueRequestRequestTypeDef = TypedDict(
    "CreateQueueRequestRequestTypeDef",
    {
        "QueueName": str,
        "Attributes": NotRequired[Mapping[QueueAttributeNameType, str]],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateQueueRequestServiceResourceCreateQueueTypeDef = TypedDict(
    "CreateQueueRequestServiceResourceCreateQueueTypeDef",
    {
        "QueueName": str,
        "Attributes": NotRequired[Mapping[QueueAttributeNameType, str]],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateQueueResultTypeDef = TypedDict(
    "CreateQueueResultTypeDef",
    {
        "QueueUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMessageBatchRequestEntryTypeDef = TypedDict(
    "DeleteMessageBatchRequestEntryTypeDef",
    {
        "Id": str,
        "ReceiptHandle": str,
    },
)

DeleteMessageBatchRequestQueueDeleteMessagesTypeDef = TypedDict(
    "DeleteMessageBatchRequestQueueDeleteMessagesTypeDef",
    {
        "Entries": Sequence["DeleteMessageBatchRequestEntryTypeDef"],
    },
)

DeleteMessageBatchRequestRequestTypeDef = TypedDict(
    "DeleteMessageBatchRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "Entries": Sequence["DeleteMessageBatchRequestEntryTypeDef"],
    },
)

DeleteMessageBatchResultEntryTypeDef = TypedDict(
    "DeleteMessageBatchResultEntryTypeDef",
    {
        "Id": str,
    },
)

DeleteMessageBatchResultTypeDef = TypedDict(
    "DeleteMessageBatchResultTypeDef",
    {
        "Successful": List["DeleteMessageBatchResultEntryTypeDef"],
        "Failed": List["BatchResultErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMessageRequestRequestTypeDef = TypedDict(
    "DeleteMessageRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "ReceiptHandle": str,
    },
)

DeleteQueueRequestRequestTypeDef = TypedDict(
    "DeleteQueueRequestRequestTypeDef",
    {
        "QueueUrl": str,
    },
)

GetQueueAttributesRequestRequestTypeDef = TypedDict(
    "GetQueueAttributesRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "AttributeNames": NotRequired[Sequence[QueueAttributeNameType]],
    },
)

GetQueueAttributesResultTypeDef = TypedDict(
    "GetQueueAttributesResultTypeDef",
    {
        "Attributes": Dict[QueueAttributeNameType, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueueUrlRequestRequestTypeDef = TypedDict(
    "GetQueueUrlRequestRequestTypeDef",
    {
        "QueueName": str,
        "QueueOwnerAWSAccountId": NotRequired[str],
    },
)

GetQueueUrlRequestServiceResourceGetQueueByNameTypeDef = TypedDict(
    "GetQueueUrlRequestServiceResourceGetQueueByNameTypeDef",
    {
        "QueueName": str,
        "QueueOwnerAWSAccountId": NotRequired[str],
    },
)

GetQueueUrlResultTypeDef = TypedDict(
    "GetQueueUrlResultTypeDef",
    {
        "QueueUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeadLetterSourceQueuesRequestRequestTypeDef = TypedDict(
    "ListDeadLetterSourceQueuesRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDeadLetterSourceQueuesResultTypeDef = TypedDict(
    "ListDeadLetterSourceQueuesResultTypeDef",
    {
        "queueUrls": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListQueueTagsRequestRequestTypeDef = TypedDict(
    "ListQueueTagsRequestRequestTypeDef",
    {
        "QueueUrl": str,
    },
)

ListQueueTagsResultTypeDef = TypedDict(
    "ListQueueTagsResultTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListQueuesRequestRequestTypeDef = TypedDict(
    "ListQueuesRequestRequestTypeDef",
    {
        "QueueNamePrefix": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListQueuesResultTypeDef = TypedDict(
    "ListQueuesResultTypeDef",
    {
        "QueueUrls": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MessageAttributeValueTypeDef = TypedDict(
    "MessageAttributeValueTypeDef",
    {
        "DataType": str,
        "StringValue": NotRequired[str],
        "BinaryValue": NotRequired[bytes],
        "StringListValues": NotRequired[List[str]],
        "BinaryListValues": NotRequired[List[bytes]],
    },
)

MessageSystemAttributeValueTypeDef = TypedDict(
    "MessageSystemAttributeValueTypeDef",
    {
        "DataType": str,
        "StringValue": NotRequired[str],
        "BinaryValue": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "StringListValues": NotRequired[Sequence[str]],
        "BinaryListValues": NotRequired[Sequence[Union[bytes, IO[bytes], StreamingBody]]],
    },
)

MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "MessageId": NotRequired[str],
        "ReceiptHandle": NotRequired[str],
        "MD5OfBody": NotRequired[str],
        "Body": NotRequired[str],
        "Attributes": NotRequired[Dict[MessageSystemAttributeNameType, str]],
        "MD5OfMessageAttributes": NotRequired[str],
        "MessageAttributes": NotRequired[Dict[str, "MessageAttributeValueTypeDef"]],
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

PurgeQueueRequestRequestTypeDef = TypedDict(
    "PurgeQueueRequestRequestTypeDef",
    {
        "QueueUrl": str,
    },
)

QueueMessageRequestTypeDef = TypedDict(
    "QueueMessageRequestTypeDef",
    {
        "receipt_handle": str,
    },
)

ReceiveMessageRequestQueueReceiveMessagesTypeDef = TypedDict(
    "ReceiveMessageRequestQueueReceiveMessagesTypeDef",
    {
        "AttributeNames": NotRequired[Sequence[QueueAttributeNameType]],
        "MessageAttributeNames": NotRequired[Sequence[str]],
        "MaxNumberOfMessages": NotRequired[int],
        "VisibilityTimeout": NotRequired[int],
        "WaitTimeSeconds": NotRequired[int],
        "ReceiveRequestAttemptId": NotRequired[str],
    },
)

ReceiveMessageRequestRequestTypeDef = TypedDict(
    "ReceiveMessageRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "AttributeNames": NotRequired[Sequence[QueueAttributeNameType]],
        "MessageAttributeNames": NotRequired[Sequence[str]],
        "MaxNumberOfMessages": NotRequired[int],
        "VisibilityTimeout": NotRequired[int],
        "WaitTimeSeconds": NotRequired[int],
        "ReceiveRequestAttemptId": NotRequired[str],
    },
)

ReceiveMessageResultTypeDef = TypedDict(
    "ReceiveMessageResultTypeDef",
    {
        "Messages": List["MessageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemovePermissionRequestQueueRemovePermissionTypeDef = TypedDict(
    "RemovePermissionRequestQueueRemovePermissionTypeDef",
    {
        "Label": str,
    },
)

RemovePermissionRequestRequestTypeDef = TypedDict(
    "RemovePermissionRequestRequestTypeDef",
    {
        "QueueUrl": str,
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

SendMessageBatchRequestEntryTypeDef = TypedDict(
    "SendMessageBatchRequestEntryTypeDef",
    {
        "Id": str,
        "MessageBody": str,
        "DelaySeconds": NotRequired[int],
        "MessageAttributes": NotRequired[Mapping[str, "MessageAttributeValueTypeDef"]],
        "MessageSystemAttributes": NotRequired[
            Mapping[Literal["AWSTraceHeader"], "MessageSystemAttributeValueTypeDef"]
        ],
        "MessageDeduplicationId": NotRequired[str],
        "MessageGroupId": NotRequired[str],
    },
)

SendMessageBatchRequestQueueSendMessagesTypeDef = TypedDict(
    "SendMessageBatchRequestQueueSendMessagesTypeDef",
    {
        "Entries": Sequence["SendMessageBatchRequestEntryTypeDef"],
    },
)

SendMessageBatchRequestRequestTypeDef = TypedDict(
    "SendMessageBatchRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "Entries": Sequence["SendMessageBatchRequestEntryTypeDef"],
    },
)

SendMessageBatchResultEntryTypeDef = TypedDict(
    "SendMessageBatchResultEntryTypeDef",
    {
        "Id": str,
        "MessageId": str,
        "MD5OfMessageBody": str,
        "MD5OfMessageAttributes": NotRequired[str],
        "MD5OfMessageSystemAttributes": NotRequired[str],
        "SequenceNumber": NotRequired[str],
    },
)

SendMessageBatchResultTypeDef = TypedDict(
    "SendMessageBatchResultTypeDef",
    {
        "Successful": List["SendMessageBatchResultEntryTypeDef"],
        "Failed": List["BatchResultErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SendMessageRequestQueueSendMessageTypeDef = TypedDict(
    "SendMessageRequestQueueSendMessageTypeDef",
    {
        "MessageBody": str,
        "DelaySeconds": NotRequired[int],
        "MessageAttributes": NotRequired[Mapping[str, "MessageAttributeValueTypeDef"]],
        "MessageSystemAttributes": NotRequired[
            Mapping[Literal["AWSTraceHeader"], "MessageSystemAttributeValueTypeDef"]
        ],
        "MessageDeduplicationId": NotRequired[str],
        "MessageGroupId": NotRequired[str],
    },
)

SendMessageRequestRequestTypeDef = TypedDict(
    "SendMessageRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "MessageBody": str,
        "DelaySeconds": NotRequired[int],
        "MessageAttributes": NotRequired[Mapping[str, "MessageAttributeValueTypeDef"]],
        "MessageSystemAttributes": NotRequired[
            Mapping[Literal["AWSTraceHeader"], "MessageSystemAttributeValueTypeDef"]
        ],
        "MessageDeduplicationId": NotRequired[str],
        "MessageGroupId": NotRequired[str],
    },
)

SendMessageResultTypeDef = TypedDict(
    "SendMessageResultTypeDef",
    {
        "MD5OfMessageBody": str,
        "MD5OfMessageAttributes": str,
        "MD5OfMessageSystemAttributes": str,
        "MessageId": str,
        "SequenceNumber": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceResourceMessageRequestTypeDef = TypedDict(
    "ServiceResourceMessageRequestTypeDef",
    {
        "queue_url": str,
        "receipt_handle": str,
    },
)

ServiceResourceQueueRequestTypeDef = TypedDict(
    "ServiceResourceQueueRequestTypeDef",
    {
        "url": str,
    },
)

SetQueueAttributesRequestQueueSetAttributesTypeDef = TypedDict(
    "SetQueueAttributesRequestQueueSetAttributesTypeDef",
    {
        "Attributes": Mapping[QueueAttributeNameType, str],
    },
)

SetQueueAttributesRequestRequestTypeDef = TypedDict(
    "SetQueueAttributesRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "Attributes": Mapping[QueueAttributeNameType, str],
    },
)

TagQueueRequestRequestTypeDef = TypedDict(
    "TagQueueRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "Tags": Mapping[str, str],
    },
)

UntagQueueRequestRequestTypeDef = TypedDict(
    "UntagQueueRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "TagKeys": Sequence[str],
    },
)
