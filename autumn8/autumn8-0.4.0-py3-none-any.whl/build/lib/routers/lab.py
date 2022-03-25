import json
import os
import shutil
import sys
import time
import traceback
from datetime import datetime
from pathlib import Path
from typing import List, Optional

import autodl
import mlmodel_model
import numpy as np
import settings
import tensorflow.compat.v1 as tf
import torch
from celery.result import AsyncResult
from fastapi import (
    APIRouter,
    Depends,
    File,
    Header,
    HTTPException,
    Query,
    Security,
    UploadFile,
)
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from pytorch.predictor import NoBenchmark
from pytorch.predictor import Predictor as PytorchPredictor
from tf1.predictor import Predictor

from estimation import perform_estimation as __perform_estimation
from worker import estimation_task, test_task

router = APIRouter()

sys.path.append(os.path.join(os.path.dirname(__file__), "../models"))
sys.path.append(os.path.join(os.path.dirname(__file__), "."))
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "../perf_predictor"))


if "SVC_ROOT" in os.environ:
    workdir = os.environ["SVC_ROOT"]
else:
    workdir = str(Path.home()) + "/onspecta_svc"

lab_api_base = "/api/lab"

# TODO: Hardcode user_id. Just a temporary solution for demo.
# In real implementation, user_id should be retrieved from a
# user management service which derives the user_id from
# authentication token provided in HTTP headers
test_user_id = 0

# Clear performance task info after restart
mlmodel_model.clear_perf_task()


class NewModelInfo(BaseModel):
    name: str
    s3_file_url: str if os.environ.get(
        "NEXT_PUBLIC_FEATURE_S3_UPLOADS"
    ) == "true" else Optional[str] = None
    framework: str
    quantization: str
    from_onspecta: Optional[bool] = False
    domain: str
    task: str
    channels: Optional[int] = None
    height: Optional[int] = None
    width: Optional[int] = None
    batch_size: int


class UpdateModelInfo(BaseModel):
    name: Optional[str] = None
    s3_file_url: Optional[str] = None
    domain: Optional[str] = None
    task: Optional[str] = None
    channels: Optional[int] = None
    height: Optional[int] = None
    width: Optional[int] = None
    batch_size: Optional[int] = None
    top1: Optional[float] = None
    top5: Optional[float] = None


def check_if_all_chunks(
    src_filename, from_onspecta, user_id, model_name, model_id, total
):
    file_extension = Path(src_filename).suffix
    if from_onspecta:
        dest_relpath = "/mlmodel_files/onspecta/" + model_name + file_extension
    else:
        dest_relpath = (
            "/mlmodel_files/"
            + str(user_id)
            + "/"
            + model_name
            + "_"
            + str(model_id)
            + file_extension
        )

    dest_path = workdir + dest_relpath
    for i in range(total):
        chunk_path = dest_path + "." + str(i)
        if not os.path.exists(chunk_path):
            return None

    # all chunks downloaded, merge them
    Path(os.path.dirname(dest_path)).mkdir(parents=True, exist_ok=True)
    with open(dest_path, "wb") as buffer:
        for i in range(total):
            chunk_path = dest_path + "." + str(i)
            f = open(chunk_path, "rb")
            data = f.read()
            f.close()
            buffer.write(data)

    # clean up
    for i in range(total):
        chunk_path = dest_path + "." + str(i)
        os.remove(chunk_path)

    return dest_relpath


# TODO: Support S3 (or similar file storage)
def save_mlmodel_file(
    src, src_filename, from_onspecta, user_id, model_name, model_id, chunk=None
):
    file_extension = Path(src_filename).suffix
    if from_onspecta:
        dest_relpath = "/mlmodel_files/onspecta/" + model_name + file_extension
    else:
        dest_relpath = (
            "/mlmodel_files/"
            + str(user_id)
            + "/"
            + model_name
            + "_"
            + str(model_id)
            + file_extension
        )

    if chunk is not None:
        dest_relpath += "." + str(chunk)
    dest_path = workdir + dest_relpath
    print(dest_path)
    Path(os.path.dirname(dest_path)).mkdir(parents=True, exist_ok=True)
    with open(dest_path, "wb") as buffer:
        shutil.copyfileobj(src, buffer)
    return dest_relpath


