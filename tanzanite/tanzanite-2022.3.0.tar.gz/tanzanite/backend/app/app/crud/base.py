# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use


from typing import (
    Any,
    Dict,
    Generic,
    List,
    Optional,
    Type,
    TypeVar,
    Union,
)

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel  # pylint: disable=no-name-in-module
from sqlalchemy.orm import Session

from tanzanite.backend.app.app.db.base_class import Base


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        NOTE: The keyword `id` is a Python reserved built-in, so while it is OK
        to use 'id' in a database table, argparse argument, or attribute,
        it has to be `id_` when used as a variable or function parameter to avoid
        shadowing the builtin. See:
          https://stackoverflow.com/questions/77552/id-is-a-bad-variable-name-in-python

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """  # noqa
        self.model = model

    def get(
        self,
        db: Session,
        id_: Union[str, int],
    ) -> Optional[ModelType]:
        """
        Gets a single object with specified ID from the database.
        """
        return db.query(self.model).filter(self.model.id == str(id_)).first()  # noqa

    def get_multi(
        self,
        db: Session,
        *,
        skip: int = 0,
        limit: int = 0,
    ) -> List[ModelType]:
        """
        Get multiple objects from the database according to specified
        offset and limits. A limit of 0 means return all objects.
        """
        if limit > 1:
            return db.query(self.model).offset(skip).limit(limit).all()
        else:
            return db.query(self.model).offset(skip).all()

    def create(
        self,
        db: Session,
        *,
        obj_in: CreateSchemaType,
    ) -> ModelType:
        """
        Creates a new object in the database.
        """
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        """
        Updates an object in the database with new data.
        """
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(
        self,
        db: Session,
        *,
        id_: Union[str, int],
    ) -> ModelType:
        """
        Removes an object with specified ID from the database.
        """
        obj = db.query(self.model).get(str(id_))
        db.delete(obj)
        db.commit()
        return obj
