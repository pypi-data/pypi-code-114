#
#   Copyright © 2021 Uncharted Software Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import logging
import os
from typing import List

from d3m import container, utils
from d3m.metadata import base as metadata_base, hyperparams
from d3m.primitive_interfaces import base, transformer
from distil.primitives import utils as distil_utils
from distil.primitives.utils import MISSING_VALUE_INDICATOR, CATEGORICALS
from distil.utils import CYTHON_DEP
from sklearn_pandas import CategoricalImputer
from distil import version

__all__ = ("CategoricalImputerPrimitive",)

logger = logging.getLogger(__name__)


class TieBreakingCategoricalImputer(CategoricalImputer):
    def __init__(self, *args, tie_breaking='error', **kwargs):
        super(TieBreakingCategoricalImputer, self).__init__(*args, **kwargs)
        self.tie_breaking = tie_breaking

        tie_breaking_strategies = ['error', 'first', 'random']
        if self.tie_breaking not in tie_breaking_strategies:
            raise ValueError(
                'Strategy {0} not in {1}'.format(self.tie_breaking, tie_breaking_strategies)
            )

    def fit(self, X, y=None):
        mask = _get_mask(X, self.missing_values)
        X = X[~mask]
        if self.strategy == 'most_frequent':
            modes = pd.Series(X).mode()
        elif self.strategy == 'constant':
            modes = np.array([self.fill_value])
        if modes.shape[0] == 0:
            raise ValueError('Data is empty or all values are null')
        elif modes.shape[0] > 1 and self.tie_breaking == 'error':
            raise ValueError('No value is repeated more than '
                            'once in the column')
        elif self.tie_breaking == 'random':
            self.fill_ = random.choice(modes[0])
        else:
            self.fill_ = modes[0]

        return self


class Hyperparams(hyperparams.Hyperparams):
    use_columns = hyperparams.Set(
        elements=hyperparams.Hyperparameter[int](-1),
        default=(),
        semantic_types=[
            "https://metadata.datadrivendiscovery.org/types/ControlParameter"
        ],
        description="A set of column indices to force primitive to operate on. If any specified column cannot be parsed, it is skipped.",
    )

    strategy = hyperparams.Enumeration[str](
        default="most_frequent",
        values=("most_frequent", "constant"),
        semantic_types=[
            "https://metadata.datadrivendiscovery.org/types/ControlParameter"
        ],
        description="Replacement strategy.  'most_frequent' will replace missing values with the mode of the column, 'constant' uses 'fill_value'",
    )

    fill_value = hyperparams.Hyperparameter[str](
        default=MISSING_VALUE_INDICATOR,
        semantic_types=[
            "https://metadata.datadrivendiscovery.org/types/ControlParameter"
        ],
        description="Value to replace missing values with.  Only applied when strategy is set to 'constant'",
    )

    error_on_empty = hyperparams.Hyperparameter[bool](
        default=False,
        semantic_types=[
            "https://metadata.datadrivendiscovery.org/types/ControlParameter"
        ],
        description="If True will raise an exception when a column consisting only of empty values is found."
        + "If False, will apply the 'fill_value' to the entire column.",
    )


class CategoricalImputerPrimitive(
    transformer.TransformerPrimitiveBase[
        container.DataFrame, container.DataFrame, Hyperparams
    ]
):
    """
    A primitive that imputes missing categorical values.  It can either replace with a constant value, or use the column mode.
    """

    metadata = metadata_base.PrimitiveMetadata(
        {
            "id": "0a9936f3-7784-4697-82f0-2a5fcc744c16",
            "version": version.__version__,
            "name": "Categorical imputer",
            "python_path": "d3m.primitives.data_transformation.imputer.DistilCategoricalImputer",
            "source": {
                "name": "Distil",
                "contact": "mailto:cbethune@uncharted.software",
                "uris": [
                    "https://gitlab.com/datadrivendiscovery/contrib/distil-primitives/-/blob/main/distil/primitives/categorical_imputer.py",
                    "https://gitlab.com/datadrivendiscovery/contrib/distil-primitives",
                ],
            },
            "installation": [
                CYTHON_DEP,
                {
                    "type": metadata_base.PrimitiveInstallationType.PIP,
                    "package": "distil-primitives",
                    "version": version.__version__,
                },
            ],
            "algorithm_types": [
                metadata_base.PrimitiveAlgorithmType.IMPUTATION,
            ],
            "primitive_family": metadata_base.PrimitiveFamily.DATA_TRANSFORMATION,
        },
    )

    def produce(
        self,
        *,
        inputs: container.DataFrame,
        timeout: float = None,
        iterations: int = None,
    ) -> base.CallResult[container.DataFrame]:

        logger.debug(f"Running {__name__}")

        # determine columns to operate on
        cols = distil_utils.get_operating_columns(
            inputs, self.hyperparams["use_columns"], CATEGORICALS
        )

        logger.debug(f"Found {len(cols)} categorical columns to evaluate")

        if len(cols) is 0:
            return base.CallResult(inputs)

        imputer = TieBreakingCategoricalImputer(
            strategy=self.hyperparams["strategy"],
            fill_value=self.hyperparams["fill_value"],
            missing_values="",
            tie_breaking="first",
        )
        outputs = inputs.copy()
        failures: List[int] = []
        for c in cols:
            input_col = inputs.iloc[:, c]
            try:
                imputer.fit(input_col)
                result = imputer.transform(input_col)
                outputs.iloc[:, c] = result
            except ValueError as e:
                # value error gets thrown when all data is missing
                if not self.hyperparams["error_on_empty"]:
                    failures.append(c)
                else:
                    raise e

        # for columns that failed using 'most_frequent' try again using 'constant'
        if not self.hyperparams["error_on_empty"]:
            imputer = TieBreakingCategoricalImputer(
                strategy="constant",
                fill_value=self.hyperparams["fill_value"],
                missing_values="",
                tie_breaking="first",
            )
            for f in failures:
                outputs_col = outputs.iloc[:, f]
                imputer.fit(outputs_col)
                result = imputer.transform(outputs_col)
                outputs.iloc[:, f] = result

        logger.debug(f"\n{outputs}")

        return base.CallResult(outputs)
