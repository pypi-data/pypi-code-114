# Copyright (c) 2020 Andrei Anton <andrei.anton@tremend.com>, Tremend Software Consulting
# Copyright (c) 2020 Stefania Budulan <stefania.budulan@tremend.com>, Tremend Software Consulting

from abc import ABC
from typing import Any


class BaseModel(ABC):
    """
    Common general interface for models and stateful/tunable algorithms.

    This provides:
    - and sklearn style interface with `fit`, `predict` and/or `fit_predict`
    - a function-like interface where you just call the model like a function
      on the input and get the output ("Keras style"), allowing simple usage
      of transformation algorithms and unsupervides ones
    - optional extra functionality for on-demand (and only once per *class*
      usage) loading of needed modules (optional dependencies)
    """

    _is_fit_predict_implemented: bool
    _are_fit_and_predict_implemented: bool
    _is_load_module_implemented: bool

    def __init__(self, *args, **kwargs):
        self._is_fit_predict_implemented = (
            self.__class__.fit_predict is not BaseModel.fit_predict
        )
        self._are_fit_and_predict_implemented = (
            self.__class__.fit is not BaseModel.fit
            and self.__class__.predict is not BaseModel.predict
        )
        assert (
            self._is_fit_predict_implemented or self._are_fit_and_predict_implemented
        ), "Subclasses mult implement either `fit` and `predict`, or `fit_predict`"

    def fit(self, X: Any, y=None) -> "BaseModel":
        ...

    def predict(self, X: Any) -> Any:
        ...

    def fit_predict(self, X: Any, y: Any = None) -> Any:
        self.fit(X)
        return self.predict(X)

    def __call__(self, X: Any) -> Any:
        if (
            hasattr(self.__class__, "fit_predict")
            and self.__class__.fit_predict is not BaseModel.fit_predict
        ):
            return self.fit_predict(X)
        else:
            self.fit(X)
            return self.predict(X)
