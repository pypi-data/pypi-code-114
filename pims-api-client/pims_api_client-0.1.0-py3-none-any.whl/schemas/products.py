from typing import Optional
from pydantic import BaseModel

class ProductFilterItem(BaseModel):
    id: str
    name: str
    code: str
    type: str
    field: Optional[str]

