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


class V2beta1ResourceMetricStatus(object):
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
        'current_average_utilization': 'int',
        'current_average_value': 'str',
        'name': 'str'
    }

    attribute_map = {
        'current_average_utilization': 'currentAverageUtilization',
        'current_average_value': 'currentAverageValue',
        'name': 'name'
    }

    def __init__(self, current_average_utilization=None, current_average_value=None, name=None, local_vars_configuration=None):  # noqa: E501
        """V2beta1ResourceMetricStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._current_average_utilization = None
        self._current_average_value = None
        self._name = None
        self.discriminator = None

        if current_average_utilization is not None:
            self.current_average_utilization = current_average_utilization
        self.current_average_value = current_average_value
        self.name = name

    @property
    def current_average_utilization(self):
        """Gets the current_average_utilization of this V2beta1ResourceMetricStatus.  # noqa: E501

        currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.  It will only be present if `targetAverageValue` was set in the corresponding metric specification.  # noqa: E501

        :return: The current_average_utilization of this V2beta1ResourceMetricStatus.  # noqa: E501
        :rtype: int
        """
        return self._current_average_utilization

    @current_average_utilization.setter
    def current_average_utilization(self, current_average_utilization):
        """Sets the current_average_utilization of this V2beta1ResourceMetricStatus.

        currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.  It will only be present if `targetAverageValue` was set in the corresponding metric specification.  # noqa: E501

        :param current_average_utilization: The current_average_utilization of this V2beta1ResourceMetricStatus.  # noqa: E501
        :type current_average_utilization: int
        """

        self._current_average_utilization = current_average_utilization

    @property
    def current_average_value(self):
        """Gets the current_average_value of this V2beta1ResourceMetricStatus.  # noqa: E501

        currentAverageValue is the current value of the average of the resource metric across all relevant pods, as a raw value (instead of as a percentage of the request), similar to the \"pods\" metric source type. It will always be set, regardless of the corresponding metric specification.  # noqa: E501

        :return: The current_average_value of this V2beta1ResourceMetricStatus.  # noqa: E501
        :rtype: str
        """
        return self._current_average_value

    @current_average_value.setter
    def current_average_value(self, current_average_value):
        """Sets the current_average_value of this V2beta1ResourceMetricStatus.

        currentAverageValue is the current value of the average of the resource metric across all relevant pods, as a raw value (instead of as a percentage of the request), similar to the \"pods\" metric source type. It will always be set, regardless of the corresponding metric specification.  # noqa: E501

        :param current_average_value: The current_average_value of this V2beta1ResourceMetricStatus.  # noqa: E501
        :type current_average_value: str
        """
        if self.local_vars_configuration.client_side_validation and current_average_value is None:  # noqa: E501
            raise ValueError("Invalid value for `current_average_value`, must not be `None`")  # noqa: E501

        self._current_average_value = current_average_value

    @property
    def name(self):
        """Gets the name of this V2beta1ResourceMetricStatus.  # noqa: E501

        name is the name of the resource in question.  # noqa: E501

        :return: The name of this V2beta1ResourceMetricStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V2beta1ResourceMetricStatus.

        name is the name of the resource in question.  # noqa: E501

        :param name: The name of this V2beta1ResourceMetricStatus.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, V2beta1ResourceMetricStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V2beta1ResourceMetricStatus):
            return True

        return self.to_dict() != other.to_dict()
