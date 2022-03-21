# -*- coding: utf-8 -*-

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use


from typing import (
    Any,
    Dict,
    Optional,
    Union,
)

from sqlalchemy.orm import Session

from tanzanite.core.security import (
    get_password_hash,
    verify_password,
)
from tanzanite.backend.app.app.crud.base import CRUDBase
from tanzanite.backend.app.app import (
    models,
    schemas,
)


# pylint: disable=redefined-outer-name


class CRUDUser(
    CRUDBase[
        models.User,
        schemas.UserCreate,
        schemas.UserUpdate,
    ]
):
    """
    User CRUD class.
    """
    def get_by_email(self, db: Session, *, email: str) -> Optional[models.User]:
        """
        Return the entry from the database associated with the
        specified email address.
        """
        return db.query(models.User).filter(models.User.email == email).first()

    def get_by_id(self, db: Session, *, id_: str) -> Optional[models.User]:
        """
        Return the entry from the database associated with the
        specified id.
        """
        return db.query(models.User).filter(models.User.id == id_).first()

    def create(self, db: Session, *, obj_in: schemas.UserCreate) -> models.User:
        """
        Create a new user object in the database.
        """
        db_obj = models.User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            is_proctor=obj_in.is_proctor,
            is_superuser=obj_in.is_superuser,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, *, db_obj: models.User) -> models.User:
        """
        Delete the user entry from the database.
        """
        db.delete(db_obj)
        db.commit()
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: models.User,
        obj_in: Union[schemas.UserUpdate, Dict[str, Any]]
    ) -> models.User:
        """
        Update the user entry in the database.
        """
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        # Don't allow user to modify their own record with this method
        # or strip the initial user of superuser privilege.
        if (
            db_obj.id == 1
            and update_data.get("is_superuser") is False
        ):
            return None
        password_string = update_data.get("password")
        if password_string is not None:
            hashed_password = get_password_hash(password_string)
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(
        self,
        db: Session,
        *,
        email: str,
        password: str
    ) -> Optional[models.User]:
        """
        Authenticate a user from the password stored in the database.
        """
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def is_active(self, user: models.User) -> bool:
        """
        Return the `is_active` status of the user.
        """
        return user.is_active

    def is_proctor(self, user: models.User) -> bool:
        """
        Return the `is_proctor` status of the user.
        """
        return user.is_proctor

    def is_superuser(self, user: models.User) -> bool:
        """
        Return the `is_superuser` status of the user.
        """
        return user.is_superuser


user = CRUDUser(models.User)


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
