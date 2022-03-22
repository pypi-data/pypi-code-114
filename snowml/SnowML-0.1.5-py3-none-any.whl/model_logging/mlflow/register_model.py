import mlflow
import numpy as np
import pandas as pd
from typing import Any, Union
from mlflow.models.signature import infer_signature
from mlflow.utils.environment import _mlflow_conda_env

class MLFlowModelProbabilityWrapper(mlflow.pyfunc.PythonModel):
  def __init__(self, model):
    self.model = model
    
  def predict(self, context, model_input):
    return np.round_(np.float64(self.model.predict_proba(model_input)[:,1]), 4)


class RegisterProbabilityModel:
    def __init__(self, model: Any, model_name: str, xtrain: Union[pd.DataFrame, np.ndarray], dependencies: list=[]):
        self.wrapper_model = MLFlowModelProbabilityWrapper(model)
        self.xtrain = xtrain
        self.dependencies = dependencies
        self.model_name = model_name

    def register(self):
        self.create_signaure()
        self.create_conda_env()
        mlflow.pyfunc.log_model(
            self.model_name, 
            python_model=self.wrapper_model, 
            conda_env=self.conda_env, 
            signature=self.signature
        )

    def create_signaure(self):
        self.signature = infer_signature(self.xtrain, self.wrapper_model.predict(None, self.xtrain))

    def create_conda_env(self):
        self.conda_env = _mlflow_conda_env(
          additional_conda_deps=None,
          additional_pip_deps=self.dependencies,
          additional_conda_channels=None,
      )

