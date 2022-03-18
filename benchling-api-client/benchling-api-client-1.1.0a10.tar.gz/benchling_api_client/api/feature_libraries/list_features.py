from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.bad_request_error import BadRequestError
from ...models.features_paginated_list import FeaturesPaginatedList
from ...models.list_features_sort import ListFeaturesSort
from ...types import Response, UNSET, Unset


def _get_kwargs(
    *,
    client: Client,
    page_size: Union[Unset, int] = 50,
    next_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, ListFeaturesSort] = ListFeaturesSort.NAMEDESC,
    name: Union[Unset, str] = UNSET,
    name_includes: Union[Unset, str] = UNSET,
    ids: Union[Unset, str] = UNSET,
    namesany_of: Union[Unset, str] = UNSET,
    feature_library_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/features".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()

    json_sort: Union[Unset, int] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params: Dict[str, Any] = {}
    if not isinstance(page_size, Unset) and page_size is not None:
        params["pageSize"] = page_size
    if not isinstance(next_token, Unset) and next_token is not None:
        params["nextToken"] = next_token
    if not isinstance(json_sort, Unset) and json_sort is not None:
        params["sort"] = json_sort
    if not isinstance(name, Unset) and name is not None:
        params["name"] = name
    if not isinstance(name_includes, Unset) and name_includes is not None:
        params["nameIncludes"] = name_includes
    if not isinstance(ids, Unset) and ids is not None:
        params["ids"] = ids
    if not isinstance(namesany_of, Unset) and namesany_of is not None:
        params["names.anyOf"] = namesany_of
    if not isinstance(feature_library_id, Unset) and feature_library_id is not None:
        params["featureLibraryId"] = feature_library_id

    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[FeaturesPaginatedList, BadRequestError]]:
    if response.status_code == 200:
        response_200 = FeaturesPaginatedList.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = BadRequestError.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[FeaturesPaginatedList, BadRequestError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    page_size: Union[Unset, int] = 50,
    next_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, ListFeaturesSort] = ListFeaturesSort.NAMEDESC,
    name: Union[Unset, str] = UNSET,
    name_includes: Union[Unset, str] = UNSET,
    ids: Union[Unset, str] = UNSET,
    namesany_of: Union[Unset, str] = UNSET,
    feature_library_id: Union[Unset, str] = UNSET,
) -> Response[Union[FeaturesPaginatedList, BadRequestError]]:
    kwargs = _get_kwargs(
        client=client,
        page_size=page_size,
        next_token=next_token,
        sort=sort,
        name=name,
        name_includes=name_includes,
        ids=ids,
        namesany_of=namesany_of,
        feature_library_id=feature_library_id,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    page_size: Union[Unset, int] = 50,
    next_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, ListFeaturesSort] = ListFeaturesSort.NAMEDESC,
    name: Union[Unset, str] = UNSET,
    name_includes: Union[Unset, str] = UNSET,
    ids: Union[Unset, str] = UNSET,
    namesany_of: Union[Unset, str] = UNSET,
    feature_library_id: Union[Unset, str] = UNSET,
) -> Optional[Union[FeaturesPaginatedList, BadRequestError]]:
    """ List Features """

    return sync_detailed(
        client=client,
        page_size=page_size,
        next_token=next_token,
        sort=sort,
        name=name,
        name_includes=name_includes,
        ids=ids,
        namesany_of=namesany_of,
        feature_library_id=feature_library_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page_size: Union[Unset, int] = 50,
    next_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, ListFeaturesSort] = ListFeaturesSort.NAMEDESC,
    name: Union[Unset, str] = UNSET,
    name_includes: Union[Unset, str] = UNSET,
    ids: Union[Unset, str] = UNSET,
    namesany_of: Union[Unset, str] = UNSET,
    feature_library_id: Union[Unset, str] = UNSET,
) -> Response[Union[FeaturesPaginatedList, BadRequestError]]:
    kwargs = _get_kwargs(
        client=client,
        page_size=page_size,
        next_token=next_token,
        sort=sort,
        name=name,
        name_includes=name_includes,
        ids=ids,
        namesany_of=namesany_of,
        feature_library_id=feature_library_id,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    page_size: Union[Unset, int] = 50,
    next_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, ListFeaturesSort] = ListFeaturesSort.NAMEDESC,
    name: Union[Unset, str] = UNSET,
    name_includes: Union[Unset, str] = UNSET,
    ids: Union[Unset, str] = UNSET,
    namesany_of: Union[Unset, str] = UNSET,
    feature_library_id: Union[Unset, str] = UNSET,
) -> Optional[Union[FeaturesPaginatedList, BadRequestError]]:
    """ List Features """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            next_token=next_token,
            sort=sort,
            name=name,
            name_includes=name_includes,
            ids=ids,
            namesany_of=namesany_of,
            feature_library_id=feature_library_id,
        )
    ).parsed
