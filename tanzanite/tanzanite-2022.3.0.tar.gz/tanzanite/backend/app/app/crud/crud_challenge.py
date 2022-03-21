# -*- coding: utf-8 -*-

# # pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use


from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy import or_
from sqlalchemy.orm import Session

from tanzanite.backend.app.app.crud.base import CRUDBase
from tanzanite.backend.app.app import (
    models,
    schemas,
)


class CRUDChallenge(
    CRUDBase[
        models.Challenge,
        schemas.ChallengeCreate,
        schemas.ChallengeUpdate,
    ]
):
    """
    Challenge CRUD class.
    """
    def create_with_owner(
        self,
        db: Session,
        *,
        obj_in: schemas.ChallengeCreate,
        owner_id: int,
    ) -> models.Challenge:
        """
        Creates a new challenge object in the database with ownership.
        """
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self,
        db: Session,
        *,
        owner_id: int,
        skip: int = 0,
        limit: int = 0,
    ) -> List[models.Challenge]:
        """
        Gets multiple objects from the database by ownership.
        """
        if limit > 1:
            return (
                db.query(self.model)
                .filter(models.Challenge.owner_id == owner_id)
                .offset(skip)
                .limit(limit)
                .all()
            )
        else:
            return (
                db.query(self.model)
                .filter(models.Challenge.owner_id == owner_id)
                .offset(skip)
                .all()
            )

    def get_multi_by_content(
        self,
        db: Session,
        *,
        query: str,
        skip: int = 0,
        limit: int = 0,
    ) -> List[models.Challenge]:
        """
        Gets multiple objects from the database by content.

        Query searches `author`, `title`, and `description`.
        """
        if limit > 1:
            return (
                db.query(self.model)
                .filter(
                    or_(
                        models.Challenge.author.contains(query),
                        models.Challenge.title.contains(query),
                        models.Challenge.description.contains(query),
                    )
                )
                .offset(skip)
                .limit(limit)
                .all()
            )
        else:
            return (
                db.query(self.model)
                .filter(
                    or_(
                        models.Challenge.author.contains(query),
                        models.Challenge.title.contains(query),
                        models.Challenge.description.contains(query),
                    )
                )
                .offset(skip)
                .all()
            )


challenge = CRUDChallenge(models.Challenge)


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
