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


class V2beta2MetricValueStatus(object):
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
        'average_utilization': 'int',
        'average_value': 'str',
        'value': 'str'
    }

    attribute_map = {
        'average_utilization': 'averageUtilization',
        'average_value': 'averageValue',
        'value': 'value'
    }

    def __init__(self, average_utilization=None, average_value=None, value=None, local_vars_configuration=None):  # noqa: E501
        """V2beta2MetricValueStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._average_utilization = None
        self._average_value = None
        self._value = None
        self.discriminator = None

        if average_utilization is not None:
            self.average_utilization = average_utilization
        if average_value is not None:
            self.average_value = average_value
        if value is not None:
            self.value = value

    @property
    def average_utilization(self):
        """Gets the average_utilization of this V2beta2MetricValueStatus.  # noqa: E501

        currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.  # noqa: E501

        :return: The average_utilization of this V2beta2MetricValueStatus.  # noqa: E501
        :rtype: int
        """
        return self._average_utilization

    @average_utilization.setter
    def average_utilization(self, average_utilization):
        """Sets the average_utilization of this V2beta2MetricValueStatus.

        currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.  # noqa: E501

        :param average_utilization: The average_utilization of this V2beta2MetricValueStatus.  # noqa: E501
        :type average_utilization: int
        """

        self._average_utilization = average_utilization

    @property
    def average_value(self):
        """Gets the average_value of this V2beta2MetricValueStatus.  # noqa: E501

        averageValue is the current value of the average of the metric across all relevant pods (as a quantity)  # noqa: E501

        :return: The average_value of this V2beta2MetricValueStatus.  # noqa: E501
        :rtype: str
        """
        return self._average_value

    @average_value.setter
    def average_value(self, average_value):
        """Sets the average_value of this V2beta2MetricValueStatus.

        averageValue is the current value of the average of the metric across all relevant pods (as a quantity)  # noqa: E501

        :param average_value: The average_value of this V2beta2MetricValueStatus.  # noqa: E501
        :type average_value: str
        """

        self._average_value = average_value

    @property
    def value(self):
        """Gets the value of this V2beta2MetricValueStatus.  # noqa: E501

        value is the current value of the metric (as a quantity).  # noqa: E501

        :return: The value of this V2beta2MetricValueStatus.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this V2beta2MetricValueStatus.

        value is the current value of the metric (as a quantity).  # noqa: E501

        :param value: The value of this V2beta2MetricValueStatus.  # noqa: E501
        :type value: str
        """

        self._value = value

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
        if not isinstance(other, V2beta2MetricValueStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V2beta2MetricValueStatus):
            return True

        return self.to_dict() != other.to_dict()
