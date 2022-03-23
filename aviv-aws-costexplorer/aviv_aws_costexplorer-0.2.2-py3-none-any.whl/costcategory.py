import logging
import typing
import pydantic
from aviv_aws_costexplorer.types.costcategories import CostCategories
from aviv_aws_costexplorer.types.costcategory import (
    CostCategory,
    CostCategoryRule,
    CostCategoryRuleDefinition,
    CostCategoryRules
)


def diff_CostCategoryRuleDefinition(cr1: CostCategoryRuleDefinition, cr2: CostCategoryRuleDefinition):
    if cr1.type != cr2.type:
        return {"type": f"{cr1.type} != {cr2.type}"}
    if cr1.definition != cr2.definition:
        return {"definition": f"{cr1.definition} != {cr2.definition}"}
    # if cr1.type in ["And", "Or"]:
    #     for rno in cr1.definition:
    #         diff_CostCategoryRuleDefinition()
    return {}


def diff_CostCategoryRules(cc1: CostCategoryRules, cc2: CostCategoryRules):
    if set(cc1.list()) != set(cc2.list()):
        return {"rules": f"{cc1.list()} != {cc2.list()}"}
    rdiff = {}
    for rule in cc1.list():
        cr1 = cc1.get(rule)
        cr2 = cc2.get(rule) 
        if cr1 != cr2:
            rdiff[rule] = diff_CostCategoryRuleDefinition(cr1.Rule, cr2.Rule)
    return rdiff
