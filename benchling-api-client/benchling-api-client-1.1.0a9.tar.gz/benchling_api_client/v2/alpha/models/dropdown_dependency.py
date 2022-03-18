from typing import Any, cast, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..extensions import NotPresentError
from ..models.base_manifest_config import BaseManifestConfig
from ..models.dropdown_dependency_types import DropdownDependencyTypes
from ..types import UNSET, Unset

T = TypeVar("T", bound="DropdownDependency")


@attr.s(auto_attribs=True, repr=False)
class DropdownDependency:
    """  """

    _options: Union[Unset, List[BaseManifestConfig]] = UNSET
    _type: Union[Unset, DropdownDependencyTypes] = UNSET
    _description: Union[Unset, None, str] = UNSET
    _name: Union[Unset, str] = UNSET

    def __repr__(self):
        fields = []
        fields.append("options={}".format(repr(self._options)))
        fields.append("type={}".format(repr(self._type)))
        fields.append("description={}".format(repr(self._description)))
        fields.append("name={}".format(repr(self._name)))
        return "DropdownDependency({})".format(", ".join(fields))

    def to_dict(self) -> Dict[str, Any]:
        options: Union[Unset, List[Any]] = UNSET
        if not isinstance(self._options, Unset):
            options = []
            for options_item_data in self._options:
                options_item = options_item_data.to_dict()

                options.append(options_item)

        type: Union[Unset, int] = UNSET
        if not isinstance(self._type, Unset):
            type = self._type.value

        description = self._description
        name = self._name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if options is not UNSET:
            field_dict["options"] = options
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

        def get_options() -> Union[Unset, List[BaseManifestConfig]]:
            options = []
            _options = d.pop("options")
            for options_item_data in _options or []:
                options_item = BaseManifestConfig.from_dict(options_item_data)

                options.append(options_item)

            return options

        options = get_options() if "options" in d else cast(Union[Unset, List[BaseManifestConfig]], UNSET)

        def get_type() -> Union[Unset, DropdownDependencyTypes]:
            type = None
            _type = d.pop("type")
            if _type is not None and _type is not UNSET:
                try:
                    type = DropdownDependencyTypes(_type)
                except ValueError:
                    type = DropdownDependencyTypes.of_unknown(_type)

            return type

        type = get_type() if "type" in d else cast(Union[Unset, DropdownDependencyTypes], UNSET)

        def get_description() -> Union[Unset, None, str]:
            description = d.pop("description")
            return description

        description = get_description() if "description" in d else cast(Union[Unset, None, str], UNSET)

        def get_name() -> Union[Unset, str]:
            name = d.pop("name")
            return name

        name = get_name() if "name" in d else cast(Union[Unset, str], UNSET)

        dropdown_dependency = cls(
            options=options,
            type=type,
            description=description,
            name=name,
        )

        return dropdown_dependency

    @property
    def options(self) -> List[BaseManifestConfig]:
        if isinstance(self._options, Unset):
            raise NotPresentError(self, "options")
        return self._options

    @options.setter
    def options(self, value: List[BaseManifestConfig]) -> None:
        self._options = value

    @options.deleter
    def options(self) -> None:
        self._options = UNSET

    @property
    def type(self) -> DropdownDependencyTypes:
        if isinstance(self._type, Unset):
            raise NotPresentError(self, "type")
        return self._type

    @type.setter
    def type(self, value: DropdownDependencyTypes) -> None:
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
