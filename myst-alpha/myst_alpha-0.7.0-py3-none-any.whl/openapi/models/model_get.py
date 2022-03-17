from typing import Any, Dict, List, Optional

from pydantic import Field
from typing_extensions import Literal

from myst.models import base_model
from myst.openapi.models.deploy_status import DeployStatus
from myst.openapi.models.time_dataset_spec import TimeDatasetSpec


class ModelGet(base_model.BaseModel):
    """Schema for model get responses."""

    object_: Literal["Node"] = Field(..., alias="object")
    uuid: str
    create_time: str
    organization: str
    owner: str
    type: Literal["Model"]
    title: str
    project: str
    creator: str
    deploy_status: DeployStatus
    connector_uuid: str
    parameters: Dict[str, Any]
    input_specs_schema: Dict[str, Any]
    update_time: Optional[str] = None
    description: Optional[str] = None
    output_specs: Optional[List[TimeDatasetSpec]] = None
