# -*- coding: utf-8 -*-

# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=unused-argument

# Standard imports
import json

from pathlib import Path
from typing import Any
from urllib.parse import urlparse

# External imports
from fastapi import (
    status,
    APIRouter,
    Depends,
)
from pydantic import EmailStr  # pylint: disable=no-name-in-module
from sqlalchemy.orm import Session

# Local imports
from tanzanite.backend.app.app import (
    crud,
    models,
    schemas,
)
from tanzanite.backend.app.app.api import deps
from tanzanite.backend.app.app.core.celery_app import celery_app
from tanzanite.backend.app.app.utils import send_test_email

router = APIRouter()


@router.get(
    "/db/",
    dependencies=[Depends(deps.get_current_active_superuser)],
    response_model=schemas.Msg,
)
def db_info(db: Session = Depends(deps.get_db)):
    """
    Return metadata about the database.
    """
    # file_path =
    # db.bind.engine.url if 'sqlite' in db.bind.engine.url else "NA"
    if 'sqlite' in db.bind.engine.url:
        db_file = Path(urlparse(str(db.bind.engine.url)).path)
        exists = db_file.exists()
    else:
        db_file, exists = "NA", True
    users = crud.user.get_multi(db)
    challenges = crud.challenge.get_multi(db=db, skip=0, limit=0)
    return {
        "msg": json.dumps(
            {
                "dialect": db.bind.dialect.dialect_description,
                "db_file": str(db_file),
                "exists": exists,
                "users": len(users),
                "challenges": len(challenges),
            }
        )
    }


@router.post(
    "/test-celery/",
    response_model=schemas.Msg,
    status_code=status.HTTP_201_CREATED,
)
@celery_app.task(soft_time_limit=5)
def test_celery(
    msg: schemas.Msg,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Test Celery worker.
    """
    celery_app.send_task("app.worker.test_celery", args=[msg.msg])
    return {"msg": "Word received"}


@router.post(
    "/test-email/",
    response_model=schemas.Msg,
    status_code=status.HTTP_201_CREATED,
)
def test_email(
    email_to: EmailStr,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Test emails.
    """
    send_test_email(email_to=email_to)
    return {"msg": "Test email sent"}


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
