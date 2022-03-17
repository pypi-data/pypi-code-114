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

from flywheel.models.origin import Origin  # noqa: F401,E501

# NOTE: This file is auto generated by the swagger code generator program.
# Do not edit the class manually.


class Provider(object):

    swagger_types = {
        'id': 'str',
        'provider_class': 'str',
        'provider_type': 'str',
        'label': 'str',
        'origin': 'Origin',
        'created': 'datetime',
        'modified': 'datetime',
        'config': 'object',
        'creds': 'object'
    }

    attribute_map = {
        'id': '_id',
        'provider_class': 'provider_class',
        'provider_type': 'provider_type',
        'label': 'label',
        'origin': 'origin',
        'created': 'created',
        'modified': 'modified',
        'config': 'config',
        'creds': 'creds'
    }

    rattribute_map = {
        '_id': 'id',
        'provider_class': 'provider_class',
        'provider_type': 'provider_type',
        'label': 'label',
        'origin': 'origin',
        'created': 'created',
        'modified': 'modified',
        'config': 'config',
        'creds': 'creds'
    }

    def __init__(self, id=None, provider_class=None, provider_type=None, label=None, origin=None, created=None, modified=None, config=None, creds=None):  # noqa: E501
        """Provider - a model defined in Swagger"""
        super(Provider, self).__init__()

        self._id = None
        self._provider_class = None
        self._provider_type = None
        self._label = None
        self._origin = None
        self._created = None
        self._modified = None
        self._config = None
        self._creds = None
        self.discriminator = None
        self.alt_discriminator = None

        if id is not None:
            self.id = id
        if provider_class is not None:
            self.provider_class = provider_class
        if provider_type is not None:
            self.provider_type = provider_type
        if label is not None:
            self.label = label
        if origin is not None:
            self.origin = origin
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified
        if config is not None:
            self.config = config
        if creds is not None:
            self.creds = creds

    @property
    def id(self):
        """Gets the id of this Provider.

        Unique database ID

        :return: The id of this Provider.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Provider.

        Unique database ID

        :param id: The id of this Provider.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def provider_class(self):
        """Gets the provider_class of this Provider.

        The provider class - one of compute or storage

        :return: The provider_class of this Provider.
        :rtype: str
        """
        return self._provider_class

    @provider_class.setter
    def provider_class(self, provider_class):
        """Sets the provider_class of this Provider.

        The provider class - one of compute or storage

        :param provider_class: The provider_class of this Provider.  # noqa: E501
        :type: str
        """

        self._provider_class = provider_class

    @property
    def provider_type(self):
        """Gets the provider_type of this Provider.

        The provider type (e.g. static or gcloud)

        :return: The provider_type of this Provider.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this Provider.

        The provider type (e.g. static or gcloud)

        :param provider_type: The provider_type of this Provider.  # noqa: E501
        :type: str
        """

        self._provider_type = provider_type

    @property
    def label(self):
        """Gets the label of this Provider.

        A human readable label for the provider

        :return: The label of this Provider.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Provider.

        A human readable label for the provider

        :param label: The label of this Provider.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def origin(self):
        """Gets the origin of this Provider.


        :return: The origin of this Provider.
        :rtype: Origin
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this Provider.


        :param origin: The origin of this Provider.  # noqa: E501
        :type: Origin
        """

        self._origin = origin

    @property
    def created(self):
        """Gets the created of this Provider.

        Creation time (automatically set)

        :return: The created of this Provider.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Provider.

        Creation time (automatically set)

        :param created: The created of this Provider.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this Provider.

        Last modification time (automatically updated)

        :return: The modified of this Provider.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this Provider.

        Last modification time (automatically updated)

        :param modified: The modified of this Provider.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def config(self):
        """Gets the config of this Provider.

        The provider-specific configuration fields.

        :return: The config of this Provider.
        :rtype: object
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this Provider.

        The provider-specific configuration fields.

        :param config: The config of this Provider.  # noqa: E501
        :type: object
        """

        self._config = config

    @property
    def creds(self):
        """Gets the creds of this Provider.

        The provider-specific credential fields.

        :return: The creds of this Provider.
        :rtype: object
        """
        return self._creds

    @creds.setter
    def creds(self, creds):
        """Sets the creds of this Provider.

        The provider-specific credential fields.

        :param creds: The creds of this Provider.  # noqa: E501
        :type: object
        """

        self._creds = creds


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
        if not isinstance(other, Provider):
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
