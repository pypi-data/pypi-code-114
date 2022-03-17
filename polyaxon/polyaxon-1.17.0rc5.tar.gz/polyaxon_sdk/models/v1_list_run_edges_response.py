#!/usr/bin/python
#
# Copyright 2018-2021 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    Polyaxon SDKs and REST API specification.

    Polyaxon SDKs and REST API specification.  # noqa: E501

    The version of the OpenAPI document: 1.16.1
    Contact: contact@polyaxon.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from polyaxon_sdk.configuration import Configuration


class V1ListRunEdgesResponse(object):
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
        'count': 'int',
        'results': 'list[V1RunEdge]',
        'previous': 'str',
        'next': 'str'
    }

    attribute_map = {
        'count': 'count',
        'results': 'results',
        'previous': 'previous',
        'next': 'next'
    }

    def __init__(self, count=None, results=None, previous=None, next=None, local_vars_configuration=None):  # noqa: E501
        """V1ListRunEdgesResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._count = None
        self._results = None
        self._previous = None
        self._next = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if results is not None:
            self.results = results
        if previous is not None:
            self.previous = previous
        if next is not None:
            self.next = next

    @property
    def count(self):
        """Gets the count of this V1ListRunEdgesResponse.  # noqa: E501


        :return: The count of this V1ListRunEdgesResponse.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this V1ListRunEdgesResponse.


        :param count: The count of this V1ListRunEdgesResponse.  # noqa: E501
        :type count: int
        """

        self._count = count

    @property
    def results(self):
        """Gets the results of this V1ListRunEdgesResponse.  # noqa: E501


        :return: The results of this V1ListRunEdgesResponse.  # noqa: E501
        :rtype: list[V1RunEdge]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this V1ListRunEdgesResponse.


        :param results: The results of this V1ListRunEdgesResponse.  # noqa: E501
        :type results: list[V1RunEdge]
        """

        self._results = results

    @property
    def previous(self):
        """Gets the previous of this V1ListRunEdgesResponse.  # noqa: E501


        :return: The previous of this V1ListRunEdgesResponse.  # noqa: E501
        :rtype: str
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Sets the previous of this V1ListRunEdgesResponse.


        :param previous: The previous of this V1ListRunEdgesResponse.  # noqa: E501
        :type previous: str
        """

        self._previous = previous

    @property
    def next(self):
        """Gets the next of this V1ListRunEdgesResponse.  # noqa: E501


        :return: The next of this V1ListRunEdgesResponse.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this V1ListRunEdgesResponse.


        :param next: The next of this V1ListRunEdgesResponse.  # noqa: E501
        :type next: str
        """

        self._next = next

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
        if not isinstance(other, V1ListRunEdgesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ListRunEdgesResponse):
            return True

        return self.to_dict() != other.to_dict()
