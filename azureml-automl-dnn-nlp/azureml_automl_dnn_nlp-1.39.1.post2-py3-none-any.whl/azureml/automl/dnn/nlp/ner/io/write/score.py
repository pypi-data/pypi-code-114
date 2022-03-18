# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Score text dataset from model produced by training run."""

from inference_schema.schema_decorators import input_schema, output_schema
from inference_schema.parameter_types.standard_py_parameter_type import StandardPythonParameterType

from azureml.automl.dnn.nlp.common.constants import ScoringLiterals, OutputLiterals

import json
import pickle
import os


def init():
    """This function is called during inferencing environment setup and initializes the model"""
    global model
    model_path = os.path.join(os.getenv(ScoringLiterals.AZUREML_MODEL_DIR_ENV), OutputLiterals.MODEL_FILE_NAME)
    with open(model_path, 'rb') as f:
        model = pickle.load(f)


@input_schema('data', StandardPythonParameterType("This\nis\nan\nexample"))
@output_schema(StandardPythonParameterType("This B-PER\nis B-PER\nan O\nexample O"))
def run(data: str) -> str:
    """ This is called every time the endpoint is invoked. It returns the prediction of the input data

    :param data: input data provided by the user
    :type data: str
    :return: json string of the result
    :rtype: str
    """
    try:
        fin_outputs = model.predict(data)
        return json.dumps({"result": fin_outputs})
    except Exception as e:
        result = str(e)
        return json.dumps({"error": result})
