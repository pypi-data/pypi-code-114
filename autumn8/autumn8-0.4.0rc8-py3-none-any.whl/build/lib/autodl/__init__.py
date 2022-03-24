import enum
import io
import json
import os
import pickle
import traceback
import urllib
import uuid
import zipfile

import boto3
import requests
import torch
import torchvision
from autodl.package_resolver import package

version = "0.2.2"  # pkg_resources.require("autodl")[0].version

# TODO: add support for other organizations to CLI
DEFAULT_ORGANIZATION_ID = 1


class Environment(enum.Enum):
    localhost = {
        "host": "http://127.0.0.1",
        "s3_host": "http://localhost:4566",
        "s3_bucket_name": "predictor-bucket",
    }
    staging = {
        "host": "http://54.83.236.20",
        "s3_host": None,
        "s3_bucket_name": "autodl-staging",
    }
    production = {
        "host": "https://autodl.autumn8.ai",
        "s3_host": None,
        "s3_bucket_name": "autodl-production",
    }


environment = Environment.production
if os.environ.get("TARGET_ENV_MODE") == "staging":
    environment = Environment.staging
if os.environ.get("TARGET_ENV_MODE") == "development":
    environment = Environment.development

autodl_host = environment.value["host"]
s3_host = environment.value["s3_host"]
bucket_name = environment.value["s3_bucket_name"]

s3 = boto3.resource("s3", region_name="us-east-1", endpoint_url=s3_host)


