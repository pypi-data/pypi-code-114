import logging
import typing
import pydantic
import boto3


class CostCategoryRuleDefinitionDimensions(pydantic.BaseModel):
    Key: typing.Union[
        typing.Literal["LINKED_ACCOUNT", "INSTANCE_TYPE", "REGION", "SERVICE"],
        str
    ]="LINKED_ACCOUNT"
    Values: typing.List[str]
    MatchOptions: typing.List[typing.Literal["EQUALS", "ABSENT", "STARTS_WITH", "ENDS_WITH", "CONTAINS", "CASE_SENSITIVE", "CASE_INSENSITIVE"]]=["EQUALS"]


class CostCategoryRuleDefinition(pydantic.BaseModel):
    # __root__: typing.Dict[
    #     typing.Literal["Dimensions", "Tags", "CostCategories", "And", "Or"],
    #     typing.Union[list, dict]
    # ]
    __root__: typing.Union[
        typing.Dict[typing.Literal["And", "Or"], list],
        typing.Dict[typing.Literal["Dimensions", "Tags", "CostCategories"], CostCategoryRuleDefinitionDimensions]
    ]
    definition: typing.Union[list, CostCategoryRuleDefinitionDimensions]
    type: str

    @property
    def definition(self):
        return list(self.__root__.values())[0]

    @property
    def type(self):
        return list(self.__root__.keys())[0]


class CostCategoryRule(pydantic.BaseModel):
    Value: typing.Optional[str]
    Rule: CostCategoryRuleDefinition
    Type: typing.Literal["REGULAR", "INHERITED_VALUE"]=None
    InheritedValue: dict=None


class CostCategoryRules(pydantic.BaseModel):
    __root__: typing.List[CostCategoryRule]=[]

    def list(self) -> typing.List[str]:
        return list(r.Value for r in self.__root__)

    def get(self, name) -> CostCategoryRule:
        return next(filter(lambda r: r.Value == name, self.__root__), None)

    def append(self, value) -> None:
        self.__root__.append(value)
        super().__init__(__root__=self.__root__)

    def __getitem__(self, item: int) -> int:
        return self.__root__[item]

    def __setitem__(self, item: int, value) -> None:
        self.__root__[item] = value
        super().__init__(__root__=self.__root__)

class CostCategory(pydantic.BaseModel):
    # class Config:
    #     extra = 'allow'
    #     validate_assignment = True

    Name: str
    CostCategoryArn: str=None
    EffectiveStart: str=None
    RuleVersion: str='CostCategoryExpression.v1'
    Rules: CostCategoryRules=[]
    _cli: boto3.Session.client=boto3.client('ce')

    def __init__(self, **data) -> None:
        super().__init__(**data)

    def dict(self, **attr: dict) -> dict:
        # For pydantic dict output
        attr['exclude_none'] = True
        attr['exclude'] = {"_cli"}
        return super().dict(**attr)

    def get_arn(self):
        refs = self._cli.list_cost_category_definitions()['CostCategoryReferences']
        cat = next(filter(lambda r: r['Name'] == self.Name, refs), None)
        return cat['CostCategoryArn'] if cat else None

    def sync(self):
        # If no CostCategoryArn, first check if we don't have one with the same Name
        if not self.CostCategoryArn:
            self.CostCategoryArn = self.get_arn()
        if self.CostCategoryArn:
            attr = self.dict(include={'CostCategoryArn', 'RuleVersion', 'Rules'})
            return self._cli.update_cost_category_definition(**attr)
        attr = self.dict(include={'Name', 'RuleVersion', 'Rules'})
        return self._cli.create_cost_category_definition(**attr)

    def describe(self):
        definition = self._cli.describe_cost_category_definition(CostCategoryArn=self.CostCategoryArn)['CostCategory']
        super().__init__(_cli=self._cli, **definition)
