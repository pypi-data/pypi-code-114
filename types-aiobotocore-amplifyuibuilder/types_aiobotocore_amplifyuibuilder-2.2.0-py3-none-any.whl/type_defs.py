"""
Type annotations for amplifyuibuilder service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_amplifyuibuilder.type_defs import ActionParametersTypeDef

    data: ActionParametersTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import SortDirectionType

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionParametersTypeDef",
    "ComponentBindingPropertiesValuePropertiesTypeDef",
    "ComponentBindingPropertiesValueTypeDef",
    "ComponentChildTypeDef",
    "ComponentConditionPropertyTypeDef",
    "ComponentDataConfigurationTypeDef",
    "ComponentEventTypeDef",
    "ComponentPropertyBindingPropertiesTypeDef",
    "ComponentPropertyTypeDef",
    "ComponentSummaryTypeDef",
    "ComponentTypeDef",
    "ComponentVariantTypeDef",
    "CreateComponentDataTypeDef",
    "CreateComponentRequestRequestTypeDef",
    "CreateComponentResponseTypeDef",
    "CreateThemeDataTypeDef",
    "CreateThemeRequestRequestTypeDef",
    "CreateThemeResponseTypeDef",
    "DeleteComponentRequestRequestTypeDef",
    "DeleteThemeRequestRequestTypeDef",
    "ExchangeCodeForTokenRequestBodyTypeDef",
    "ExchangeCodeForTokenRequestRequestTypeDef",
    "ExchangeCodeForTokenResponseTypeDef",
    "ExportComponentsRequestRequestTypeDef",
    "ExportComponentsResponseTypeDef",
    "ExportThemesRequestRequestTypeDef",
    "ExportThemesResponseTypeDef",
    "FormBindingElementTypeDef",
    "GetComponentRequestRequestTypeDef",
    "GetComponentResponseTypeDef",
    "GetThemeRequestRequestTypeDef",
    "GetThemeResponseTypeDef",
    "ListComponentsRequestRequestTypeDef",
    "ListComponentsResponseTypeDef",
    "ListThemesRequestRequestTypeDef",
    "ListThemesResponseTypeDef",
    "MutationActionSetStateParameterTypeDef",
    "PaginatorConfigTypeDef",
    "PredicateTypeDef",
    "RefreshTokenRequestBodyTypeDef",
    "RefreshTokenRequestRequestTypeDef",
    "RefreshTokenResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SortPropertyTypeDef",
    "ThemeSummaryTypeDef",
    "ThemeTypeDef",
    "ThemeValueTypeDef",
    "ThemeValuesTypeDef",
    "UpdateComponentDataTypeDef",
    "UpdateComponentRequestRequestTypeDef",
    "UpdateComponentResponseTypeDef",
    "UpdateThemeDataTypeDef",
    "UpdateThemeRequestRequestTypeDef",
    "UpdateThemeResponseTypeDef",
)

ActionParametersTypeDef = TypedDict(
    "ActionParametersTypeDef",
    {
        "anchor": NotRequired["ComponentPropertyTypeDef"],
        "fields": NotRequired[Mapping[str, "ComponentPropertyTypeDef"]],
        "global": NotRequired["ComponentPropertyTypeDef"],
        "id": NotRequired["ComponentPropertyTypeDef"],
        "model": NotRequired[str],
        "state": NotRequired["MutationActionSetStateParameterTypeDef"],
        "target": NotRequired["ComponentPropertyTypeDef"],
        "type": NotRequired["ComponentPropertyTypeDef"],
        "url": NotRequired["ComponentPropertyTypeDef"],
    },
)

ComponentBindingPropertiesValuePropertiesTypeDef = TypedDict(
    "ComponentBindingPropertiesValuePropertiesTypeDef",
    {
        "bucket": NotRequired[str],
        "defaultValue": NotRequired[str],
        "field": NotRequired[str],
        "key": NotRequired[str],
        "model": NotRequired[str],
        "predicates": NotRequired[Sequence["PredicateTypeDef"]],
        "userAttribute": NotRequired[str],
    },
)

ComponentBindingPropertiesValueTypeDef = TypedDict(
    "ComponentBindingPropertiesValueTypeDef",
    {
        "bindingProperties": NotRequired["ComponentBindingPropertiesValuePropertiesTypeDef"],
        "defaultValue": NotRequired[str],
        "type": NotRequired[str],
    },
)

ComponentChildTypeDef = TypedDict(
    "ComponentChildTypeDef",
    {
        "componentType": str,
        "name": str,
        "properties": Mapping[str, "ComponentPropertyTypeDef"],
        "children": NotRequired[Sequence[Dict[str, Any]]],
        "events": NotRequired[Mapping[str, "ComponentEventTypeDef"]],
    },
)

ComponentConditionPropertyTypeDef = TypedDict(
    "ComponentConditionPropertyTypeDef",
    {
        "else": NotRequired[Dict[str, Any]],
        "field": NotRequired[str],
        "operand": NotRequired[str],
        "operandType": NotRequired[str],
        "operator": NotRequired[str],
        "property": NotRequired[str],
        "then": NotRequired[Dict[str, Any]],
    },
)

ComponentDataConfigurationTypeDef = TypedDict(
    "ComponentDataConfigurationTypeDef",
    {
        "model": str,
        "identifiers": NotRequired[Sequence[str]],
        "predicate": NotRequired["PredicateTypeDef"],
        "sort": NotRequired[Sequence["SortPropertyTypeDef"]],
    },
)

ComponentEventTypeDef = TypedDict(
    "ComponentEventTypeDef",
    {
        "action": NotRequired[str],
        "parameters": NotRequired["ActionParametersTypeDef"],
    },
)

ComponentPropertyBindingPropertiesTypeDef = TypedDict(
    "ComponentPropertyBindingPropertiesTypeDef",
    {
        "property": str,
        "field": NotRequired[str],
    },
)

ComponentPropertyTypeDef = TypedDict(
    "ComponentPropertyTypeDef",
    {
        "bindingProperties": NotRequired["ComponentPropertyBindingPropertiesTypeDef"],
        "bindings": NotRequired[Mapping[str, "FormBindingElementTypeDef"]],
        "collectionBindingProperties": NotRequired["ComponentPropertyBindingPropertiesTypeDef"],
        "componentName": NotRequired[str],
        "concat": NotRequired[Sequence[Dict[str, Any]]],
        "condition": NotRequired[Dict[str, Any]],
        "configured": NotRequired[bool],
        "defaultValue": NotRequired[str],
        "event": NotRequired[str],
        "importedValue": NotRequired[str],
        "model": NotRequired[str],
        "property": NotRequired[str],
        "type": NotRequired[str],
        "userAttribute": NotRequired[str],
        "value": NotRequired[str],
    },
)

ComponentSummaryTypeDef = TypedDict(
    "ComponentSummaryTypeDef",
    {
        "appId": str,
        "componentType": str,
        "environmentName": str,
        "id": str,
        "name": str,
    },
)

ComponentTypeDef = TypedDict(
    "ComponentTypeDef",
    {
        "appId": str,
        "bindingProperties": Dict[str, "ComponentBindingPropertiesValueTypeDef"],
        "componentType": str,
        "createdAt": datetime,
        "environmentName": str,
        "id": str,
        "name": str,
        "overrides": Dict[str, Dict[str, str]],
        "properties": Dict[str, "ComponentPropertyTypeDef"],
        "variants": List["ComponentVariantTypeDef"],
        "children": NotRequired[List["ComponentChildTypeDef"]],
        "collectionProperties": NotRequired[Dict[str, "ComponentDataConfigurationTypeDef"]],
        "events": NotRequired[Dict[str, "ComponentEventTypeDef"]],
        "modifiedAt": NotRequired[datetime],
        "schemaVersion": NotRequired[str],
        "sourceId": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

ComponentVariantTypeDef = TypedDict(
    "ComponentVariantTypeDef",
    {
        "overrides": NotRequired[Mapping[str, Mapping[str, str]]],
        "variantValues": NotRequired[Mapping[str, str]],
    },
)

CreateComponentDataTypeDef = TypedDict(
    "CreateComponentDataTypeDef",
    {
        "bindingProperties": Mapping[str, "ComponentBindingPropertiesValueTypeDef"],
        "componentType": str,
        "name": str,
        "overrides": Mapping[str, Mapping[str, str]],
        "properties": Mapping[str, "ComponentPropertyTypeDef"],
        "variants": Sequence["ComponentVariantTypeDef"],
        "children": NotRequired[Sequence["ComponentChildTypeDef"]],
        "collectionProperties": NotRequired[Mapping[str, "ComponentDataConfigurationTypeDef"]],
        "events": NotRequired[Mapping[str, "ComponentEventTypeDef"]],
        "schemaVersion": NotRequired[str],
        "sourceId": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateComponentRequestRequestTypeDef = TypedDict(
    "CreateComponentRequestRequestTypeDef",
    {
        "appId": str,
        "componentToCreate": "CreateComponentDataTypeDef",
        "environmentName": str,
        "clientToken": NotRequired[str],
    },
)

CreateComponentResponseTypeDef = TypedDict(
    "CreateComponentResponseTypeDef",
    {
        "entity": "ComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateThemeDataTypeDef = TypedDict(
    "CreateThemeDataTypeDef",
    {
        "name": str,
        "values": Sequence["ThemeValuesTypeDef"],
        "overrides": NotRequired[Sequence["ThemeValuesTypeDef"]],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateThemeRequestRequestTypeDef = TypedDict(
    "CreateThemeRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "themeToCreate": "CreateThemeDataTypeDef",
        "clientToken": NotRequired[str],
    },
)

CreateThemeResponseTypeDef = TypedDict(
    "CreateThemeResponseTypeDef",
    {
        "entity": "ThemeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteComponentRequestRequestTypeDef = TypedDict(
    "DeleteComponentRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)

DeleteThemeRequestRequestTypeDef = TypedDict(
    "DeleteThemeRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)

ExchangeCodeForTokenRequestBodyTypeDef = TypedDict(
    "ExchangeCodeForTokenRequestBodyTypeDef",
    {
        "code": str,
        "redirectUri": str,
    },
)

ExchangeCodeForTokenRequestRequestTypeDef = TypedDict(
    "ExchangeCodeForTokenRequestRequestTypeDef",
    {
        "provider": Literal["figma"],
        "request": "ExchangeCodeForTokenRequestBodyTypeDef",
    },
)

ExchangeCodeForTokenResponseTypeDef = TypedDict(
    "ExchangeCodeForTokenResponseTypeDef",
    {
        "accessToken": str,
        "expiresIn": int,
        "refreshToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportComponentsRequestRequestTypeDef = TypedDict(
    "ExportComponentsRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "nextToken": NotRequired[str],
    },
)

ExportComponentsResponseTypeDef = TypedDict(
    "ExportComponentsResponseTypeDef",
    {
        "entities": List["ComponentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportThemesRequestRequestTypeDef = TypedDict(
    "ExportThemesRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "nextToken": NotRequired[str],
    },
)

ExportThemesResponseTypeDef = TypedDict(
    "ExportThemesResponseTypeDef",
    {
        "entities": List["ThemeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FormBindingElementTypeDef = TypedDict(
    "FormBindingElementTypeDef",
    {
        "element": str,
        "property": str,
    },
)

GetComponentRequestRequestTypeDef = TypedDict(
    "GetComponentRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)

GetComponentResponseTypeDef = TypedDict(
    "GetComponentResponseTypeDef",
    {
        "component": "ComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetThemeRequestRequestTypeDef = TypedDict(
    "GetThemeRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)

GetThemeResponseTypeDef = TypedDict(
    "GetThemeResponseTypeDef",
    {
        "theme": "ThemeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListComponentsRequestRequestTypeDef = TypedDict(
    "ListComponentsRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListComponentsResponseTypeDef = TypedDict(
    "ListComponentsResponseTypeDef",
    {
        "entities": List["ComponentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListThemesRequestRequestTypeDef = TypedDict(
    "ListThemesRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListThemesResponseTypeDef = TypedDict(
    "ListThemesResponseTypeDef",
    {
        "entities": List["ThemeSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MutationActionSetStateParameterTypeDef = TypedDict(
    "MutationActionSetStateParameterTypeDef",
    {
        "componentName": str,
        "property": str,
        "set": "ComponentPropertyTypeDef",
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

PredicateTypeDef = TypedDict(
    "PredicateTypeDef",
    {
        "and": NotRequired[Sequence[Dict[str, Any]]],
        "field": NotRequired[str],
        "operand": NotRequired[str],
        "operator": NotRequired[str],
        "or": NotRequired[Sequence[Dict[str, Any]]],
    },
)

RefreshTokenRequestBodyTypeDef = TypedDict(
    "RefreshTokenRequestBodyTypeDef",
    {
        "token": str,
    },
)

RefreshTokenRequestRequestTypeDef = TypedDict(
    "RefreshTokenRequestRequestTypeDef",
    {
        "provider": Literal["figma"],
        "refreshTokenBody": "RefreshTokenRequestBodyTypeDef",
    },
)

RefreshTokenResponseTypeDef = TypedDict(
    "RefreshTokenResponseTypeDef",
    {
        "accessToken": str,
        "expiresIn": int,
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

SortPropertyTypeDef = TypedDict(
    "SortPropertyTypeDef",
    {
        "direction": SortDirectionType,
        "field": str,
    },
)

ThemeSummaryTypeDef = TypedDict(
    "ThemeSummaryTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
    },
)

ThemeTypeDef = TypedDict(
    "ThemeTypeDef",
    {
        "appId": str,
        "createdAt": datetime,
        "environmentName": str,
        "id": str,
        "name": str,
        "values": List["ThemeValuesTypeDef"],
        "modifiedAt": NotRequired[datetime],
        "overrides": NotRequired[List["ThemeValuesTypeDef"]],
        "tags": NotRequired[Dict[str, str]],
    },
)

ThemeValueTypeDef = TypedDict(
    "ThemeValueTypeDef",
    {
        "children": NotRequired[Sequence[Dict[str, Any]]],
        "value": NotRequired[str],
    },
)

ThemeValuesTypeDef = TypedDict(
    "ThemeValuesTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[Dict[str, Any]],
    },
)

UpdateComponentDataTypeDef = TypedDict(
    "UpdateComponentDataTypeDef",
    {
        "bindingProperties": NotRequired[Mapping[str, "ComponentBindingPropertiesValueTypeDef"]],
        "children": NotRequired[Sequence["ComponentChildTypeDef"]],
        "collectionProperties": NotRequired[Mapping[str, "ComponentDataConfigurationTypeDef"]],
        "componentType": NotRequired[str],
        "events": NotRequired[Mapping[str, "ComponentEventTypeDef"]],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "overrides": NotRequired[Mapping[str, Mapping[str, str]]],
        "properties": NotRequired[Mapping[str, "ComponentPropertyTypeDef"]],
        "schemaVersion": NotRequired[str],
        "sourceId": NotRequired[str],
        "variants": NotRequired[Sequence["ComponentVariantTypeDef"]],
    },
)

UpdateComponentRequestRequestTypeDef = TypedDict(
    "UpdateComponentRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "updatedComponent": "UpdateComponentDataTypeDef",
        "clientToken": NotRequired[str],
    },
)

UpdateComponentResponseTypeDef = TypedDict(
    "UpdateComponentResponseTypeDef",
    {
        "entity": "ComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateThemeDataTypeDef = TypedDict(
    "UpdateThemeDataTypeDef",
    {
        "values": Sequence["ThemeValuesTypeDef"],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "overrides": NotRequired[Sequence["ThemeValuesTypeDef"]],
    },
)

UpdateThemeRequestRequestTypeDef = TypedDict(
    "UpdateThemeRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "updatedTheme": "UpdateThemeDataTypeDef",
        "clientToken": NotRequired[str],
    },
)

UpdateThemeResponseTypeDef = TypedDict(
    "UpdateThemeResponseTypeDef",
    {
        "entity": "ThemeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
