from collections import defaultdict
from copy import deepcopy
from typing import Dict, List, Tuple

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db.models import Model, Q

from .consts import DUMP_CURRENT_VERSION, REL_MODELS_FOREIGN_KEY, REL_MODELS_REVERS_KEY
from .exceptions import ObjImportException
from ..model_versions.models import VersionedModelMixin, VersionModel, is_instance_versioned, \
    ModelWithVersionedRelations
from ..model_versions.utils.consts import REL_VERSION_FIELD_END, REL_VERSION_PATTERN_FIELD_END
from ..model_versions.utils.strings import int_arr_to_str
from ..utils.db import create_model_from_dict, get_model_field_names
from ..utils.inspect import get_class_by_name

# переопределенные модели экспортеров
importers = {}


def register(model_name):
    def register_importer(load_cls):
        global importers
        importers[model_name] = load_cls
    return register_importer


def dump_import(models_module_name, object_dump: dict, model_class, **kwargs):
    """ Загружает json модели и связанных с ней моделей в БД """
    if not object_dump:
        raise ValidationError(f'This dump is empty')

    if (dump_version := object_dump.get('dump_version')) != DUMP_CURRENT_VERSION:
        raise ValidationError(f'This version of dump {dump_version} does not support')

    class_name = model_class.__name__
    if (model_name := object_dump.get('model_name')) != class_name:
        raise ValidationError(f'The imported class "{model_name}" does not match the current "{class_name}"')

    _, _, msgs = dump_import_to_model(models_module_name, object_dump, **kwargs)
    return msgs


def get_importer(class_name):
    importer = importers.get(class_name, BaseImporter)
    return importer


def dump_import_to_model(models_module_name: str, object_dump: dict, **kwargs):
    """ Загружает json модели и связанных с ней моделей в БД """
    class_name = object_dump['model_name']
    importer = get_importer(class_name)
    instance, version_instance, msgs = importer(models_module_name, object_dump, **kwargs).model_import()
    return instance, version_instance, msgs


