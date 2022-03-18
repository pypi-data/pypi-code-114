from typing import Any, cast, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..extensions import NotPresentError
from ..models.base_manifest_config import BaseManifestConfig
from ..models.schema_dependency_types import SchemaDependencyTypes
from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemaDependency")


@attr.s(auto_attribs=True, repr=False)
class SchemaDependency:
    """  """

    _field_definitions: Union[Unset, List[BaseManifestConfig]] = UNSET
    _type: Union[Unset, SchemaDependencyTypes] = UNSET
    _description: Union[Unset, None, str] = UNSET
    _name: Union[Unset, str] = UNSET

    def __repr__(self):
        fields = []
        fields.append("field_definitions={}".format(repr(self._field_definitions)))
        fields.append("type={}".format(repr(self._type)))
        fields.append("description={}".format(repr(self._description)))
        fields.append("name={}".format(repr(self._name)))
        return "SchemaDependency({})".format(", ".join(fields))

    def to_dict(self) -> Dict[str, Any]:
        field_definitions: Union[Unset, List[Any]] = UNSET
        if not isinstance(self._field_definitions, Unset):
            field_definitions = []
            for field_definitions_item_data in self._field_definitions:
                field_definitions_item = field_definitions_item_data.to_dict()

                field_definitions.append(field_definitions_item)

        type: Union[Unset, int] = UNSET
        if not isinstance(self._type, Unset):
            type = self._type.value

        description = self._description
        name = self._name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if field_definitions is not UNSET:
            field_dict["fieldDefinitions"] = field_definitions
        if type is not UNSET:
            field_dict["type"] = type
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def get_field_definitions() -> Union[Unset, List[BaseManifestConfig]]:
            field_definitions = []
            _field_definitions = d.pop("fieldDefinitions")
            for field_definitions_item_data in _field_definitions or []:
                field_definitions_item = BaseManifestConfig.from_dict(field_definitions_item_data)

                field_definitions.append(field_definitions_item)

            return field_definitions

        field_definitions = (
            get_field_definitions()
            if "fieldDefinitions" in d
            else cast(Union[Unset, List[BaseManifestConfig]], UNSET)
        )

        def get_type() -> Union[Unset, SchemaDependencyTypes]:
            type = None
            _type = d.pop("type")
            if _type is not None and _type is not UNSET:
                try:
                    type = SchemaDependencyTypes(_type)
                except ValueError:
                    type = SchemaDependencyTypes.of_unknown(_type)

            return type

        type = get_type() if "type" in d else cast(Union[Unset, SchemaDependencyTypes], UNSET)

        def get_description() -> Union[Unset, None, str]:
            description = d.pop("description")
            return description

        description = get_description() if "description" in d else cast(Union[Unset, None, str], UNSET)

        def get_name() -> Union[Unset, str]:
            name = d.pop("name")
            return name

        name = get_name() if "name" in d else cast(Union[Unset, str], UNSET)

        schema_dependency = cls(
            field_definitions=field_definitions,
            type=type,
            description=description,
            name=name,
        )

        return schema_dependency

    @property
    def field_definitions(self) -> List[BaseManifestConfig]:
        if isinstance(self._field_definitions, Unset):
            raise NotPresentError(self, "field_definitions")
        return self._field_definitions

    @field_definitions.setter
    def field_definitions(self, value: List[BaseManifestConfig]) -> None:
        self._field_definitions = value

    @field_definitions.deleter
    def field_definitions(self) -> None:
        self._field_definitions = UNSET

    @property
    def type(self) -> SchemaDependencyTypes:
        if isinstance(self._type, Unset):
            raise NotPresentError(self, "type")
        return self._type

    @type.setter
    def type(self, value: SchemaDependencyTypes) -> None:
        self._type = value

    @type.deleter
    def type(self) -> None:
        self._type = UNSET

    @property
    def description(self) -> Optional[str]:
        if isinstance(self._description, Unset):
            raise NotPresentError(self, "description")
        return self._description

    @description.setter
    def description(self, value: Optional[str]) -> None:
        self._description = value

    @description.deleter
    def description(self) -> None:
        self._description = UNSET

    @property
    def name(self) -> str:
        if isinstance(self._name, Unset):
            raise NotPresentError(self, "name")
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @name.deleter
    def name(self) -> None:
        self._name = UNSET