# Create new model entry
@router.post(lab_api_base + "/model")
async def new_model(model_info: NewModelInfo):
    print("Create new model {}".format(model_info))

    if (
        model_info.framework != "TENSORFLOW"
        and model_info.framework != "PYTORCH"
    ):
        raise HTTPException(status_code=400, detail="Unsupported framework")

    model_id = mlmodel_model.create(test_user_id, model_info.name)
    fields = {}
    if model_info.s3_file_url != "":
        # TODO validate - check if url responds
        fields["s3_file_url"] = model_info.s3_file_url

    if model_info.framework is not None:
        fields["framework"] = model_info.framework
    else:
        raise HTTPException(
            status_code=400, detail="Missing framework in request body"
        )

    if model_info.quantization is not None:
        fields["quantization"] = model_info.quantization
    else:
        raise HTTPException(
            status_code=400, detail="Missing quantization in request body"
        )

    if model_info.from_onspecta is not None:
        fields["from_onspecta"] = model_info.from_onspecta
    else:
        raise HTTPException(
            status_code=400, detail="Missing from_onspecta in request body"
        )

    if model_info.domain is None:
        raise HTTPException(
            status_code=400, detail="Missing domain in request body"
        )

    if model_info.task is None:
        raise HTTPException(
            status_code=400, detail="Missing task in request body"
        )

    if (
        settings.is_domain_task_supported(model_info.domain, model_info.task)
        == False
    ):
        raise HTTPException(status_code=400, detail="Domain/task not supported")

    fields["domain"] = model_info.domain
    fields["task"] = model_info.task

    if model_info.channels is not None:
        fields["channels"] = model_info.channels
    else:
        if model_info.domain == "Computer Vision":
            raise HTTPException(
                status_code=400,
                detail="Missing channels for Computer Vision network",
            )

    if model_info.height is not None:
        fields["height"] = model_info.height
    else:
        if model_info.domain == "Computer Vision":
            raise HTTPException(
                status_code=400,
                detail="Missing height for Computer Vision network",
            )

    if model_info.width is not None:
        fields["width"] = model_info.width
    else:
        if model_info.domain == "Computer Vision":
            raise HTTPException(
                status_code=400,
                detail="Missing width for Computer Vision network",
            )

    if model_info.batch_size is not None:
        fields["batch_size"] = model_info.batch_size
    else:
        raise HTTPException(
            status_code=400, detail="Missing batch_size in rquest body"
        )

    if len(fields) != 0:
        mlmodel_model.update(model_id, **fields)
    return {"model_id": model_id}


# Delete model entry
@router.delete(lab_api_base + "/model")
async def delete_model(model_id: int):
    mlmodel_model.delete(model_id)
    return {"message": "Deleted", "model_id": model_id}


# Upload model file
@router.put(lab_api_base + "/model/file")
async def upload_model_file(model_id: int, model_file: UploadFile = File(...)):
    mlmodel = mlmodel_model.get(model_id)
    dest_relpath = save_mlmodel_file(
        model_file.file,
        model_file.filename,
        mlmodel.from_onspecta,
        test_user_id,
        mlmodel.name,
        model_id,
    )
    fields = {"local_relpath": dest_relpath}
    mlmodel_model.update(model_id, **fields)
    return {
        "message": "uploaded file",
        "model_relpath": dest_relpath,
        "model_id": model_id,
    }


@router.put(lab_api_base + "/model/file/chunk")
async def upload_model_file_chunk(
    model_id: int, chunk: int, total: int, model_file: UploadFile = File(...)
):
    mlmodel = mlmodel_model.get(model_id)
    save_mlmodel_file(
        model_file.file,
        model_file.filename,
        mlmodel.from_onspecta,
        test_user_id,
        mlmodel.name,
        model_id,
        chunk,
    )
    dest_relpath = check_if_all_chunks(
        model_file.filename,
        mlmodel.from_onspecta,
        test_user_id,
        mlmodel.name,
        model_id,
        total,
    )
    if dest_relpath is not None:
        fields = {"local_relpath": dest_relpath}
        mlmodel_model.update(model_id, **fields)
    return {"message": "uploaded chunk", "model_id": model_id}


# Update model information
@router.put(lab_api_base + "/model/info")
async def update_model_info(model_id: int, model_info: UpdateModelInfo):
    print("Update model info {}".format(model_info))
    fields = {}
    if model_info.name is not None:
        fields["name"] = model_info.name
    if model_info.s3_file_url is not None:
        fields["s3_file_url"] = model_info.s3_file_url
    if model_info.domain is not None:
        fields["domain"] = model_info.domain
    if model_info.task is not None:
        fields["task"] = model_info.task
    if model_info.channels is not None:
        fields["channels"] = model_info.channels
    if model_info.height is not None:
        fields["height"] = model_info.height
    if model_info.width is not None:
        fields["width"] = model_info.width
    if model_info.batch_size is not None:
        fields["batch_size"] = model_info.batch_size
    if len(fields) != 0:
        mlmodel_model.update(model_id, **fields)

    if (model_info.top1 is not None) or (model_info.top5 is not None):
        mlmodel_model.add_or_update_accuracy(
            model_id, model_info.top1, model_info.top5
        )

    return {"message": "Model info updated", "model_id": model_id}


