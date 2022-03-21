import json
import typing
from json import JSONEncoder
import numpy


class NumpyEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


from sanic import Sanic
from sanic import response
from pydantic import schema_of
import importlib
from typing import Any

app = Sanic(name="abottle")

USERMODEL = None


@app.post("/predict")
async def predict(request):
    # FIXME: should comprese resposne content
    user_response = USERMODEL.predict(**request.json)
    response_content = json.dumps(user_response, cls=NumpyEncoder)
    # log here
    return response.text(content=response_content, media_type="application/json")


@app.post("/metrics")
async def metrics(request):
    raise NotImplementedError()


@app.get("/healthz")
async def healthz(request):
    if hasattr(USERMODEL, "status"):
        return USERMODEL.status()
    return response.text(True)


@app.get("/readyz")
async def readyz(request):
    if hasattr(USERMODEL, "status"):
        return USERMODEL.status()
    return response.text(True)


@app.get("/meta")
async def meta(request):
    if hasattr(USERMODEL, "meta"):
        user_meta = USERMODEL.meta()
        if user_meta:
            return user_meta
    user_meta = USERMODEL.predict.__annotations__
    user_meta_dict = {}
    for key in user_meta:
        user_meta_dict[key] = schema_of(user_meta[key], title=key)
    return response.json(user_meta_dict)


from pathlib import Path
import importlib
import argparse
import os
import sys


def locate(usermodel_name):
    package_dir = Path(__name__).resolve().parent
    sys.path.append(str(package_dir))
    usermodel_names = usermodel_name.split(".")
    module = importlib.import_module(usermodel_names[0])
    my_class = None
    for attr in usermodel_names[1:]:
        my_class = getattr(module, attr)
    return my_class


from yaml import load as yaml_load

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class Struct(object):
    def __init__(self, data):
        for name, value in data.items():
            setattr(self, name, self._wrap(value))

    def _wrap(self, value):
        if isinstance(value, (tuple, list, set, frozenset)):
            return type(value)([self._wrap(v) for v in value])
        else:
            return Struct(value) if isinstance(value, dict) else value


def load(usermodel_name, wrapper, config=None, *args, **kwargs):

    config_data = None
    config_obj = None

    if config:
        try:
            with open(config, "r") as f:
                config_data = yaml_load(f, Loader=Loader)
        except FileNotFoundError:
            config_data = yaml_load(config, Loader=Loader)

        config_obj = Struct(config_data)

    usermodel = locate(usermodel_name)()

    if config_obj and not hasattr(usermodel, "Config"):
        usermodel.Config = config_obj
    elif hasattr(usermodel, "Config"):
        print("your user model contain Config field, will ignore --config argument")
    elif not config_obj and not hasattr(usermodel, "Config"):
        raise Exception(
            "your user model did not contain Config field, and you did not pass any config"
        )

    wrapper_cls = locate(wrapper)
    config_field_name = wrapper.split(".")[-1]

    if hasattr(usermodel.Config, config_field_name):
        usermodel = wrapper_cls.load_from(usermodel)

    else:
        raise Exception(
            f"no config field {config_field_name} found in your model, as the wrapper {wrapper} you passed, {config_field_name} will be your config field name, and it must exsits in your config"
        )
    return usermodel


import os


def start_server(**kwargs):
    kwargs["workers"] = os.cpu_count() * 2 - 1
    app.run(**kwargs)


def run_tester(**kwargs):
    signatures = USERMODEL.evaluate.__func__.__annotations__
    pass_kwargs = {}
    for (
        signature_name,
        signature_type,
    ) in signatures.items():
        value = kwargs.get(signature_name, None)
        if signature_name == "return":
            continue
        if (
            not value
        ):  # FIXME: <signature_name> may means a kwarg with default name, but in this code, we assume it as a error
            raise Exception(f"you should set {signature_name}")
        pass_kwargs[signature_name] = signature_type(value)
    return USERMODEL.evaluate(**pass_kwargs)


def main():
    parser = argparse.ArgumentParser(description="Warp you python object with a bottle")
    parser.add_argument("usermodel_name", help="your python object moudle")
    parser.add_argument(
        "--wrapper",
        help="which model wrapper you want to use? abottle.TritonModel? abottle.ONNXModel, abottle.TensorRTModel?, abottle.PytrochModel? or any wrapper class that implemented abottle.BaseModel!",
        default="abottle.TritonModel",
    )
    parser.add_argument("--as", dest="as_", help="server? tester?", default="server")
    parser.add_argument(
        "--config",
        required=False,
        dest="config",
        help="config yaml file path or content in string",
    )
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", default=8081)
    # FIXME: shuold set file path and batch size as fix argument?

    args, unknowns = parser.parse_known_args()
    global USERMODEL
    USERMODEL = load(**vars(args))

    if args.as_ == "server":
        start_server(host=args.host, port=args.port)
    if args.as_ == "tester":
        tester_args = {}
        for unknown in unknowns:
            unknown.replace("-", "")
            k, v = unknown.split("=")
            tester_args[k] = v
        print(run_tester(**tester_args))


if __name__ == "__main__":
    main()
