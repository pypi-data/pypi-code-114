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


class V1IO(object):
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
        'name': 'str',
        'description': 'str',
        'type': 'str',
        'value': 'object',
        'is_optional': 'bool',
        'is_list': 'bool',
        'is_flag': 'bool',
        'arg_format': 'str',
        'delay_validation': 'bool',
        'options': 'list[object]',
        'connection': 'str',
        'to_init': 'bool',
        'to_env': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'value': 'value',
        'is_optional': 'isOptional',
        'is_list': 'isList',
        'is_flag': 'isFlag',
        'arg_format': 'argFormat',
        'delay_validation': 'delayValidation',
        'options': 'options',
        'connection': 'connection',
        'to_init': 'toInit',
        'to_env': 'toEnv'
    }

    def __init__(self, name=None, description=None, type=None, value=None, is_optional=None, is_list=None, is_flag=None, arg_format=None, delay_validation=None, options=None, connection=None, to_init=None, to_env=None, local_vars_configuration=None):  # noqa: E501
        """V1IO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._type = None
        self._value = None
        self._is_optional = None
        self._is_list = None
        self._is_flag = None
        self._arg_format = None
        self._delay_validation = None
        self._options = None
        self._connection = None
        self._to_init = None
        self._to_env = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if is_optional is not None:
            self.is_optional = is_optional
        if is_list is not None:
            self.is_list = is_list
        if is_flag is not None:
            self.is_flag = is_flag
        if arg_format is not None:
            self.arg_format = arg_format
        if delay_validation is not None:
            self.delay_validation = delay_validation
        if options is not None:
            self.options = options
        if connection is not None:
            self.connection = connection
        if to_init is not None:
            self.to_init = to_init
        if to_env is not None:
            self.to_env = to_env

    @property
    def name(self):
        """Gets the name of this V1IO.  # noqa: E501


        :return: The name of this V1IO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1IO.


        :param name: The name of this V1IO.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this V1IO.  # noqa: E501


        :return: The description of this V1IO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1IO.


        :param description: The description of this V1IO.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this V1IO.  # noqa: E501


        :return: The type of this V1IO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1IO.


        :param type: The type of this V1IO.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def value(self):
        """Gets the value of this V1IO.  # noqa: E501


        :return: The value of this V1IO.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this V1IO.


        :param value: The value of this V1IO.  # noqa: E501
        :type value: object
        """

        self._value = value

    @property
    def is_optional(self):
        """Gets the is_optional of this V1IO.  # noqa: E501


        :return: The is_optional of this V1IO.  # noqa: E501
        :rtype: bool
        """
        return self._is_optional

    @is_optional.setter
    def is_optional(self, is_optional):
        """Sets the is_optional of this V1IO.


        :param is_optional: The is_optional of this V1IO.  # noqa: E501
        :type is_optional: bool
        """

        self._is_optional = is_optional

    @property
    def is_list(self):
        """Gets the is_list of this V1IO.  # noqa: E501


        :return: The is_list of this V1IO.  # noqa: E501
        :rtype: bool
        """
        return self._is_list

    @is_list.setter
    def is_list(self, is_list):
        """Sets the is_list of this V1IO.


        :param is_list: The is_list of this V1IO.  # noqa: E501
        :type is_list: bool
        """

        self._is_list = is_list

    @property
    def is_flag(self):
        """Gets the is_flag of this V1IO.  # noqa: E501


        :return: The is_flag of this V1IO.  # noqa: E501
        :rtype: bool
        """
        return self._is_flag

    @is_flag.setter
    def is_flag(self, is_flag):
        """Sets the is_flag of this V1IO.


        :param is_flag: The is_flag of this V1IO.  # noqa: E501
        :type is_flag: bool
        """

        self._is_flag = is_flag

    @property
    def arg_format(self):
        """Gets the arg_format of this V1IO.  # noqa: E501


        :return: The arg_format of this V1IO.  # noqa: E501
        :rtype: str
        """
        return self._arg_format

    @arg_format.setter
    def arg_format(self, arg_format):
        """Sets the arg_format of this V1IO.


        :param arg_format: The arg_format of this V1IO.  # noqa: E501
        :type arg_format: str
        """

        self._arg_format = arg_format

    @property
    def delay_validation(self):
        """Gets the delay_validation of this V1IO.  # noqa: E501


        :return: The delay_validation of this V1IO.  # noqa: E501
        :rtype: bool
        """
        return self._delay_validation

    @delay_validation.setter
    def delay_validation(self, delay_validation):
        """Sets the delay_validation of this V1IO.


        :param delay_validation: The delay_validation of this V1IO.  # noqa: E501
        :type delay_validation: bool
        """

        self._delay_validation = delay_validation

    @property
    def options(self):
        """Gets the options of this V1IO.  # noqa: E501


        :return: The options of this V1IO.  # noqa: E501
        :rtype: list[object]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this V1IO.


        :param options: The options of this V1IO.  # noqa: E501
        :type options: list[object]
        """

        self._options = options

    @property
    def connection(self):
        """Gets the connection of this V1IO.  # noqa: E501


        :return: The connection of this V1IO.  # noqa: E501
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """Sets the connection of this V1IO.


        :param connection: The connection of this V1IO.  # noqa: E501
        :type connection: str
        """

        self._connection = connection

    @property
    def to_init(self):
        """Gets the to_init of this V1IO.  # noqa: E501


        :return: The to_init of this V1IO.  # noqa: E501
        :rtype: bool
        """
        return self._to_init

    @to_init.setter
    def to_init(self, to_init):
        """Sets the to_init of this V1IO.


        :param to_init: The to_init of this V1IO.  # noqa: E501
        :type to_init: bool
        """

        self._to_init = to_init

    @property
    def to_env(self):
        """Gets the to_env of this V1IO.  # noqa: E501


        :return: The to_env of this V1IO.  # noqa: E501
        :rtype: str
        """
        return self._to_env

    @to_env.setter
    def to_env(self, to_env):
        """Sets the to_env of this V1IO.


        :param to_env: The to_env of this V1IO.  # noqa: E501
        :type to_env: str
        """

        self._to_env = to_env

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
        if not isinstance(other, V1IO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1IO):
            return True

        return self.to_dict() != other.to_dict()