@router.post(lab_api_base + "/model_prediction")
async def get_prediction(model_id: int, input_file: UploadFile = File(...)):
    model = mlmodel_model.get(model_id)
    input = np.load(input_file.file)
    print(input)
    print(
        autodl.loadModel(workdir + model.local_relpath)(torch.from_numpy(input))
    )


@router.get(lab_api_base + "/model/info")
async def get_model_info(model_id: int):
    model = mlmodel_model.get(model_id)
    model_info = {}
    model_info["id"] = model.id
    model_info["name"] = model.name
    model_info["s3_file_url"] = model.s3_file_url
    model_info["framework"] = model.framework
    model_info["accuracy"] = model.accuracy
    model_info["quantization"] = model.quantization
    model_info["domain"] = model.domain
    model_info["task"] = model.task
    model_info["channels"] = model.channels
    model_info["height"] = model.height
    model_info["width"] = model.width
    model_info["batch_size"] = model.batch_size
    print("Get model info {}".format(model_info))

    return {"message": "Get Model Info", "model_info": model_info}


# Tag model
@router.put(lab_api_base + "/model/tags")
async def add_tags(model_id: int, tags: List[str]):
    print("Add tags {}".format(tags))
    for tag in tags:
        mlmodel_model.add_tag(model_id, tag)
    return {"message": "Tags added", "model_id": model_id}


def fake_data_generator(model, model_id, threads, enable_dls, hw):
    bs = model.batch_size
    print("Generating fake data")
    for provider in settings.cloud_instances:
        for instance in provider["instance_types"]:
            instance_config = get_instance_config(
                model, model_id, threads, enable_dls, hw, provider, instance
            )

            if instance_config is None:
                continue

            run_threads = instance_config

            latency = (100.0 / run_threads) * 1.3  # Fake data
            throughput = (1000.0 / latency) * bs
            print("throughput: {} bs {}".format(throughput, bs))
            mlmodel_model.add_or_update_metrics(
                model_id,
                run_threads,
                enable_dls,
                instance["hw"],
                latency,
                throughput,
            )


def perform_estimation(model_id, threads, enable_dls, hw):
    model = mlmodel_model.get(model_id)

    def raiseError(message):
        raise HTTPException(status_code=400, detail=message)

    def update(
        model_id,
        pred_cnt,
        total,
        run_threads,
        enable_dls,
        hw,
        latency,
        throughput,
    ):
        mlmodel_model.add_or_update_metrics(
            model_id,
            run_threads,
            enable_dls,
            instance["hw"],
            latency,
            throughput,
        )

    width = model.width
    height = model.height
    channels = model.channels
    bs = model.batch_size
    quantization = model.quantization
    model_params = [
        model_id,
        model.framework,
        workdir + model.local_relpath,
        width,
        height,
        channels,
        quantization,
        bs,
    ]
    try:
        __perform_estimation(
            model_params, threads, enable_dls, hw, raiseError, update
        )
    except:
        print(traceback.format_exc())
        fake_data_generator(model, model_id, threads, enable_dls, hw)


def render_instance_estimations(metrics):
    instance_estimations = []
    for entry in metrics:
        instances_list = settings.find_instances_with_config(
            entry["hw"], entry["num_threads"]
        )
        if len(instances_list) > 0:
            for instance in instances_list:
                instance_metrics = {}
                instance_metrics["service_provider"] = instance[0]
                instance_metrics["instance_type"] = instance[1]
                instance_metrics["hw"] = entry["hw"]
                instance_metrics["num_threads"] = entry["num_threads"]
                instance_metrics["batch_size"] = entry["batch_size"]
                instance_metrics["latency"] = entry["latency"]
                instance_metrics["throughput"] = entry["throughput"]
                usd_per_hr = instance[2]
                instance_metrics["cost_performance"] = (
                    entry["throughput"] * 60 * 60
                ) / usd_per_hr
                instance_estimations.append(instance_metrics)

    return instance_estimations


# Get predictor estimation result
@router.get(lab_api_base + "/model/estimation")
async def get_estimation(
    model_id: str,
    threads: Optional[int] = None,
    hw: Optional[str] = None,
    enable_dls: Optional[bool] = False,
    force: Optional[bool] = False,
):

    # Retrieve estimation from database if available
    if force == True:
        perform_estimation(model_id, threads, enable_dls, hw)

    result = mlmodel_model.get_metrics(model_id)
    # If there is no metrics entry on system, do analysis
    if len(result) == 0:
        perform_estimation(model_id, threads, enable_dls, hw)
        result = mlmodel_model.get_metrics(model_id)

    instance_estimations = render_instance_estimations(result)

    return {
        "message": "Estimation",
        "model_id": model_id,
        "estimation": instance_estimations,
    }


