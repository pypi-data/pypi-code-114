"""
Type annotations for budgets service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/type_defs.html)

Usage::

    ```python
    from mypy_boto3_budgets.type_defs import ActionHistoryDetailsTypeDef

    data: ActionHistoryDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    ActionStatusType,
    ActionSubTypeType,
    ActionTypeType,
    ApprovalModelType,
    AutoAdjustTypeType,
    BudgetTypeType,
    ComparisonOperatorType,
    EventTypeType,
    ExecutionTypeType,
    NotificationStateType,
    NotificationTypeType,
    SubscriptionTypeType,
    ThresholdTypeType,
    TimeUnitType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionHistoryDetailsTypeDef",
    "ActionHistoryTypeDef",
    "ActionThresholdTypeDef",
    "ActionTypeDef",
    "AutoAdjustDataTypeDef",
    "BudgetNotificationsForAccountTypeDef",
    "BudgetPerformanceHistoryTypeDef",
    "BudgetTypeDef",
    "BudgetedAndActualAmountsTypeDef",
    "CalculatedSpendTypeDef",
    "CostTypesTypeDef",
    "CreateBudgetActionRequestRequestTypeDef",
    "CreateBudgetActionResponseTypeDef",
    "CreateBudgetRequestRequestTypeDef",
    "CreateNotificationRequestRequestTypeDef",
    "CreateSubscriberRequestRequestTypeDef",
    "DefinitionTypeDef",
    "DeleteBudgetActionRequestRequestTypeDef",
    "DeleteBudgetActionResponseTypeDef",
    "DeleteBudgetRequestRequestTypeDef",
    "DeleteNotificationRequestRequestTypeDef",
    "DeleteSubscriberRequestRequestTypeDef",
    "DescribeBudgetActionHistoriesRequestRequestTypeDef",
    "DescribeBudgetActionHistoriesResponseTypeDef",
    "DescribeBudgetActionRequestRequestTypeDef",
    "DescribeBudgetActionResponseTypeDef",
    "DescribeBudgetActionsForAccountRequestRequestTypeDef",
    "DescribeBudgetActionsForAccountResponseTypeDef",
    "DescribeBudgetActionsForBudgetRequestRequestTypeDef",
    "DescribeBudgetActionsForBudgetResponseTypeDef",
    "DescribeBudgetNotificationsForAccountRequestRequestTypeDef",
    "DescribeBudgetNotificationsForAccountResponseTypeDef",
    "DescribeBudgetPerformanceHistoryRequestRequestTypeDef",
    "DescribeBudgetPerformanceHistoryResponseTypeDef",
    "DescribeBudgetRequestRequestTypeDef",
    "DescribeBudgetResponseTypeDef",
    "DescribeBudgetsRequestRequestTypeDef",
    "DescribeBudgetsResponseTypeDef",
    "DescribeNotificationsForBudgetRequestRequestTypeDef",
    "DescribeNotificationsForBudgetResponseTypeDef",
    "DescribeSubscribersForNotificationRequestRequestTypeDef",
    "DescribeSubscribersForNotificationResponseTypeDef",
    "ExecuteBudgetActionRequestRequestTypeDef",
    "ExecuteBudgetActionResponseTypeDef",
    "HistoricalOptionsTypeDef",
    "IamActionDefinitionTypeDef",
    "NotificationTypeDef",
    "NotificationWithSubscribersTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "ScpActionDefinitionTypeDef",
    "SpendTypeDef",
    "SsmActionDefinitionTypeDef",
    "SubscriberTypeDef",
    "TimePeriodTypeDef",
    "UpdateBudgetActionRequestRequestTypeDef",
    "UpdateBudgetActionResponseTypeDef",
    "UpdateBudgetRequestRequestTypeDef",
    "UpdateNotificationRequestRequestTypeDef",
    "UpdateSubscriberRequestRequestTypeDef",
)

ActionHistoryDetailsTypeDef = TypedDict(
    "ActionHistoryDetailsTypeDef",
    {
        "Message": str,
        "Action": "ActionTypeDef",
    },
)

ActionHistoryTypeDef = TypedDict(
    "ActionHistoryTypeDef",
    {
        "Timestamp": datetime,
        "Status": ActionStatusType,
        "EventType": EventTypeType,
        "ActionHistoryDetails": "ActionHistoryDetailsTypeDef",
    },
)

ActionThresholdTypeDef = TypedDict(
    "ActionThresholdTypeDef",
    {
        "ActionThresholdValue": float,
        "ActionThresholdType": ThresholdTypeType,
    },
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "ActionId": str,
        "BudgetName": str,
        "NotificationType": NotificationTypeType,
        "ActionType": ActionTypeType,
        "ActionThreshold": "ActionThresholdTypeDef",
        "Definition": "DefinitionTypeDef",
        "ExecutionRoleArn": str,
        "ApprovalModel": ApprovalModelType,
        "Status": ActionStatusType,
        "Subscribers": List["SubscriberTypeDef"],
    },
)

AutoAdjustDataTypeDef = TypedDict(
    "AutoAdjustDataTypeDef",
    {
        "AutoAdjustType": AutoAdjustTypeType,
        "HistoricalOptions": NotRequired["HistoricalOptionsTypeDef"],
        "LastAutoAdjustTime": NotRequired[Union[datetime, str]],
    },
)

BudgetNotificationsForAccountTypeDef = TypedDict(
    "BudgetNotificationsForAccountTypeDef",
    {
        "Notifications": NotRequired[List["NotificationTypeDef"]],
        "BudgetName": NotRequired[str],
    },
)

BudgetPerformanceHistoryTypeDef = TypedDict(
    "BudgetPerformanceHistoryTypeDef",
    {
        "BudgetName": NotRequired[str],
        "BudgetType": NotRequired[BudgetTypeType],
        "CostFilters": NotRequired[Dict[str, List[str]]],
        "CostTypes": NotRequired["CostTypesTypeDef"],
        "TimeUnit": NotRequired[TimeUnitType],
        "BudgetedAndActualAmountsList": NotRequired[List["BudgetedAndActualAmountsTypeDef"]],
    },
)

BudgetTypeDef = TypedDict(
    "BudgetTypeDef",
    {
        "BudgetName": str,
        "TimeUnit": TimeUnitType,
        "BudgetType": BudgetTypeType,
        "BudgetLimit": NotRequired["SpendTypeDef"],
        "PlannedBudgetLimits": NotRequired[Mapping[str, "SpendTypeDef"]],
        "CostFilters": NotRequired[Mapping[str, Sequence[str]]],
        "CostTypes": NotRequired["CostTypesTypeDef"],
        "TimePeriod": NotRequired["TimePeriodTypeDef"],
        "CalculatedSpend": NotRequired["CalculatedSpendTypeDef"],
        "LastUpdatedTime": NotRequired[Union[datetime, str]],
        "AutoAdjustData": NotRequired["AutoAdjustDataTypeDef"],
    },
)

BudgetedAndActualAmountsTypeDef = TypedDict(
    "BudgetedAndActualAmountsTypeDef",
    {
        "BudgetedAmount": NotRequired["SpendTypeDef"],
        "ActualAmount": NotRequired["SpendTypeDef"],
        "TimePeriod": NotRequired["TimePeriodTypeDef"],
    },
)

CalculatedSpendTypeDef = TypedDict(
    "CalculatedSpendTypeDef",
    {
        "ActualSpend": "SpendTypeDef",
        "ForecastedSpend": NotRequired["SpendTypeDef"],
    },
)

CostTypesTypeDef = TypedDict(
    "CostTypesTypeDef",
    {
        "IncludeTax": NotRequired[bool],
        "IncludeSubscription": NotRequired[bool],
        "UseBlended": NotRequired[bool],
        "IncludeRefund": NotRequired[bool],
        "IncludeCredit": NotRequired[bool],
        "IncludeUpfront": NotRequired[bool],
        "IncludeRecurring": NotRequired[bool],
        "IncludeOtherSubscription": NotRequired[bool],
        "IncludeSupport": NotRequired[bool],
        "IncludeDiscount": NotRequired[bool],
        "UseAmortized": NotRequired[bool],
    },
)

CreateBudgetActionRequestRequestTypeDef = TypedDict(
    "CreateBudgetActionRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "NotificationType": NotificationTypeType,
        "ActionType": ActionTypeType,
        "ActionThreshold": "ActionThresholdTypeDef",
        "Definition": "DefinitionTypeDef",
        "ExecutionRoleArn": str,
        "ApprovalModel": ApprovalModelType,
        "Subscribers": Sequence["SubscriberTypeDef"],
    },
)

CreateBudgetActionResponseTypeDef = TypedDict(
    "CreateBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBudgetRequestRequestTypeDef = TypedDict(
    "CreateBudgetRequestRequestTypeDef",
    {
        "AccountId": str,
        "Budget": "BudgetTypeDef",
        "NotificationsWithSubscribers": NotRequired[Sequence["NotificationWithSubscribersTypeDef"]],
    },
)

CreateNotificationRequestRequestTypeDef = TypedDict(
    "CreateNotificationRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": "NotificationTypeDef",
        "Subscribers": Sequence["SubscriberTypeDef"],
    },
)

CreateSubscriberRequestRequestTypeDef = TypedDict(
    "CreateSubscriberRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": "NotificationTypeDef",
        "Subscriber": "SubscriberTypeDef",
    },
)

DefinitionTypeDef = TypedDict(
    "DefinitionTypeDef",
    {
        "IamActionDefinition": NotRequired["IamActionDefinitionTypeDef"],
        "ScpActionDefinition": NotRequired["ScpActionDefinitionTypeDef"],
        "SsmActionDefinition": NotRequired["SsmActionDefinitionTypeDef"],
    },
)

DeleteBudgetActionRequestRequestTypeDef = TypedDict(
    "DeleteBudgetActionRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
    },
)

DeleteBudgetActionResponseTypeDef = TypedDict(
    "DeleteBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Action": "ActionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBudgetRequestRequestTypeDef = TypedDict(
    "DeleteBudgetRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
    },
)

DeleteNotificationRequestRequestTypeDef = TypedDict(
    "DeleteNotificationRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": "NotificationTypeDef",
    },
)

DeleteSubscriberRequestRequestTypeDef = TypedDict(
    "DeleteSubscriberRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": "NotificationTypeDef",
        "Subscriber": "SubscriberTypeDef",
    },
)

DescribeBudgetActionHistoriesRequestRequestTypeDef = TypedDict(
    "DescribeBudgetActionHistoriesRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
        "TimePeriod": NotRequired["TimePeriodTypeDef"],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeBudgetActionHistoriesResponseTypeDef = TypedDict(
    "DescribeBudgetActionHistoriesResponseTypeDef",
    {
        "ActionHistories": List["ActionHistoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBudgetActionRequestRequestTypeDef = TypedDict(
    "DescribeBudgetActionRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
    },
)

DescribeBudgetActionResponseTypeDef = TypedDict(
    "DescribeBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Action": "ActionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBudgetActionsForAccountRequestRequestTypeDef = TypedDict(
    "DescribeBudgetActionsForAccountRequestRequestTypeDef",
    {
        "AccountId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeBudgetActionsForAccountResponseTypeDef = TypedDict(
    "DescribeBudgetActionsForAccountResponseTypeDef",
    {
        "Actions": List["ActionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBudgetActionsForBudgetRequestRequestTypeDef = TypedDict(
    "DescribeBudgetActionsForBudgetRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeBudgetActionsForBudgetResponseTypeDef = TypedDict(
    "DescribeBudgetActionsForBudgetResponseTypeDef",
    {
        "Actions": List["ActionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBudgetNotificationsForAccountRequestRequestTypeDef = TypedDict(
    "DescribeBudgetNotificationsForAccountRequestRequestTypeDef",
    {
        "AccountId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeBudgetNotificationsForAccountResponseTypeDef = TypedDict(
    "DescribeBudgetNotificationsForAccountResponseTypeDef",
    {
        "BudgetNotificationsForAccount": List["BudgetNotificationsForAccountTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBudgetPerformanceHistoryRequestRequestTypeDef = TypedDict(
    "DescribeBudgetPerformanceHistoryRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "TimePeriod": NotRequired["TimePeriodTypeDef"],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeBudgetPerformanceHistoryResponseTypeDef = TypedDict(
    "DescribeBudgetPerformanceHistoryResponseTypeDef",
    {
        "BudgetPerformanceHistory": "BudgetPerformanceHistoryTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBudgetRequestRequestTypeDef = TypedDict(
    "DescribeBudgetRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
    },
)

DescribeBudgetResponseTypeDef = TypedDict(
    "DescribeBudgetResponseTypeDef",
    {
        "Budget": "BudgetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBudgetsRequestRequestTypeDef = TypedDict(
    "DescribeBudgetsRequestRequestTypeDef",
    {
        "AccountId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeBudgetsResponseTypeDef = TypedDict(
    "DescribeBudgetsResponseTypeDef",
    {
        "Budgets": List["BudgetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNotificationsForBudgetRequestRequestTypeDef = TypedDict(
    "DescribeNotificationsForBudgetRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeNotificationsForBudgetResponseTypeDef = TypedDict(
    "DescribeNotificationsForBudgetResponseTypeDef",
    {
        "Notifications": List["NotificationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSubscribersForNotificationRequestRequestTypeDef = TypedDict(
    "DescribeSubscribersForNotificationRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": "NotificationTypeDef",
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeSubscribersForNotificationResponseTypeDef = TypedDict(
    "DescribeSubscribersForNotificationResponseTypeDef",
    {
        "Subscribers": List["SubscriberTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExecuteBudgetActionRequestRequestTypeDef = TypedDict(
    "ExecuteBudgetActionRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
        "ExecutionType": ExecutionTypeType,
    },
)

ExecuteBudgetActionResponseTypeDef = TypedDict(
    "ExecuteBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
        "ExecutionType": ExecutionTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HistoricalOptionsTypeDef = TypedDict(
    "HistoricalOptionsTypeDef",
    {
        "BudgetAdjustmentPeriod": int,
        "LookBackAvailablePeriods": NotRequired[int],
    },
)

IamActionDefinitionTypeDef = TypedDict(
    "IamActionDefinitionTypeDef",
    {
        "PolicyArn": str,
        "Roles": NotRequired[Sequence[str]],
        "Groups": NotRequired[Sequence[str]],
        "Users": NotRequired[Sequence[str]],
    },
)

NotificationTypeDef = TypedDict(
    "NotificationTypeDef",
    {
        "NotificationType": NotificationTypeType,
        "ComparisonOperator": ComparisonOperatorType,
        "Threshold": float,
        "ThresholdType": NotRequired[ThresholdTypeType],
        "NotificationState": NotRequired[NotificationStateType],
    },
)

NotificationWithSubscribersTypeDef = TypedDict(
    "NotificationWithSubscribersTypeDef",
    {
        "Notification": "NotificationTypeDef",
        "Subscribers": Sequence["SubscriberTypeDef"],
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

ScpActionDefinitionTypeDef = TypedDict(
    "ScpActionDefinitionTypeDef",
    {
        "PolicyId": str,
        "TargetIds": Sequence[str],
    },
)

SpendTypeDef = TypedDict(
    "SpendTypeDef",
    {
        "Amount": str,
        "Unit": str,
    },
)

SsmActionDefinitionTypeDef = TypedDict(
    "SsmActionDefinitionTypeDef",
    {
        "ActionSubType": ActionSubTypeType,
        "Region": str,
        "InstanceIds": Sequence[str],
    },
)

SubscriberTypeDef = TypedDict(
    "SubscriberTypeDef",
    {
        "SubscriptionType": SubscriptionTypeType,
        "Address": str,
    },
)

TimePeriodTypeDef = TypedDict(
    "TimePeriodTypeDef",
    {
        "Start": NotRequired[Union[datetime, str]],
        "End": NotRequired[Union[datetime, str]],
    },
)

UpdateBudgetActionRequestRequestTypeDef = TypedDict(
    "UpdateBudgetActionRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
        "NotificationType": NotRequired[NotificationTypeType],
        "ActionThreshold": NotRequired["ActionThresholdTypeDef"],
        "Definition": NotRequired["DefinitionTypeDef"],
        "ExecutionRoleArn": NotRequired[str],
        "ApprovalModel": NotRequired[ApprovalModelType],
        "Subscribers": NotRequired[Sequence["SubscriberTypeDef"]],
    },
)

UpdateBudgetActionResponseTypeDef = TypedDict(
    "UpdateBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "OldAction": "ActionTypeDef",
        "NewAction": "ActionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBudgetRequestRequestTypeDef = TypedDict(
    "UpdateBudgetRequestRequestTypeDef",
    {
        "AccountId": str,
        "NewBudget": "BudgetTypeDef",
    },
)

UpdateNotificationRequestRequestTypeDef = TypedDict(
    "UpdateNotificationRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "OldNotification": "NotificationTypeDef",
        "NewNotification": "NotificationTypeDef",
    },
)

UpdateSubscriberRequestRequestTypeDef = TypedDict(
    "UpdateSubscriberRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": "NotificationTypeDef",
        "OldSubscriber": "SubscriberTypeDef",
        "NewSubscriber": "SubscriberTypeDef",
    },
)
