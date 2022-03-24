from .base_executor import BaseExecutor
from pims_api_client.schemas.products import ProductFilterItem

class ProductsMethodsExecutor(BaseExecutor):

    async def fetch_filters(self):
        response = await self.client.get('pim/api/v1/product/filter')
        return ProductFilterItem.parse_obj(response)