class BaseImporter:
    """ Базовый класс для загрузки разных видов моделей из дампа """
    unique_fields = ['name']
    ignore_fields = ('id',)  # поля, которые игнорируются при создании инстанса модели

    def __init__(self, models_module_name: str,
                 data_dump_dict: dict,
                 msgs: Dict[int, List[str]] = None,
                 is_skip_exists_version=False,
                 is_skip_exists_object=True,
                 add_unique_fields: dict = None,
                 is_second_level=False,
                 version_pattern: str = '',
                 ):
        """
            models_module_name: str - модуль с джанго-моделями (models.py)
            data_dump_dict: dict - анные для импорта
            msgs: Dict[int, List[str]] = структура куда будут складываться сообщения (логи)
            is_skip_exists_version - если True, то все существующие версии обектов не будут импортироваться
                и не будет генерироваться ошибка.
                Если False то будет выброшено исключение и импорт будет прекращен при попытке загрузить
                существующую версию.
            is_skip_exists_object - если True, то если импортруемый объект существует (указанной версии),
                он не будет импортирован. А так же все объекты, которые он содержит
            add_unique_fields: dict - дополнительные уникальные для объекта поля и их значения (как правило нужно
                для передачи свойств рекурсивно в конструктор BaseImporter
            is_second_level - объект 2-го уровня (вспомогательный параметр)
            version_pattern - версия объекта, выбранная у родителя
        """
        self.models_module_name = models_module_name
        self._data_dump = deepcopy(data_dump_dict)
        self.class_name = self._data_dump['model_name']
        self.model = get_class_by_name(self.models_module_name, self.class_name)
        self.msgs: Dict[int, List[str]] = msgs or defaultdict(list)  # {messages.INFO: [], messages.ERROR: []}
        self.is_skip_exists_version = is_skip_exists_version
        self.is_skip_exists_object = is_skip_exists_object
        self.is_versioned = issubclass(self.model, VersionedModelMixin)
        self.obj_dump = deepcopy(self._data_dump[self.class_name]['json'] if 'json' in self._data_dump[self.class_name]
                                 else self._data_dump[self.class_name])
        self.add_unique_fields = add_unique_fields or {}
        self.is_second_level = is_second_level
        self.version_pattern = version_pattern

    @property
    def _unique_fields_dict(self) -> dict:
        unique_fields_dict = {field_name: self.obj_dump[field_name] for field_name in self.unique_fields}
        unique_fields_dict.update(self.add_unique_fields)
        return unique_fields_dict

    def model_import(self) -> Tuple[Model, VersionModel, Dict[int, List[str]]]:

        if self.class_name != 'Node' and self.is_skip_exists_object and self.is_second_level:
            if instance := self.model.objects.filter(**self._unique_fields_dict).first():
                # noinspection PyUnusedLocal
                version_instance = None
                if (
                    not is_instance_versioned(instance) or
                    (version_instance := instance.get_version_by_pattern(self.version_pattern))
                ):
                    # если импорт только головных объектов и текущий обект уже существует в БД
                    # (и его версия подходит родителю, то просто вернем его)
                    return instance, version_instance, self.msgs

        # Это объекты на которые ссылается текущая сущность
        for field in self.obj_dump:
            if field.endswith(REL_VERSION_FIELD_END) and not self.obj_dump[field]:
                # по дефолту там строка. нужно None поставить
                self.obj_dump[field] = None

        # по foreignkey - одна связь. Ссылку на объект нужно записать в основную модель.
        for rel_name, rel_instance_dict in self._data_dump.get(REL_MODELS_FOREIGN_KEY, {}).items():

            if self.is_skip_exists_object:
                # нужно чтобы зависимый объект подтянулся с calculated версией
                version_pattern = (self.obj_dump.get(f'{rel_name}{REL_VERSION_FIELD_END}') or
                                   self.obj_dump.get(f'{rel_name}{REL_VERSION_PATTERN_FIELD_END}'))
            else:
                version_pattern = None

            rel_instance, rel_version_instance, self.msgs = dump_import_to_model(
                self.models_module_name, rel_instance_dict,
                msgs=self.msgs,
                is_skip_exists_version=True,
                is_skip_exists_object=self.is_skip_exists_object,
                is_second_level=True,
                version_pattern=version_pattern
            )
            self.obj_dump[f'{rel_name}'] = rel_instance

            if is_instance_versioned(rel_instance) and issubclass(self.model, ModelWithVersionedRelations):
                if rel_version_str := self.obj_dump.get(f'{rel_name}{REL_VERSION_FIELD_END}'):
                    if rel_version_str != rel_version_instance.version:
                        raise Exception(f'Импортируемая версия {rel_name}:{rel_version_str} '
                                        f'не соответствует {self.obj_dump["name"]}:{rel_version_instance.version}')
                    self.obj_dump[f'{rel_name}{REL_VERSION_FIELD_END}'] = rel_version_instance

        try:
            instance = self.model.objects.get(**self._unique_fields_dict)
        except self.model.DoesNotExist:
            instance = self._create_instance()
        else:
            # апдейтим только неверсионную модель
            if not self.is_versioned:
                # по умолчанию пропускаем существующие объекты
                if not self.is_skip_exists_object:
                    self._update_instance(instance)

        # reverse relations - много связей. Здесь объекты, которые ссылаются на текущую сущность
        for rel_name, relation_list in self._data_dump.get(REL_MODELS_REVERS_KEY, {}).items():
            if relation_list:
                rel_class_name = relation_list[0]['model_name']
                rel_importer = get_importer(rel_class_name)
                add_unique_fields = {f'{self.class_name.lower()}_id': instance.pk}

                # удалить лишние
                q = Q()
                for rel_instance_dict in relation_list:
                    q |= Q(**{fn: rel_instance_dict[rel_class_name][fn] for fn in rel_importer.unique_fields})
                q = Q(q) & Q(**{f'{self.class_name.lower()}_id': instance.pk})
                getattr(instance, rel_name).exclude(q).delete()

                for rel_instance_dict in relation_list:
                    rel_instance_dict[rel_instance_dict['model_name']][self.class_name.lower()] = instance
                    _, _, self.msgs = dump_import_to_model(
                        self.models_module_name, rel_instance_dict,
                        msgs=self.msgs,
                        is_skip_exists_version=True,
                        is_skip_exists_object=self.is_skip_exists_object,
                        add_unique_fields=add_unique_fields,
                        is_second_level=True,
                    )

        if is_instance_versioned(instance):
            # создаем версию
            version_instance = self._update_instance_and_create_version(instance)
        else:
            version_instance = None

        return instance, version_instance, self.msgs

    def _create_instance(self):
        return self._create_model_from_dict()

    def _update_instance(self, instance):
        self._update_model_from_dict(instance)

    def _update_instance_and_create_version(self, instance: VersionedModelMixin):
        """ Создает версию основной модели """
        import_ver_arr = self._data_dump[self.class_name]['version_arr']
        version_str = int_arr_to_str(import_ver_arr)

        # такая версия есть
        if version_instance := instance.versions_set.filter(version_arr=import_ver_arr).first():
            if self.is_skip_exists_version:
                return version_instance
            else:
                raise ObjImportException(
                    f'Версия "{version_str}" {self.class_name}:{str(instance)} уже существует. '
                    f'Вы можете изменить значение версии у этого объекта ("version_arr: {import_ver_arr}") '
                    f'в импортируемом файле и импортировать снова.')

        last_version = instance.last_version if instance.last_version else None
        if last_version and last_version.version_arr > import_ver_arr:
            # текущая версия больше, чем импортируемая - просто запишем версию (без сохранения основной модели)
            self._update_model_from_dict_without_save(instance)
        else:
            # noinspection PyTypeChecker
            self._update_instance(instance)

        _, version_instance = instance.create_or_update_version(version_str)
        self.msgs[messages.INFO].append(f'Создана версия "{version_str}" {self.class_name}:{str(instance)}')

        return version_instance

    def _create_model_from_dict(self):
        """ Создает экземпляр модели в БД из словаря """
        instance = create_model_from_dict(self.model, self.obj_dump, self.ignore_fields)
        self.msgs[messages.INFO].append(f'Создан объект {self.class_name} {str(instance)}')
        return instance

    def _update_model_from_dict_without_save(self, instance):
        db_field_names = set(get_model_field_names(instance.__class__))
        for field_name in db_field_names & self.obj_dump.keys():
            if field_name not in self.ignore_fields:
                setattr(instance, field_name, self.obj_dump[field_name])

    def _update_model_from_dict(self, instance):
        """ Обновляет модель данными из словаря """
        self._update_model_from_dict_without_save(instance)
        instance.save()
        self.msgs[messages.INFO].append(f'Обновлен объект {self.class_name} {str(instance)}')
