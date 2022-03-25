import os
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Optional

import mlmodel_model
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
from fastapi.responses import FileResponse
from pydantic import BaseModel

router = APIRouter()

sys.path.append(os.path.join(os.path.dirname(__file__), "../models"))
sys.path.append(os.path.join(os.path.dirname(__file__), "."))
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


if "SVC_ROOT" in os.environ:
    workdir = os.environ["SVC_ROOT"]
else:
    workdir = str(Path.home()) + "/onspecta_svc"

recommendations_api_base = "/api/recommendations"


@router.get(recommendations_api_base + "/best_by_task")
async def get_recommendation(
    domain: Optional[str] = None, task: Optional[str] = None
):
    best_task_models = mlmodel_model.get_models_by_filter(
        None, None, None, None, None, domain, task, None, None, None, False
    )

    return {
        "message": "Get best models for a task",
        "best_cost_performance": max(
            best_task_models, key=lambda x: (x["cost_performance"] or 0)
        ),
        "best_throughput": max(
            best_task_models, key=lambda x: (x["throughput"] or 0)
        ),
        "best_latency": min(
            best_task_models, key=lambda x: (x["latency"] or 999999)
        ),
        "best_accuracy": max(
            best_task_models, key=lambda x: (x["accuracy"] or 0)
        ),
    }


@router.get(recommendations_api_base + "/recommendations")
async def get_best_models(
    user_id: Optional[int] = None,
    domain: Optional[str] = None,
    task: Optional[str] = None,
    latency_max: Optional[float] = None,
    throughput_min: Optional[float] = None,
    cost_perf_min: Optional[int] = None,
    accuracy_min: Optional[float] = None,
):
    if latency_max == None:
        latency_max = sys.float_info.max

    if throughput_min == None:
        throughput_min = 0.0

    if cost_perf_min == None:
        cost_perf_min = 0

    if accuracy_min == None:
        accuracy_min = 0

    default_mlmodels = mlmodel_model.get_models_by_filter(
        True, -1, None, None, None, domain, task, None, None, None
    )

    user_mlmodels = []
    if user_id != None:
        user_mlmodels = mlmodel_model.get_models_by_filter(
            False, user_id, None, None, None, domain, task, None, None, None
        )

    final_models = []
    for model in default_mlmodels:
        if model["accuracy"] != None:
            if model["accuracy"] * 100 < accuracy_min:
                continue

        if model["throughput"] != None:
            if model["throughput"] < throughput_min:
                continue

        if model["latency"] != None:
            if model["latency"] > latency_max:
                continue

        if model["cost_performance"] != None:
            if model["cost_performance"] < cost_perf_min:
                continue

        final_models.append(model)

    for model in user_mlmodels:
        if model["accuracy"] != None:
            if model["accuracy"] * 100 < accuracy_min:
                continue

        if model["throughput"] != None:
            if model["throughput"] < throughput_min:
                continue

        if model["latency"] != None:
            if model["latency"] > latency_max:
                continue

        if model["cost_performance"] != None:
            if model["cost_performance"] < cost_perf_min:
                continue

        final_models.append(model)

    return {"message": "Get list of models", "models": final_models}
