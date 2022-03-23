"""
Type annotations for location service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_location/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_location.type_defs import AssociateTrackerConsumerRequestRequestTypeDef

    data: AssociateTrackerConsumerRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    BatchItemErrorCodeType,
    DimensionUnitType,
    DistanceUnitType,
    IntendedUseType,
    PositionFilteringType,
    PricingPlanType,
    RouteMatrixErrorCodeType,
    TravelModeType,
    VehicleWeightUnitType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateTrackerConsumerRequestRequestTypeDef",
    "BatchDeleteDevicePositionHistoryErrorTypeDef",
    "BatchDeleteDevicePositionHistoryRequestRequestTypeDef",
    "BatchDeleteDevicePositionHistoryResponseTypeDef",
    "BatchDeleteGeofenceErrorTypeDef",
    "BatchDeleteGeofenceRequestRequestTypeDef",
    "BatchDeleteGeofenceResponseTypeDef",
    "BatchEvaluateGeofencesErrorTypeDef",
    "BatchEvaluateGeofencesRequestRequestTypeDef",
    "BatchEvaluateGeofencesResponseTypeDef",
    "BatchGetDevicePositionErrorTypeDef",
    "BatchGetDevicePositionRequestRequestTypeDef",
    "BatchGetDevicePositionResponseTypeDef",
    "BatchItemErrorTypeDef",
    "BatchPutGeofenceErrorTypeDef",
    "BatchPutGeofenceRequestEntryTypeDef",
    "BatchPutGeofenceRequestRequestTypeDef",
    "BatchPutGeofenceResponseTypeDef",
    "BatchPutGeofenceSuccessTypeDef",
    "BatchUpdateDevicePositionErrorTypeDef",
    "BatchUpdateDevicePositionRequestRequestTypeDef",
    "BatchUpdateDevicePositionResponseTypeDef",
    "CalculateRouteCarModeOptionsTypeDef",
    "CalculateRouteMatrixRequestRequestTypeDef",
    "CalculateRouteMatrixResponseTypeDef",
    "CalculateRouteMatrixSummaryTypeDef",
    "CalculateRouteRequestRequestTypeDef",
    "CalculateRouteResponseTypeDef",
    "CalculateRouteSummaryTypeDef",
    "CalculateRouteTruckModeOptionsTypeDef",
    "CreateGeofenceCollectionRequestRequestTypeDef",
    "CreateGeofenceCollectionResponseTypeDef",
    "CreateMapRequestRequestTypeDef",
    "CreateMapResponseTypeDef",
    "CreatePlaceIndexRequestRequestTypeDef",
    "CreatePlaceIndexResponseTypeDef",
    "CreateRouteCalculatorRequestRequestTypeDef",
    "CreateRouteCalculatorResponseTypeDef",
    "CreateTrackerRequestRequestTypeDef",
    "CreateTrackerResponseTypeDef",
    "DataSourceConfigurationTypeDef",
    "DeleteGeofenceCollectionRequestRequestTypeDef",
    "DeleteMapRequestRequestTypeDef",
    "DeletePlaceIndexRequestRequestTypeDef",
    "DeleteRouteCalculatorRequestRequestTypeDef",
    "DeleteTrackerRequestRequestTypeDef",
    "DescribeGeofenceCollectionRequestRequestTypeDef",
    "DescribeGeofenceCollectionResponseTypeDef",
    "DescribeMapRequestRequestTypeDef",
    "DescribeMapResponseTypeDef",
    "DescribePlaceIndexRequestRequestTypeDef",
    "DescribePlaceIndexResponseTypeDef",
    "DescribeRouteCalculatorRequestRequestTypeDef",
    "DescribeRouteCalculatorResponseTypeDef",
    "DescribeTrackerRequestRequestTypeDef",
    "DescribeTrackerResponseTypeDef",
    "DevicePositionTypeDef",
    "DevicePositionUpdateTypeDef",
    "DisassociateTrackerConsumerRequestRequestTypeDef",
    "GeofenceGeometryTypeDef",
    "GetDevicePositionHistoryRequestRequestTypeDef",
    "GetDevicePositionHistoryResponseTypeDef",
    "GetDevicePositionRequestRequestTypeDef",
    "GetDevicePositionResponseTypeDef",
    "GetGeofenceRequestRequestTypeDef",
    "GetGeofenceResponseTypeDef",
    "GetMapGlyphsRequestRequestTypeDef",
    "GetMapGlyphsResponseTypeDef",
    "GetMapSpritesRequestRequestTypeDef",
    "GetMapSpritesResponseTypeDef",
    "GetMapStyleDescriptorRequestRequestTypeDef",
    "GetMapStyleDescriptorResponseTypeDef",
    "GetMapTileRequestRequestTypeDef",
    "GetMapTileResponseTypeDef",
    "LegGeometryTypeDef",
    "LegTypeDef",
    "ListDevicePositionsRequestRequestTypeDef",
    "ListDevicePositionsResponseEntryTypeDef",
    "ListDevicePositionsResponseTypeDef",
    "ListGeofenceCollectionsRequestRequestTypeDef",
    "ListGeofenceCollectionsResponseEntryTypeDef",
    "ListGeofenceCollectionsResponseTypeDef",
    "ListGeofenceResponseEntryTypeDef",
    "ListGeofencesRequestRequestTypeDef",
    "ListGeofencesResponseTypeDef",
    "ListMapsRequestRequestTypeDef",
    "ListMapsResponseEntryTypeDef",
    "ListMapsResponseTypeDef",
    "ListPlaceIndexesRequestRequestTypeDef",
    "ListPlaceIndexesResponseEntryTypeDef",
    "ListPlaceIndexesResponseTypeDef",
    "ListRouteCalculatorsRequestRequestTypeDef",
    "ListRouteCalculatorsResponseEntryTypeDef",
    "ListRouteCalculatorsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTrackerConsumersRequestRequestTypeDef",
    "ListTrackerConsumersResponseTypeDef",
    "ListTrackersRequestRequestTypeDef",
    "ListTrackersResponseEntryTypeDef",
    "ListTrackersResponseTypeDef",
    "MapConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PlaceGeometryTypeDef",
    "PlaceTypeDef",
    "PositionalAccuracyTypeDef",
    "PutGeofenceRequestRequestTypeDef",
    "PutGeofenceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RouteMatrixEntryErrorTypeDef",
    "RouteMatrixEntryTypeDef",
    "SearchForPositionResultTypeDef",
    "SearchForSuggestionsResultTypeDef",
    "SearchForTextResultTypeDef",
    "SearchPlaceIndexForPositionRequestRequestTypeDef",
    "SearchPlaceIndexForPositionResponseTypeDef",
    "SearchPlaceIndexForPositionSummaryTypeDef",
    "SearchPlaceIndexForSuggestionsRequestRequestTypeDef",
    "SearchPlaceIndexForSuggestionsResponseTypeDef",
    "SearchPlaceIndexForSuggestionsSummaryTypeDef",
    "SearchPlaceIndexForTextRequestRequestTypeDef",
    "SearchPlaceIndexForTextResponseTypeDef",
    "SearchPlaceIndexForTextSummaryTypeDef",
    "StepTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TimeZoneTypeDef",
    "TruckDimensionsTypeDef",
    "TruckWeightTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateGeofenceCollectionRequestRequestTypeDef",
    "UpdateGeofenceCollectionResponseTypeDef",
    "UpdateMapRequestRequestTypeDef",
    "UpdateMapResponseTypeDef",
    "UpdatePlaceIndexRequestRequestTypeDef",
    "UpdatePlaceIndexResponseTypeDef",
    "UpdateRouteCalculatorRequestRequestTypeDef",
    "UpdateRouteCalculatorResponseTypeDef",
    "UpdateTrackerRequestRequestTypeDef",
    "UpdateTrackerResponseTypeDef",
)

AssociateTrackerConsumerRequestRequestTypeDef = TypedDict(
    "AssociateTrackerConsumerRequestRequestTypeDef",
    {
        "ConsumerArn": str,
        "TrackerName": str,
    },
)

BatchDeleteDevicePositionHistoryErrorTypeDef = TypedDict(
    "BatchDeleteDevicePositionHistoryErrorTypeDef",
    {
        "DeviceId": str,
        "Error": "BatchItemErrorTypeDef",
    },
)

BatchDeleteDevicePositionHistoryRequestRequestTypeDef = TypedDict(
    "BatchDeleteDevicePositionHistoryRequestRequestTypeDef",
    {
        "DeviceIds": Sequence[str],
        "TrackerName": str,
    },
)

BatchDeleteDevicePositionHistoryResponseTypeDef = TypedDict(
    "BatchDeleteDevicePositionHistoryResponseTypeDef",
    {
        "Errors": List["BatchDeleteDevicePositionHistoryErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeleteGeofenceErrorTypeDef = TypedDict(
    "BatchDeleteGeofenceErrorTypeDef",
    {
        "Error": "BatchItemErrorTypeDef",
        "GeofenceId": str,
    },
)

BatchDeleteGeofenceRequestRequestTypeDef = TypedDict(
    "BatchDeleteGeofenceRequestRequestTypeDef",
    {
        "CollectionName": str,
        "GeofenceIds": Sequence[str],
    },
)

BatchDeleteGeofenceResponseTypeDef = TypedDict(
    "BatchDeleteGeofenceResponseTypeDef",
    {
        "Errors": List["BatchDeleteGeofenceErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchEvaluateGeofencesErrorTypeDef = TypedDict(
    "BatchEvaluateGeofencesErrorTypeDef",
    {
        "DeviceId": str,
        "Error": "BatchItemErrorTypeDef",
        "SampleTime": datetime,
    },
)

BatchEvaluateGeofencesRequestRequestTypeDef = TypedDict(
    "BatchEvaluateGeofencesRequestRequestTypeDef",
    {
        "CollectionName": str,
        "DevicePositionUpdates": Sequence["DevicePositionUpdateTypeDef"],
    },
)

BatchEvaluateGeofencesResponseTypeDef = TypedDict(
    "BatchEvaluateGeofencesResponseTypeDef",
    {
        "Errors": List["BatchEvaluateGeofencesErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDevicePositionErrorTypeDef = TypedDict(
    "BatchGetDevicePositionErrorTypeDef",
    {
        "DeviceId": str,
        "Error": "BatchItemErrorTypeDef",
    },
)

BatchGetDevicePositionRequestRequestTypeDef = TypedDict(
    "BatchGetDevicePositionRequestRequestTypeDef",
    {
        "DeviceIds": Sequence[str],
        "TrackerName": str,
    },
)

BatchGetDevicePositionResponseTypeDef = TypedDict(
    "BatchGetDevicePositionResponseTypeDef",
    {
        "DevicePositions": List["DevicePositionTypeDef"],
        "Errors": List["BatchGetDevicePositionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchItemErrorTypeDef = TypedDict(
    "BatchItemErrorTypeDef",
    {
        "Code": NotRequired[BatchItemErrorCodeType],
        "Message": NotRequired[str],
    },
)

BatchPutGeofenceErrorTypeDef = TypedDict(
    "BatchPutGeofenceErrorTypeDef",
    {
        "Error": "BatchItemErrorTypeDef",
        "GeofenceId": str,
    },
)

BatchPutGeofenceRequestEntryTypeDef = TypedDict(
    "BatchPutGeofenceRequestEntryTypeDef",
    {
        "GeofenceId": str,
        "Geometry": "GeofenceGeometryTypeDef",
    },
)

BatchPutGeofenceRequestRequestTypeDef = TypedDict(
    "BatchPutGeofenceRequestRequestTypeDef",
    {
        "CollectionName": str,
        "Entries": Sequence["BatchPutGeofenceRequestEntryTypeDef"],
    },
)

BatchPutGeofenceResponseTypeDef = TypedDict(
    "BatchPutGeofenceResponseTypeDef",
    {
        "Errors": List["BatchPutGeofenceErrorTypeDef"],
        "Successes": List["BatchPutGeofenceSuccessTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPutGeofenceSuccessTypeDef = TypedDict(
    "BatchPutGeofenceSuccessTypeDef",
    {
        "CreateTime": datetime,
        "GeofenceId": str,
        "UpdateTime": datetime,
    },
)

BatchUpdateDevicePositionErrorTypeDef = TypedDict(
    "BatchUpdateDevicePositionErrorTypeDef",
    {
        "DeviceId": str,
        "Error": "BatchItemErrorTypeDef",
        "SampleTime": datetime,
    },
)

BatchUpdateDevicePositionRequestRequestTypeDef = TypedDict(
    "BatchUpdateDevicePositionRequestRequestTypeDef",
    {
        "TrackerName": str,
        "Updates": Sequence["DevicePositionUpdateTypeDef"],
    },
)

BatchUpdateDevicePositionResponseTypeDef = TypedDict(
    "BatchUpdateDevicePositionResponseTypeDef",
    {
        "Errors": List["BatchUpdateDevicePositionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CalculateRouteCarModeOptionsTypeDef = TypedDict(
    "CalculateRouteCarModeOptionsTypeDef",
    {
        "AvoidFerries": NotRequired[bool],
        "AvoidTolls": NotRequired[bool],
    },
)

CalculateRouteMatrixRequestRequestTypeDef = TypedDict(
    "CalculateRouteMatrixRequestRequestTypeDef",
    {
        "CalculatorName": str,
        "DeparturePositions": Sequence[Sequence[float]],
        "DestinationPositions": Sequence[Sequence[float]],
        "CarModeOptions": NotRequired["CalculateRouteCarModeOptionsTypeDef"],
        "DepartNow": NotRequired[bool],
        "DepartureTime": NotRequired[Union[datetime, str]],
        "DistanceUnit": NotRequired[DistanceUnitType],
        "TravelMode": NotRequired[TravelModeType],
        "TruckModeOptions": NotRequired["CalculateRouteTruckModeOptionsTypeDef"],
    },
)

CalculateRouteMatrixResponseTypeDef = TypedDict(
    "CalculateRouteMatrixResponseTypeDef",
    {
        "RouteMatrix": List[List["RouteMatrixEntryTypeDef"]],
        "SnappedDeparturePositions": List[List[float]],
        "SnappedDestinationPositions": List[List[float]],
        "Summary": "CalculateRouteMatrixSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CalculateRouteMatrixSummaryTypeDef = TypedDict(
    "CalculateRouteMatrixSummaryTypeDef",
    {
        "DataSource": str,
        "DistanceUnit": DistanceUnitType,
        "ErrorCount": int,
        "RouteCount": int,
    },
)

CalculateRouteRequestRequestTypeDef = TypedDict(
    "CalculateRouteRequestRequestTypeDef",
    {
        "CalculatorName": str,
        "DeparturePosition": Sequence[float],
        "DestinationPosition": Sequence[float],
        "CarModeOptions": NotRequired["CalculateRouteCarModeOptionsTypeDef"],
        "DepartNow": NotRequired[bool],
        "DepartureTime": NotRequired[Union[datetime, str]],
        "DistanceUnit": NotRequired[DistanceUnitType],
        "IncludeLegGeometry": NotRequired[bool],
        "TravelMode": NotRequired[TravelModeType],
        "TruckModeOptions": NotRequired["CalculateRouteTruckModeOptionsTypeDef"],
        "WaypointPositions": NotRequired[Sequence[Sequence[float]]],
    },
)

CalculateRouteResponseTypeDef = TypedDict(
    "CalculateRouteResponseTypeDef",
    {
        "Legs": List["LegTypeDef"],
        "Summary": "CalculateRouteSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CalculateRouteSummaryTypeDef = TypedDict(
    "CalculateRouteSummaryTypeDef",
    {
        "DataSource": str,
        "Distance": float,
        "DistanceUnit": DistanceUnitType,
        "DurationSeconds": float,
        "RouteBBox": List[float],
    },
)

CalculateRouteTruckModeOptionsTypeDef = TypedDict(
    "CalculateRouteTruckModeOptionsTypeDef",
    {
        "AvoidFerries": NotRequired[bool],
        "AvoidTolls": NotRequired[bool],
        "Dimensions": NotRequired["TruckDimensionsTypeDef"],
        "Weight": NotRequired["TruckWeightTypeDef"],
    },
)

CreateGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "CreateGeofenceCollectionRequestRequestTypeDef",
    {
        "CollectionName": str,
        "Description": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "PricingPlan": NotRequired[PricingPlanType],
        "PricingPlanDataSource": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateGeofenceCollectionResponseTypeDef = TypedDict(
    "CreateGeofenceCollectionResponseTypeDef",
    {
        "CollectionArn": str,
        "CollectionName": str,
        "CreateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMapRequestRequestTypeDef = TypedDict(
    "CreateMapRequestRequestTypeDef",
    {
        "Configuration": "MapConfigurationTypeDef",
        "MapName": str,
        "Description": NotRequired[str],
        "PricingPlan": NotRequired[PricingPlanType],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateMapResponseTypeDef = TypedDict(
    "CreateMapResponseTypeDef",
    {
        "CreateTime": datetime,
        "MapArn": str,
        "MapName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePlaceIndexRequestRequestTypeDef = TypedDict(
    "CreatePlaceIndexRequestRequestTypeDef",
    {
        "DataSource": str,
        "IndexName": str,
        "DataSourceConfiguration": NotRequired["DataSourceConfigurationTypeDef"],
        "Description": NotRequired[str],
        "PricingPlan": NotRequired[PricingPlanType],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreatePlaceIndexResponseTypeDef = TypedDict(
    "CreatePlaceIndexResponseTypeDef",
    {
        "CreateTime": datetime,
        "IndexArn": str,
        "IndexName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRouteCalculatorRequestRequestTypeDef = TypedDict(
    "CreateRouteCalculatorRequestRequestTypeDef",
    {
        "CalculatorName": str,
        "DataSource": str,
        "Description": NotRequired[str],
        "PricingPlan": NotRequired[PricingPlanType],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateRouteCalculatorResponseTypeDef = TypedDict(
    "CreateRouteCalculatorResponseTypeDef",
    {
        "CalculatorArn": str,
        "CalculatorName": str,
        "CreateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTrackerRequestRequestTypeDef = TypedDict(
    "CreateTrackerRequestRequestTypeDef",
    {
        "TrackerName": str,
        "Description": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "PositionFiltering": NotRequired[PositionFilteringType],
        "PricingPlan": NotRequired[PricingPlanType],
        "PricingPlanDataSource": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateTrackerResponseTypeDef = TypedDict(
    "CreateTrackerResponseTypeDef",
    {
        "CreateTime": datetime,
        "TrackerArn": str,
        "TrackerName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSourceConfigurationTypeDef = TypedDict(
    "DataSourceConfigurationTypeDef",
    {
        "IntendedUse": NotRequired[IntendedUseType],
    },
)

DeleteGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "DeleteGeofenceCollectionRequestRequestTypeDef",
    {
        "CollectionName": str,
    },
)

DeleteMapRequestRequestTypeDef = TypedDict(
    "DeleteMapRequestRequestTypeDef",
    {
        "MapName": str,
    },
)

DeletePlaceIndexRequestRequestTypeDef = TypedDict(
    "DeletePlaceIndexRequestRequestTypeDef",
    {
        "IndexName": str,
    },
)

DeleteRouteCalculatorRequestRequestTypeDef = TypedDict(
    "DeleteRouteCalculatorRequestRequestTypeDef",
    {
        "CalculatorName": str,
    },
)

DeleteTrackerRequestRequestTypeDef = TypedDict(
    "DeleteTrackerRequestRequestTypeDef",
    {
        "TrackerName": str,
    },
)

DescribeGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "DescribeGeofenceCollectionRequestRequestTypeDef",
    {
        "CollectionName": str,
    },
)

DescribeGeofenceCollectionResponseTypeDef = TypedDict(
    "DescribeGeofenceCollectionResponseTypeDef",
    {
        "CollectionArn": str,
        "CollectionName": str,
        "CreateTime": datetime,
        "Description": str,
        "KmsKeyId": str,
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
        "Tags": Dict[str, str],
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMapRequestRequestTypeDef = TypedDict(
    "DescribeMapRequestRequestTypeDef",
    {
        "MapName": str,
    },
)

DescribeMapResponseTypeDef = TypedDict(
    "DescribeMapResponseTypeDef",
    {
        "Configuration": "MapConfigurationTypeDef",
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "MapArn": str,
        "MapName": str,
        "PricingPlan": PricingPlanType,
        "Tags": Dict[str, str],
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePlaceIndexRequestRequestTypeDef = TypedDict(
    "DescribePlaceIndexRequestRequestTypeDef",
    {
        "IndexName": str,
    },
)

DescribePlaceIndexResponseTypeDef = TypedDict(
    "DescribePlaceIndexResponseTypeDef",
    {
        "CreateTime": datetime,
        "DataSource": str,
        "DataSourceConfiguration": "DataSourceConfigurationTypeDef",
        "Description": str,
        "IndexArn": str,
        "IndexName": str,
        "PricingPlan": PricingPlanType,
        "Tags": Dict[str, str],
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRouteCalculatorRequestRequestTypeDef = TypedDict(
    "DescribeRouteCalculatorRequestRequestTypeDef",
    {
        "CalculatorName": str,
    },
)

DescribeRouteCalculatorResponseTypeDef = TypedDict(
    "DescribeRouteCalculatorResponseTypeDef",
    {
        "CalculatorArn": str,
        "CalculatorName": str,
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "PricingPlan": PricingPlanType,
        "Tags": Dict[str, str],
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrackerRequestRequestTypeDef = TypedDict(
    "DescribeTrackerRequestRequestTypeDef",
    {
        "TrackerName": str,
    },
)

DescribeTrackerResponseTypeDef = TypedDict(
    "DescribeTrackerResponseTypeDef",
    {
        "CreateTime": datetime,
        "Description": str,
        "KmsKeyId": str,
        "PositionFiltering": PositionFilteringType,
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
        "Tags": Dict[str, str],
        "TrackerArn": str,
        "TrackerName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DevicePositionTypeDef = TypedDict(
    "DevicePositionTypeDef",
    {
        "Position": List[float],
        "ReceivedTime": datetime,
        "SampleTime": datetime,
        "Accuracy": NotRequired["PositionalAccuracyTypeDef"],
        "DeviceId": NotRequired[str],
        "PositionProperties": NotRequired[Dict[str, str]],
    },
)

DevicePositionUpdateTypeDef = TypedDict(
    "DevicePositionUpdateTypeDef",
    {
        "DeviceId": str,
        "Position": Sequence[float],
        "SampleTime": Union[datetime, str],
        "Accuracy": NotRequired["PositionalAccuracyTypeDef"],
        "PositionProperties": NotRequired[Mapping[str, str]],
    },
)

DisassociateTrackerConsumerRequestRequestTypeDef = TypedDict(
    "DisassociateTrackerConsumerRequestRequestTypeDef",
    {
        "ConsumerArn": str,
        "TrackerName": str,
    },
)

GeofenceGeometryTypeDef = TypedDict(
    "GeofenceGeometryTypeDef",
    {
        "Polygon": NotRequired[Sequence[Sequence[Sequence[float]]]],
    },
)

GetDevicePositionHistoryRequestRequestTypeDef = TypedDict(
    "GetDevicePositionHistoryRequestRequestTypeDef",
    {
        "DeviceId": str,
        "TrackerName": str,
        "EndTimeExclusive": NotRequired[Union[datetime, str]],
        "NextToken": NotRequired[str],
        "StartTimeInclusive": NotRequired[Union[datetime, str]],
    },
)

GetDevicePositionHistoryResponseTypeDef = TypedDict(
    "GetDevicePositionHistoryResponseTypeDef",
    {
        "DevicePositions": List["DevicePositionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDevicePositionRequestRequestTypeDef = TypedDict(
    "GetDevicePositionRequestRequestTypeDef",
    {
        "DeviceId": str,
        "TrackerName": str,
    },
)

GetDevicePositionResponseTypeDef = TypedDict(
    "GetDevicePositionResponseTypeDef",
    {
        "Accuracy": "PositionalAccuracyTypeDef",
        "DeviceId": str,
        "Position": List[float],
        "PositionProperties": Dict[str, str],
        "ReceivedTime": datetime,
        "SampleTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGeofenceRequestRequestTypeDef = TypedDict(
    "GetGeofenceRequestRequestTypeDef",
    {
        "CollectionName": str,
        "GeofenceId": str,
    },
)

GetGeofenceResponseTypeDef = TypedDict(
    "GetGeofenceResponseTypeDef",
    {
        "CreateTime": datetime,
        "GeofenceId": str,
        "Geometry": "GeofenceGeometryTypeDef",
        "Status": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMapGlyphsRequestRequestTypeDef = TypedDict(
    "GetMapGlyphsRequestRequestTypeDef",
    {
        "FontStack": str,
        "FontUnicodeRange": str,
        "MapName": str,
    },
)

GetMapGlyphsResponseTypeDef = TypedDict(
    "GetMapGlyphsResponseTypeDef",
    {
        "Blob": StreamingBody,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMapSpritesRequestRequestTypeDef = TypedDict(
    "GetMapSpritesRequestRequestTypeDef",
    {
        "FileName": str,
        "MapName": str,
    },
)

GetMapSpritesResponseTypeDef = TypedDict(
    "GetMapSpritesResponseTypeDef",
    {
        "Blob": StreamingBody,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMapStyleDescriptorRequestRequestTypeDef = TypedDict(
    "GetMapStyleDescriptorRequestRequestTypeDef",
    {
        "MapName": str,
    },
)

GetMapStyleDescriptorResponseTypeDef = TypedDict(
    "GetMapStyleDescriptorResponseTypeDef",
    {
        "Blob": StreamingBody,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMapTileRequestRequestTypeDef = TypedDict(
    "GetMapTileRequestRequestTypeDef",
    {
        "MapName": str,
        "X": str,
        "Y": str,
        "Z": str,
    },
)

GetMapTileResponseTypeDef = TypedDict(
    "GetMapTileResponseTypeDef",
    {
        "Blob": StreamingBody,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LegGeometryTypeDef = TypedDict(
    "LegGeometryTypeDef",
    {
        "LineString": NotRequired[List[List[float]]],
    },
)

LegTypeDef = TypedDict(
    "LegTypeDef",
    {
        "Distance": float,
        "DurationSeconds": float,
        "EndPosition": List[float],
        "StartPosition": List[float],
        "Steps": List["StepTypeDef"],
        "Geometry": NotRequired["LegGeometryTypeDef"],
    },
)

ListDevicePositionsRequestRequestTypeDef = TypedDict(
    "ListDevicePositionsRequestRequestTypeDef",
    {
        "TrackerName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListDevicePositionsResponseEntryTypeDef = TypedDict(
    "ListDevicePositionsResponseEntryTypeDef",
    {
        "DeviceId": str,
        "Position": List[float],
        "SampleTime": datetime,
        "Accuracy": NotRequired["PositionalAccuracyTypeDef"],
        "PositionProperties": NotRequired[Dict[str, str]],
    },
)

ListDevicePositionsResponseTypeDef = TypedDict(
    "ListDevicePositionsResponseTypeDef",
    {
        "Entries": List["ListDevicePositionsResponseEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGeofenceCollectionsRequestRequestTypeDef = TypedDict(
    "ListGeofenceCollectionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListGeofenceCollectionsResponseEntryTypeDef = TypedDict(
    "ListGeofenceCollectionsResponseEntryTypeDef",
    {
        "CollectionName": str,
        "CreateTime": datetime,
        "Description": str,
        "UpdateTime": datetime,
        "PricingPlan": NotRequired[PricingPlanType],
        "PricingPlanDataSource": NotRequired[str],
    },
)

ListGeofenceCollectionsResponseTypeDef = TypedDict(
    "ListGeofenceCollectionsResponseTypeDef",
    {
        "Entries": List["ListGeofenceCollectionsResponseEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGeofenceResponseEntryTypeDef = TypedDict(
    "ListGeofenceResponseEntryTypeDef",
    {
        "CreateTime": datetime,
        "GeofenceId": str,
        "Geometry": "GeofenceGeometryTypeDef",
        "Status": str,
        "UpdateTime": datetime,
    },
)

ListGeofencesRequestRequestTypeDef = TypedDict(
    "ListGeofencesRequestRequestTypeDef",
    {
        "CollectionName": str,
        "NextToken": NotRequired[str],
    },
)

ListGeofencesResponseTypeDef = TypedDict(
    "ListGeofencesResponseTypeDef",
    {
        "Entries": List["ListGeofenceResponseEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMapsRequestRequestTypeDef = TypedDict(
    "ListMapsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListMapsResponseEntryTypeDef = TypedDict(
    "ListMapsResponseEntryTypeDef",
    {
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "MapName": str,
        "UpdateTime": datetime,
        "PricingPlan": NotRequired[PricingPlanType],
    },
)

ListMapsResponseTypeDef = TypedDict(
    "ListMapsResponseTypeDef",
    {
        "Entries": List["ListMapsResponseEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPlaceIndexesRequestRequestTypeDef = TypedDict(
    "ListPlaceIndexesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListPlaceIndexesResponseEntryTypeDef = TypedDict(
    "ListPlaceIndexesResponseEntryTypeDef",
    {
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "IndexName": str,
        "UpdateTime": datetime,
        "PricingPlan": NotRequired[PricingPlanType],
    },
)

ListPlaceIndexesResponseTypeDef = TypedDict(
    "ListPlaceIndexesResponseTypeDef",
    {
        "Entries": List["ListPlaceIndexesResponseEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRouteCalculatorsRequestRequestTypeDef = TypedDict(
    "ListRouteCalculatorsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListRouteCalculatorsResponseEntryTypeDef = TypedDict(
    "ListRouteCalculatorsResponseEntryTypeDef",
    {
        "CalculatorName": str,
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "UpdateTime": datetime,
        "PricingPlan": NotRequired[PricingPlanType],
    },
)

ListRouteCalculatorsResponseTypeDef = TypedDict(
    "ListRouteCalculatorsResponseTypeDef",
    {
        "Entries": List["ListRouteCalculatorsResponseEntryTypeDef"],
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
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrackerConsumersRequestRequestTypeDef = TypedDict(
    "ListTrackerConsumersRequestRequestTypeDef",
    {
        "TrackerName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListTrackerConsumersResponseTypeDef = TypedDict(
    "ListTrackerConsumersResponseTypeDef",
    {
        "ConsumerArns": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrackersRequestRequestTypeDef = TypedDict(
    "ListTrackersRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListTrackersResponseEntryTypeDef = TypedDict(
    "ListTrackersResponseEntryTypeDef",
    {
        "CreateTime": datetime,
        "Description": str,
        "TrackerName": str,
        "UpdateTime": datetime,
        "PricingPlan": NotRequired[PricingPlanType],
        "PricingPlanDataSource": NotRequired[str],
    },
)

ListTrackersResponseTypeDef = TypedDict(
    "ListTrackersResponseTypeDef",
    {
        "Entries": List["ListTrackersResponseEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MapConfigurationTypeDef = TypedDict(
    "MapConfigurationTypeDef",
    {
        "Style": str,
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

PlaceGeometryTypeDef = TypedDict(
    "PlaceGeometryTypeDef",
    {
        "Point": NotRequired[List[float]],
    },
)

PlaceTypeDef = TypedDict(
    "PlaceTypeDef",
    {
        "Geometry": "PlaceGeometryTypeDef",
        "AddressNumber": NotRequired[str],
        "Country": NotRequired[str],
        "Interpolated": NotRequired[bool],
        "Label": NotRequired[str],
        "Municipality": NotRequired[str],
        "Neighborhood": NotRequired[str],
        "PostalCode": NotRequired[str],
        "Region": NotRequired[str],
        "Street": NotRequired[str],
        "SubRegion": NotRequired[str],
        "TimeZone": NotRequired["TimeZoneTypeDef"],
    },
)

PositionalAccuracyTypeDef = TypedDict(
    "PositionalAccuracyTypeDef",
    {
        "Horizontal": float,
    },
)

PutGeofenceRequestRequestTypeDef = TypedDict(
    "PutGeofenceRequestRequestTypeDef",
    {
        "CollectionName": str,
        "GeofenceId": str,
        "Geometry": "GeofenceGeometryTypeDef",
    },
)

PutGeofenceResponseTypeDef = TypedDict(
    "PutGeofenceResponseTypeDef",
    {
        "CreateTime": datetime,
        "GeofenceId": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

RouteMatrixEntryErrorTypeDef = TypedDict(
    "RouteMatrixEntryErrorTypeDef",
    {
        "Code": RouteMatrixErrorCodeType,
        "Message": NotRequired[str],
    },
)

RouteMatrixEntryTypeDef = TypedDict(
    "RouteMatrixEntryTypeDef",
    {
        "Distance": NotRequired[float],
        "DurationSeconds": NotRequired[float],
        "Error": NotRequired["RouteMatrixEntryErrorTypeDef"],
    },
)

SearchForPositionResultTypeDef = TypedDict(
    "SearchForPositionResultTypeDef",
    {
        "Distance": float,
        "Place": "PlaceTypeDef",
    },
)

SearchForSuggestionsResultTypeDef = TypedDict(
    "SearchForSuggestionsResultTypeDef",
    {
        "Text": str,
    },
)

SearchForTextResultTypeDef = TypedDict(
    "SearchForTextResultTypeDef",
    {
        "Place": "PlaceTypeDef",
        "Distance": NotRequired[float],
        "Relevance": NotRequired[float],
    },
)

SearchPlaceIndexForPositionRequestRequestTypeDef = TypedDict(
    "SearchPlaceIndexForPositionRequestRequestTypeDef",
    {
        "IndexName": str,
        "Position": Sequence[float],
        "Language": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

SearchPlaceIndexForPositionResponseTypeDef = TypedDict(
    "SearchPlaceIndexForPositionResponseTypeDef",
    {
        "Results": List["SearchForPositionResultTypeDef"],
        "Summary": "SearchPlaceIndexForPositionSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchPlaceIndexForPositionSummaryTypeDef = TypedDict(
    "SearchPlaceIndexForPositionSummaryTypeDef",
    {
        "DataSource": str,
        "Position": List[float],
        "Language": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

SearchPlaceIndexForSuggestionsRequestRequestTypeDef = TypedDict(
    "SearchPlaceIndexForSuggestionsRequestRequestTypeDef",
    {
        "IndexName": str,
        "Text": str,
        "BiasPosition": NotRequired[Sequence[float]],
        "FilterBBox": NotRequired[Sequence[float]],
        "FilterCountries": NotRequired[Sequence[str]],
        "Language": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

SearchPlaceIndexForSuggestionsResponseTypeDef = TypedDict(
    "SearchPlaceIndexForSuggestionsResponseTypeDef",
    {
        "Results": List["SearchForSuggestionsResultTypeDef"],
        "Summary": "SearchPlaceIndexForSuggestionsSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchPlaceIndexForSuggestionsSummaryTypeDef = TypedDict(
    "SearchPlaceIndexForSuggestionsSummaryTypeDef",
    {
        "DataSource": str,
        "Text": str,
        "BiasPosition": NotRequired[List[float]],
        "FilterBBox": NotRequired[List[float]],
        "FilterCountries": NotRequired[List[str]],
        "Language": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

SearchPlaceIndexForTextRequestRequestTypeDef = TypedDict(
    "SearchPlaceIndexForTextRequestRequestTypeDef",
    {
        "IndexName": str,
        "Text": str,
        "BiasPosition": NotRequired[Sequence[float]],
        "FilterBBox": NotRequired[Sequence[float]],
        "FilterCountries": NotRequired[Sequence[str]],
        "Language": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

SearchPlaceIndexForTextResponseTypeDef = TypedDict(
    "SearchPlaceIndexForTextResponseTypeDef",
    {
        "Results": List["SearchForTextResultTypeDef"],
        "Summary": "SearchPlaceIndexForTextSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchPlaceIndexForTextSummaryTypeDef = TypedDict(
    "SearchPlaceIndexForTextSummaryTypeDef",
    {
        "DataSource": str,
        "Text": str,
        "BiasPosition": NotRequired[List[float]],
        "FilterBBox": NotRequired[List[float]],
        "FilterCountries": NotRequired[List[str]],
        "Language": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ResultBBox": NotRequired[List[float]],
    },
)

StepTypeDef = TypedDict(
    "StepTypeDef",
    {
        "Distance": float,
        "DurationSeconds": float,
        "EndPosition": List[float],
        "StartPosition": List[float],
        "GeometryOffset": NotRequired[int],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

TimeZoneTypeDef = TypedDict(
    "TimeZoneTypeDef",
    {
        "Name": str,
        "Offset": NotRequired[int],
    },
)

TruckDimensionsTypeDef = TypedDict(
    "TruckDimensionsTypeDef",
    {
        "Height": NotRequired[float],
        "Length": NotRequired[float],
        "Unit": NotRequired[DimensionUnitType],
        "Width": NotRequired[float],
    },
)

TruckWeightTypeDef = TypedDict(
    "TruckWeightTypeDef",
    {
        "Total": NotRequired[float],
        "Unit": NotRequired[VehicleWeightUnitType],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "UpdateGeofenceCollectionRequestRequestTypeDef",
    {
        "CollectionName": str,
        "Description": NotRequired[str],
        "PricingPlan": NotRequired[PricingPlanType],
        "PricingPlanDataSource": NotRequired[str],
    },
)

UpdateGeofenceCollectionResponseTypeDef = TypedDict(
    "UpdateGeofenceCollectionResponseTypeDef",
    {
        "CollectionArn": str,
        "CollectionName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMapRequestRequestTypeDef = TypedDict(
    "UpdateMapRequestRequestTypeDef",
    {
        "MapName": str,
        "Description": NotRequired[str],
        "PricingPlan": NotRequired[PricingPlanType],
    },
)

UpdateMapResponseTypeDef = TypedDict(
    "UpdateMapResponseTypeDef",
    {
        "MapArn": str,
        "MapName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePlaceIndexRequestRequestTypeDef = TypedDict(
    "UpdatePlaceIndexRequestRequestTypeDef",
    {
        "IndexName": str,
        "DataSourceConfiguration": NotRequired["DataSourceConfigurationTypeDef"],
        "Description": NotRequired[str],
        "PricingPlan": NotRequired[PricingPlanType],
    },
)

UpdatePlaceIndexResponseTypeDef = TypedDict(
    "UpdatePlaceIndexResponseTypeDef",
    {
        "IndexArn": str,
        "IndexName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRouteCalculatorRequestRequestTypeDef = TypedDict(
    "UpdateRouteCalculatorRequestRequestTypeDef",
    {
        "CalculatorName": str,
        "Description": NotRequired[str],
        "PricingPlan": NotRequired[PricingPlanType],
    },
)

UpdateRouteCalculatorResponseTypeDef = TypedDict(
    "UpdateRouteCalculatorResponseTypeDef",
    {
        "CalculatorArn": str,
        "CalculatorName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTrackerRequestRequestTypeDef = TypedDict(
    "UpdateTrackerRequestRequestTypeDef",
    {
        "TrackerName": str,
        "Description": NotRequired[str],
        "PositionFiltering": NotRequired[PositionFilteringType],
        "PricingPlan": NotRequired[PricingPlanType],
        "PricingPlanDataSource": NotRequired[str],
    },
)

UpdateTrackerResponseTypeDef = TypedDict(
    "UpdateTrackerResponseTypeDef",
    {
        "TrackerArn": str,
        "TrackerName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