def on_update_message(data):
    print("==================== Update progress ======================")
    print(data["result"])
    result = json.loads(data["result"])


def schedule_new_estimation_task(model, threads, enable_dls, hw):
    model_filepath = mlmodel_model.get_model_filepath(model)
    if os.path.exists(model_filepath) == False:
        raise HTTPException(status_code=400, detail="Model file not found")

    width = model.width
    height = model.height
    channels = model.channels
    bs = model.batch_size
    task = estimation_task.apply_async(
        args=(
            model.id,
            model.framework,
            model_filepath,
            model.width,
            model.height,
            model.channels,
            model.quantization,
            model.batch_size,
            threads,
            enable_dls,
            hw,
        )
    )
    fields = {}
    fields["perf_task_id"] = task.id
    mlmodel_model.update(model.id, **fields)

    return task


# Get predictor estimation result (Async)
@router.get(lab_api_base + "/model/async_estimation")
async def get_async_estimation(
    model_id: str,
    threads: Optional[int] = None,
    hw: Optional[str] = None,
    enable_dls: Optional[bool] = False,
    force: Optional[bool] = False,
):

    model = mlmodel_model.get(model_id)
    create_new_task = False

    if model.perf_task_id != None:
        task_result = AsyncResult(model.perf_task_id)
        print("--- task_result", task_result)
        if task_result.status != "PROGRESS":
            if task_result.status == "SUCCESS":
                for estimation in task_result.result["estimations"]:
                    mlmodel_model.add_or_update_metrics(
                        model_id,
                        estimation[0],
                        estimation[1],
                        estimation[2],
                        estimation[3],
                        estimation[4],
                    )
            else:
                raise "Unhandled task status attained: {}".format(
                    task_result.status
                )

            if force == True:
                # To force create new performance estimation task, clear the task id in DB first
                fields = {}
                fields["perf_task_id"] = None
                mlmodel_model.update(model_id, **fields)
                create_new_task = True

        if create_new_task == False:
            print("==== task_result {}".format(task_result))
            print("==== task_result.result {}".format(task_result.result))
            current = task_result.result["current"]
            total = task_result.result["total"]

            result = mlmodel_model.get_metrics(model_id)
            instance_estimations = render_instance_estimations(result)

            return JSONResponse(
                {
                    "model_id": model_id,
                    "task_id": model.perf_task_id,
                    "task_status": task_result.status,
                    "task_progress": 100 * current // total,
                    # "task_result":task_result.result,
                    "model_estimations": instance_estimations,
                }
            )
    elif force is False:
        metrics = mlmodel_model.get_metrics(model_id)
        if len(metrics) > 0:
            instance_estimations = render_instance_estimations(metrics)

            return JSONResponse(
                {
                    "model_id": model_id,
                    "model_estimations": instance_estimations,
                }
            )

    # Schedule new perf task if task is not completed or in progress
    task = schedule_new_estimation_task(model, threads, enable_dls, hw)

    return {
        "message": "Async Estimation",
        "model_id": model_id,
        "task_id": task.id,
    }


@router.get(lab_api_base + "/supported_hardwares")
async def get_procs():
    return {
        "message": "Get hardware supported",
        "hardware": settings.supported_hardwares,
    }


@router.get(lab_api_base + "/supported_frameworks")
async def get_frameworks():
    return {
        "message": "Get ML frameworks supported",
        "frameworks": settings.supported_frameworks,
    }


@router.get(lab_api_base + "/supported_quants")
async def get_quants():
    return {
        "message": "Get Quantizations modes supported",
        "quants": settings.supported_quants,
    }


@router.get(lab_api_base + "/supported_domains")
async def get_domains():
    return {
        "message": "Get domains and tasks supported",
        "domains": settings.supported_domains,
    }


@router.post(lab_api_base + "/test_worker", status_code=201)
async def run_task():
    task = create_task.delay(3)
    task_result = AsyncResult(task.id)
    return JSONResponse(
        {
            "task_id": task.id,
            "task_status": task_result.status,
            "task_result": task_result.result,
        }
    )


@router.get(lab_api_base + "/check_task")
async def check_task(task_id: str):
    task_result = AsyncResult(task_id)
    return JSONResponse(
        {
            "task_id": task_id,
            "task_status": task_result.status,
            "task_result": task_result.result,
        }
    )
