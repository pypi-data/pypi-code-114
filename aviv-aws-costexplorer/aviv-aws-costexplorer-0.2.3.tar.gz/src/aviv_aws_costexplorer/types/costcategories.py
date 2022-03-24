import logging
import typing
import pydantic
import boto3
from aviv_aws_costexplorer import base
from aviv_aws_costexplorer.types.costcategory import CostCategory

class CostCategories(pydantic.BaseModel):
    class Config:
        extra = 'allow'

    __root__: typing.List[CostCategory]=[]
    _cli: boto3.Session.client=boto3.client('ce')

    def __init__(self, _cli: boto3.Session.client=None, role_arn: str=None, **data) -> None:
        if role_arn:
            _cli = base.AWSClient.client('ce', role_arn=role_arn)
        # Ensure cli is passed on to CostCategory
        if '__root__' in data and _cli:
            for c in data['__root__']:
                c['_cli'] = _cli
        super().__init__(**data)
        if _cli:
            self._cli = _cli

    def list(self) -> None:
        definitions = self._cli.list_cost_category_definitions()['CostCategoryReferences']
        self.__init__(_cli=self._cli, __root__=definitions)

    def get(self, name) -> CostCategory:
        return next(filter(lambda r: r.Name == name, self.__root__), None)
