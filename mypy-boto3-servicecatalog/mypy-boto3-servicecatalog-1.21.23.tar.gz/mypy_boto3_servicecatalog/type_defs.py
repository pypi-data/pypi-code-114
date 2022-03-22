"""
Type annotations for servicecatalog service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/type_defs.html)

Usage::

    ```python
    from mypy_boto3_servicecatalog.type_defs import AcceptPortfolioShareInputRequestTypeDef

    data: AcceptPortfolioShareInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AccessLevelFilterKeyType,
    AccessStatusType,
    ChangeActionType,
    CopyProductStatusType,
    DescribePortfolioShareTypeType,
    EvaluationTypeType,
    OrganizationNodeTypeType,
    PortfolioShareTypeType,
    ProductTypeType,
    ProductViewFilterByType,
    ProductViewSortByType,
    PropertyKeyType,
    ProvisionedProductPlanStatusType,
    ProvisionedProductStatusType,
    ProvisioningArtifactGuidanceType,
    ProvisioningArtifactTypeType,
    RecordStatusType,
    ReplacementType,
    RequiresRecreationType,
    ResourceAttributeType,
    ServiceActionAssociationErrorCodeType,
    ServiceActionDefinitionKeyType,
    ShareStatusType,
    SortOrderType,
    StackInstanceStatusType,
    StackSetOperationTypeType,
    StatusType,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcceptPortfolioShareInputRequestTypeDef",
    "AccessLevelFilterTypeDef",
    "AssociateBudgetWithResourceInputRequestTypeDef",
    "AssociatePrincipalWithPortfolioInputRequestTypeDef",
    "AssociateProductWithPortfolioInputRequestTypeDef",
    "AssociateServiceActionWithProvisioningArtifactInputRequestTypeDef",
    "AssociateTagOptionWithResourceInputRequestTypeDef",
    "BatchAssociateServiceActionWithProvisioningArtifactInputRequestTypeDef",
    "BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef",
    "BatchDisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef",
    "BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef",
    "BudgetDetailTypeDef",
    "CloudWatchDashboardTypeDef",
    "ConstraintDetailTypeDef",
    "ConstraintSummaryTypeDef",
    "CopyProductInputRequestTypeDef",
    "CopyProductOutputTypeDef",
    "CreateConstraintInputRequestTypeDef",
    "CreateConstraintOutputTypeDef",
    "CreatePortfolioInputRequestTypeDef",
    "CreatePortfolioOutputTypeDef",
    "CreatePortfolioShareInputRequestTypeDef",
    "CreatePortfolioShareOutputTypeDef",
    "CreateProductInputRequestTypeDef",
    "CreateProductOutputTypeDef",
    "CreateProvisionedProductPlanInputRequestTypeDef",
    "CreateProvisionedProductPlanOutputTypeDef",
    "CreateProvisioningArtifactInputRequestTypeDef",
    "CreateProvisioningArtifactOutputTypeDef",
    "CreateServiceActionInputRequestTypeDef",
    "CreateServiceActionOutputTypeDef",
    "CreateTagOptionInputRequestTypeDef",
    "CreateTagOptionOutputTypeDef",
    "DeleteConstraintInputRequestTypeDef",
    "DeletePortfolioInputRequestTypeDef",
    "DeletePortfolioShareInputRequestTypeDef",
    "DeletePortfolioShareOutputTypeDef",
    "DeleteProductInputRequestTypeDef",
    "DeleteProvisionedProductPlanInputRequestTypeDef",
    "DeleteProvisioningArtifactInputRequestTypeDef",
    "DeleteServiceActionInputRequestTypeDef",
    "DeleteTagOptionInputRequestTypeDef",
    "DescribeConstraintInputRequestTypeDef",
    "DescribeConstraintOutputTypeDef",
    "DescribeCopyProductStatusInputRequestTypeDef",
    "DescribeCopyProductStatusOutputTypeDef",
    "DescribePortfolioInputRequestTypeDef",
    "DescribePortfolioOutputTypeDef",
    "DescribePortfolioShareStatusInputRequestTypeDef",
    "DescribePortfolioShareStatusOutputTypeDef",
    "DescribePortfolioSharesInputRequestTypeDef",
    "DescribePortfolioSharesOutputTypeDef",
    "DescribeProductAsAdminInputRequestTypeDef",
    "DescribeProductAsAdminOutputTypeDef",
    "DescribeProductInputRequestTypeDef",
    "DescribeProductOutputTypeDef",
    "DescribeProductViewInputRequestTypeDef",
    "DescribeProductViewOutputTypeDef",
    "DescribeProvisionedProductInputRequestTypeDef",
    "DescribeProvisionedProductOutputTypeDef",
    "DescribeProvisionedProductPlanInputRequestTypeDef",
    "DescribeProvisionedProductPlanOutputTypeDef",
    "DescribeProvisioningArtifactInputRequestTypeDef",
    "DescribeProvisioningArtifactOutputTypeDef",
    "DescribeProvisioningParametersInputRequestTypeDef",
    "DescribeProvisioningParametersOutputTypeDef",
    "DescribeRecordInputRequestTypeDef",
    "DescribeRecordOutputTypeDef",
    "DescribeServiceActionExecutionParametersInputRequestTypeDef",
    "DescribeServiceActionExecutionParametersOutputTypeDef",
    "DescribeServiceActionInputRequestTypeDef",
    "DescribeServiceActionOutputTypeDef",
    "DescribeTagOptionInputRequestTypeDef",
    "DescribeTagOptionOutputTypeDef",
    "DisassociateBudgetFromResourceInputRequestTypeDef",
    "DisassociatePrincipalFromPortfolioInputRequestTypeDef",
    "DisassociateProductFromPortfolioInputRequestTypeDef",
    "DisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef",
    "DisassociateTagOptionFromResourceInputRequestTypeDef",
    "ExecuteProvisionedProductPlanInputRequestTypeDef",
    "ExecuteProvisionedProductPlanOutputTypeDef",
    "ExecuteProvisionedProductServiceActionInputRequestTypeDef",
    "ExecuteProvisionedProductServiceActionOutputTypeDef",
    "ExecutionParameterTypeDef",
    "FailedServiceActionAssociationTypeDef",
    "GetAWSOrganizationsAccessStatusOutputTypeDef",
    "GetProvisionedProductOutputsInputRequestTypeDef",
    "GetProvisionedProductOutputsOutputTypeDef",
    "ImportAsProvisionedProductInputRequestTypeDef",
    "ImportAsProvisionedProductOutputTypeDef",
    "LaunchPathSummaryTypeDef",
    "LaunchPathTypeDef",
    "ListAcceptedPortfolioSharesInputRequestTypeDef",
    "ListAcceptedPortfolioSharesOutputTypeDef",
    "ListBudgetsForResourceInputRequestTypeDef",
    "ListBudgetsForResourceOutputTypeDef",
    "ListConstraintsForPortfolioInputRequestTypeDef",
    "ListConstraintsForPortfolioOutputTypeDef",
    "ListLaunchPathsInputRequestTypeDef",
    "ListLaunchPathsOutputTypeDef",
    "ListOrganizationPortfolioAccessInputRequestTypeDef",
    "ListOrganizationPortfolioAccessOutputTypeDef",
    "ListPortfolioAccessInputRequestTypeDef",
    "ListPortfolioAccessOutputTypeDef",
    "ListPortfoliosForProductInputRequestTypeDef",
    "ListPortfoliosForProductOutputTypeDef",
    "ListPortfoliosInputRequestTypeDef",
    "ListPortfoliosOutputTypeDef",
    "ListPrincipalsForPortfolioInputRequestTypeDef",
    "ListPrincipalsForPortfolioOutputTypeDef",
    "ListProvisionedProductPlansInputRequestTypeDef",
    "ListProvisionedProductPlansOutputTypeDef",
    "ListProvisioningArtifactsForServiceActionInputRequestTypeDef",
    "ListProvisioningArtifactsForServiceActionOutputTypeDef",
    "ListProvisioningArtifactsInputRequestTypeDef",
    "ListProvisioningArtifactsOutputTypeDef",
    "ListRecordHistoryInputRequestTypeDef",
    "ListRecordHistoryOutputTypeDef",
    "ListRecordHistorySearchFilterTypeDef",
    "ListResourcesForTagOptionInputRequestTypeDef",
    "ListResourcesForTagOptionOutputTypeDef",
    "ListServiceActionsForProvisioningArtifactInputRequestTypeDef",
    "ListServiceActionsForProvisioningArtifactOutputTypeDef",
    "ListServiceActionsInputRequestTypeDef",
    "ListServiceActionsOutputTypeDef",
    "ListStackInstancesForProvisionedProductInputRequestTypeDef",
    "ListStackInstancesForProvisionedProductOutputTypeDef",
    "ListTagOptionsFiltersTypeDef",
    "ListTagOptionsInputRequestTypeDef",
    "ListTagOptionsOutputTypeDef",
    "OrganizationNodeTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterConstraintsTypeDef",
    "PortfolioDetailTypeDef",
    "PortfolioShareDetailTypeDef",
    "PrincipalTypeDef",
    "ProductViewAggregationValueTypeDef",
    "ProductViewDetailTypeDef",
    "ProductViewSummaryTypeDef",
    "ProvisionProductInputRequestTypeDef",
    "ProvisionProductOutputTypeDef",
    "ProvisionedProductAttributeTypeDef",
    "ProvisionedProductDetailTypeDef",
    "ProvisionedProductPlanDetailsTypeDef",
    "ProvisionedProductPlanSummaryTypeDef",
    "ProvisioningArtifactDetailTypeDef",
    "ProvisioningArtifactOutputTypeDef",
    "ProvisioningArtifactParameterTypeDef",
    "ProvisioningArtifactPreferencesTypeDef",
    "ProvisioningArtifactPropertiesTypeDef",
    "ProvisioningArtifactSummaryTypeDef",
    "ProvisioningArtifactTypeDef",
    "ProvisioningArtifactViewTypeDef",
    "ProvisioningParameterTypeDef",
    "ProvisioningPreferencesTypeDef",
    "RecordDetailTypeDef",
    "RecordErrorTypeDef",
    "RecordOutputTypeDef",
    "RecordTagTypeDef",
    "RejectPortfolioShareInputRequestTypeDef",
    "ResourceChangeDetailTypeDef",
    "ResourceChangeTypeDef",
    "ResourceDetailTypeDef",
    "ResourceTargetDefinitionTypeDef",
    "ResponseMetadataTypeDef",
    "ScanProvisionedProductsInputRequestTypeDef",
    "ScanProvisionedProductsOutputTypeDef",
    "SearchProductsAsAdminInputRequestTypeDef",
    "SearchProductsAsAdminOutputTypeDef",
    "SearchProductsInputRequestTypeDef",
    "SearchProductsOutputTypeDef",
    "SearchProvisionedProductsInputRequestTypeDef",
    "SearchProvisionedProductsOutputTypeDef",
    "ServiceActionAssociationTypeDef",
    "ServiceActionDetailTypeDef",
    "ServiceActionSummaryTypeDef",
    "ShareDetailsTypeDef",
    "ShareErrorTypeDef",
    "StackInstanceTypeDef",
    "TagOptionDetailTypeDef",
    "TagOptionSummaryTypeDef",
    "TagTypeDef",
    "TerminateProvisionedProductInputRequestTypeDef",
    "TerminateProvisionedProductOutputTypeDef",
    "UpdateConstraintInputRequestTypeDef",
    "UpdateConstraintOutputTypeDef",
    "UpdatePortfolioInputRequestTypeDef",
    "UpdatePortfolioOutputTypeDef",
    "UpdatePortfolioShareInputRequestTypeDef",
    "UpdatePortfolioShareOutputTypeDef",
    "UpdateProductInputRequestTypeDef",
    "UpdateProductOutputTypeDef",
    "UpdateProvisionedProductInputRequestTypeDef",
    "UpdateProvisionedProductOutputTypeDef",
    "UpdateProvisionedProductPropertiesInputRequestTypeDef",
    "UpdateProvisionedProductPropertiesOutputTypeDef",
    "UpdateProvisioningArtifactInputRequestTypeDef",
    "UpdateProvisioningArtifactOutputTypeDef",
    "UpdateProvisioningParameterTypeDef",
    "UpdateProvisioningPreferencesTypeDef",
    "UpdateServiceActionInputRequestTypeDef",
    "UpdateServiceActionOutputTypeDef",
    "UpdateTagOptionInputRequestTypeDef",
    "UpdateTagOptionOutputTypeDef",
    "UsageInstructionTypeDef",
)

AcceptPortfolioShareInputRequestTypeDef = TypedDict(
    "AcceptPortfolioShareInputRequestTypeDef",
    {
        "PortfolioId": str,
        "AcceptLanguage": NotRequired[str],
        "PortfolioShareType": NotRequired[PortfolioShareTypeType],
    },
)

AccessLevelFilterTypeDef = TypedDict(
    "AccessLevelFilterTypeDef",
    {
        "Key": NotRequired[AccessLevelFilterKeyType],
        "Value": NotRequired[str],
    },
)

AssociateBudgetWithResourceInputRequestTypeDef = TypedDict(
    "AssociateBudgetWithResourceInputRequestTypeDef",
    {
        "BudgetName": str,
        "ResourceId": str,
    },
)

AssociatePrincipalWithPortfolioInputRequestTypeDef = TypedDict(
    "AssociatePrincipalWithPortfolioInputRequestTypeDef",
    {
        "PortfolioId": str,
        "PrincipalARN": str,
        "PrincipalType": Literal["IAM"],
        "AcceptLanguage": NotRequired[str],
    },
)

AssociateProductWithPortfolioInputRequestTypeDef = TypedDict(
    "AssociateProductWithPortfolioInputRequestTypeDef",
    {
        "ProductId": str,
        "PortfolioId": str,
        "AcceptLanguage": NotRequired[str],
        "SourcePortfolioId": NotRequired[str],
    },
)

AssociateServiceActionWithProvisioningArtifactInputRequestTypeDef = TypedDict(
    "AssociateServiceActionWithProvisioningArtifactInputRequestTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "ServiceActionId": str,
        "AcceptLanguage": NotRequired[str],
    },
)

AssociateTagOptionWithResourceInputRequestTypeDef = TypedDict(
    "AssociateTagOptionWithResourceInputRequestTypeDef",
    {
        "ResourceId": str,
        "TagOptionId": str,
    },
)

BatchAssociateServiceActionWithProvisioningArtifactInputRequestTypeDef = TypedDict(
    "BatchAssociateServiceActionWithProvisioningArtifactInputRequestTypeDef",
    {
        "ServiceActionAssociations": Sequence["ServiceActionAssociationTypeDef"],
        "AcceptLanguage": NotRequired[str],
    },
)

BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef = TypedDict(
    "BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef",
    {
        "FailedServiceActionAssociations": List["FailedServiceActionAssociationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef = TypedDict(
    "BatchDisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef",
    {
        "ServiceActionAssociations": Sequence["ServiceActionAssociationTypeDef"],
        "AcceptLanguage": NotRequired[str],
    },
)

BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef = TypedDict(
    "BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef",
    {
        "FailedServiceActionAssociations": List["FailedServiceActionAssociationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BudgetDetailTypeDef = TypedDict(
    "BudgetDetailTypeDef",
    {
        "BudgetName": NotRequired[str],
    },
)

CloudWatchDashboardTypeDef = TypedDict(
    "CloudWatchDashboardTypeDef",
    {
        "Name": NotRequired[str],
    },
)

ConstraintDetailTypeDef = TypedDict(
    "ConstraintDetailTypeDef",
    {
        "ConstraintId": NotRequired[str],
        "Type": NotRequired[str],
        "Description": NotRequired[str],
        "Owner": NotRequired[str],
        "ProductId": NotRequired[str],
        "PortfolioId": NotRequired[str],
    },
)

ConstraintSummaryTypeDef = TypedDict(
    "ConstraintSummaryTypeDef",
    {
        "Type": NotRequired[str],
        "Description": NotRequired[str],
    },
)

CopyProductInputRequestTypeDef = TypedDict(
    "CopyProductInputRequestTypeDef",
    {
        "SourceProductArn": str,
        "IdempotencyToken": str,
        "AcceptLanguage": NotRequired[str],
        "TargetProductId": NotRequired[str],
        "TargetProductName": NotRequired[str],
        "SourceProvisioningArtifactIdentifiers": NotRequired[Sequence[Mapping[Literal["Id"], str]]],
        "CopyOptions": NotRequired[Sequence[Literal["CopyTags"]]],
    },
)

CopyProductOutputTypeDef = TypedDict(
    "CopyProductOutputTypeDef",
    {
        "CopyProductToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateConstraintInputRequestTypeDef = TypedDict(
    "CreateConstraintInputRequestTypeDef",
    {
        "PortfolioId": str,
        "ProductId": str,
        "Parameters": str,
        "Type": str,
        "IdempotencyToken": str,
        "AcceptLanguage": NotRequired[str],
        "Description": NotRequired[str],
    },
)

CreateConstraintOutputTypeDef = TypedDict(
    "CreateConstraintOutputTypeDef",
    {
        "ConstraintDetail": "ConstraintDetailTypeDef",
        "ConstraintParameters": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePortfolioInputRequestTypeDef = TypedDict(
    "CreatePortfolioInputRequestTypeDef",
    {
        "DisplayName": str,
        "ProviderName": str,
        "IdempotencyToken": str,
        "AcceptLanguage": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreatePortfolioOutputTypeDef = TypedDict(
    "CreatePortfolioOutputTypeDef",
    {
        "PortfolioDetail": "PortfolioDetailTypeDef",
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePortfolioShareInputRequestTypeDef = TypedDict(
    "CreatePortfolioShareInputRequestTypeDef",
    {
        "PortfolioId": str,
        "AcceptLanguage": NotRequired[str],
        "AccountId": NotRequired[str],
        "OrganizationNode": NotRequired["OrganizationNodeTypeDef"],
        "ShareTagOptions": NotRequired[bool],
    },
)

CreatePortfolioShareOutputTypeDef = TypedDict(
    "CreatePortfolioShareOutputTypeDef",
    {
        "PortfolioShareToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProductInputRequestTypeDef = TypedDict(
    "CreateProductInputRequestTypeDef",
    {
        "Name": str,
        "Owner": str,
        "ProductType": ProductTypeType,
        "ProvisioningArtifactParameters": "ProvisioningArtifactPropertiesTypeDef",
        "IdempotencyToken": str,
        "AcceptLanguage": NotRequired[str],
        "Description": NotRequired[str],
        "Distributor": NotRequired[str],
        "SupportDescription": NotRequired[str],
        "SupportEmail": NotRequired[str],
        "SupportUrl": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateProductOutputTypeDef = TypedDict(
    "CreateProductOutputTypeDef",
    {
        "ProductViewDetail": "ProductViewDetailTypeDef",
        "ProvisioningArtifactDetail": "ProvisioningArtifactDetailTypeDef",
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProvisionedProductPlanInputRequestTypeDef = TypedDict(
    "CreateProvisionedProductPlanInputRequestTypeDef",
    {
        "PlanName": str,
        "PlanType": Literal["CLOUDFORMATION"],
        "ProductId": str,
        "ProvisionedProductName": str,
        "ProvisioningArtifactId": str,
        "IdempotencyToken": str,
        "AcceptLanguage": NotRequired[str],
        "NotificationArns": NotRequired[Sequence[str]],
        "PathId": NotRequired[str],
        "ProvisioningParameters": NotRequired[Sequence["UpdateProvisioningParameterTypeDef"]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateProvisionedProductPlanOutputTypeDef = TypedDict(
    "CreateProvisionedProductPlanOutputTypeDef",
    {
        "PlanName": str,
        "PlanId": str,
        "ProvisionProductId": str,
        "ProvisionedProductName": str,
        "ProvisioningArtifactId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProvisioningArtifactInputRequestTypeDef = TypedDict(
    "CreateProvisioningArtifactInputRequestTypeDef",
    {
        "ProductId": str,
        "Parameters": "ProvisioningArtifactPropertiesTypeDef",
        "IdempotencyToken": str,
        "AcceptLanguage": NotRequired[str],
    },
)

CreateProvisioningArtifactOutputTypeDef = TypedDict(
    "CreateProvisioningArtifactOutputTypeDef",
    {
        "ProvisioningArtifactDetail": "ProvisioningArtifactDetailTypeDef",
        "Info": Dict[str, str],
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateServiceActionInputRequestTypeDef = TypedDict(
    "CreateServiceActionInputRequestTypeDef",
    {
        "Name": str,
        "DefinitionType": Literal["SSM_AUTOMATION"],
        "Definition": Mapping[ServiceActionDefinitionKeyType, str],
        "IdempotencyToken": str,
        "Description": NotRequired[str],
        "AcceptLanguage": NotRequired[str],
    },
)

CreateServiceActionOutputTypeDef = TypedDict(
    "CreateServiceActionOutputTypeDef",
    {
        "ServiceActionDetail": "ServiceActionDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTagOptionInputRequestTypeDef = TypedDict(
    "CreateTagOptionInputRequestTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

CreateTagOptionOutputTypeDef = TypedDict(
    "CreateTagOptionOutputTypeDef",
    {
        "TagOptionDetail": "TagOptionDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConstraintInputRequestTypeDef = TypedDict(
    "DeleteConstraintInputRequestTypeDef",
    {
        "Id": str,
        "AcceptLanguage": NotRequired[str],
    },
)

DeletePortfolioInputRequestTypeDef = TypedDict(
    "DeletePortfolioInputRequestTypeDef",
    {
        "Id": str,
        "AcceptLanguage": NotRequired[str],
    },
)

DeletePortfolioShareInputRequestTypeDef = TypedDict(
    "DeletePortfolioShareInputRequestTypeDef",
    {
        "PortfolioId": str,
        "AcceptLanguage": NotRequired[str],
        "AccountId": NotRequired[str],
        "OrganizationNode": NotRequired["OrganizationNodeTypeDef"],
    },
)

DeletePortfolioShareOutputTypeDef = TypedDict(
    "DeletePortfolioShareOutputTypeDef",
    {
        "PortfolioShareToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProductInputRequestTypeDef = TypedDict(
    "DeleteProductInputRequestTypeDef",
    {
        "Id": str,
        "AcceptLanguage": NotRequired[str],
    },
)

DeleteProvisionedProductPlanInputRequestTypeDef = TypedDict(
    "DeleteProvisionedProductPlanInputRequestTypeDef",
    {
        "PlanId": str,
        "AcceptLanguage": NotRequired[str],
        "IgnoreErrors": NotRequired[bool],
    },
)

DeleteProvisioningArtifactInputRequestTypeDef = TypedDict(
    "DeleteProvisioningArtifactInputRequestTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "AcceptLanguage": NotRequired[str],
    },
)

DeleteServiceActionInputRequestTypeDef = TypedDict(
    "DeleteServiceActionInputRequestTypeDef",
    {
        "Id": str,
        "AcceptLanguage": NotRequired[str],
    },
)

DeleteTagOptionInputRequestTypeDef = TypedDict(
    "DeleteTagOptionInputRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeConstraintInputRequestTypeDef = TypedDict(
    "DescribeConstraintInputRequestTypeDef",
    {
        "Id": str,
        "AcceptLanguage": NotRequired[str],
    },
)

DescribeConstraintOutputTypeDef = TypedDict(
    "DescribeConstraintOutputTypeDef",
    {
        "ConstraintDetail": "ConstraintDetailTypeDef",
        "ConstraintParameters": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCopyProductStatusInputRequestTypeDef = TypedDict(
    "DescribeCopyProductStatusInputRequestTypeDef",
    {
        "CopyProductToken": str,
        "AcceptLanguage": NotRequired[str],
    },
)

DescribeCopyProductStatusOutputTypeDef = TypedDict(
    "DescribeCopyProductStatusOutputTypeDef",
    {
        "CopyProductStatus": CopyProductStatusType,
        "TargetProductId": str,
        "StatusDetail": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePortfolioInputRequestTypeDef = TypedDict(
    "DescribePortfolioInputRequestTypeDef",
    {
        "Id": str,
        "AcceptLanguage": NotRequired[str],
    },
)

DescribePortfolioOutputTypeDef = TypedDict(
    "DescribePortfolioOutputTypeDef",
    {
        "PortfolioDetail": "PortfolioDetailTypeDef",
        "Tags": List["TagTypeDef"],
        "TagOptions": List["TagOptionDetailTypeDef"],
        "Budgets": List["BudgetDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePortfolioShareStatusInputRequestTypeDef = TypedDict(
    "DescribePortfolioShareStatusInputRequestTypeDef",
    {
        "PortfolioShareToken": str,
    },
)

DescribePortfolioShareStatusOutputTypeDef = TypedDict(
    "DescribePortfolioShareStatusOutputTypeDef",
    {
        "PortfolioShareToken": str,
        "PortfolioId": str,
        "OrganizationNodeValue": str,
        "Status": ShareStatusType,
        "ShareDetails": "ShareDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePortfolioSharesInputRequestTypeDef = TypedDict(
    "DescribePortfolioSharesInputRequestTypeDef",
    {
        "PortfolioId": str,
        "Type": DescribePortfolioShareTypeType,
        "PageToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)

DescribePortfolioSharesOutputTypeDef = TypedDict(
    "DescribePortfolioSharesOutputTypeDef",
    {
        "NextPageToken": str,
        "PortfolioShareDetails": List["PortfolioShareDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProductAsAdminInputRequestTypeDef = TypedDict(
    "DescribeProductAsAdminInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "SourcePortfolioId": NotRequired[str],
    },
)

DescribeProductAsAdminOutputTypeDef = TypedDict(
    "DescribeProductAsAdminOutputTypeDef",
    {
        "ProductViewDetail": "ProductViewDetailTypeDef",
        "ProvisioningArtifactSummaries": List["ProvisioningArtifactSummaryTypeDef"],
        "Tags": List["TagTypeDef"],
        "TagOptions": List["TagOptionDetailTypeDef"],
        "Budgets": List["BudgetDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProductInputRequestTypeDef = TypedDict(
    "DescribeProductInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
    },
)

DescribeProductOutputTypeDef = TypedDict(
    "DescribeProductOutputTypeDef",
    {
        "ProductViewSummary": "ProductViewSummaryTypeDef",
        "ProvisioningArtifacts": List["ProvisioningArtifactTypeDef"],
        "Budgets": List["BudgetDetailTypeDef"],
        "LaunchPaths": List["LaunchPathTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProductViewInputRequestTypeDef = TypedDict(
    "DescribeProductViewInputRequestTypeDef",
    {
        "Id": str,
        "AcceptLanguage": NotRequired[str],
    },
)

DescribeProductViewOutputTypeDef = TypedDict(
    "DescribeProductViewOutputTypeDef",
    {
        "ProductViewSummary": "ProductViewSummaryTypeDef",
        "ProvisioningArtifacts": List["ProvisioningArtifactTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProvisionedProductInputRequestTypeDef = TypedDict(
    "DescribeProvisionedProductInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
    },
)

DescribeProvisionedProductOutputTypeDef = TypedDict(
    "DescribeProvisionedProductOutputTypeDef",
    {
        "ProvisionedProductDetail": "ProvisionedProductDetailTypeDef",
        "CloudWatchDashboards": List["CloudWatchDashboardTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProvisionedProductPlanInputRequestTypeDef = TypedDict(
    "DescribeProvisionedProductPlanInputRequestTypeDef",
    {
        "PlanId": str,
        "AcceptLanguage": NotRequired[str],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
    },
)

DescribeProvisionedProductPlanOutputTypeDef = TypedDict(
    "DescribeProvisionedProductPlanOutputTypeDef",
    {
        "ProvisionedProductPlanDetails": "ProvisionedProductPlanDetailsTypeDef",
        "ResourceChanges": List["ResourceChangeTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProvisioningArtifactInputRequestTypeDef = TypedDict(
    "DescribeProvisioningArtifactInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "ProvisioningArtifactId": NotRequired[str],
        "ProductId": NotRequired[str],
        "ProvisioningArtifactName": NotRequired[str],
        "ProductName": NotRequired[str],
        "Verbose": NotRequired[bool],
    },
)

DescribeProvisioningArtifactOutputTypeDef = TypedDict(
    "DescribeProvisioningArtifactOutputTypeDef",
    {
        "ProvisioningArtifactDetail": "ProvisioningArtifactDetailTypeDef",
        "Info": Dict[str, str],
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProvisioningParametersInputRequestTypeDef = TypedDict(
    "DescribeProvisioningParametersInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "ProductId": NotRequired[str],
        "ProductName": NotRequired[str],
        "ProvisioningArtifactId": NotRequired[str],
        "ProvisioningArtifactName": NotRequired[str],
        "PathId": NotRequired[str],
        "PathName": NotRequired[str],
    },
)

DescribeProvisioningParametersOutputTypeDef = TypedDict(
    "DescribeProvisioningParametersOutputTypeDef",
    {
        "ProvisioningArtifactParameters": List["ProvisioningArtifactParameterTypeDef"],
        "ConstraintSummaries": List["ConstraintSummaryTypeDef"],
        "UsageInstructions": List["UsageInstructionTypeDef"],
        "TagOptions": List["TagOptionSummaryTypeDef"],
        "ProvisioningArtifactPreferences": "ProvisioningArtifactPreferencesTypeDef",
        "ProvisioningArtifactOutputs": List["ProvisioningArtifactOutputTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRecordInputRequestTypeDef = TypedDict(
    "DescribeRecordInputRequestTypeDef",
    {
        "Id": str,
        "AcceptLanguage": NotRequired[str],
        "PageToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)

DescribeRecordOutputTypeDef = TypedDict(
    "DescribeRecordOutputTypeDef",
    {
        "RecordDetail": "RecordDetailTypeDef",
        "RecordOutputs": List["RecordOutputTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServiceActionExecutionParametersInputRequestTypeDef = TypedDict(
    "DescribeServiceActionExecutionParametersInputRequestTypeDef",
    {
        "ProvisionedProductId": str,
        "ServiceActionId": str,
        "AcceptLanguage": NotRequired[str],
    },
)

DescribeServiceActionExecutionParametersOutputTypeDef = TypedDict(
    "DescribeServiceActionExecutionParametersOutputTypeDef",
    {
        "ServiceActionParameters": List["ExecutionParameterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServiceActionInputRequestTypeDef = TypedDict(
    "DescribeServiceActionInputRequestTypeDef",
    {
        "Id": str,
        "AcceptLanguage": NotRequired[str],
    },
)

DescribeServiceActionOutputTypeDef = TypedDict(
    "DescribeServiceActionOutputTypeDef",
    {
        "ServiceActionDetail": "ServiceActionDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTagOptionInputRequestTypeDef = TypedDict(
    "DescribeTagOptionInputRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeTagOptionOutputTypeDef = TypedDict(
    "DescribeTagOptionOutputTypeDef",
    {
        "TagOptionDetail": "TagOptionDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateBudgetFromResourceInputRequestTypeDef = TypedDict(
    "DisassociateBudgetFromResourceInputRequestTypeDef",
    {
        "BudgetName": str,
        "ResourceId": str,
    },
)

DisassociatePrincipalFromPortfolioInputRequestTypeDef = TypedDict(
    "DisassociatePrincipalFromPortfolioInputRequestTypeDef",
    {
        "PortfolioId": str,
        "PrincipalARN": str,
        "AcceptLanguage": NotRequired[str],
    },
)

DisassociateProductFromPortfolioInputRequestTypeDef = TypedDict(
    "DisassociateProductFromPortfolioInputRequestTypeDef",
    {
        "ProductId": str,
        "PortfolioId": str,
        "AcceptLanguage": NotRequired[str],
    },
)

DisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef = TypedDict(
    "DisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "ServiceActionId": str,
        "AcceptLanguage": NotRequired[str],
    },
)

DisassociateTagOptionFromResourceInputRequestTypeDef = TypedDict(
    "DisassociateTagOptionFromResourceInputRequestTypeDef",
    {
        "ResourceId": str,
        "TagOptionId": str,
    },
)

ExecuteProvisionedProductPlanInputRequestTypeDef = TypedDict(
    "ExecuteProvisionedProductPlanInputRequestTypeDef",
    {
        "PlanId": str,
        "IdempotencyToken": str,
        "AcceptLanguage": NotRequired[str],
    },
)

ExecuteProvisionedProductPlanOutputTypeDef = TypedDict(
    "ExecuteProvisionedProductPlanOutputTypeDef",
    {
        "RecordDetail": "RecordDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExecuteProvisionedProductServiceActionInputRequestTypeDef = TypedDict(
    "ExecuteProvisionedProductServiceActionInputRequestTypeDef",
    {
        "ProvisionedProductId": str,
        "ServiceActionId": str,
        "ExecuteToken": str,
        "AcceptLanguage": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, Sequence[str]]],
    },
)

ExecuteProvisionedProductServiceActionOutputTypeDef = TypedDict(
    "ExecuteProvisionedProductServiceActionOutputTypeDef",
    {
        "RecordDetail": "RecordDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExecutionParameterTypeDef = TypedDict(
    "ExecutionParameterTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
        "DefaultValues": NotRequired[List[str]],
    },
)

FailedServiceActionAssociationTypeDef = TypedDict(
    "FailedServiceActionAssociationTypeDef",
    {
        "ServiceActionId": NotRequired[str],
        "ProductId": NotRequired[str],
        "ProvisioningArtifactId": NotRequired[str],
        "ErrorCode": NotRequired[ServiceActionAssociationErrorCodeType],
        "ErrorMessage": NotRequired[str],
    },
)

GetAWSOrganizationsAccessStatusOutputTypeDef = TypedDict(
    "GetAWSOrganizationsAccessStatusOutputTypeDef",
    {
        "AccessStatus": AccessStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProvisionedProductOutputsInputRequestTypeDef = TypedDict(
    "GetProvisionedProductOutputsInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "ProvisionedProductId": NotRequired[str],
        "ProvisionedProductName": NotRequired[str],
        "OutputKeys": NotRequired[Sequence[str]],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
    },
)

GetProvisionedProductOutputsOutputTypeDef = TypedDict(
    "GetProvisionedProductOutputsOutputTypeDef",
    {
        "Outputs": List["RecordOutputTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportAsProvisionedProductInputRequestTypeDef = TypedDict(
    "ImportAsProvisionedProductInputRequestTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "ProvisionedProductName": str,
        "PhysicalId": str,
        "IdempotencyToken": str,
        "AcceptLanguage": NotRequired[str],
    },
)

ImportAsProvisionedProductOutputTypeDef = TypedDict(
    "ImportAsProvisionedProductOutputTypeDef",
    {
        "RecordDetail": "RecordDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LaunchPathSummaryTypeDef = TypedDict(
    "LaunchPathSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "ConstraintSummaries": NotRequired[List["ConstraintSummaryTypeDef"]],
        "Tags": NotRequired[List["TagTypeDef"]],
        "Name": NotRequired[str],
    },
)

LaunchPathTypeDef = TypedDict(
    "LaunchPathTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
    },
)

ListAcceptedPortfolioSharesInputRequestTypeDef = TypedDict(
    "ListAcceptedPortfolioSharesInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "PageToken": NotRequired[str],
        "PageSize": NotRequired[int],
        "PortfolioShareType": NotRequired[PortfolioShareTypeType],
    },
)

ListAcceptedPortfolioSharesOutputTypeDef = TypedDict(
    "ListAcceptedPortfolioSharesOutputTypeDef",
    {
        "PortfolioDetails": List["PortfolioDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBudgetsForResourceInputRequestTypeDef = TypedDict(
    "ListBudgetsForResourceInputRequestTypeDef",
    {
        "ResourceId": str,
        "AcceptLanguage": NotRequired[str],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
    },
)

ListBudgetsForResourceOutputTypeDef = TypedDict(
    "ListBudgetsForResourceOutputTypeDef",
    {
        "Budgets": List["BudgetDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConstraintsForPortfolioInputRequestTypeDef = TypedDict(
    "ListConstraintsForPortfolioInputRequestTypeDef",
    {
        "PortfolioId": str,
        "AcceptLanguage": NotRequired[str],
        "ProductId": NotRequired[str],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
    },
)

ListConstraintsForPortfolioOutputTypeDef = TypedDict(
    "ListConstraintsForPortfolioOutputTypeDef",
    {
        "ConstraintDetails": List["ConstraintDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLaunchPathsInputRequestTypeDef = TypedDict(
    "ListLaunchPathsInputRequestTypeDef",
    {
        "ProductId": str,
        "AcceptLanguage": NotRequired[str],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
    },
)

ListLaunchPathsOutputTypeDef = TypedDict(
    "ListLaunchPathsOutputTypeDef",
    {
        "LaunchPathSummaries": List["LaunchPathSummaryTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOrganizationPortfolioAccessInputRequestTypeDef = TypedDict(
    "ListOrganizationPortfolioAccessInputRequestTypeDef",
    {
        "PortfolioId": str,
        "OrganizationNodeType": OrganizationNodeTypeType,
        "AcceptLanguage": NotRequired[str],
        "PageToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)

ListOrganizationPortfolioAccessOutputTypeDef = TypedDict(
    "ListOrganizationPortfolioAccessOutputTypeDef",
    {
        "OrganizationNodes": List["OrganizationNodeTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPortfolioAccessInputRequestTypeDef = TypedDict(
    "ListPortfolioAccessInputRequestTypeDef",
    {
        "PortfolioId": str,
        "AcceptLanguage": NotRequired[str],
        "OrganizationParentId": NotRequired[str],
        "PageToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)

ListPortfolioAccessOutputTypeDef = TypedDict(
    "ListPortfolioAccessOutputTypeDef",
    {
        "AccountIds": List[str],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPortfoliosForProductInputRequestTypeDef = TypedDict(
    "ListPortfoliosForProductInputRequestTypeDef",
    {
        "ProductId": str,
        "AcceptLanguage": NotRequired[str],
        "PageToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)

ListPortfoliosForProductOutputTypeDef = TypedDict(
    "ListPortfoliosForProductOutputTypeDef",
    {
        "PortfolioDetails": List["PortfolioDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPortfoliosInputRequestTypeDef = TypedDict(
    "ListPortfoliosInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "PageToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)

ListPortfoliosOutputTypeDef = TypedDict(
    "ListPortfoliosOutputTypeDef",
    {
        "PortfolioDetails": List["PortfolioDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPrincipalsForPortfolioInputRequestTypeDef = TypedDict(
    "ListPrincipalsForPortfolioInputRequestTypeDef",
    {
        "PortfolioId": str,
        "AcceptLanguage": NotRequired[str],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
    },
)

ListPrincipalsForPortfolioOutputTypeDef = TypedDict(
    "ListPrincipalsForPortfolioOutputTypeDef",
    {
        "Principals": List["PrincipalTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProvisionedProductPlansInputRequestTypeDef = TypedDict(
    "ListProvisionedProductPlansInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "ProvisionProductId": NotRequired[str],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
        "AccessLevelFilter": NotRequired["AccessLevelFilterTypeDef"],
    },
)

ListProvisionedProductPlansOutputTypeDef = TypedDict(
    "ListProvisionedProductPlansOutputTypeDef",
    {
        "ProvisionedProductPlans": List["ProvisionedProductPlanSummaryTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProvisioningArtifactsForServiceActionInputRequestTypeDef = TypedDict(
    "ListProvisioningArtifactsForServiceActionInputRequestTypeDef",
    {
        "ServiceActionId": str,
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
        "AcceptLanguage": NotRequired[str],
    },
)

ListProvisioningArtifactsForServiceActionOutputTypeDef = TypedDict(
    "ListProvisioningArtifactsForServiceActionOutputTypeDef",
    {
        "ProvisioningArtifactViews": List["ProvisioningArtifactViewTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProvisioningArtifactsInputRequestTypeDef = TypedDict(
    "ListProvisioningArtifactsInputRequestTypeDef",
    {
        "ProductId": str,
        "AcceptLanguage": NotRequired[str],
    },
)

ListProvisioningArtifactsOutputTypeDef = TypedDict(
    "ListProvisioningArtifactsOutputTypeDef",
    {
        "ProvisioningArtifactDetails": List["ProvisioningArtifactDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecordHistoryInputRequestTypeDef = TypedDict(
    "ListRecordHistoryInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "AccessLevelFilter": NotRequired["AccessLevelFilterTypeDef"],
        "SearchFilter": NotRequired["ListRecordHistorySearchFilterTypeDef"],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
    },
)

ListRecordHistoryOutputTypeDef = TypedDict(
    "ListRecordHistoryOutputTypeDef",
    {
        "RecordDetails": List["RecordDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecordHistorySearchFilterTypeDef = TypedDict(
    "ListRecordHistorySearchFilterTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

ListResourcesForTagOptionInputRequestTypeDef = TypedDict(
    "ListResourcesForTagOptionInputRequestTypeDef",
    {
        "TagOptionId": str,
        "ResourceType": NotRequired[str],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
    },
)

ListResourcesForTagOptionOutputTypeDef = TypedDict(
    "ListResourcesForTagOptionOutputTypeDef",
    {
        "ResourceDetails": List["ResourceDetailTypeDef"],
        "PageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceActionsForProvisioningArtifactInputRequestTypeDef = TypedDict(
    "ListServiceActionsForProvisioningArtifactInputRequestTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
        "AcceptLanguage": NotRequired[str],
    },
)

ListServiceActionsForProvisioningArtifactOutputTypeDef = TypedDict(
    "ListServiceActionsForProvisioningArtifactOutputTypeDef",
    {
        "ServiceActionSummaries": List["ServiceActionSummaryTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceActionsInputRequestTypeDef = TypedDict(
    "ListServiceActionsInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
    },
)

ListServiceActionsOutputTypeDef = TypedDict(
    "ListServiceActionsOutputTypeDef",
    {
        "ServiceActionSummaries": List["ServiceActionSummaryTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStackInstancesForProvisionedProductInputRequestTypeDef = TypedDict(
    "ListStackInstancesForProvisionedProductInputRequestTypeDef",
    {
        "ProvisionedProductId": str,
        "AcceptLanguage": NotRequired[str],
        "PageToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)

ListStackInstancesForProvisionedProductOutputTypeDef = TypedDict(
    "ListStackInstancesForProvisionedProductOutputTypeDef",
    {
        "StackInstances": List["StackInstanceTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagOptionsFiltersTypeDef = TypedDict(
    "ListTagOptionsFiltersTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "Active": NotRequired[bool],
    },
)

ListTagOptionsInputRequestTypeDef = TypedDict(
    "ListTagOptionsInputRequestTypeDef",
    {
        "Filters": NotRequired["ListTagOptionsFiltersTypeDef"],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
    },
)

ListTagOptionsOutputTypeDef = TypedDict(
    "ListTagOptionsOutputTypeDef",
    {
        "TagOptionDetails": List["TagOptionDetailTypeDef"],
        "PageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OrganizationNodeTypeDef = TypedDict(
    "OrganizationNodeTypeDef",
    {
        "Type": NotRequired[OrganizationNodeTypeType],
        "Value": NotRequired[str],
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

ParameterConstraintsTypeDef = TypedDict(
    "ParameterConstraintsTypeDef",
    {
        "AllowedValues": NotRequired[List[str]],
        "AllowedPattern": NotRequired[str],
        "ConstraintDescription": NotRequired[str],
        "MaxLength": NotRequired[str],
        "MinLength": NotRequired[str],
        "MaxValue": NotRequired[str],
        "MinValue": NotRequired[str],
    },
)

PortfolioDetailTypeDef = TypedDict(
    "PortfolioDetailTypeDef",
    {
        "Id": NotRequired[str],
        "ARN": NotRequired[str],
        "DisplayName": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "ProviderName": NotRequired[str],
    },
)

PortfolioShareDetailTypeDef = TypedDict(
    "PortfolioShareDetailTypeDef",
    {
        "PrincipalId": NotRequired[str],
        "Type": NotRequired[DescribePortfolioShareTypeType],
        "Accepted": NotRequired[bool],
        "ShareTagOptions": NotRequired[bool],
    },
)

PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "PrincipalARN": NotRequired[str],
        "PrincipalType": NotRequired[Literal["IAM"]],
    },
)

ProductViewAggregationValueTypeDef = TypedDict(
    "ProductViewAggregationValueTypeDef",
    {
        "Value": NotRequired[str],
        "ApproximateCount": NotRequired[int],
    },
)

ProductViewDetailTypeDef = TypedDict(
    "ProductViewDetailTypeDef",
    {
        "ProductViewSummary": NotRequired["ProductViewSummaryTypeDef"],
        "Status": NotRequired[StatusType],
        "ProductARN": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
    },
)

ProductViewSummaryTypeDef = TypedDict(
    "ProductViewSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "ProductId": NotRequired[str],
        "Name": NotRequired[str],
        "Owner": NotRequired[str],
        "ShortDescription": NotRequired[str],
        "Type": NotRequired[ProductTypeType],
        "Distributor": NotRequired[str],
        "HasDefaultPath": NotRequired[bool],
        "SupportEmail": NotRequired[str],
        "SupportDescription": NotRequired[str],
        "SupportUrl": NotRequired[str],
    },
)

ProvisionProductInputRequestTypeDef = TypedDict(
    "ProvisionProductInputRequestTypeDef",
    {
        "ProvisionedProductName": str,
        "ProvisionToken": str,
        "AcceptLanguage": NotRequired[str],
        "ProductId": NotRequired[str],
        "ProductName": NotRequired[str],
        "ProvisioningArtifactId": NotRequired[str],
        "ProvisioningArtifactName": NotRequired[str],
        "PathId": NotRequired[str],
        "PathName": NotRequired[str],
        "ProvisioningParameters": NotRequired[Sequence["ProvisioningParameterTypeDef"]],
        "ProvisioningPreferences": NotRequired["ProvisioningPreferencesTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "NotificationArns": NotRequired[Sequence[str]],
    },
)

ProvisionProductOutputTypeDef = TypedDict(
    "ProvisionProductOutputTypeDef",
    {
        "RecordDetail": "RecordDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ProvisionedProductAttributeTypeDef = TypedDict(
    "ProvisionedProductAttributeTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "Type": NotRequired[str],
        "Id": NotRequired[str],
        "Status": NotRequired[ProvisionedProductStatusType],
        "StatusMessage": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "IdempotencyToken": NotRequired[str],
        "LastRecordId": NotRequired[str],
        "LastProvisioningRecordId": NotRequired[str],
        "LastSuccessfulProvisioningRecordId": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "PhysicalId": NotRequired[str],
        "ProductId": NotRequired[str],
        "ProductName": NotRequired[str],
        "ProvisioningArtifactId": NotRequired[str],
        "ProvisioningArtifactName": NotRequired[str],
        "UserArn": NotRequired[str],
        "UserArnSession": NotRequired[str],
    },
)

ProvisionedProductDetailTypeDef = TypedDict(
    "ProvisionedProductDetailTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "Type": NotRequired[str],
        "Id": NotRequired[str],
        "Status": NotRequired[ProvisionedProductStatusType],
        "StatusMessage": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "IdempotencyToken": NotRequired[str],
        "LastRecordId": NotRequired[str],
        "LastProvisioningRecordId": NotRequired[str],
        "LastSuccessfulProvisioningRecordId": NotRequired[str],
        "ProductId": NotRequired[str],
        "ProvisioningArtifactId": NotRequired[str],
        "LaunchRoleArn": NotRequired[str],
    },
)

ProvisionedProductPlanDetailsTypeDef = TypedDict(
    "ProvisionedProductPlanDetailsTypeDef",
    {
        "CreatedTime": NotRequired[datetime],
        "PathId": NotRequired[str],
        "ProductId": NotRequired[str],
        "PlanName": NotRequired[str],
        "PlanId": NotRequired[str],
        "ProvisionProductId": NotRequired[str],
        "ProvisionProductName": NotRequired[str],
        "PlanType": NotRequired[Literal["CLOUDFORMATION"]],
        "ProvisioningArtifactId": NotRequired[str],
        "Status": NotRequired[ProvisionedProductPlanStatusType],
        "UpdatedTime": NotRequired[datetime],
        "NotificationArns": NotRequired[List[str]],
        "ProvisioningParameters": NotRequired[List["UpdateProvisioningParameterTypeDef"]],
        "Tags": NotRequired[List["TagTypeDef"]],
        "StatusMessage": NotRequired[str],
    },
)

ProvisionedProductPlanSummaryTypeDef = TypedDict(
    "ProvisionedProductPlanSummaryTypeDef",
    {
        "PlanName": NotRequired[str],
        "PlanId": NotRequired[str],
        "ProvisionProductId": NotRequired[str],
        "ProvisionProductName": NotRequired[str],
        "PlanType": NotRequired[Literal["CLOUDFORMATION"]],
        "ProvisioningArtifactId": NotRequired[str],
    },
)

ProvisioningArtifactDetailTypeDef = TypedDict(
    "ProvisioningArtifactDetailTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Type": NotRequired[ProvisioningArtifactTypeType],
        "CreatedTime": NotRequired[datetime],
        "Active": NotRequired[bool],
        "Guidance": NotRequired[ProvisioningArtifactGuidanceType],
    },
)

ProvisioningArtifactOutputTypeDef = TypedDict(
    "ProvisioningArtifactOutputTypeDef",
    {
        "Key": NotRequired[str],
        "Description": NotRequired[str],
    },
)

ProvisioningArtifactParameterTypeDef = TypedDict(
    "ProvisioningArtifactParameterTypeDef",
    {
        "ParameterKey": NotRequired[str],
        "DefaultValue": NotRequired[str],
        "ParameterType": NotRequired[str],
        "IsNoEcho": NotRequired[bool],
        "Description": NotRequired[str],
        "ParameterConstraints": NotRequired["ParameterConstraintsTypeDef"],
    },
)

ProvisioningArtifactPreferencesTypeDef = TypedDict(
    "ProvisioningArtifactPreferencesTypeDef",
    {
        "StackSetAccounts": NotRequired[List[str]],
        "StackSetRegions": NotRequired[List[str]],
    },
)

ProvisioningArtifactPropertiesTypeDef = TypedDict(
    "ProvisioningArtifactPropertiesTypeDef",
    {
        "Info": Mapping[str, str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Type": NotRequired[ProvisioningArtifactTypeType],
        "DisableTemplateValidation": NotRequired[bool],
    },
)

ProvisioningArtifactSummaryTypeDef = TypedDict(
    "ProvisioningArtifactSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "ProvisioningArtifactMetadata": NotRequired[Dict[str, str]],
    },
)

ProvisioningArtifactTypeDef = TypedDict(
    "ProvisioningArtifactTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "Guidance": NotRequired[ProvisioningArtifactGuidanceType],
    },
)

ProvisioningArtifactViewTypeDef = TypedDict(
    "ProvisioningArtifactViewTypeDef",
    {
        "ProductViewSummary": NotRequired["ProductViewSummaryTypeDef"],
        "ProvisioningArtifact": NotRequired["ProvisioningArtifactTypeDef"],
    },
)

ProvisioningParameterTypeDef = TypedDict(
    "ProvisioningParameterTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

ProvisioningPreferencesTypeDef = TypedDict(
    "ProvisioningPreferencesTypeDef",
    {
        "StackSetAccounts": NotRequired[Sequence[str]],
        "StackSetRegions": NotRequired[Sequence[str]],
        "StackSetFailureToleranceCount": NotRequired[int],
        "StackSetFailureTolerancePercentage": NotRequired[int],
        "StackSetMaxConcurrencyCount": NotRequired[int],
        "StackSetMaxConcurrencyPercentage": NotRequired[int],
    },
)

RecordDetailTypeDef = TypedDict(
    "RecordDetailTypeDef",
    {
        "RecordId": NotRequired[str],
        "ProvisionedProductName": NotRequired[str],
        "Status": NotRequired[RecordStatusType],
        "CreatedTime": NotRequired[datetime],
        "UpdatedTime": NotRequired[datetime],
        "ProvisionedProductType": NotRequired[str],
        "RecordType": NotRequired[str],
        "ProvisionedProductId": NotRequired[str],
        "ProductId": NotRequired[str],
        "ProvisioningArtifactId": NotRequired[str],
        "PathId": NotRequired[str],
        "RecordErrors": NotRequired[List["RecordErrorTypeDef"]],
        "RecordTags": NotRequired[List["RecordTagTypeDef"]],
        "LaunchRoleArn": NotRequired[str],
    },
)

RecordErrorTypeDef = TypedDict(
    "RecordErrorTypeDef",
    {
        "Code": NotRequired[str],
        "Description": NotRequired[str],
    },
)

RecordOutputTypeDef = TypedDict(
    "RecordOutputTypeDef",
    {
        "OutputKey": NotRequired[str],
        "OutputValue": NotRequired[str],
        "Description": NotRequired[str],
    },
)

RecordTagTypeDef = TypedDict(
    "RecordTagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

RejectPortfolioShareInputRequestTypeDef = TypedDict(
    "RejectPortfolioShareInputRequestTypeDef",
    {
        "PortfolioId": str,
        "AcceptLanguage": NotRequired[str],
        "PortfolioShareType": NotRequired[PortfolioShareTypeType],
    },
)

ResourceChangeDetailTypeDef = TypedDict(
    "ResourceChangeDetailTypeDef",
    {
        "Target": NotRequired["ResourceTargetDefinitionTypeDef"],
        "Evaluation": NotRequired[EvaluationTypeType],
        "CausingEntity": NotRequired[str],
    },
)

ResourceChangeTypeDef = TypedDict(
    "ResourceChangeTypeDef",
    {
        "Action": NotRequired[ChangeActionType],
        "LogicalResourceId": NotRequired[str],
        "PhysicalResourceId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "Replacement": NotRequired[ReplacementType],
        "Scope": NotRequired[List[ResourceAttributeType]],
        "Details": NotRequired[List["ResourceChangeDetailTypeDef"]],
    },
)

ResourceDetailTypeDef = TypedDict(
    "ResourceDetailTypeDef",
    {
        "Id": NotRequired[str],
        "ARN": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
    },
)

ResourceTargetDefinitionTypeDef = TypedDict(
    "ResourceTargetDefinitionTypeDef",
    {
        "Attribute": NotRequired[ResourceAttributeType],
        "Name": NotRequired[str],
        "RequiresRecreation": NotRequired[RequiresRecreationType],
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

ScanProvisionedProductsInputRequestTypeDef = TypedDict(
    "ScanProvisionedProductsInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "AccessLevelFilter": NotRequired["AccessLevelFilterTypeDef"],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
    },
)

ScanProvisionedProductsOutputTypeDef = TypedDict(
    "ScanProvisionedProductsOutputTypeDef",
    {
        "ProvisionedProducts": List["ProvisionedProductDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchProductsAsAdminInputRequestTypeDef = TypedDict(
    "SearchProductsAsAdminInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "PortfolioId": NotRequired[str],
        "Filters": NotRequired[Mapping[ProductViewFilterByType, Sequence[str]]],
        "SortBy": NotRequired[ProductViewSortByType],
        "SortOrder": NotRequired[SortOrderType],
        "PageToken": NotRequired[str],
        "PageSize": NotRequired[int],
        "ProductSource": NotRequired[Literal["ACCOUNT"]],
    },
)

SearchProductsAsAdminOutputTypeDef = TypedDict(
    "SearchProductsAsAdminOutputTypeDef",
    {
        "ProductViewDetails": List["ProductViewDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchProductsInputRequestTypeDef = TypedDict(
    "SearchProductsInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "Filters": NotRequired[Mapping[ProductViewFilterByType, Sequence[str]]],
        "PageSize": NotRequired[int],
        "SortBy": NotRequired[ProductViewSortByType],
        "SortOrder": NotRequired[SortOrderType],
        "PageToken": NotRequired[str],
    },
)

SearchProductsOutputTypeDef = TypedDict(
    "SearchProductsOutputTypeDef",
    {
        "ProductViewSummaries": List["ProductViewSummaryTypeDef"],
        "ProductViewAggregations": Dict[str, List["ProductViewAggregationValueTypeDef"]],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchProvisionedProductsInputRequestTypeDef = TypedDict(
    "SearchProvisionedProductsInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "AccessLevelFilter": NotRequired["AccessLevelFilterTypeDef"],
        "Filters": NotRequired[Mapping[Literal["SearchQuery"], Sequence[str]]],
        "SortBy": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
    },
)

SearchProvisionedProductsOutputTypeDef = TypedDict(
    "SearchProvisionedProductsOutputTypeDef",
    {
        "ProvisionedProducts": List["ProvisionedProductAttributeTypeDef"],
        "TotalResultsCount": int,
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceActionAssociationTypeDef = TypedDict(
    "ServiceActionAssociationTypeDef",
    {
        "ServiceActionId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
    },
)

ServiceActionDetailTypeDef = TypedDict(
    "ServiceActionDetailTypeDef",
    {
        "ServiceActionSummary": NotRequired["ServiceActionSummaryTypeDef"],
        "Definition": NotRequired[Dict[ServiceActionDefinitionKeyType, str]],
    },
)

ServiceActionSummaryTypeDef = TypedDict(
    "ServiceActionSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "DefinitionType": NotRequired[Literal["SSM_AUTOMATION"]],
    },
)

ShareDetailsTypeDef = TypedDict(
    "ShareDetailsTypeDef",
    {
        "SuccessfulShares": NotRequired[List[str]],
        "ShareErrors": NotRequired[List["ShareErrorTypeDef"]],
    },
)

ShareErrorTypeDef = TypedDict(
    "ShareErrorTypeDef",
    {
        "Accounts": NotRequired[List[str]],
        "Message": NotRequired[str],
        "Error": NotRequired[str],
    },
)

StackInstanceTypeDef = TypedDict(
    "StackInstanceTypeDef",
    {
        "Account": NotRequired[str],
        "Region": NotRequired[str],
        "StackInstanceStatus": NotRequired[StackInstanceStatusType],
    },
)

TagOptionDetailTypeDef = TypedDict(
    "TagOptionDetailTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "Active": NotRequired[bool],
        "Id": NotRequired[str],
        "Owner": NotRequired[str],
    },
)

TagOptionSummaryTypeDef = TypedDict(
    "TagOptionSummaryTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[List[str]],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TerminateProvisionedProductInputRequestTypeDef = TypedDict(
    "TerminateProvisionedProductInputRequestTypeDef",
    {
        "TerminateToken": str,
        "ProvisionedProductName": NotRequired[str],
        "ProvisionedProductId": NotRequired[str],
        "IgnoreErrors": NotRequired[bool],
        "AcceptLanguage": NotRequired[str],
        "RetainPhysicalResources": NotRequired[bool],
    },
)

TerminateProvisionedProductOutputTypeDef = TypedDict(
    "TerminateProvisionedProductOutputTypeDef",
    {
        "RecordDetail": "RecordDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateConstraintInputRequestTypeDef = TypedDict(
    "UpdateConstraintInputRequestTypeDef",
    {
        "Id": str,
        "AcceptLanguage": NotRequired[str],
        "Description": NotRequired[str],
        "Parameters": NotRequired[str],
    },
)

UpdateConstraintOutputTypeDef = TypedDict(
    "UpdateConstraintOutputTypeDef",
    {
        "ConstraintDetail": "ConstraintDetailTypeDef",
        "ConstraintParameters": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePortfolioInputRequestTypeDef = TypedDict(
    "UpdatePortfolioInputRequestTypeDef",
    {
        "Id": str,
        "AcceptLanguage": NotRequired[str],
        "DisplayName": NotRequired[str],
        "Description": NotRequired[str],
        "ProviderName": NotRequired[str],
        "AddTags": NotRequired[Sequence["TagTypeDef"]],
        "RemoveTags": NotRequired[Sequence[str]],
    },
)

UpdatePortfolioOutputTypeDef = TypedDict(
    "UpdatePortfolioOutputTypeDef",
    {
        "PortfolioDetail": "PortfolioDetailTypeDef",
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePortfolioShareInputRequestTypeDef = TypedDict(
    "UpdatePortfolioShareInputRequestTypeDef",
    {
        "PortfolioId": str,
        "AcceptLanguage": NotRequired[str],
        "AccountId": NotRequired[str],
        "OrganizationNode": NotRequired["OrganizationNodeTypeDef"],
        "ShareTagOptions": NotRequired[bool],
    },
)

UpdatePortfolioShareOutputTypeDef = TypedDict(
    "UpdatePortfolioShareOutputTypeDef",
    {
        "PortfolioShareToken": str,
        "Status": ShareStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateProductInputRequestTypeDef = TypedDict(
    "UpdateProductInputRequestTypeDef",
    {
        "Id": str,
        "AcceptLanguage": NotRequired[str],
        "Name": NotRequired[str],
        "Owner": NotRequired[str],
        "Description": NotRequired[str],
        "Distributor": NotRequired[str],
        "SupportDescription": NotRequired[str],
        "SupportEmail": NotRequired[str],
        "SupportUrl": NotRequired[str],
        "AddTags": NotRequired[Sequence["TagTypeDef"]],
        "RemoveTags": NotRequired[Sequence[str]],
    },
)

UpdateProductOutputTypeDef = TypedDict(
    "UpdateProductOutputTypeDef",
    {
        "ProductViewDetail": "ProductViewDetailTypeDef",
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateProvisionedProductInputRequestTypeDef = TypedDict(
    "UpdateProvisionedProductInputRequestTypeDef",
    {
        "UpdateToken": str,
        "AcceptLanguage": NotRequired[str],
        "ProvisionedProductName": NotRequired[str],
        "ProvisionedProductId": NotRequired[str],
        "ProductId": NotRequired[str],
        "ProductName": NotRequired[str],
        "ProvisioningArtifactId": NotRequired[str],
        "ProvisioningArtifactName": NotRequired[str],
        "PathId": NotRequired[str],
        "PathName": NotRequired[str],
        "ProvisioningParameters": NotRequired[Sequence["UpdateProvisioningParameterTypeDef"]],
        "ProvisioningPreferences": NotRequired["UpdateProvisioningPreferencesTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

UpdateProvisionedProductOutputTypeDef = TypedDict(
    "UpdateProvisionedProductOutputTypeDef",
    {
        "RecordDetail": "RecordDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateProvisionedProductPropertiesInputRequestTypeDef = TypedDict(
    "UpdateProvisionedProductPropertiesInputRequestTypeDef",
    {
        "ProvisionedProductId": str,
        "ProvisionedProductProperties": Mapping[PropertyKeyType, str],
        "IdempotencyToken": str,
        "AcceptLanguage": NotRequired[str],
    },
)

UpdateProvisionedProductPropertiesOutputTypeDef = TypedDict(
    "UpdateProvisionedProductPropertiesOutputTypeDef",
    {
        "ProvisionedProductId": str,
        "ProvisionedProductProperties": Dict[PropertyKeyType, str],
        "RecordId": str,
        "Status": RecordStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateProvisioningArtifactInputRequestTypeDef = TypedDict(
    "UpdateProvisioningArtifactInputRequestTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "AcceptLanguage": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Active": NotRequired[bool],
        "Guidance": NotRequired[ProvisioningArtifactGuidanceType],
    },
)

UpdateProvisioningArtifactOutputTypeDef = TypedDict(
    "UpdateProvisioningArtifactOutputTypeDef",
    {
        "ProvisioningArtifactDetail": "ProvisioningArtifactDetailTypeDef",
        "Info": Dict[str, str],
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateProvisioningParameterTypeDef = TypedDict(
    "UpdateProvisioningParameterTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "UsePreviousValue": NotRequired[bool],
    },
)

UpdateProvisioningPreferencesTypeDef = TypedDict(
    "UpdateProvisioningPreferencesTypeDef",
    {
        "StackSetAccounts": NotRequired[Sequence[str]],
        "StackSetRegions": NotRequired[Sequence[str]],
        "StackSetFailureToleranceCount": NotRequired[int],
        "StackSetFailureTolerancePercentage": NotRequired[int],
        "StackSetMaxConcurrencyCount": NotRequired[int],
        "StackSetMaxConcurrencyPercentage": NotRequired[int],
        "StackSetOperationType": NotRequired[StackSetOperationTypeType],
    },
)

UpdateServiceActionInputRequestTypeDef = TypedDict(
    "UpdateServiceActionInputRequestTypeDef",
    {
        "Id": str,
        "Name": NotRequired[str],
        "Definition": NotRequired[Mapping[ServiceActionDefinitionKeyType, str]],
        "Description": NotRequired[str],
        "AcceptLanguage": NotRequired[str],
    },
)

UpdateServiceActionOutputTypeDef = TypedDict(
    "UpdateServiceActionOutputTypeDef",
    {
        "ServiceActionDetail": "ServiceActionDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTagOptionInputRequestTypeDef = TypedDict(
    "UpdateTagOptionInputRequestTypeDef",
    {
        "Id": str,
        "Value": NotRequired[str],
        "Active": NotRequired[bool],
    },
)

UpdateTagOptionOutputTypeDef = TypedDict(
    "UpdateTagOptionOutputTypeDef",
    {
        "TagOptionDetail": "TagOptionDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UsageInstructionTypeDef = TypedDict(
    "UsageInstructionTypeDef",
    {
        "Type": NotRequired[str],
        "Value": NotRequired[str],
    },
)
