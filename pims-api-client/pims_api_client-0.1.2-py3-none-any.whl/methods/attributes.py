from pims_api_client.schemas import AttributeFilter, AttributeListItem
from pims_api_client.schemas import PagedListResponse
from typing import Optional
from .base_executor import BaseExecutor
from ..schemas.attributes import default_attribute_filter


class AttributeMethodsExecutor(BaseExecutor):

    async def fetch_attributes(self, params: AttributeFilter = default_attribute_filter):

        response = await self.client.get('pim/api/v1/attribute', params=params.dict())
        return PagedListResponse[AttributeListItem].parse_obj(response)

    async def fetch_attribute(self, uid: str):
        response = await self.client.get(f'pim/api/v1/attribute/{uid}')
        return AttributeListItem.parse_obj(response)
