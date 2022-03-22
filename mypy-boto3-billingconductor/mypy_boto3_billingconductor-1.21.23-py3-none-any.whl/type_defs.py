"""
Type annotations for billingconductor service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/type_defs.html)

Usage::

    ```python
    from mypy_boto3_billingconductor.type_defs import AccountAssociationsListElementTypeDef

    data: AccountAssociationsListElementTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AssociateResourceErrorReasonType,
    BillingGroupStatusType,
    CurrencyCodeType,
    CustomLineItemRelationshipType,
    CustomLineItemTypeType,
    PricingRuleScopeType,
    PricingRuleTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountAssociationsListElementTypeDef",
    "AccountGroupingTypeDef",
    "AssociateAccountsInputRequestTypeDef",
    "AssociateAccountsOutputTypeDef",
    "AssociatePricingRulesInputRequestTypeDef",
    "AssociatePricingRulesOutputTypeDef",
    "AssociateResourceErrorTypeDef",
    "AssociateResourceResponseElementTypeDef",
    "BatchAssociateResourcesToCustomLineItemInputRequestTypeDef",
    "BatchAssociateResourcesToCustomLineItemOutputTypeDef",
    "BatchDisassociateResourcesFromCustomLineItemInputRequestTypeDef",
    "BatchDisassociateResourcesFromCustomLineItemOutputTypeDef",
    "BillingGroupCostReportElementTypeDef",
    "BillingGroupListElementTypeDef",
    "ComputationPreferenceTypeDef",
    "CreateBillingGroupInputRequestTypeDef",
    "CreateBillingGroupOutputTypeDef",
    "CreateCustomLineItemInputRequestTypeDef",
    "CreateCustomLineItemOutputTypeDef",
    "CreatePricingPlanInputRequestTypeDef",
    "CreatePricingPlanOutputTypeDef",
    "CreatePricingRuleInputRequestTypeDef",
    "CreatePricingRuleOutputTypeDef",
    "CustomLineItemBillingPeriodRangeTypeDef",
    "CustomLineItemChargeDetailsTypeDef",
    "CustomLineItemFlatChargeDetailsTypeDef",
    "CustomLineItemListElementTypeDef",
    "CustomLineItemPercentageChargeDetailsTypeDef",
    "DeleteBillingGroupInputRequestTypeDef",
    "DeleteBillingGroupOutputTypeDef",
    "DeleteCustomLineItemInputRequestTypeDef",
    "DeleteCustomLineItemOutputTypeDef",
    "DeletePricingPlanInputRequestTypeDef",
    "DeletePricingPlanOutputTypeDef",
    "DeletePricingRuleInputRequestTypeDef",
    "DeletePricingRuleOutputTypeDef",
    "DisassociateAccountsInputRequestTypeDef",
    "DisassociateAccountsOutputTypeDef",
    "DisassociatePricingRulesInputRequestTypeDef",
    "DisassociatePricingRulesOutputTypeDef",
    "DisassociateResourceResponseElementTypeDef",
    "ListAccountAssociationsFilterTypeDef",
    "ListAccountAssociationsInputRequestTypeDef",
    "ListAccountAssociationsOutputTypeDef",
    "ListBillingGroupCostReportsFilterTypeDef",
    "ListBillingGroupCostReportsInputRequestTypeDef",
    "ListBillingGroupCostReportsOutputTypeDef",
    "ListBillingGroupsFilterTypeDef",
    "ListBillingGroupsInputRequestTypeDef",
    "ListBillingGroupsOutputTypeDef",
    "ListCustomLineItemChargeDetailsTypeDef",
    "ListCustomLineItemFlatChargeDetailsTypeDef",
    "ListCustomLineItemPercentageChargeDetailsTypeDef",
    "ListCustomLineItemsFilterTypeDef",
    "ListCustomLineItemsInputRequestTypeDef",
    "ListCustomLineItemsOutputTypeDef",
    "ListPricingPlansAssociatedWithPricingRuleInputRequestTypeDef",
    "ListPricingPlansAssociatedWithPricingRuleOutputTypeDef",
    "ListPricingPlansFilterTypeDef",
    "ListPricingPlansInputRequestTypeDef",
    "ListPricingPlansOutputTypeDef",
    "ListPricingRulesAssociatedToPricingPlanInputRequestTypeDef",
    "ListPricingRulesAssociatedToPricingPlanOutputTypeDef",
    "ListPricingRulesFilterTypeDef",
    "ListPricingRulesInputRequestTypeDef",
    "ListPricingRulesOutputTypeDef",
    "ListResourcesAssociatedToCustomLineItemFilterTypeDef",
    "ListResourcesAssociatedToCustomLineItemInputRequestTypeDef",
    "ListResourcesAssociatedToCustomLineItemOutputTypeDef",
    "ListResourcesAssociatedToCustomLineItemResponseElementTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PricingPlanListElementTypeDef",
    "PricingRuleListElementTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateBillingGroupInputRequestTypeDef",
    "UpdateBillingGroupOutputTypeDef",
    "UpdateCustomLineItemChargeDetailsTypeDef",
    "UpdateCustomLineItemFlatChargeDetailsTypeDef",
    "UpdateCustomLineItemInputRequestTypeDef",
    "UpdateCustomLineItemOutputTypeDef",
    "UpdateCustomLineItemPercentageChargeDetailsTypeDef",
    "UpdatePricingPlanInputRequestTypeDef",
    "UpdatePricingPlanOutputTypeDef",
    "UpdatePricingRuleInputRequestTypeDef",
    "UpdatePricingRuleOutputTypeDef",
)

AccountAssociationsListElementTypeDef = TypedDict(
    "AccountAssociationsListElementTypeDef",
    {
        "AccountId": NotRequired[str],
        "BillingGroupArn": NotRequired[str],
        "AccountName": NotRequired[str],
        "AccountEmail": NotRequired[str],
    },
)

AccountGroupingTypeDef = TypedDict(
    "AccountGroupingTypeDef",
    {
        "LinkedAccountIds": Sequence[str],
    },
)

AssociateAccountsInputRequestTypeDef = TypedDict(
    "AssociateAccountsInputRequestTypeDef",
    {
        "Arn": str,
        "AccountIds": Sequence[str],
    },
)

AssociateAccountsOutputTypeDef = TypedDict(
    "AssociateAccountsOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociatePricingRulesInputRequestTypeDef = TypedDict(
    "AssociatePricingRulesInputRequestTypeDef",
    {
        "Arn": str,
        "PricingRuleArns": Sequence[str],
    },
)

AssociatePricingRulesOutputTypeDef = TypedDict(
    "AssociatePricingRulesOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateResourceErrorTypeDef = TypedDict(
    "AssociateResourceErrorTypeDef",
    {
        "Message": NotRequired[str],
        "Reason": NotRequired[AssociateResourceErrorReasonType],
    },
)

AssociateResourceResponseElementTypeDef = TypedDict(
    "AssociateResourceResponseElementTypeDef",
    {
        "Arn": NotRequired[str],
        "Error": NotRequired["AssociateResourceErrorTypeDef"],
    },
)

BatchAssociateResourcesToCustomLineItemInputRequestTypeDef = TypedDict(
    "BatchAssociateResourcesToCustomLineItemInputRequestTypeDef",
    {
        "TargetArn": str,
        "ResourceArns": Sequence[str],
        "BillingPeriodRange": NotRequired["CustomLineItemBillingPeriodRangeTypeDef"],
    },
)

BatchAssociateResourcesToCustomLineItemOutputTypeDef = TypedDict(
    "BatchAssociateResourcesToCustomLineItemOutputTypeDef",
    {
        "SuccessfullyAssociatedResources": List["AssociateResourceResponseElementTypeDef"],
        "FailedAssociatedResources": List["AssociateResourceResponseElementTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDisassociateResourcesFromCustomLineItemInputRequestTypeDef = TypedDict(
    "BatchDisassociateResourcesFromCustomLineItemInputRequestTypeDef",
    {
        "TargetArn": str,
        "ResourceArns": Sequence[str],
        "BillingPeriodRange": NotRequired["CustomLineItemBillingPeriodRangeTypeDef"],
    },
)

BatchDisassociateResourcesFromCustomLineItemOutputTypeDef = TypedDict(
    "BatchDisassociateResourcesFromCustomLineItemOutputTypeDef",
    {
        "SuccessfullyDisassociatedResources": List["DisassociateResourceResponseElementTypeDef"],
        "FailedDisassociatedResources": List["DisassociateResourceResponseElementTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BillingGroupCostReportElementTypeDef = TypedDict(
    "BillingGroupCostReportElementTypeDef",
    {
        "Arn": NotRequired[str],
        "AWSCost": NotRequired[str],
        "ProformaCost": NotRequired[str],
        "Margin": NotRequired[str],
        "MarginPercentage": NotRequired[str],
        "Currency": NotRequired[str],
    },
)

BillingGroupListElementTypeDef = TypedDict(
    "BillingGroupListElementTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "Description": NotRequired[str],
        "PrimaryAccountId": NotRequired[str],
        "ComputationPreference": NotRequired["ComputationPreferenceTypeDef"],
        "Size": NotRequired[int],
        "CreationTime": NotRequired[int],
        "LastModifiedTime": NotRequired[int],
        "Status": NotRequired[BillingGroupStatusType],
        "StatusReason": NotRequired[str],
    },
)

ComputationPreferenceTypeDef = TypedDict(
    "ComputationPreferenceTypeDef",
    {
        "PricingPlanArn": str,
    },
)

CreateBillingGroupInputRequestTypeDef = TypedDict(
    "CreateBillingGroupInputRequestTypeDef",
    {
        "Name": str,
        "AccountGrouping": "AccountGroupingTypeDef",
        "ComputationPreference": "ComputationPreferenceTypeDef",
        "ClientToken": NotRequired[str],
        "PrimaryAccountId": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateBillingGroupOutputTypeDef = TypedDict(
    "CreateBillingGroupOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCustomLineItemInputRequestTypeDef = TypedDict(
    "CreateCustomLineItemInputRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "BillingGroupArn": str,
        "ChargeDetails": "CustomLineItemChargeDetailsTypeDef",
        "ClientToken": NotRequired[str],
        "BillingPeriodRange": NotRequired["CustomLineItemBillingPeriodRangeTypeDef"],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateCustomLineItemOutputTypeDef = TypedDict(
    "CreateCustomLineItemOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePricingPlanInputRequestTypeDef = TypedDict(
    "CreatePricingPlanInputRequestTypeDef",
    {
        "Name": str,
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "PricingRuleArns": NotRequired[Sequence[str]],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreatePricingPlanOutputTypeDef = TypedDict(
    "CreatePricingPlanOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePricingRuleInputRequestTypeDef = TypedDict(
    "CreatePricingRuleInputRequestTypeDef",
    {
        "Name": str,
        "Scope": PricingRuleScopeType,
        "Type": PricingRuleTypeType,
        "ModifierPercentage": float,
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "Service": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreatePricingRuleOutputTypeDef = TypedDict(
    "CreatePricingRuleOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomLineItemBillingPeriodRangeTypeDef = TypedDict(
    "CustomLineItemBillingPeriodRangeTypeDef",
    {
        "InclusiveStartBillingPeriod": str,
        "ExclusiveEndBillingPeriod": str,
    },
)

CustomLineItemChargeDetailsTypeDef = TypedDict(
    "CustomLineItemChargeDetailsTypeDef",
    {
        "Type": CustomLineItemTypeType,
        "Flat": NotRequired["CustomLineItemFlatChargeDetailsTypeDef"],
        "Percentage": NotRequired["CustomLineItemPercentageChargeDetailsTypeDef"],
    },
)

CustomLineItemFlatChargeDetailsTypeDef = TypedDict(
    "CustomLineItemFlatChargeDetailsTypeDef",
    {
        "ChargeValue": float,
    },
)

CustomLineItemListElementTypeDef = TypedDict(
    "CustomLineItemListElementTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "ChargeDetails": NotRequired["ListCustomLineItemChargeDetailsTypeDef"],
        "CurrencyCode": NotRequired[CurrencyCodeType],
        "Description": NotRequired[str],
        "ProductCode": NotRequired[str],
        "BillingGroupArn": NotRequired[str],
        "CreationTime": NotRequired[int],
        "LastModifiedTime": NotRequired[int],
        "AssociationSize": NotRequired[int],
    },
)

CustomLineItemPercentageChargeDetailsTypeDef = TypedDict(
    "CustomLineItemPercentageChargeDetailsTypeDef",
    {
        "PercentageValue": float,
        "AssociatedValues": NotRequired[Sequence[str]],
    },
)

DeleteBillingGroupInputRequestTypeDef = TypedDict(
    "DeleteBillingGroupInputRequestTypeDef",
    {
        "Arn": str,
    },
)

DeleteBillingGroupOutputTypeDef = TypedDict(
    "DeleteBillingGroupOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCustomLineItemInputRequestTypeDef = TypedDict(
    "DeleteCustomLineItemInputRequestTypeDef",
    {
        "Arn": str,
        "BillingPeriodRange": NotRequired["CustomLineItemBillingPeriodRangeTypeDef"],
    },
)

DeleteCustomLineItemOutputTypeDef = TypedDict(
    "DeleteCustomLineItemOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePricingPlanInputRequestTypeDef = TypedDict(
    "DeletePricingPlanInputRequestTypeDef",
    {
        "Arn": str,
    },
)

DeletePricingPlanOutputTypeDef = TypedDict(
    "DeletePricingPlanOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePricingRuleInputRequestTypeDef = TypedDict(
    "DeletePricingRuleInputRequestTypeDef",
    {
        "Arn": str,
    },
)

DeletePricingRuleOutputTypeDef = TypedDict(
    "DeletePricingRuleOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateAccountsInputRequestTypeDef = TypedDict(
    "DisassociateAccountsInputRequestTypeDef",
    {
        "Arn": str,
        "AccountIds": Sequence[str],
    },
)

DisassociateAccountsOutputTypeDef = TypedDict(
    "DisassociateAccountsOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociatePricingRulesInputRequestTypeDef = TypedDict(
    "DisassociatePricingRulesInputRequestTypeDef",
    {
        "Arn": str,
        "PricingRuleArns": Sequence[str],
    },
)

DisassociatePricingRulesOutputTypeDef = TypedDict(
    "DisassociatePricingRulesOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateResourceResponseElementTypeDef = TypedDict(
    "DisassociateResourceResponseElementTypeDef",
    {
        "Arn": NotRequired[str],
        "Error": NotRequired["AssociateResourceErrorTypeDef"],
    },
)

ListAccountAssociationsFilterTypeDef = TypedDict(
    "ListAccountAssociationsFilterTypeDef",
    {
        "Association": NotRequired[str],
        "AccountId": NotRequired[str],
    },
)

ListAccountAssociationsInputRequestTypeDef = TypedDict(
    "ListAccountAssociationsInputRequestTypeDef",
    {
        "BillingPeriod": NotRequired[str],
        "Filters": NotRequired["ListAccountAssociationsFilterTypeDef"],
        "NextToken": NotRequired[str],
    },
)

ListAccountAssociationsOutputTypeDef = TypedDict(
    "ListAccountAssociationsOutputTypeDef",
    {
        "LinkedAccounts": List["AccountAssociationsListElementTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBillingGroupCostReportsFilterTypeDef = TypedDict(
    "ListBillingGroupCostReportsFilterTypeDef",
    {
        "BillingGroupArns": NotRequired[Sequence[str]],
    },
)

ListBillingGroupCostReportsInputRequestTypeDef = TypedDict(
    "ListBillingGroupCostReportsInputRequestTypeDef",
    {
        "BillingPeriod": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired["ListBillingGroupCostReportsFilterTypeDef"],
    },
)

ListBillingGroupCostReportsOutputTypeDef = TypedDict(
    "ListBillingGroupCostReportsOutputTypeDef",
    {
        "BillingGroupCostReports": List["BillingGroupCostReportElementTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBillingGroupsFilterTypeDef = TypedDict(
    "ListBillingGroupsFilterTypeDef",
    {
        "Arns": NotRequired[Sequence[str]],
        "PricingPlan": NotRequired[str],
    },
)

ListBillingGroupsInputRequestTypeDef = TypedDict(
    "ListBillingGroupsInputRequestTypeDef",
    {
        "BillingPeriod": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired["ListBillingGroupsFilterTypeDef"],
    },
)

ListBillingGroupsOutputTypeDef = TypedDict(
    "ListBillingGroupsOutputTypeDef",
    {
        "BillingGroups": List["BillingGroupListElementTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCustomLineItemChargeDetailsTypeDef = TypedDict(
    "ListCustomLineItemChargeDetailsTypeDef",
    {
        "Type": CustomLineItemTypeType,
        "Flat": NotRequired["ListCustomLineItemFlatChargeDetailsTypeDef"],
        "Percentage": NotRequired["ListCustomLineItemPercentageChargeDetailsTypeDef"],
    },
)

ListCustomLineItemFlatChargeDetailsTypeDef = TypedDict(
    "ListCustomLineItemFlatChargeDetailsTypeDef",
    {
        "ChargeValue": float,
    },
)

ListCustomLineItemPercentageChargeDetailsTypeDef = TypedDict(
    "ListCustomLineItemPercentageChargeDetailsTypeDef",
    {
        "PercentageValue": float,
    },
)

ListCustomLineItemsFilterTypeDef = TypedDict(
    "ListCustomLineItemsFilterTypeDef",
    {
        "Names": NotRequired[Sequence[str]],
        "BillingGroups": NotRequired[Sequence[str]],
        "Arns": NotRequired[Sequence[str]],
    },
)

ListCustomLineItemsInputRequestTypeDef = TypedDict(
    "ListCustomLineItemsInputRequestTypeDef",
    {
        "BillingPeriod": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired["ListCustomLineItemsFilterTypeDef"],
    },
)

ListCustomLineItemsOutputTypeDef = TypedDict(
    "ListCustomLineItemsOutputTypeDef",
    {
        "CustomLineItems": List["CustomLineItemListElementTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPricingPlansAssociatedWithPricingRuleInputRequestTypeDef = TypedDict(
    "ListPricingPlansAssociatedWithPricingRuleInputRequestTypeDef",
    {
        "PricingRuleArn": str,
        "BillingPeriod": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListPricingPlansAssociatedWithPricingRuleOutputTypeDef = TypedDict(
    "ListPricingPlansAssociatedWithPricingRuleOutputTypeDef",
    {
        "BillingPeriod": str,
        "PricingRuleArn": str,
        "PricingPlanArns": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPricingPlansFilterTypeDef = TypedDict(
    "ListPricingPlansFilterTypeDef",
    {
        "Arns": NotRequired[Sequence[str]],
    },
)

ListPricingPlansInputRequestTypeDef = TypedDict(
    "ListPricingPlansInputRequestTypeDef",
    {
        "BillingPeriod": NotRequired[str],
        "Filters": NotRequired["ListPricingPlansFilterTypeDef"],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListPricingPlansOutputTypeDef = TypedDict(
    "ListPricingPlansOutputTypeDef",
    {
        "BillingPeriod": str,
        "PricingPlans": List["PricingPlanListElementTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPricingRulesAssociatedToPricingPlanInputRequestTypeDef = TypedDict(
    "ListPricingRulesAssociatedToPricingPlanInputRequestTypeDef",
    {
        "PricingPlanArn": str,
        "BillingPeriod": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListPricingRulesAssociatedToPricingPlanOutputTypeDef = TypedDict(
    "ListPricingRulesAssociatedToPricingPlanOutputTypeDef",
    {
        "BillingPeriod": str,
        "PricingPlanArn": str,
        "PricingRuleArns": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPricingRulesFilterTypeDef = TypedDict(
    "ListPricingRulesFilterTypeDef",
    {
        "Arns": NotRequired[Sequence[str]],
    },
)

ListPricingRulesInputRequestTypeDef = TypedDict(
    "ListPricingRulesInputRequestTypeDef",
    {
        "BillingPeriod": NotRequired[str],
        "Filters": NotRequired["ListPricingRulesFilterTypeDef"],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListPricingRulesOutputTypeDef = TypedDict(
    "ListPricingRulesOutputTypeDef",
    {
        "BillingPeriod": str,
        "PricingRules": List["PricingRuleListElementTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourcesAssociatedToCustomLineItemFilterTypeDef = TypedDict(
    "ListResourcesAssociatedToCustomLineItemFilterTypeDef",
    {
        "Relationship": NotRequired[CustomLineItemRelationshipType],
    },
)

ListResourcesAssociatedToCustomLineItemInputRequestTypeDef = TypedDict(
    "ListResourcesAssociatedToCustomLineItemInputRequestTypeDef",
    {
        "Arn": str,
        "BillingPeriod": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired["ListResourcesAssociatedToCustomLineItemFilterTypeDef"],
    },
)

ListResourcesAssociatedToCustomLineItemOutputTypeDef = TypedDict(
    "ListResourcesAssociatedToCustomLineItemOutputTypeDef",
    {
        "Arn": str,
        "AssociatedResources": List[
            "ListResourcesAssociatedToCustomLineItemResponseElementTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourcesAssociatedToCustomLineItemResponseElementTypeDef = TypedDict(
    "ListResourcesAssociatedToCustomLineItemResponseElementTypeDef",
    {
        "Arn": NotRequired[str],
        "Relationship": NotRequired[CustomLineItemRelationshipType],
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
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

PricingPlanListElementTypeDef = TypedDict(
    "PricingPlanListElementTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "Description": NotRequired[str],
        "Size": NotRequired[int],
        "CreationTime": NotRequired[int],
        "LastModifiedTime": NotRequired[int],
    },
)

PricingRuleListElementTypeDef = TypedDict(
    "PricingRuleListElementTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "Description": NotRequired[str],
        "Scope": NotRequired[PricingRuleScopeType],
        "Type": NotRequired[PricingRuleTypeType],
        "ModifierPercentage": NotRequired[float],
        "Service": NotRequired[str],
        "AssociatedPricingPlanCount": NotRequired[int],
        "CreationTime": NotRequired[int],
        "LastModifiedTime": NotRequired[int],
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

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateBillingGroupInputRequestTypeDef = TypedDict(
    "UpdateBillingGroupInputRequestTypeDef",
    {
        "Arn": str,
        "Name": NotRequired[str],
        "Status": NotRequired[BillingGroupStatusType],
        "ComputationPreference": NotRequired["ComputationPreferenceTypeDef"],
        "Description": NotRequired[str],
    },
)

UpdateBillingGroupOutputTypeDef = TypedDict(
    "UpdateBillingGroupOutputTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "PrimaryAccountId": str,
        "PricingPlanArn": str,
        "Size": int,
        "LastModifiedTime": int,
        "Status": BillingGroupStatusType,
        "StatusReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCustomLineItemChargeDetailsTypeDef = TypedDict(
    "UpdateCustomLineItemChargeDetailsTypeDef",
    {
        "Flat": NotRequired["UpdateCustomLineItemFlatChargeDetailsTypeDef"],
        "Percentage": NotRequired["UpdateCustomLineItemPercentageChargeDetailsTypeDef"],
    },
)

UpdateCustomLineItemFlatChargeDetailsTypeDef = TypedDict(
    "UpdateCustomLineItemFlatChargeDetailsTypeDef",
    {
        "ChargeValue": float,
    },
)

UpdateCustomLineItemInputRequestTypeDef = TypedDict(
    "UpdateCustomLineItemInputRequestTypeDef",
    {
        "Arn": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "ChargeDetails": NotRequired["UpdateCustomLineItemChargeDetailsTypeDef"],
        "BillingPeriodRange": NotRequired["CustomLineItemBillingPeriodRangeTypeDef"],
    },
)

UpdateCustomLineItemOutputTypeDef = TypedDict(
    "UpdateCustomLineItemOutputTypeDef",
    {
        "Arn": str,
        "BillingGroupArn": str,
        "Name": str,
        "Description": str,
        "ChargeDetails": "ListCustomLineItemChargeDetailsTypeDef",
        "LastModifiedTime": int,
        "AssociationSize": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCustomLineItemPercentageChargeDetailsTypeDef = TypedDict(
    "UpdateCustomLineItemPercentageChargeDetailsTypeDef",
    {
        "PercentageValue": float,
    },
)

UpdatePricingPlanInputRequestTypeDef = TypedDict(
    "UpdatePricingPlanInputRequestTypeDef",
    {
        "Arn": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)

UpdatePricingPlanOutputTypeDef = TypedDict(
    "UpdatePricingPlanOutputTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "Size": int,
        "LastModifiedTime": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePricingRuleInputRequestTypeDef = TypedDict(
    "UpdatePricingRuleInputRequestTypeDef",
    {
        "Arn": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Type": NotRequired[PricingRuleTypeType],
        "ModifierPercentage": NotRequired[float],
    },
)

UpdatePricingRuleOutputTypeDef = TypedDict(
    "UpdatePricingRuleOutputTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "Scope": PricingRuleScopeType,
        "Type": PricingRuleTypeType,
        "ModifierPercentage": float,
        "Service": str,
        "AssociatedPricingPlanCount": int,
        "LastModifiedTime": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
