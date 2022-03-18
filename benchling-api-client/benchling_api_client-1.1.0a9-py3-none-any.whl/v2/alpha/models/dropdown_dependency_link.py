from typing import Any, cast, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..extensions import NotPresentError
from ..models.dropdown_dependency_types import DropdownDependencyTypes
from ..models.subdependency_link import SubdependencyLink
from ..types import UNSET, Unset

T = TypeVar("T", bound="DropdownDependencyLink")


@attr.s(auto_attribs=True, repr=False)
class DropdownDependencyLink:
    """  """

    _options: Union[Unset, List[SubdependencyLink]] = UNSET
    _type: Union[Unset, DropdownDependencyTypes] = UNSET
    _api_url: Union[Unset, None, str] = UNSET
    _description: Union[Unset, None, str] = UNSET
    _name: Union[Unset, None, str] = UNSET
    _resource_id: Union[Unset, str] = UNSET
    _resource_name: Union[Unset, None, str] = UNSET

    def __repr__(self):
        fields = []
        fields.append("options={}".format(repr(self._options)))
        fields.append("type={}".format(repr(self._type)))
        fields.append("api_url={}".format(repr(self._api_url)))
        fields.append("description={}".format(repr(self._description)))
        fields.append("name={}".format(repr(self._name)))
        fields.append("resource_id={}".format(repr(self._resource_id)))
        fields.append("resource_name={}".format(repr(self._resource_name)))
        return "DropdownDependencyLink({})".format(", ".join(fields))

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

        api_url = self._api_url
        description = self._description
        name = self._name
        resource_id = self._resource_id
        resource_name = self._resource_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if options is not UNSET:
            field_dict["options"] = options
        if type is not UNSET:
            field_dict["type"] = type
        if api_url is not UNSET:
            field_dict["apiURL"] = api_url
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if resource_name is not UNSET:
            field_dict["resourceName"] = resource_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def get_options() -> Union[Unset, List[SubdependencyLink]]:
            options = []
            _options = d.pop("options")
            for options_item_data in _options or []:
                options_item = SubdependencyLink.from_dict(options_item_data)

                options.append(options_item)

            return options

        options = get_options() if "options" in d else cast(Union[Unset, List[SubdependencyLink]], UNSET)

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

        def get_api_url() -> Union[Unset, None, str]:
            api_url = d.pop("apiURL")
            return api_url

        api_url = get_api_url() if "apiURL" in d else cast(Union[Unset, None, str], UNSET)

        def get_description() -> Union[Unset, None, str]:
            description = d.pop("description")
            return description

        description = get_description() if "description" in d else cast(Union[Unset, None, str], UNSET)

        def get_name() -> Union[Unset, None, str]:
            name = d.pop("name")
            return name

        name = get_name() if "name" in d else cast(Union[Unset, None, str], UNSET)

        def get_resource_id() -> Union[Unset, str]:
            resource_id = d.pop("resourceId")
            return resource_id

        resource_id = get_resource_id() if "resourceId" in d else cast(Union[Unset, str], UNSET)

        def get_resource_name() -> Union[Unset, None, str]:
            resource_name = d.pop("resourceName")
            return resource_name

        resource_name = get_resource_name() if "resourceName" in d else cast(Union[Unset, None, str], UNSET)

        dropdown_dependency_link = cls(
            options=options,
            type=type,
            api_url=api_url,
            description=description,
            name=name,
            resource_id=resource_id,
            resource_name=resource_name,
        )

        return dropdown_dependency_link

    @property
    def options(self) -> List[SubdependencyLink]:
        if isinstance(self._options, Unset):
            raise NotPresentError(self, "options")
        return self._options

    @options.setter
    def options(self, value: List[SubdependencyLink]) -> None:
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
    def api_url(self) -> Optional[str]:
        if isinstance(self._api_url, Unset):
            raise NotPresentError(self, "api_url")
        return self._api_url

    @api_url.setter
    def api_url(self, value: Optional[str]) -> None:
        self._api_url = value

    @api_url.deleter
    def api_url(self) -> None:
        self._api_url = UNSET

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
    def name(self) -> Optional[str]:
        if isinstance(self._name, Unset):
            raise NotPresentError(self, "name")
        return self._name

    @name.setter
    def name(self, value: Optional[str]) -> None:
        self._name = value

    @name.deleter
    def name(self) -> None:
        self._name = UNSET

    @property
    def resource_id(self) -> str:
        if isinstance(self._resource_id, Unset):
            raise NotPresentError(self, "resource_id")
        return self._resource_id

    @resource_id.setter
    def resource_id(self, value: str) -> None:
        self._resource_id = value

    @resource_id.deleter
    def resource_id(self) -> None:
        self._resource_id = UNSET

    @property
    def resource_name(self) -> Optional[str]:
        if isinstance(self._resource_name, Unset):
            raise NotPresentError(self, "resource_name")
        return self._resource_name

    @resource_name.setter
    def resource_name(self, value: Optional[str]) -> None:
        self._resource_name = value

    @resource_name.deleter
    def resource_name(self) -> None:
        self._resource_name = UNSET
