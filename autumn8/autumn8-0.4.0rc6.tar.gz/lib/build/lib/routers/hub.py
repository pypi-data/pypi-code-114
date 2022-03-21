from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi import UploadFile, File
from fastapi.responses import FileResponse
import os
import sys
import shutil
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from fastapi import Header, Query
from pathlib import Path

router = APIRouter()

sys.path.append(os.path.join(os.path.dirname(__file__), '../models'))
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import mlmodel_model

if "SVC_ROOT" in os.environ:
  workdir = os.environ["SVC_ROOT"]
else:
  workdir = str(Path.home()) + '/onspecta_svc'

hub_api_base = '/api/hub'

class NewModelInfo(BaseModel):
  name: str
  framework: str
  quantization: str

@router.get(hub_api_base + "/model/file")
async def get_model_file(model_id:int):
  mlmodel = mlmodel_model.get(model_id)
  file_path = mlmodel_model.get_model_filepath(mlmodel)
  return FileResponse(file_path)

@router.get(hub_api_base + "/models")
async def get_models(user_id:Optional[int] = None,
                     from_onspecta:Optional[bool] = False,
                     name:Optional[str] = None,
                     quantization:Optional[str] = None,
                     framework:Optional[str] = None,
                     domain:Optional[str] = None,
                     task: Optional[str] = None,
                     tags:List[str] = Query(None),
                     limit:Optional[int] = None,
                     offset:Optional[int] = None):
  mlmodels = mlmodel_model.get_models_by_filter(from_onspecta, user_id, name, framework, quantization, domain, task, tags, limit, offset)
  return ({"message": "Get list of models", "models":mlmodels})
