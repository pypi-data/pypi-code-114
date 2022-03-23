"""
Type annotations for clouddirectory service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_clouddirectory/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_clouddirectory.type_defs import AddFacetToObjectRequestRequestTypeDef

    data: AddFacetToObjectRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    BatchReadExceptionTypeType,
    ConsistencyLevelType,
    DirectoryStateType,
    FacetAttributeTypeType,
    FacetStyleType,
    ObjectTypeType,
    RangeModeType,
    RequiredAttributeBehaviorType,
    RuleTypeType,
    UpdateActionTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddFacetToObjectRequestRequestTypeDef",
    "ApplySchemaRequestRequestTypeDef",
    "ApplySchemaResponseTypeDef",
    "AttachObjectRequestRequestTypeDef",
    "AttachObjectResponseTypeDef",
    "AttachPolicyRequestRequestTypeDef",
    "AttachToIndexRequestRequestTypeDef",
    "AttachToIndexResponseTypeDef",
    "AttachTypedLinkRequestRequestTypeDef",
    "AttachTypedLinkResponseTypeDef",
    "AttributeKeyAndValueTypeDef",
    "AttributeKeyTypeDef",
    "AttributeNameAndValueTypeDef",
    "BatchAddFacetToObjectTypeDef",
    "BatchAttachObjectResponseTypeDef",
    "BatchAttachObjectTypeDef",
    "BatchAttachPolicyTypeDef",
    "BatchAttachToIndexResponseTypeDef",
    "BatchAttachToIndexTypeDef",
    "BatchAttachTypedLinkResponseTypeDef",
    "BatchAttachTypedLinkTypeDef",
    "BatchCreateIndexResponseTypeDef",
    "BatchCreateIndexTypeDef",
    "BatchCreateObjectResponseTypeDef",
    "BatchCreateObjectTypeDef",
    "BatchDeleteObjectTypeDef",
    "BatchDetachFromIndexResponseTypeDef",
    "BatchDetachFromIndexTypeDef",
    "BatchDetachObjectResponseTypeDef",
    "BatchDetachObjectTypeDef",
    "BatchDetachPolicyTypeDef",
    "BatchDetachTypedLinkTypeDef",
    "BatchGetLinkAttributesResponseTypeDef",
    "BatchGetLinkAttributesTypeDef",
    "BatchGetObjectAttributesResponseTypeDef",
    "BatchGetObjectAttributesTypeDef",
    "BatchGetObjectInformationResponseTypeDef",
    "BatchGetObjectInformationTypeDef",
    "BatchListAttachedIndicesResponseTypeDef",
    "BatchListAttachedIndicesTypeDef",
    "BatchListIncomingTypedLinksResponseTypeDef",
    "BatchListIncomingTypedLinksTypeDef",
    "BatchListIndexResponseTypeDef",
    "BatchListIndexTypeDef",
    "BatchListObjectAttributesResponseTypeDef",
    "BatchListObjectAttributesTypeDef",
    "BatchListObjectChildrenResponseTypeDef",
    "BatchListObjectChildrenTypeDef",
    "BatchListObjectParentPathsResponseTypeDef",
    "BatchListObjectParentPathsTypeDef",
    "BatchListObjectParentsResponseTypeDef",
    "BatchListObjectParentsTypeDef",
    "BatchListObjectPoliciesResponseTypeDef",
    "BatchListObjectPoliciesTypeDef",
    "BatchListOutgoingTypedLinksResponseTypeDef",
    "BatchListOutgoingTypedLinksTypeDef",
    "BatchListPolicyAttachmentsResponseTypeDef",
    "BatchListPolicyAttachmentsTypeDef",
    "BatchLookupPolicyResponseTypeDef",
    "BatchLookupPolicyTypeDef",
    "BatchReadExceptionTypeDef",
    "BatchReadOperationResponseTypeDef",
    "BatchReadOperationTypeDef",
    "BatchReadRequestRequestTypeDef",
    "BatchReadResponseTypeDef",
    "BatchReadSuccessfulResponseTypeDef",
    "BatchRemoveFacetFromObjectTypeDef",
    "BatchUpdateLinkAttributesTypeDef",
    "BatchUpdateObjectAttributesResponseTypeDef",
    "BatchUpdateObjectAttributesTypeDef",
    "BatchWriteOperationResponseTypeDef",
    "BatchWriteOperationTypeDef",
    "BatchWriteRequestRequestTypeDef",
    "BatchWriteResponseTypeDef",
    "CreateDirectoryRequestRequestTypeDef",
    "CreateDirectoryResponseTypeDef",
    "CreateFacetRequestRequestTypeDef",
    "CreateIndexRequestRequestTypeDef",
    "CreateIndexResponseTypeDef",
    "CreateObjectRequestRequestTypeDef",
    "CreateObjectResponseTypeDef",
    "CreateSchemaRequestRequestTypeDef",
    "CreateSchemaResponseTypeDef",
    "CreateTypedLinkFacetRequestRequestTypeDef",
    "DeleteDirectoryRequestRequestTypeDef",
    "DeleteDirectoryResponseTypeDef",
    "DeleteFacetRequestRequestTypeDef",
    "DeleteObjectRequestRequestTypeDef",
    "DeleteSchemaRequestRequestTypeDef",
    "DeleteSchemaResponseTypeDef",
    "DeleteTypedLinkFacetRequestRequestTypeDef",
    "DetachFromIndexRequestRequestTypeDef",
    "DetachFromIndexResponseTypeDef",
    "DetachObjectRequestRequestTypeDef",
    "DetachObjectResponseTypeDef",
    "DetachPolicyRequestRequestTypeDef",
    "DetachTypedLinkRequestRequestTypeDef",
    "DirectoryTypeDef",
    "DisableDirectoryRequestRequestTypeDef",
    "DisableDirectoryResponseTypeDef",
    "EnableDirectoryRequestRequestTypeDef",
    "EnableDirectoryResponseTypeDef",
    "FacetAttributeDefinitionTypeDef",
    "FacetAttributeReferenceTypeDef",
    "FacetAttributeTypeDef",
    "FacetAttributeUpdateTypeDef",
    "FacetTypeDef",
    "GetAppliedSchemaVersionRequestRequestTypeDef",
    "GetAppliedSchemaVersionResponseTypeDef",
    "GetDirectoryRequestRequestTypeDef",
    "GetDirectoryResponseTypeDef",
    "GetFacetRequestRequestTypeDef",
    "GetFacetResponseTypeDef",
    "GetLinkAttributesRequestRequestTypeDef",
    "GetLinkAttributesResponseTypeDef",
    "GetObjectAttributesRequestRequestTypeDef",
    "GetObjectAttributesResponseTypeDef",
    "GetObjectInformationRequestRequestTypeDef",
    "GetObjectInformationResponseTypeDef",
    "GetSchemaAsJsonRequestRequestTypeDef",
    "GetSchemaAsJsonResponseTypeDef",
    "GetTypedLinkFacetInformationRequestRequestTypeDef",
    "GetTypedLinkFacetInformationResponseTypeDef",
    "IndexAttachmentTypeDef",
    "LinkAttributeActionTypeDef",
    "LinkAttributeUpdateTypeDef",
    "ListAppliedSchemaArnsRequestRequestTypeDef",
    "ListAppliedSchemaArnsResponseTypeDef",
    "ListAttachedIndicesRequestRequestTypeDef",
    "ListAttachedIndicesResponseTypeDef",
    "ListDevelopmentSchemaArnsRequestRequestTypeDef",
    "ListDevelopmentSchemaArnsResponseTypeDef",
    "ListDirectoriesRequestRequestTypeDef",
    "ListDirectoriesResponseTypeDef",
    "ListFacetAttributesRequestRequestTypeDef",
    "ListFacetAttributesResponseTypeDef",
    "ListFacetNamesRequestRequestTypeDef",
    "ListFacetNamesResponseTypeDef",
    "ListIncomingTypedLinksRequestRequestTypeDef",
    "ListIncomingTypedLinksResponseTypeDef",
    "ListIndexRequestRequestTypeDef",
    "ListIndexResponseTypeDef",
    "ListManagedSchemaArnsRequestRequestTypeDef",
    "ListManagedSchemaArnsResponseTypeDef",
    "ListObjectAttributesRequestRequestTypeDef",
    "ListObjectAttributesResponseTypeDef",
    "ListObjectChildrenRequestRequestTypeDef",
    "ListObjectChildrenResponseTypeDef",
    "ListObjectParentPathsRequestRequestTypeDef",
    "ListObjectParentPathsResponseTypeDef",
    "ListObjectParentsRequestRequestTypeDef",
    "ListObjectParentsResponseTypeDef",
    "ListObjectPoliciesRequestRequestTypeDef",
    "ListObjectPoliciesResponseTypeDef",
    "ListOutgoingTypedLinksRequestRequestTypeDef",
    "ListOutgoingTypedLinksResponseTypeDef",
    "ListPolicyAttachmentsRequestRequestTypeDef",
    "ListPolicyAttachmentsResponseTypeDef",
    "ListPublishedSchemaArnsRequestRequestTypeDef",
    "ListPublishedSchemaArnsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTypedLinkFacetAttributesRequestRequestTypeDef",
    "ListTypedLinkFacetAttributesResponseTypeDef",
    "ListTypedLinkFacetNamesRequestRequestTypeDef",
    "ListTypedLinkFacetNamesResponseTypeDef",
    "LookupPolicyRequestRequestTypeDef",
    "LookupPolicyResponseTypeDef",
    "ObjectAttributeActionTypeDef",
    "ObjectAttributeRangeTypeDef",
    "ObjectAttributeUpdateTypeDef",
    "ObjectIdentifierAndLinkNameTupleTypeDef",
    "ObjectReferenceTypeDef",
    "PaginatorConfigTypeDef",
    "PathToObjectIdentifiersTypeDef",
    "PolicyAttachmentTypeDef",
    "PolicyToPathTypeDef",
    "PublishSchemaRequestRequestTypeDef",
    "PublishSchemaResponseTypeDef",
    "PutSchemaFromJsonRequestRequestTypeDef",
    "PutSchemaFromJsonResponseTypeDef",
    "RemoveFacetFromObjectRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RuleTypeDef",
    "SchemaFacetTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TypedAttributeValueRangeTypeDef",
    "TypedAttributeValueTypeDef",
    "TypedLinkAttributeDefinitionTypeDef",
    "TypedLinkAttributeRangeTypeDef",
    "TypedLinkFacetAttributeUpdateTypeDef",
    "TypedLinkFacetTypeDef",
    "TypedLinkSchemaAndFacetNameTypeDef",
    "TypedLinkSpecifierTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateFacetRequestRequestTypeDef",
    "UpdateLinkAttributesRequestRequestTypeDef",
    "UpdateObjectAttributesRequestRequestTypeDef",
    "UpdateObjectAttributesResponseTypeDef",
    "UpdateSchemaRequestRequestTypeDef",
    "UpdateSchemaResponseTypeDef",
    "UpdateTypedLinkFacetRequestRequestTypeDef",
    "UpgradeAppliedSchemaRequestRequestTypeDef",
    "UpgradeAppliedSchemaResponseTypeDef",
    "UpgradePublishedSchemaRequestRequestTypeDef",
    "UpgradePublishedSchemaResponseTypeDef",
)

AddFacetToObjectRequestRequestTypeDef = TypedDict(
    "AddFacetToObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "SchemaFacet": "SchemaFacetTypeDef",
        "ObjectReference": "ObjectReferenceTypeDef",
        "ObjectAttributeList": NotRequired[Sequence["AttributeKeyAndValueTypeDef"]],
    },
)

ApplySchemaRequestRequestTypeDef = TypedDict(
    "ApplySchemaRequestRequestTypeDef",
    {
        "PublishedSchemaArn": str,
        "DirectoryArn": str,
    },
)

ApplySchemaResponseTypeDef = TypedDict(
    "ApplySchemaResponseTypeDef",
    {
        "AppliedSchemaArn": str,
        "DirectoryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachObjectRequestRequestTypeDef = TypedDict(
    "AttachObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ParentReference": "ObjectReferenceTypeDef",
        "ChildReference": "ObjectReferenceTypeDef",
        "LinkName": str,
    },
)

AttachObjectResponseTypeDef = TypedDict(
    "AttachObjectResponseTypeDef",
    {
        "AttachedObjectIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachPolicyRequestRequestTypeDef = TypedDict(
    "AttachPolicyRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "PolicyReference": "ObjectReferenceTypeDef",
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

AttachToIndexRequestRequestTypeDef = TypedDict(
    "AttachToIndexRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "IndexReference": "ObjectReferenceTypeDef",
        "TargetReference": "ObjectReferenceTypeDef",
    },
)

AttachToIndexResponseTypeDef = TypedDict(
    "AttachToIndexResponseTypeDef",
    {
        "AttachedObjectIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachTypedLinkRequestRequestTypeDef = TypedDict(
    "AttachTypedLinkRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "SourceObjectReference": "ObjectReferenceTypeDef",
        "TargetObjectReference": "ObjectReferenceTypeDef",
        "TypedLinkFacet": "TypedLinkSchemaAndFacetNameTypeDef",
        "Attributes": Sequence["AttributeNameAndValueTypeDef"],
    },
)

AttachTypedLinkResponseTypeDef = TypedDict(
    "AttachTypedLinkResponseTypeDef",
    {
        "TypedLinkSpecifier": "TypedLinkSpecifierTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttributeKeyAndValueTypeDef = TypedDict(
    "AttributeKeyAndValueTypeDef",
    {
        "Key": "AttributeKeyTypeDef",
        "Value": "TypedAttributeValueTypeDef",
    },
)

AttributeKeyTypeDef = TypedDict(
    "AttributeKeyTypeDef",
    {
        "SchemaArn": str,
        "FacetName": str,
        "Name": str,
    },
)

AttributeNameAndValueTypeDef = TypedDict(
    "AttributeNameAndValueTypeDef",
    {
        "AttributeName": str,
        "Value": "TypedAttributeValueTypeDef",
    },
)

BatchAddFacetToObjectTypeDef = TypedDict(
    "BatchAddFacetToObjectTypeDef",
    {
        "SchemaFacet": "SchemaFacetTypeDef",
        "ObjectAttributeList": Sequence["AttributeKeyAndValueTypeDef"],
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

BatchAttachObjectResponseTypeDef = TypedDict(
    "BatchAttachObjectResponseTypeDef",
    {
        "attachedObjectIdentifier": NotRequired[str],
    },
)

BatchAttachObjectTypeDef = TypedDict(
    "BatchAttachObjectTypeDef",
    {
        "ParentReference": "ObjectReferenceTypeDef",
        "ChildReference": "ObjectReferenceTypeDef",
        "LinkName": str,
    },
)

BatchAttachPolicyTypeDef = TypedDict(
    "BatchAttachPolicyTypeDef",
    {
        "PolicyReference": "ObjectReferenceTypeDef",
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

BatchAttachToIndexResponseTypeDef = TypedDict(
    "BatchAttachToIndexResponseTypeDef",
    {
        "AttachedObjectIdentifier": NotRequired[str],
    },
)

BatchAttachToIndexTypeDef = TypedDict(
    "BatchAttachToIndexTypeDef",
    {
        "IndexReference": "ObjectReferenceTypeDef",
        "TargetReference": "ObjectReferenceTypeDef",
    },
)

BatchAttachTypedLinkResponseTypeDef = TypedDict(
    "BatchAttachTypedLinkResponseTypeDef",
    {
        "TypedLinkSpecifier": NotRequired["TypedLinkSpecifierTypeDef"],
    },
)

BatchAttachTypedLinkTypeDef = TypedDict(
    "BatchAttachTypedLinkTypeDef",
    {
        "SourceObjectReference": "ObjectReferenceTypeDef",
        "TargetObjectReference": "ObjectReferenceTypeDef",
        "TypedLinkFacet": "TypedLinkSchemaAndFacetNameTypeDef",
        "Attributes": Sequence["AttributeNameAndValueTypeDef"],
    },
)

BatchCreateIndexResponseTypeDef = TypedDict(
    "BatchCreateIndexResponseTypeDef",
    {
        "ObjectIdentifier": NotRequired[str],
    },
)

BatchCreateIndexTypeDef = TypedDict(
    "BatchCreateIndexTypeDef",
    {
        "OrderedIndexedAttributeList": Sequence["AttributeKeyTypeDef"],
        "IsUnique": bool,
        "ParentReference": NotRequired["ObjectReferenceTypeDef"],
        "LinkName": NotRequired[str],
        "BatchReferenceName": NotRequired[str],
    },
)

BatchCreateObjectResponseTypeDef = TypedDict(
    "BatchCreateObjectResponseTypeDef",
    {
        "ObjectIdentifier": NotRequired[str],
    },
)

BatchCreateObjectTypeDef = TypedDict(
    "BatchCreateObjectTypeDef",
    {
        "SchemaFacet": Sequence["SchemaFacetTypeDef"],
        "ObjectAttributeList": Sequence["AttributeKeyAndValueTypeDef"],
        "ParentReference": NotRequired["ObjectReferenceTypeDef"],
        "LinkName": NotRequired[str],
        "BatchReferenceName": NotRequired[str],
    },
)

BatchDeleteObjectTypeDef = TypedDict(
    "BatchDeleteObjectTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

BatchDetachFromIndexResponseTypeDef = TypedDict(
    "BatchDetachFromIndexResponseTypeDef",
    {
        "DetachedObjectIdentifier": NotRequired[str],
    },
)

BatchDetachFromIndexTypeDef = TypedDict(
    "BatchDetachFromIndexTypeDef",
    {
        "IndexReference": "ObjectReferenceTypeDef",
        "TargetReference": "ObjectReferenceTypeDef",
    },
)

BatchDetachObjectResponseTypeDef = TypedDict(
    "BatchDetachObjectResponseTypeDef",
    {
        "detachedObjectIdentifier": NotRequired[str],
    },
)

BatchDetachObjectTypeDef = TypedDict(
    "BatchDetachObjectTypeDef",
    {
        "ParentReference": "ObjectReferenceTypeDef",
        "LinkName": str,
        "BatchReferenceName": NotRequired[str],
    },
)

BatchDetachPolicyTypeDef = TypedDict(
    "BatchDetachPolicyTypeDef",
    {
        "PolicyReference": "ObjectReferenceTypeDef",
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

BatchDetachTypedLinkTypeDef = TypedDict(
    "BatchDetachTypedLinkTypeDef",
    {
        "TypedLinkSpecifier": "TypedLinkSpecifierTypeDef",
    },
)

BatchGetLinkAttributesResponseTypeDef = TypedDict(
    "BatchGetLinkAttributesResponseTypeDef",
    {
        "Attributes": NotRequired[List["AttributeKeyAndValueTypeDef"]],
    },
)

BatchGetLinkAttributesTypeDef = TypedDict(
    "BatchGetLinkAttributesTypeDef",
    {
        "TypedLinkSpecifier": "TypedLinkSpecifierTypeDef",
        "AttributeNames": Sequence[str],
    },
)

BatchGetObjectAttributesResponseTypeDef = TypedDict(
    "BatchGetObjectAttributesResponseTypeDef",
    {
        "Attributes": NotRequired[List["AttributeKeyAndValueTypeDef"]],
    },
)

BatchGetObjectAttributesTypeDef = TypedDict(
    "BatchGetObjectAttributesTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
        "SchemaFacet": "SchemaFacetTypeDef",
        "AttributeNames": Sequence[str],
    },
)

BatchGetObjectInformationResponseTypeDef = TypedDict(
    "BatchGetObjectInformationResponseTypeDef",
    {
        "SchemaFacets": NotRequired[List["SchemaFacetTypeDef"]],
        "ObjectIdentifier": NotRequired[str],
    },
)

BatchGetObjectInformationTypeDef = TypedDict(
    "BatchGetObjectInformationTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

BatchListAttachedIndicesResponseTypeDef = TypedDict(
    "BatchListAttachedIndicesResponseTypeDef",
    {
        "IndexAttachments": NotRequired[List["IndexAttachmentTypeDef"]],
        "NextToken": NotRequired[str],
    },
)

BatchListAttachedIndicesTypeDef = TypedDict(
    "BatchListAttachedIndicesTypeDef",
    {
        "TargetReference": "ObjectReferenceTypeDef",
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

BatchListIncomingTypedLinksResponseTypeDef = TypedDict(
    "BatchListIncomingTypedLinksResponseTypeDef",
    {
        "LinkSpecifiers": NotRequired[List["TypedLinkSpecifierTypeDef"]],
        "NextToken": NotRequired[str],
    },
)

BatchListIncomingTypedLinksTypeDef = TypedDict(
    "BatchListIncomingTypedLinksTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
        "FilterAttributeRanges": NotRequired[Sequence["TypedLinkAttributeRangeTypeDef"]],
        "FilterTypedLink": NotRequired["TypedLinkSchemaAndFacetNameTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

BatchListIndexResponseTypeDef = TypedDict(
    "BatchListIndexResponseTypeDef",
    {
        "IndexAttachments": NotRequired[List["IndexAttachmentTypeDef"]],
        "NextToken": NotRequired[str],
    },
)

BatchListIndexTypeDef = TypedDict(
    "BatchListIndexTypeDef",
    {
        "IndexReference": "ObjectReferenceTypeDef",
        "RangesOnIndexedValues": NotRequired[Sequence["ObjectAttributeRangeTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

BatchListObjectAttributesResponseTypeDef = TypedDict(
    "BatchListObjectAttributesResponseTypeDef",
    {
        "Attributes": NotRequired[List["AttributeKeyAndValueTypeDef"]],
        "NextToken": NotRequired[str],
    },
)

BatchListObjectAttributesTypeDef = TypedDict(
    "BatchListObjectAttributesTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "FacetFilter": NotRequired["SchemaFacetTypeDef"],
    },
)

BatchListObjectChildrenResponseTypeDef = TypedDict(
    "BatchListObjectChildrenResponseTypeDef",
    {
        "Children": NotRequired[Dict[str, str]],
        "NextToken": NotRequired[str],
    },
)

BatchListObjectChildrenTypeDef = TypedDict(
    "BatchListObjectChildrenTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

BatchListObjectParentPathsResponseTypeDef = TypedDict(
    "BatchListObjectParentPathsResponseTypeDef",
    {
        "PathToObjectIdentifiersList": NotRequired[List["PathToObjectIdentifiersTypeDef"]],
        "NextToken": NotRequired[str],
    },
)

BatchListObjectParentPathsTypeDef = TypedDict(
    "BatchListObjectParentPathsTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

BatchListObjectParentsResponseTypeDef = TypedDict(
    "BatchListObjectParentsResponseTypeDef",
    {
        "ParentLinks": NotRequired[List["ObjectIdentifierAndLinkNameTupleTypeDef"]],
        "NextToken": NotRequired[str],
    },
)

BatchListObjectParentsTypeDef = TypedDict(
    "BatchListObjectParentsTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

BatchListObjectPoliciesResponseTypeDef = TypedDict(
    "BatchListObjectPoliciesResponseTypeDef",
    {
        "AttachedPolicyIds": NotRequired[List[str]],
        "NextToken": NotRequired[str],
    },
)

BatchListObjectPoliciesTypeDef = TypedDict(
    "BatchListObjectPoliciesTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

BatchListOutgoingTypedLinksResponseTypeDef = TypedDict(
    "BatchListOutgoingTypedLinksResponseTypeDef",
    {
        "TypedLinkSpecifiers": NotRequired[List["TypedLinkSpecifierTypeDef"]],
        "NextToken": NotRequired[str],
    },
)

BatchListOutgoingTypedLinksTypeDef = TypedDict(
    "BatchListOutgoingTypedLinksTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
        "FilterAttributeRanges": NotRequired[Sequence["TypedLinkAttributeRangeTypeDef"]],
        "FilterTypedLink": NotRequired["TypedLinkSchemaAndFacetNameTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

BatchListPolicyAttachmentsResponseTypeDef = TypedDict(
    "BatchListPolicyAttachmentsResponseTypeDef",
    {
        "ObjectIdentifiers": NotRequired[List[str]],
        "NextToken": NotRequired[str],
    },
)

BatchListPolicyAttachmentsTypeDef = TypedDict(
    "BatchListPolicyAttachmentsTypeDef",
    {
        "PolicyReference": "ObjectReferenceTypeDef",
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

BatchLookupPolicyResponseTypeDef = TypedDict(
    "BatchLookupPolicyResponseTypeDef",
    {
        "PolicyToPathList": NotRequired[List["PolicyToPathTypeDef"]],
        "NextToken": NotRequired[str],
    },
)

BatchLookupPolicyTypeDef = TypedDict(
    "BatchLookupPolicyTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

BatchReadExceptionTypeDef = TypedDict(
    "BatchReadExceptionTypeDef",
    {
        "Type": NotRequired[BatchReadExceptionTypeType],
        "Message": NotRequired[str],
    },
)

BatchReadOperationResponseTypeDef = TypedDict(
    "BatchReadOperationResponseTypeDef",
    {
        "SuccessfulResponse": NotRequired["BatchReadSuccessfulResponseTypeDef"],
        "ExceptionResponse": NotRequired["BatchReadExceptionTypeDef"],
    },
)

BatchReadOperationTypeDef = TypedDict(
    "BatchReadOperationTypeDef",
    {
        "ListObjectAttributes": NotRequired["BatchListObjectAttributesTypeDef"],
        "ListObjectChildren": NotRequired["BatchListObjectChildrenTypeDef"],
        "ListAttachedIndices": NotRequired["BatchListAttachedIndicesTypeDef"],
        "ListObjectParentPaths": NotRequired["BatchListObjectParentPathsTypeDef"],
        "GetObjectInformation": NotRequired["BatchGetObjectInformationTypeDef"],
        "GetObjectAttributes": NotRequired["BatchGetObjectAttributesTypeDef"],
        "ListObjectParents": NotRequired["BatchListObjectParentsTypeDef"],
        "ListObjectPolicies": NotRequired["BatchListObjectPoliciesTypeDef"],
        "ListPolicyAttachments": NotRequired["BatchListPolicyAttachmentsTypeDef"],
        "LookupPolicy": NotRequired["BatchLookupPolicyTypeDef"],
        "ListIndex": NotRequired["BatchListIndexTypeDef"],
        "ListOutgoingTypedLinks": NotRequired["BatchListOutgoingTypedLinksTypeDef"],
        "ListIncomingTypedLinks": NotRequired["BatchListIncomingTypedLinksTypeDef"],
        "GetLinkAttributes": NotRequired["BatchGetLinkAttributesTypeDef"],
    },
)

BatchReadRequestRequestTypeDef = TypedDict(
    "BatchReadRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "Operations": Sequence["BatchReadOperationTypeDef"],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)

BatchReadResponseTypeDef = TypedDict(
    "BatchReadResponseTypeDef",
    {
        "Responses": List["BatchReadOperationResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchReadSuccessfulResponseTypeDef = TypedDict(
    "BatchReadSuccessfulResponseTypeDef",
    {
        "ListObjectAttributes": NotRequired["BatchListObjectAttributesResponseTypeDef"],
        "ListObjectChildren": NotRequired["BatchListObjectChildrenResponseTypeDef"],
        "GetObjectInformation": NotRequired["BatchGetObjectInformationResponseTypeDef"],
        "GetObjectAttributes": NotRequired["BatchGetObjectAttributesResponseTypeDef"],
        "ListAttachedIndices": NotRequired["BatchListAttachedIndicesResponseTypeDef"],
        "ListObjectParentPaths": NotRequired["BatchListObjectParentPathsResponseTypeDef"],
        "ListObjectPolicies": NotRequired["BatchListObjectPoliciesResponseTypeDef"],
        "ListPolicyAttachments": NotRequired["BatchListPolicyAttachmentsResponseTypeDef"],
        "LookupPolicy": NotRequired["BatchLookupPolicyResponseTypeDef"],
        "ListIndex": NotRequired["BatchListIndexResponseTypeDef"],
        "ListOutgoingTypedLinks": NotRequired["BatchListOutgoingTypedLinksResponseTypeDef"],
        "ListIncomingTypedLinks": NotRequired["BatchListIncomingTypedLinksResponseTypeDef"],
        "GetLinkAttributes": NotRequired["BatchGetLinkAttributesResponseTypeDef"],
        "ListObjectParents": NotRequired["BatchListObjectParentsResponseTypeDef"],
    },
)

BatchRemoveFacetFromObjectTypeDef = TypedDict(
    "BatchRemoveFacetFromObjectTypeDef",
    {
        "SchemaFacet": "SchemaFacetTypeDef",
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

BatchUpdateLinkAttributesTypeDef = TypedDict(
    "BatchUpdateLinkAttributesTypeDef",
    {
        "TypedLinkSpecifier": "TypedLinkSpecifierTypeDef",
        "AttributeUpdates": Sequence["LinkAttributeUpdateTypeDef"],
    },
)

BatchUpdateObjectAttributesResponseTypeDef = TypedDict(
    "BatchUpdateObjectAttributesResponseTypeDef",
    {
        "ObjectIdentifier": NotRequired[str],
    },
)

BatchUpdateObjectAttributesTypeDef = TypedDict(
    "BatchUpdateObjectAttributesTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
        "AttributeUpdates": Sequence["ObjectAttributeUpdateTypeDef"],
    },
)

BatchWriteOperationResponseTypeDef = TypedDict(
    "BatchWriteOperationResponseTypeDef",
    {
        "CreateObject": NotRequired["BatchCreateObjectResponseTypeDef"],
        "AttachObject": NotRequired["BatchAttachObjectResponseTypeDef"],
        "DetachObject": NotRequired["BatchDetachObjectResponseTypeDef"],
        "UpdateObjectAttributes": NotRequired["BatchUpdateObjectAttributesResponseTypeDef"],
        "DeleteObject": NotRequired[Dict[str, Any]],
        "AddFacetToObject": NotRequired[Dict[str, Any]],
        "RemoveFacetFromObject": NotRequired[Dict[str, Any]],
        "AttachPolicy": NotRequired[Dict[str, Any]],
        "DetachPolicy": NotRequired[Dict[str, Any]],
        "CreateIndex": NotRequired["BatchCreateIndexResponseTypeDef"],
        "AttachToIndex": NotRequired["BatchAttachToIndexResponseTypeDef"],
        "DetachFromIndex": NotRequired["BatchDetachFromIndexResponseTypeDef"],
        "AttachTypedLink": NotRequired["BatchAttachTypedLinkResponseTypeDef"],
        "DetachTypedLink": NotRequired[Dict[str, Any]],
        "UpdateLinkAttributes": NotRequired[Dict[str, Any]],
    },
)

BatchWriteOperationTypeDef = TypedDict(
    "BatchWriteOperationTypeDef",
    {
        "CreateObject": NotRequired["BatchCreateObjectTypeDef"],
        "AttachObject": NotRequired["BatchAttachObjectTypeDef"],
        "DetachObject": NotRequired["BatchDetachObjectTypeDef"],
        "UpdateObjectAttributes": NotRequired["BatchUpdateObjectAttributesTypeDef"],
        "DeleteObject": NotRequired["BatchDeleteObjectTypeDef"],
        "AddFacetToObject": NotRequired["BatchAddFacetToObjectTypeDef"],
        "RemoveFacetFromObject": NotRequired["BatchRemoveFacetFromObjectTypeDef"],
        "AttachPolicy": NotRequired["BatchAttachPolicyTypeDef"],
        "DetachPolicy": NotRequired["BatchDetachPolicyTypeDef"],
        "CreateIndex": NotRequired["BatchCreateIndexTypeDef"],
        "AttachToIndex": NotRequired["BatchAttachToIndexTypeDef"],
        "DetachFromIndex": NotRequired["BatchDetachFromIndexTypeDef"],
        "AttachTypedLink": NotRequired["BatchAttachTypedLinkTypeDef"],
        "DetachTypedLink": NotRequired["BatchDetachTypedLinkTypeDef"],
        "UpdateLinkAttributes": NotRequired["BatchUpdateLinkAttributesTypeDef"],
    },
)

BatchWriteRequestRequestTypeDef = TypedDict(
    "BatchWriteRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "Operations": Sequence["BatchWriteOperationTypeDef"],
    },
)

BatchWriteResponseTypeDef = TypedDict(
    "BatchWriteResponseTypeDef",
    {
        "Responses": List["BatchWriteOperationResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDirectoryRequestRequestTypeDef = TypedDict(
    "CreateDirectoryRequestRequestTypeDef",
    {
        "Name": str,
        "SchemaArn": str,
    },
)

CreateDirectoryResponseTypeDef = TypedDict(
    "CreateDirectoryResponseTypeDef",
    {
        "DirectoryArn": str,
        "Name": str,
        "ObjectIdentifier": str,
        "AppliedSchemaArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFacetRequestRequestTypeDef = TypedDict(
    "CreateFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
        "Attributes": NotRequired[Sequence["FacetAttributeTypeDef"]],
        "ObjectType": NotRequired[ObjectTypeType],
        "FacetStyle": NotRequired[FacetStyleType],
    },
)

CreateIndexRequestRequestTypeDef = TypedDict(
    "CreateIndexRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "OrderedIndexedAttributeList": Sequence["AttributeKeyTypeDef"],
        "IsUnique": bool,
        "ParentReference": NotRequired["ObjectReferenceTypeDef"],
        "LinkName": NotRequired[str],
    },
)

CreateIndexResponseTypeDef = TypedDict(
    "CreateIndexResponseTypeDef",
    {
        "ObjectIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateObjectRequestRequestTypeDef = TypedDict(
    "CreateObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "SchemaFacets": Sequence["SchemaFacetTypeDef"],
        "ObjectAttributeList": NotRequired[Sequence["AttributeKeyAndValueTypeDef"]],
        "ParentReference": NotRequired["ObjectReferenceTypeDef"],
        "LinkName": NotRequired[str],
    },
)

CreateObjectResponseTypeDef = TypedDict(
    "CreateObjectResponseTypeDef",
    {
        "ObjectIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSchemaRequestRequestTypeDef = TypedDict(
    "CreateSchemaRequestRequestTypeDef",
    {
        "Name": str,
    },
)

CreateSchemaResponseTypeDef = TypedDict(
    "CreateSchemaResponseTypeDef",
    {
        "SchemaArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTypedLinkFacetRequestRequestTypeDef = TypedDict(
    "CreateTypedLinkFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Facet": "TypedLinkFacetTypeDef",
    },
)

DeleteDirectoryRequestRequestTypeDef = TypedDict(
    "DeleteDirectoryRequestRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)

DeleteDirectoryResponseTypeDef = TypedDict(
    "DeleteDirectoryResponseTypeDef",
    {
        "DirectoryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFacetRequestRequestTypeDef = TypedDict(
    "DeleteFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)

DeleteObjectRequestRequestTypeDef = TypedDict(
    "DeleteObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

DeleteSchemaRequestRequestTypeDef = TypedDict(
    "DeleteSchemaRequestRequestTypeDef",
    {
        "SchemaArn": str,
    },
)

DeleteSchemaResponseTypeDef = TypedDict(
    "DeleteSchemaResponseTypeDef",
    {
        "SchemaArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTypedLinkFacetRequestRequestTypeDef = TypedDict(
    "DeleteTypedLinkFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)

DetachFromIndexRequestRequestTypeDef = TypedDict(
    "DetachFromIndexRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "IndexReference": "ObjectReferenceTypeDef",
        "TargetReference": "ObjectReferenceTypeDef",
    },
)

DetachFromIndexResponseTypeDef = TypedDict(
    "DetachFromIndexResponseTypeDef",
    {
        "DetachedObjectIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachObjectRequestRequestTypeDef = TypedDict(
    "DetachObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ParentReference": "ObjectReferenceTypeDef",
        "LinkName": str,
    },
)

DetachObjectResponseTypeDef = TypedDict(
    "DetachObjectResponseTypeDef",
    {
        "DetachedObjectIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachPolicyRequestRequestTypeDef = TypedDict(
    "DetachPolicyRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "PolicyReference": "ObjectReferenceTypeDef",
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

DetachTypedLinkRequestRequestTypeDef = TypedDict(
    "DetachTypedLinkRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "TypedLinkSpecifier": "TypedLinkSpecifierTypeDef",
    },
)

DirectoryTypeDef = TypedDict(
    "DirectoryTypeDef",
    {
        "Name": NotRequired[str],
        "DirectoryArn": NotRequired[str],
        "State": NotRequired[DirectoryStateType],
        "CreationDateTime": NotRequired[datetime],
    },
)

DisableDirectoryRequestRequestTypeDef = TypedDict(
    "DisableDirectoryRequestRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)

DisableDirectoryResponseTypeDef = TypedDict(
    "DisableDirectoryResponseTypeDef",
    {
        "DirectoryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableDirectoryRequestRequestTypeDef = TypedDict(
    "EnableDirectoryRequestRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)

EnableDirectoryResponseTypeDef = TypedDict(
    "EnableDirectoryResponseTypeDef",
    {
        "DirectoryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FacetAttributeDefinitionTypeDef = TypedDict(
    "FacetAttributeDefinitionTypeDef",
    {
        "Type": FacetAttributeTypeType,
        "DefaultValue": NotRequired["TypedAttributeValueTypeDef"],
        "IsImmutable": NotRequired[bool],
        "Rules": NotRequired[Mapping[str, "RuleTypeDef"]],
    },
)

FacetAttributeReferenceTypeDef = TypedDict(
    "FacetAttributeReferenceTypeDef",
    {
        "TargetFacetName": str,
        "TargetAttributeName": str,
    },
)

FacetAttributeTypeDef = TypedDict(
    "FacetAttributeTypeDef",
    {
        "Name": str,
        "AttributeDefinition": NotRequired["FacetAttributeDefinitionTypeDef"],
        "AttributeReference": NotRequired["FacetAttributeReferenceTypeDef"],
        "RequiredBehavior": NotRequired[RequiredAttributeBehaviorType],
    },
)

FacetAttributeUpdateTypeDef = TypedDict(
    "FacetAttributeUpdateTypeDef",
    {
        "Attribute": NotRequired["FacetAttributeTypeDef"],
        "Action": NotRequired[UpdateActionTypeType],
    },
)

FacetTypeDef = TypedDict(
    "FacetTypeDef",
    {
        "Name": NotRequired[str],
        "ObjectType": NotRequired[ObjectTypeType],
        "FacetStyle": NotRequired[FacetStyleType],
    },
)

GetAppliedSchemaVersionRequestRequestTypeDef = TypedDict(
    "GetAppliedSchemaVersionRequestRequestTypeDef",
    {
        "SchemaArn": str,
    },
)

GetAppliedSchemaVersionResponseTypeDef = TypedDict(
    "GetAppliedSchemaVersionResponseTypeDef",
    {
        "AppliedSchemaArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDirectoryRequestRequestTypeDef = TypedDict(
    "GetDirectoryRequestRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)

GetDirectoryResponseTypeDef = TypedDict(
    "GetDirectoryResponseTypeDef",
    {
        "Directory": "DirectoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFacetRequestRequestTypeDef = TypedDict(
    "GetFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)

GetFacetResponseTypeDef = TypedDict(
    "GetFacetResponseTypeDef",
    {
        "Facet": "FacetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLinkAttributesRequestRequestTypeDef = TypedDict(
    "GetLinkAttributesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "TypedLinkSpecifier": "TypedLinkSpecifierTypeDef",
        "AttributeNames": Sequence[str],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)

GetLinkAttributesResponseTypeDef = TypedDict(
    "GetLinkAttributesResponseTypeDef",
    {
        "Attributes": List["AttributeKeyAndValueTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetObjectAttributesRequestRequestTypeDef = TypedDict(
    "GetObjectAttributesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
        "SchemaFacet": "SchemaFacetTypeDef",
        "AttributeNames": Sequence[str],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)

GetObjectAttributesResponseTypeDef = TypedDict(
    "GetObjectAttributesResponseTypeDef",
    {
        "Attributes": List["AttributeKeyAndValueTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetObjectInformationRequestRequestTypeDef = TypedDict(
    "GetObjectInformationRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)

GetObjectInformationResponseTypeDef = TypedDict(
    "GetObjectInformationResponseTypeDef",
    {
        "SchemaFacets": List["SchemaFacetTypeDef"],
        "ObjectIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSchemaAsJsonRequestRequestTypeDef = TypedDict(
    "GetSchemaAsJsonRequestRequestTypeDef",
    {
        "SchemaArn": str,
    },
)

GetSchemaAsJsonResponseTypeDef = TypedDict(
    "GetSchemaAsJsonResponseTypeDef",
    {
        "Name": str,
        "Document": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTypedLinkFacetInformationRequestRequestTypeDef = TypedDict(
    "GetTypedLinkFacetInformationRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)

GetTypedLinkFacetInformationResponseTypeDef = TypedDict(
    "GetTypedLinkFacetInformationResponseTypeDef",
    {
        "IdentityAttributeOrder": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IndexAttachmentTypeDef = TypedDict(
    "IndexAttachmentTypeDef",
    {
        "IndexedAttributes": NotRequired[List["AttributeKeyAndValueTypeDef"]],
        "ObjectIdentifier": NotRequired[str],
    },
)

LinkAttributeActionTypeDef = TypedDict(
    "LinkAttributeActionTypeDef",
    {
        "AttributeActionType": NotRequired[UpdateActionTypeType],
        "AttributeUpdateValue": NotRequired["TypedAttributeValueTypeDef"],
    },
)

LinkAttributeUpdateTypeDef = TypedDict(
    "LinkAttributeUpdateTypeDef",
    {
        "AttributeKey": NotRequired["AttributeKeyTypeDef"],
        "AttributeAction": NotRequired["LinkAttributeActionTypeDef"],
    },
)

ListAppliedSchemaArnsRequestRequestTypeDef = TypedDict(
    "ListAppliedSchemaArnsRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "SchemaArn": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListAppliedSchemaArnsResponseTypeDef = TypedDict(
    "ListAppliedSchemaArnsResponseTypeDef",
    {
        "SchemaArns": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAttachedIndicesRequestRequestTypeDef = TypedDict(
    "ListAttachedIndicesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "TargetReference": "ObjectReferenceTypeDef",
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)

ListAttachedIndicesResponseTypeDef = TypedDict(
    "ListAttachedIndicesResponseTypeDef",
    {
        "IndexAttachments": List["IndexAttachmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevelopmentSchemaArnsRequestRequestTypeDef = TypedDict(
    "ListDevelopmentSchemaArnsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDevelopmentSchemaArnsResponseTypeDef = TypedDict(
    "ListDevelopmentSchemaArnsResponseTypeDef",
    {
        "SchemaArns": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDirectoriesRequestRequestTypeDef = TypedDict(
    "ListDirectoriesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "state": NotRequired[DirectoryStateType],
    },
)

ListDirectoriesResponseTypeDef = TypedDict(
    "ListDirectoriesResponseTypeDef",
    {
        "Directories": List["DirectoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFacetAttributesRequestRequestTypeDef = TypedDict(
    "ListFacetAttributesRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListFacetAttributesResponseTypeDef = TypedDict(
    "ListFacetAttributesResponseTypeDef",
    {
        "Attributes": List["FacetAttributeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFacetNamesRequestRequestTypeDef = TypedDict(
    "ListFacetNamesRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListFacetNamesResponseTypeDef = TypedDict(
    "ListFacetNamesResponseTypeDef",
    {
        "FacetNames": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIncomingTypedLinksRequestRequestTypeDef = TypedDict(
    "ListIncomingTypedLinksRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
        "FilterAttributeRanges": NotRequired[Sequence["TypedLinkAttributeRangeTypeDef"]],
        "FilterTypedLink": NotRequired["TypedLinkSchemaAndFacetNameTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)

ListIncomingTypedLinksResponseTypeDef = TypedDict(
    "ListIncomingTypedLinksResponseTypeDef",
    {
        "LinkSpecifiers": List["TypedLinkSpecifierTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIndexRequestRequestTypeDef = TypedDict(
    "ListIndexRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "IndexReference": "ObjectReferenceTypeDef",
        "RangesOnIndexedValues": NotRequired[Sequence["ObjectAttributeRangeTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)

ListIndexResponseTypeDef = TypedDict(
    "ListIndexResponseTypeDef",
    {
        "IndexAttachments": List["IndexAttachmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListManagedSchemaArnsRequestRequestTypeDef = TypedDict(
    "ListManagedSchemaArnsRequestRequestTypeDef",
    {
        "SchemaArn": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListManagedSchemaArnsResponseTypeDef = TypedDict(
    "ListManagedSchemaArnsResponseTypeDef",
    {
        "SchemaArns": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListObjectAttributesRequestRequestTypeDef = TypedDict(
    "ListObjectAttributesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
        "FacetFilter": NotRequired["SchemaFacetTypeDef"],
    },
)

ListObjectAttributesResponseTypeDef = TypedDict(
    "ListObjectAttributesResponseTypeDef",
    {
        "Attributes": List["AttributeKeyAndValueTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListObjectChildrenRequestRequestTypeDef = TypedDict(
    "ListObjectChildrenRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)

ListObjectChildrenResponseTypeDef = TypedDict(
    "ListObjectChildrenResponseTypeDef",
    {
        "Children": Dict[str, str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListObjectParentPathsRequestRequestTypeDef = TypedDict(
    "ListObjectParentPathsRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListObjectParentPathsResponseTypeDef = TypedDict(
    "ListObjectParentPathsResponseTypeDef",
    {
        "PathToObjectIdentifiersList": List["PathToObjectIdentifiersTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListObjectParentsRequestRequestTypeDef = TypedDict(
    "ListObjectParentsRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
        "IncludeAllLinksToEachParent": NotRequired[bool],
    },
)

ListObjectParentsResponseTypeDef = TypedDict(
    "ListObjectParentsResponseTypeDef",
    {
        "Parents": Dict[str, str],
        "NextToken": str,
        "ParentLinks": List["ObjectIdentifierAndLinkNameTupleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListObjectPoliciesRequestRequestTypeDef = TypedDict(
    "ListObjectPoliciesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)

ListObjectPoliciesResponseTypeDef = TypedDict(
    "ListObjectPoliciesResponseTypeDef",
    {
        "AttachedPolicyIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOutgoingTypedLinksRequestRequestTypeDef = TypedDict(
    "ListOutgoingTypedLinksRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
        "FilterAttributeRanges": NotRequired[Sequence["TypedLinkAttributeRangeTypeDef"]],
        "FilterTypedLink": NotRequired["TypedLinkSchemaAndFacetNameTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)

ListOutgoingTypedLinksResponseTypeDef = TypedDict(
    "ListOutgoingTypedLinksResponseTypeDef",
    {
        "TypedLinkSpecifiers": List["TypedLinkSpecifierTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPolicyAttachmentsRequestRequestTypeDef = TypedDict(
    "ListPolicyAttachmentsRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "PolicyReference": "ObjectReferenceTypeDef",
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)

ListPolicyAttachmentsResponseTypeDef = TypedDict(
    "ListPolicyAttachmentsResponseTypeDef",
    {
        "ObjectIdentifiers": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPublishedSchemaArnsRequestRequestTypeDef = TypedDict(
    "ListPublishedSchemaArnsRequestRequestTypeDef",
    {
        "SchemaArn": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListPublishedSchemaArnsResponseTypeDef = TypedDict(
    "ListPublishedSchemaArnsResponseTypeDef",
    {
        "SchemaArns": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTypedLinkFacetAttributesRequestRequestTypeDef = TypedDict(
    "ListTypedLinkFacetAttributesRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListTypedLinkFacetAttributesResponseTypeDef = TypedDict(
    "ListTypedLinkFacetAttributesResponseTypeDef",
    {
        "Attributes": List["TypedLinkAttributeDefinitionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTypedLinkFacetNamesRequestRequestTypeDef = TypedDict(
    "ListTypedLinkFacetNamesRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListTypedLinkFacetNamesResponseTypeDef = TypedDict(
    "ListTypedLinkFacetNamesResponseTypeDef",
    {
        "FacetNames": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LookupPolicyRequestRequestTypeDef = TypedDict(
    "LookupPolicyRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

LookupPolicyResponseTypeDef = TypedDict(
    "LookupPolicyResponseTypeDef",
    {
        "PolicyToPathList": List["PolicyToPathTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ObjectAttributeActionTypeDef = TypedDict(
    "ObjectAttributeActionTypeDef",
    {
        "ObjectAttributeActionType": NotRequired[UpdateActionTypeType],
        "ObjectAttributeUpdateValue": NotRequired["TypedAttributeValueTypeDef"],
    },
)

ObjectAttributeRangeTypeDef = TypedDict(
    "ObjectAttributeRangeTypeDef",
    {
        "AttributeKey": NotRequired["AttributeKeyTypeDef"],
        "Range": NotRequired["TypedAttributeValueRangeTypeDef"],
    },
)

ObjectAttributeUpdateTypeDef = TypedDict(
    "ObjectAttributeUpdateTypeDef",
    {
        "ObjectAttributeKey": NotRequired["AttributeKeyTypeDef"],
        "ObjectAttributeAction": NotRequired["ObjectAttributeActionTypeDef"],
    },
)

ObjectIdentifierAndLinkNameTupleTypeDef = TypedDict(
    "ObjectIdentifierAndLinkNameTupleTypeDef",
    {
        "ObjectIdentifier": NotRequired[str],
        "LinkName": NotRequired[str],
    },
)

ObjectReferenceTypeDef = TypedDict(
    "ObjectReferenceTypeDef",
    {
        "Selector": NotRequired[str],
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

PathToObjectIdentifiersTypeDef = TypedDict(
    "PathToObjectIdentifiersTypeDef",
    {
        "Path": NotRequired[str],
        "ObjectIdentifiers": NotRequired[List[str]],
    },
)

PolicyAttachmentTypeDef = TypedDict(
    "PolicyAttachmentTypeDef",
    {
        "PolicyId": NotRequired[str],
        "ObjectIdentifier": NotRequired[str],
        "PolicyType": NotRequired[str],
    },
)

PolicyToPathTypeDef = TypedDict(
    "PolicyToPathTypeDef",
    {
        "Path": NotRequired[str],
        "Policies": NotRequired[List["PolicyAttachmentTypeDef"]],
    },
)

PublishSchemaRequestRequestTypeDef = TypedDict(
    "PublishSchemaRequestRequestTypeDef",
    {
        "DevelopmentSchemaArn": str,
        "Version": str,
        "MinorVersion": NotRequired[str],
        "Name": NotRequired[str],
    },
)

PublishSchemaResponseTypeDef = TypedDict(
    "PublishSchemaResponseTypeDef",
    {
        "PublishedSchemaArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutSchemaFromJsonRequestRequestTypeDef = TypedDict(
    "PutSchemaFromJsonRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Document": str,
    },
)

PutSchemaFromJsonResponseTypeDef = TypedDict(
    "PutSchemaFromJsonResponseTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveFacetFromObjectRequestRequestTypeDef = TypedDict(
    "RemoveFacetFromObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "SchemaFacet": "SchemaFacetTypeDef",
        "ObjectReference": "ObjectReferenceTypeDef",
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

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "Type": NotRequired[RuleTypeType],
        "Parameters": NotRequired[Mapping[str, str]],
    },
)

SchemaFacetTypeDef = TypedDict(
    "SchemaFacetTypeDef",
    {
        "SchemaArn": NotRequired[str],
        "FacetName": NotRequired[str],
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
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

TypedAttributeValueRangeTypeDef = TypedDict(
    "TypedAttributeValueRangeTypeDef",
    {
        "StartMode": RangeModeType,
        "EndMode": RangeModeType,
        "StartValue": NotRequired["TypedAttributeValueTypeDef"],
        "EndValue": NotRequired["TypedAttributeValueTypeDef"],
    },
)

TypedAttributeValueTypeDef = TypedDict(
    "TypedAttributeValueTypeDef",
    {
        "StringValue": NotRequired[str],
        "BinaryValue": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "BooleanValue": NotRequired[bool],
        "NumberValue": NotRequired[str],
        "DatetimeValue": NotRequired[Union[datetime, str]],
    },
)

TypedLinkAttributeDefinitionTypeDef = TypedDict(
    "TypedLinkAttributeDefinitionTypeDef",
    {
        "Name": str,
        "Type": FacetAttributeTypeType,
        "RequiredBehavior": RequiredAttributeBehaviorType,
        "DefaultValue": NotRequired["TypedAttributeValueTypeDef"],
        "IsImmutable": NotRequired[bool],
        "Rules": NotRequired[Mapping[str, "RuleTypeDef"]],
    },
)

TypedLinkAttributeRangeTypeDef = TypedDict(
    "TypedLinkAttributeRangeTypeDef",
    {
        "Range": "TypedAttributeValueRangeTypeDef",
        "AttributeName": NotRequired[str],
    },
)

TypedLinkFacetAttributeUpdateTypeDef = TypedDict(
    "TypedLinkFacetAttributeUpdateTypeDef",
    {
        "Attribute": "TypedLinkAttributeDefinitionTypeDef",
        "Action": UpdateActionTypeType,
    },
)

TypedLinkFacetTypeDef = TypedDict(
    "TypedLinkFacetTypeDef",
    {
        "Name": str,
        "Attributes": Sequence["TypedLinkAttributeDefinitionTypeDef"],
        "IdentityAttributeOrder": Sequence[str],
    },
)

TypedLinkSchemaAndFacetNameTypeDef = TypedDict(
    "TypedLinkSchemaAndFacetNameTypeDef",
    {
        "SchemaArn": str,
        "TypedLinkName": str,
    },
)

TypedLinkSpecifierTypeDef = TypedDict(
    "TypedLinkSpecifierTypeDef",
    {
        "TypedLinkFacet": "TypedLinkSchemaAndFacetNameTypeDef",
        "SourceObjectReference": "ObjectReferenceTypeDef",
        "TargetObjectReference": "ObjectReferenceTypeDef",
        "IdentityAttributeValues": List["AttributeNameAndValueTypeDef"],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateFacetRequestRequestTypeDef = TypedDict(
    "UpdateFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
        "AttributeUpdates": NotRequired[Sequence["FacetAttributeUpdateTypeDef"]],
        "ObjectType": NotRequired[ObjectTypeType],
    },
)

UpdateLinkAttributesRequestRequestTypeDef = TypedDict(
    "UpdateLinkAttributesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "TypedLinkSpecifier": "TypedLinkSpecifierTypeDef",
        "AttributeUpdates": Sequence["LinkAttributeUpdateTypeDef"],
    },
)

UpdateObjectAttributesRequestRequestTypeDef = TypedDict(
    "UpdateObjectAttributesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
        "AttributeUpdates": Sequence["ObjectAttributeUpdateTypeDef"],
    },
)

UpdateObjectAttributesResponseTypeDef = TypedDict(
    "UpdateObjectAttributesResponseTypeDef",
    {
        "ObjectIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSchemaRequestRequestTypeDef = TypedDict(
    "UpdateSchemaRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)

UpdateSchemaResponseTypeDef = TypedDict(
    "UpdateSchemaResponseTypeDef",
    {
        "SchemaArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTypedLinkFacetRequestRequestTypeDef = TypedDict(
    "UpdateTypedLinkFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
        "AttributeUpdates": Sequence["TypedLinkFacetAttributeUpdateTypeDef"],
        "IdentityAttributeOrder": Sequence[str],
    },
)

UpgradeAppliedSchemaRequestRequestTypeDef = TypedDict(
    "UpgradeAppliedSchemaRequestRequestTypeDef",
    {
        "PublishedSchemaArn": str,
        "DirectoryArn": str,
        "DryRun": NotRequired[bool],
    },
)

UpgradeAppliedSchemaResponseTypeDef = TypedDict(
    "UpgradeAppliedSchemaResponseTypeDef",
    {
        "UpgradedSchemaArn": str,
        "DirectoryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpgradePublishedSchemaRequestRequestTypeDef = TypedDict(
    "UpgradePublishedSchemaRequestRequestTypeDef",
    {
        "DevelopmentSchemaArn": str,
        "PublishedSchemaArn": str,
        "MinorVersion": str,
        "DryRun": NotRequired[bool],
    },
)

UpgradePublishedSchemaResponseTypeDef = TypedDict(
    "UpgradePublishedSchemaResponseTypeDef",
    {
        "UpgradedSchemaArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
