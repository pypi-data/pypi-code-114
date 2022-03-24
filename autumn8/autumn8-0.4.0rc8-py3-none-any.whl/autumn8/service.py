import io
import os
import uuid

from lib.autumn8 import api


def upload_model(environment, organization_id, model_config, model_file):
    autodl_host = environment.value["host"]
    if type(model_file) == io.BytesIO:
        model_file.seek(0)
        model_file_name = model_config["name"]  # TODO add extension?
    else:
        model_file_name = os.path.basename(model_file)

    s3_file_url = f"autodl-staging/models/{uuid.uuid4()}-{model_file_name}"

    print("Uploading the model files...")
    api.post_model_file(environment, model_file, s3_file_url)
    model_config["s3_file_url"] = s3_file_url

    print("Creating the model entry in AutoDL...")
    model_id = api.post_model(environment, organization_id, model_config)

    print("Starting up performance predictor...")
    api.async_estimation(environment, organization_id, model_id)
    return f"{autodl_host}/{organization_id}/performancePredictor/dashboard/{model_id}"
