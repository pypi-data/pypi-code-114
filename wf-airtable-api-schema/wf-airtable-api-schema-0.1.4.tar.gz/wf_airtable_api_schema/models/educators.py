from typing import Optional

from pydantic import BaseModel

from . import response as response_models
MODEL_TYPE = 'educator'


class APIEducatorFields(BaseModel):
    full_name: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[list[str]] = None
    details: Optional[str] = None
    home_address: Optional[str] = None
    target_community: Optional[list[str]] = None
    stage: Optional[str] = None
    visioning_album_complete: Optional[bool] = None
    affiliation_agreement_url: Optional[str] = None
    current_roles: Optional[list[str]] = None
    source: Optional[list[str]] = None
    source_other: Optional[str] = None
    race_and_ethnicity: Optional[list[str]] = None
    race_and_ethnicity_other: Optional[str] = None
    educational_attainment: Optional[str] = None
    income_background: Optional[str] = None
    gender: Optional[str] = None
    lgbtqia_identifying: Optional[bool] = None
    pronouns: Optional[str] = None
    montessori_certified: Optional[bool] = None


class APIEducatorRelationships(BaseModel):
    educators_schools: Optional[response_models.APILinksAndData] = None
    assigned_partners: Optional[response_models.APILinks] = None
    languages: Optional[response_models.APILinksAndData] = None
    montessori_certifications: Optional[response_models.APILinksAndData] = None


class APIEducatorData(response_models.APIData):
    fields: APIEducatorFields


class ListAPIEducatorData(BaseModel):
    __root__: list[APIEducatorData]
