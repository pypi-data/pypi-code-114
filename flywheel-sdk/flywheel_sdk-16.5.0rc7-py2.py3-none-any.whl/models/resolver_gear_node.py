# coding: utf-8

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


## NOTE: This file is auto generated by the swagger code generator program.
## Do not edit the file manually.

import pprint
import re  # noqa: F401

import six

from flywheel.models.gear import Gear  # noqa: F401,E501
from flywheel.models.gear_doc import GearDoc  # noqa: F401,E501
from flywheel.models.gear_exchange import GearExchange  # noqa: F401,E501
from flywheel.models.resolver_node import ResolverNode  # noqa: F401,E501

# NOTE: This file is auto generated by the swagger code generator program.
# Do not edit the class manually.

from .mixins import GearMixin

class ResolverGearNode(GearMixin):

    swagger_types = {
        'id': 'str',
        'category': 'str',
        'gear': 'Gear',
        'exchange': 'GearExchange',
        'created': 'datetime',
        'modified': 'datetime',
        'disabled': 'datetime'
    }

    attribute_map = {
        'id': '_id',
        'category': 'category',
        'gear': 'gear',
        'exchange': 'exchange',
        'created': 'created',
        'modified': 'modified',
        'disabled': 'disabled'
    }

    rattribute_map = {
        '_id': 'id',
        'category': 'category',
        'gear': 'gear',
        'exchange': 'exchange',
        'created': 'created',
        'modified': 'modified',
        'disabled': 'disabled'
    }

    def __init__(self, id=None, category=None, gear=None, exchange=None, created=None, modified=None, disabled=None):  # noqa: E501
        """ResolverGearNode - a model defined in Swagger"""
        super(ResolverGearNode, self).__init__()

        self._id = None
        self._category = None
        self._gear = None
        self._exchange = None
        self._created = None
        self._modified = None
        self._disabled = None
        self.discriminator = None
        self.alt_discriminator = None

        if id is not None:
            self.id = id
        self.category = category
        if gear is not None:
            self.gear = gear
        if exchange is not None:
            self.exchange = exchange
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified
        if disabled is not None:
            self.disabled = disabled

    @property
    def id(self):
        """Gets the id of this ResolverGearNode.

        Unique database ID

        :return: The id of this ResolverGearNode.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResolverGearNode.

        Unique database ID

        :param id: The id of this ResolverGearNode.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def category(self):
        """Gets the category of this ResolverGearNode.

        The gear category

        :return: The category of this ResolverGearNode.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ResolverGearNode.

        The gear category

        :param category: The category of this ResolverGearNode.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def gear(self):
        """Gets the gear of this ResolverGearNode.


        :return: The gear of this ResolverGearNode.
        :rtype: Gear
        """
        return self._gear

    @gear.setter
    def gear(self, gear):
        """Sets the gear of this ResolverGearNode.


        :param gear: The gear of this ResolverGearNode.  # noqa: E501
        :type: Gear
        """

        self._gear = gear

    @property
    def exchange(self):
        """Gets the exchange of this ResolverGearNode.


        :return: The exchange of this ResolverGearNode.
        :rtype: GearExchange
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this ResolverGearNode.


        :param exchange: The exchange of this ResolverGearNode.  # noqa: E501
        :type: GearExchange
        """

        self._exchange = exchange

    @property
    def created(self):
        """Gets the created of this ResolverGearNode.

        Creation time (automatically set)

        :return: The created of this ResolverGearNode.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ResolverGearNode.

        Creation time (automatically set)

        :param created: The created of this ResolverGearNode.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this ResolverGearNode.

        Last modification time (automatically updated)

        :return: The modified of this ResolverGearNode.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this ResolverGearNode.

        Last modification time (automatically updated)

        :param modified: The modified of this ResolverGearNode.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def disabled(self):
        """Gets the disabled of this ResolverGearNode.

        The time the gear was disabled (automatically set)

        :return: The disabled of this ResolverGearNode.
        :rtype: datetime
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this ResolverGearNode.

        The time the gear was disabled (automatically set)

        :param disabled: The disabled of this ResolverGearNode.  # noqa: E501
        :type: datetime
        """

        self._disabled = disabled


    @staticmethod
    def positional_to_model(value):
        """Converts a positional argument to a model value"""
        return value

    def return_value(self):
        """Unwraps return value from model"""
        return self

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResolverGearNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

    # Container emulation
    def __getitem__(self, key):
        """Returns the value of key"""
        key = self._map_key(key)
        return getattr(self, key)

    def __setitem__(self, key, value):
        """Sets the value of key"""
        key = self._map_key(key)
        setattr(self, key, value)

    def __contains__(self, key):
        """Checks if the given value is a key in this object"""
        key = self._map_key(key, raise_on_error=False)
        return key is not None

    def keys(self):
        """Returns the list of json properties in the object"""
        return self.__class__.rattribute_map.keys()

    def values(self):
        """Returns the list of values in the object"""
        for key in self.__class__.attribute_map.keys():
            yield getattr(self, key)

    def items(self):
        """Returns the list of json property to value mapping"""
        for key, prop in self.__class__.rattribute_map.items():
            yield key, getattr(self, prop)

    def get(self, key, default=None):
        """Get the value of the provided json property, or default"""
        key = self._map_key(key, raise_on_error=False)
        if key:
            return getattr(self, key, default)
        return default

    def _map_key(self, key, raise_on_error=True):
        result = self.__class__.rattribute_map.get(key)
        if result is None:
            if raise_on_error:
                raise AttributeError('Invalid attribute name: {}'.format(key))
            return None
        return '_' + result
