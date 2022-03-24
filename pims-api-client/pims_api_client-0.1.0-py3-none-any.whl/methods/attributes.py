from pims_api_client.schemas import AttributeFilter, AttributeListItem
from pims_api_client.schemas import PagedListResponse
from .base_executor import BaseExecutor

class AttributeMethodsExecutor(BaseExecutor):

    async def fetch_attributes(self, params: AttributeFilter):
        response = await self.client.get('pim/api/v1/attributes', params=params.dict())
        return PagedListResponse[AttributeListItem].parse_obj(response)

    async def fetch_attribute(self, uid: str):
        response = await self.client.get(f'pim/api/v1/attribute/{uid}')
        return AttributeListItem.parse_obj(response)
