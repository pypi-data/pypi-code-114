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


class V1DaemonSetCondition(object):
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
        'last_transition_time': 'datetime',
        'message': 'str',
        'reason': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'last_transition_time': 'lastTransitionTime',
        'message': 'message',
        'reason': 'reason',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, last_transition_time=None, message=None, reason=None, status=None, type=None, local_vars_configuration=None):  # noqa: E501
        """V1DaemonSetCondition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._last_transition_time = None
        self._message = None
        self._reason = None
        self._status = None
        self._type = None
        self.discriminator = None

        if last_transition_time is not None:
            self.last_transition_time = last_transition_time
        if message is not None:
            self.message = message
        if reason is not None:
            self.reason = reason
        self.status = status
        self.type = type

    @property
    def last_transition_time(self):
        """Gets the last_transition_time of this V1DaemonSetCondition.  # noqa: E501

        Last time the condition transitioned from one status to another.  # noqa: E501

        :return: The last_transition_time of this V1DaemonSetCondition.  # noqa: E501
        :rtype: datetime
        """
        return self._last_transition_time

    @last_transition_time.setter
    def last_transition_time(self, last_transition_time):
        """Sets the last_transition_time of this V1DaemonSetCondition.

        Last time the condition transitioned from one status to another.  # noqa: E501

        :param last_transition_time: The last_transition_time of this V1DaemonSetCondition.  # noqa: E501
        :type last_transition_time: datetime
        """

        self._last_transition_time = last_transition_time

    @property
    def message(self):
        """Gets the message of this V1DaemonSetCondition.  # noqa: E501

        A human readable message indicating details about the transition.  # noqa: E501

        :return: The message of this V1DaemonSetCondition.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this V1DaemonSetCondition.

        A human readable message indicating details about the transition.  # noqa: E501

        :param message: The message of this V1DaemonSetCondition.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def reason(self):
        """Gets the reason of this V1DaemonSetCondition.  # noqa: E501

        The reason for the condition's last transition.  # noqa: E501

        :return: The reason of this V1DaemonSetCondition.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this V1DaemonSetCondition.

        The reason for the condition's last transition.  # noqa: E501

        :param reason: The reason of this V1DaemonSetCondition.  # noqa: E501
        :type reason: str
        """

        self._reason = reason

    @property
    def status(self):
        """Gets the status of this V1DaemonSetCondition.  # noqa: E501

        Status of the condition, one of True, False, Unknown.  # noqa: E501

        :return: The status of this V1DaemonSetCondition.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V1DaemonSetCondition.

        Status of the condition, one of True, False, Unknown.  # noqa: E501

        :param status: The status of this V1DaemonSetCondition.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def type(self):
        """Gets the type of this V1DaemonSetCondition.  # noqa: E501

        Type of DaemonSet condition.  # noqa: E501

        :return: The type of this V1DaemonSetCondition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1DaemonSetCondition.

        Type of DaemonSet condition.  # noqa: E501

        :param type: The type of this V1DaemonSetCondition.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, V1DaemonSetCondition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1DaemonSetCondition):
            return True

        return self.to_dict() != other.to_dict()
