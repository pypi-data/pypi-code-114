# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.22.6
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from kubernetes_asyncio.client.configuration import Configuration


class V1Capabilities(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'add': 'list[str]',
        'drop': 'list[str]'
    }

    attribute_map = {
        'add': 'add',
        'drop': 'drop'
    }

    def __init__(self, add=None, drop=None, local_vars_configuration=None):  # noqa: E501
        """V1Capabilities - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._add = None
        self._drop = None
        self.discriminator = None

        if add is not None:
            self.add = add
        if drop is not None:
            self.drop = drop

    @property
    def add(self):
        """Gets the add of this V1Capabilities.  # noqa: E501

        Added capabilities  # noqa: E501

        :return: The add of this V1Capabilities.  # noqa: E501
        :rtype: list[str]
        """
        return self._add

    @add.setter
    def add(self, add):
        """Sets the add of this V1Capabilities.

        Added capabilities  # noqa: E501

        :param add: The add of this V1Capabilities.  # noqa: E501
        :type add: list[str]
        """

        self._add = add

    @property
    def drop(self):
        """Gets the drop of this V1Capabilities.  # noqa: E501

        Removed capabilities  # noqa: E501

        :return: The drop of this V1Capabilities.  # noqa: E501
        :rtype: list[str]
        """
        return self._drop

    @drop.setter
    def drop(self, drop):
        """Sets the drop of this V1Capabilities.

        Removed capabilities  # noqa: E501

        :param drop: The drop of this V1Capabilities.  # noqa: E501
        :type drop: list[str]
        """

        self._drop = drop

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1Capabilities):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1Capabilities):
            return True

        return self.to_dict() != other.to_dict()
