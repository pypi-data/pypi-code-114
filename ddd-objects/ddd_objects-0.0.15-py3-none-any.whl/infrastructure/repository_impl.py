from typing import List, Dict, Optional
from ..domain.repository import Repository
from ..domain.entity import Entity
from ..domain.value_obj import ValueObject, ID, Page
from ..domain.exception import (
    IDNotExistError,
    UpdateError,
    OverLimitError,
    KeyExistError
)
from .ao import AOResult, exception_class_dec

class RepositoryImpl(Repository):
    def attach(self, aggregate: Entity) -> None:
        raise NotImplementedError
    def detach(self, aggregate: Entity) -> None:
        raise NotImplementedError
    def finde_by_helper(self)-> List[Entity]:
        raise NotImplementedError
    def find_all_helper(self) -> List[Entity]:
        raise NotImplementedError
    def save_helper(self)->None:
        raise NotImplementedError
    def save_all_helper(self)->None:
        raise NotImplementedError


class SqlalchemyRepositoryImpl(RepositoryImpl):
    def __init__(
        self,
        session_cls
    ) -> None:
        self.session = session_cls()
        self.cache = {}

    def attach(self, aggregate: Entity) -> None:
        if aggregate.id is None:
            return
        else:
            self.cache[aggregate.id.get_value()] = self.get_json(aggregate)
    
    def detach(self, aggregate: Entity) -> None:
        id = aggregate.id 
        if  id is None or id.get_value() not in self.cache:
            return
        else:
            del self.cache[id.get_value()]

    def get_json(self, aggregate:Entity) -> Dict:
        d = vars(aggregate)
        return {
            key: d[key].get_value() 
                if hasattr(d[key], 'get_value') else d[key] for key in d 
                if d[key].is_changeable and d[key].get_value() is not None
        }

    @exception_class_dec()
    def find_by_id_helper(self, id: ID, do_cls)->Optional[Entity]:
        result = self.session.query(do_cls).filter(do_cls.id==id.get_value()).all()
        self.session.commit()
        return result
        # if result:
        #     return self.converter.to_entity(result[0])
        # else:
        #     return None

    @exception_class_dec()
    def find_by_helper(
        self, 
        by_name: str, 
        by: ValueObject, 
        do_cls, 
        page: Optional[Page] = None,
        # return_format=list
    )->Optional[List[Entity]]:
        if page is None:
            result = self.session.query(do_cls) \
                .filter(getattr(do_cls, by_name)==by.get_value()) \
                .all()
        else:
            result = self.session.query(do_cls) \
                .filter(getattr(do_cls, by_name)==by.get_value()) \
                .limit(page.page_size) \
                .offset(page.get_value()*page.page_size) \
                .all()
        self.session.commit()
        return result
        # result = [self.converter.to_entity(r) for r in result]
        # if result and return_format==list:
        #     return result
        # elif result:
        #     return result[0]
        # else:
        #     return None

    @exception_class_dec()
    def find_all_helper(self, do_cls) -> List[Entity]:
        result = self.session.query(do_cls).all()
        self.session.commit()
        # result = [self.converter.to_entity(r) for r in result]
        return result

    @exception_class_dec()
    def save_helper(self, x: Entity, do_cls, key_mapper={}, ignore_keys=['id']):
        """
        key_mapper: key mapper between Entity and DO, used to convert attributes name
                    format like {entity.key: dto.key}
        """
        self.check_unique_keys(x, do_cls, key_mapper, ignore_keys)
        if x.id.get_value() is None:
            x_do = self.converter.to_do(x)
            self.session.add(x_do)
        else:
            if self.find_by_id_helper(x.id, do_cls) is None:
                raise IDNotExistError(f"ID({x.id.get_value()}) doesn't exist")
            d = vars(x)
            key_mapper = {
                key: key_mapper[key] if key in key_mapper else key  for key in d 
                if d[key].get_value is not None 
            }
            x_do = self.converter.to_do(x)
            content = self.get_json(x)
            content = {
                key_mapper[key]: getattr(x_do, key_mapper[key]) for key in content
            }
            if not content:
                raise UpdateError("There's not information can be updated")
            self.session.query(do_cls) \
                .filter(do_cls.id==x.id.get_value()) \
                .update(content, synchronize_session=False)
        self.session.flush()
        self.session.commit()

    @exception_class_dec()
    def save_all_helper(self, aggregates: List[Entity], id_cls, limit=20) -> None:
        # only support insert option
        if len(aggregates)>limit:
            raise OverLimitError(f'The lenght of aritlces if over the limit({limit})')
        for i in range(len(aggregates)):
            aggregates[i].id = id_cls()
        articles_do = [self.converter.to_do(a) for a in aggregates]
        self.session.add_all(articles_do)
        self.session.commit()

    def check_unique_keys(self, x: Entity, do_cls, key_mapper={}, ignore_keys=['id']):
        d = vars(x)
        unique_keys = [
            key for key in d 
                if d[key] is not None 
                and d[key].get_value() is not None
                and d[key].is_unique and key not in ignore_keys
        ]
        key_mapper = {
            key: key_mapper[key] if key in key_mapper else key  for key in unique_keys
        }
        for key in unique_keys:
            result = self.session.query(do_cls) \
                .add_columns(do_cls.id) \
                .filter(getattr(do_cls, key_mapper[key])==d[key].get_value()) \
                .all()
            self.session.commit()
            if result:
                raise KeyExistError(f'The {key} already exists')
        return True 