class LayerConfig(object):
    params = list()
    name = None

    def __init__(self, name, params):
        self.name = name
        self.params = params

    def __str__(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.__str__()


def get_layers_configs(model, dummy_input):
    layers = get_children_of_model(model)

    input_shapes = {}

    def get_input_shape(name):
        def hook(model, input, output):
            # activation[name] = output.detach()
            try:
                input_shapes[name] = input[0].shape
            except:
                pass

        return hook

    output_shapes = {}

    def get_output_shape(name):
        def hook(model, input, output):
            # activation[name] = output.detach()
            try:
                output_shapes[name] = output.shape
            except:
                pass

        return hook

    for i, layer in enumerate(layers):
        layer.register_forward_hook(get_input_shape(str(i)))
        layer.register_forward_hook(get_output_shape(str(i)))

    model(*dummy_input)

    layers_configs = []

    for i, layer in enumerate(layers):
        try:
            input_shape = input_shapes[str(i)]
            output_shape = output_shapes[str(i)]
        except:
            continue
        if isinstance(layer, torch.nn.Conv2d):
            params = [
                float(input_shape[1]),
                float(input_shape[2]),
                float(layer.out_channels),
                float(layer.kernel_size[0]),
                float(layer.stride[0]),
                float(layer.dilation[0]),
                float(layer.padding[0]),
                float(input_shape[0]),
            ]
            config = LayerConfig("Conv2D", params)
        elif isinstance(layer, torch.nn.Linear):
            params = [
                float(input_shape[1]),
                layer.out_features,
                float(input_shape[0]),
            ]
            config = LayerConfig("Linear", params)
        elif isinstance(layer, torch.nn.ReLU):
            x = input_shape[2] if len(input_shape) > 2 else 1
            params = [float(input_shape[1]), x, float(input_shape[0])]
            config = LayerConfig("ReLU", params)
        elif isinstance(layer, torch.nn.EmbeddingBag):
            params = [
                float(input_shape[0]),
                float(output_shape[0]),
                float(output_shape[1]),
                float(layer.num_embeddings),
            ]
            config = LayerConfig("EmbeddingBag", params)
        elif isinstance(layer, torch.nn.Dropout2d):
            x = input_shape[2] if len(input_shape) > 2 else 1
            params = [float(input_shape[1]), x, layer.p, float(input_shape[0])]
            config = LayerConfig("Dropout2d", params)
        elif isinstance(layer, torch.nn.Dropout):
            params = [float(input_shape[1]), layer.p, float(input_shape[0])]
            config = LayerConfig("Dropout", params)
        elif isinstance(layer, torchvision.ops.misc.FrozenBatchNorm2d):
            params = [
                float(input_shape[2]),
                layer.weight.shape[0],
                float(input_shape[0]),
            ]
            config = LayerConfig("BatchNorm2d", params)
        elif isinstance(layer, torch.nn.BatchNorm2d):
            params = [
                float(input_shape[2]),
                layer.num_features,
                float(input_shape[0]),
            ]
            config = LayerConfig("BatchNorm2d", params)
        elif isinstance(layer, torch.nn.MaxPool2d):
            params = [
                float(input_shape[1]),
                float(input_shape[2]),
                float(layer.kernel_size),
                float(layer.stride),
                float(layer.dilation),
                float(layer.padding),
                float(input_shape[0]),
            ]
            config = LayerConfig("MaxPool2d", params)
        elif isinstance(layer, torch.nn.AdaptiveAvgPool2d):
            params = [
                float(input_shape[1]),
                float(input_shape[2]),
                float(input_shape[3]),
                float(layer.output_size[0]),
            ]
            config = LayerConfig("AdaptiveAvgPool2d", params)
        else:
            # unknown layer type
            config = LayerConfig(type(layer).__name__, None)

        layers_configs.append(config)

    return layers_configs


def use_environment(new_environment):
    global autodl_host, environment, s3_host, bucket_name
    environment = new_environment

    autodl_host = environment.value["host"]
    s3_host = environment.value["s3_host"]
    bucket_name = environment.value["s3_bucket_name"]


def get_children_of_model(model: torch.nn.Module):
    # get children from model!
    children = list(model.children())
    flatt_children = []
    if children == []:
        # if model has no children; model is last child! :O
        return model
    else:
        # look for children from children... to the last child!
        for child in children:
            try:
                flatt_children.extend(get_children_of_model(child))
            except TypeError:
                flatt_children.append(get_children_of_model(child))
    return flatt_children


def write_model(model, dummy_input, bytes):
    traced = torch.jit.trace(model, dummy_input)
    traced.save(bytes)


def export_pytorch_model_repr(
    model, dummy_input, interns=[], externs=[], max_search_depth=5
):
    bytes = io.BytesIO()
    assert issubclass(model.__class__, torch.nn.Module)
    if not isinstance(dummy_input, tuple):
        dummy_input = (dummy_input,)

    file, requirements, package_name = package(
        model, interns, externs, max_search_depth
    )

    layers_configs = get_layers_configs(model, dummy_input)

    with zipfile.ZipFile(bytes, "w") as zip:
        zip.writestr("modelConfig", pickle.dumps(layers_configs))
        zip.writestr(
            "MANIFEST",
            json.dumps(
                {
                    "version": version,
                    "package_name": package_name,
                }
            ),
        )
        zip.write(file.name, arcname="model.package")
        zip.writestr("requirements.json", json.dumps(requirements))

    bytes.seek(0)
    return bytes


def load(filename):
    with zipfile.ZipFile(filename) as z:
        with z.open("modelConfig", "r") as modelFile:
            modelConfig = pickle.loads(modelFile.read())

    return modelConfig


def loadModel(filename):
    with zipfile.ZipFile(filename) as z:
        with z.open("MANIFEST", "r") as manifest:
            package_name = json.loads(manifest.read())["package_name"]
        with z.open("model.package", "r") as modelFile:
            resource_name = "model.pkl"
            imp = torch.package.PackageImporter(modelFile)
            loaded_model = imp.load_pickle(package_name, resource_name)
            return loaded_model


def urlWithParams(url, params):
    url_parse = urllib.parse.urlparse(url)
    url_new_query = urllib.parse.urlencode(params)
    url_parse = url_parse._replace(query=url_new_query)

    new_url = urllib.parse.urlunparse(url_parse)
    return new_url


def postModel(model_config):
    response = requests.post(
        urlWithParams(
            "{}/api/lab/model".format(autodl_host),
            {"organization_id": DEFAULT_ORGANIZATION_ID},
        ),
        headers={"Content-Type": "application/json"},
        data=json.dumps(model_config),
    )
    if response.status_code != 200:
        raise Exception("Received response {}".format(response.status_code))
    return json.loads(response.text)["model_id"]


def deleteModel(model_id):
    new_url = urlWithParams(
        "{}/api/lab/model".format(autodl_host),
        {"model_id": model_id, "organization_id": DEFAULT_ORGANIZATION_ID},
    )
    response = requests.delete(new_url)
    if response.status_code != 200:
        raise Exception("Received response {}".format(response.status_code))


def postModelFile(file, s3_file_url):
    if isinstance(file, io.BytesIO):
        f = file
    else:
        f = open(file, "rb")

    s3.Bucket(bucket_name).Object(s3_file_url).upload_fileobj(f)


def asyncEstimation(model_id):
    new_url = urlWithParams(
        "{}/api/lab/model/async_estimation".format(autodl_host),
        {"model_id": model_id, "organization_id": DEFAULT_ORGANIZATION_ID},
    )
    response = requests.get(new_url)
    if response.status_code != 200:
        raise Exception("Received response {}".format(response.status_code))
    return response


def uploadModel(model_config, model_file):
    s3_file_url = "autodl-staging/models/{}-{}".format(
        uuid.uuid4(), model_config["name"]
    )
    if type(model_file) == io.BytesIO:
        model_file.seek(0)

    print("Uploading the model files...")
    postModelFile(model_file, s3_file_url)
    model_config["s3_file_url"] = s3_file_url

    try:
        print("Creating the model entry in AutoDL...")
        model_id = postModel(model_config)
    except:
        traceback.print_exc()
        # deleteModel(model_id)
        return

    print("Starting up performance predictor...")
    asyncEstimation(model_id)
    return "{}/{}/performanceEstimator/dashboard/{}".format(
        autodl_host, DEFAULT_ORGANIZATION_ID, model_id
    )


attached_models = []


def attach_model(
    model, example_input, interns=[], externs=[], max_search_depth=5
):
    attached_models.append(
        (model, example_input, interns, externs, max_search_depth)
    )
