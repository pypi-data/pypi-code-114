"""Within a flow all series with the same dimension should have comparable units.

<p>This check identifies how consistent the units are used within each dimension.</p>
<table style="width:100%">
  <tr>
    <th>Unit</th>
    <th>Dimension</th>
  </tr>
  <tr>
    <td>kPa</td>
    <td>Pressure</td>
  </tr>
  <tr>
    <td>kPa</td>
    <td>Pressure</td>
  </tr>
  <tr>
    <td style="background-color:rgba(250,105,106,1)">barg</td>
    <td>Pressure</td>
  </tr>
  <tr>
    <td>C</td>
    <td>Temperature</td>
  </tr>
</table>
<p class="scoring-explanation">The score of this check is calculated based on the consistency
of the units over all dimensions.
Imagine that a flow contains 4 different dimensions and that for one of those dimensions
there is 1 serie with a deviating unit.
In this case the score would be 80% =  4 (dimensions) / 5 (units)</p>
<div class="ts-check-impact">
<p>Not having comparable or consistent units hinders the interpretation over a set of series.
Downstream analysis will also become responsible for the unit conversion or correct normalization
which can lead to errors.</p>
</div>
"""

import pandas as pd

from pint import UndefinedUnitError
from pint.util import to_units_container

import timeseer

from timeseer.analysis.utils import get_unit_registry
from timeseer.metadata import fields


_CHECK_NAME = "Unit consistency"

META = {
    "checks": [
        {
            "name": _CHECK_NAME,
            "kpi": "Metadata",
            "group": "Unit",
        }
    ],
    "conditions": [
        {
            "min_series": 2,
        }
    ],
    "signature": "multivariate",
}


def _get_dimensionality(ureg, unit):
    try:
        return ureg.get_dimensionality(unit)
    except (UndefinedUnitError, AttributeError, ValueError, KeyError):
        return "Unknown"


def _get_symbol(ureg, unit):
    try:
        return ureg.get_symbol(unit)
    except (UndefinedUnitError, AttributeError, ValueError, KeyError):
        return unit


def _run_unit_to_dimension_ration(inputs: list[timeseer.AnalysisInput]):
    ureg = get_unit_registry()
    units = pd.DataFrame(map(lambda x: x.metadata.get_field(fields.Unit), inputs))
    units.drop_duplicates(inplace=True)
    units.dropna(inplace=True)
    units.replace(to_replace=".*%.*", value="pct", regex=True, inplace=True)
    units.drop_duplicates(inplace=True)
    units = units[0].apply(lambda x: _get_symbol(ureg, x))
    units.drop_duplicates(inplace=True)
    dimensions = units.apply(lambda x: _get_dimensionality(ureg, x))
    nb_units = len(
        units[
            ~dimensions.isin(["Unknown", to_units_container("", registry=ureg)])
        ].dropna()
    )
    dimensions.drop_duplicates(inplace=True)
    nb_dimensions = len(
        dimensions[
            ~dimensions.isin(["Unknown", to_units_container("", registry=ureg)])
        ].dropna()
    )
    if nb_units == 0:
        return 0
    return 1 - (nb_dimensions / nb_units)


def run(
    analysis_input: timeseer.MultivariateAnalysisInput,
):  # pylint: disable=missing-function-docstring
    inputs = analysis_input.inputs

    unit_to_dimension_ratio = _run_unit_to_dimension_ration(inputs)
    check = timeseer.CheckResult(_CHECK_NAME, float(unit_to_dimension_ratio))

    return timeseer.AnalysisResult(check_results=[check])
