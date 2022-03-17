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


class V1CustomResourceDefinitionNames(object):
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
        'categories': 'list[str]',
        'kind': 'str',
        'list_kind': 'str',
        'plural': 'str',
        'short_names': 'list[str]',
        'singular': 'str'
    }

    attribute_map = {
        'categories': 'categories',
        'kind': 'kind',
        'list_kind': 'listKind',
        'plural': 'plural',
        'short_names': 'shortNames',
        'singular': 'singular'
    }

    def __init__(self, categories=None, kind=None, list_kind=None, plural=None, short_names=None, singular=None, local_vars_configuration=None):  # noqa: E501
        """V1CustomResourceDefinitionNames - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._categories = None
        self._kind = None
        self._list_kind = None
        self._plural = None
        self._short_names = None
        self._singular = None
        self.discriminator = None

        if categories is not None:
            self.categories = categories
        self.kind = kind
        if list_kind is not None:
            self.list_kind = list_kind
        self.plural = plural
        if short_names is not None:
            self.short_names = short_names
        if singular is not None:
            self.singular = singular

    @property
    def categories(self):
        """Gets the categories of this V1CustomResourceDefinitionNames.  # noqa: E501

        categories is a list of grouped resources this custom resource belongs to (e.g. 'all'). This is published in API discovery documents, and used by clients to support invocations like `kubectl get all`.  # noqa: E501

        :return: The categories of this V1CustomResourceDefinitionNames.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this V1CustomResourceDefinitionNames.

        categories is a list of grouped resources this custom resource belongs to (e.g. 'all'). This is published in API discovery documents, and used by clients to support invocations like `kubectl get all`.  # noqa: E501

        :param categories: The categories of this V1CustomResourceDefinitionNames.  # noqa: E501
        :type categories: list[str]
        """

        self._categories = categories

    @property
    def kind(self):
        """Gets the kind of this V1CustomResourceDefinitionNames.  # noqa: E501

        kind is the serialized kind of the resource. It is normally CamelCase and singular. Custom resource instances will use this value as the `kind` attribute in API calls.  # noqa: E501

        :return: The kind of this V1CustomResourceDefinitionNames.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1CustomResourceDefinitionNames.

        kind is the serialized kind of the resource. It is normally CamelCase and singular. Custom resource instances will use this value as the `kind` attribute in API calls.  # noqa: E501

        :param kind: The kind of this V1CustomResourceDefinitionNames.  # noqa: E501
        :type kind: str
        """
        if self.local_vars_configuration.client_side_validation and kind is None:  # noqa: E501
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501

        self._kind = kind

    @property
    def list_kind(self):
        """Gets the list_kind of this V1CustomResourceDefinitionNames.  # noqa: E501

        listKind is the serialized kind of the list for this resource. Defaults to \"`kind`List\".  # noqa: E501

        :return: The list_kind of this V1CustomResourceDefinitionNames.  # noqa: E501
        :rtype: str
        """
        return self._list_kind

    @list_kind.setter
    def list_kind(self, list_kind):
        """Sets the list_kind of this V1CustomResourceDefinitionNames.

        listKind is the serialized kind of the list for this resource. Defaults to \"`kind`List\".  # noqa: E501

        :param list_kind: The list_kind of this V1CustomResourceDefinitionNames.  # noqa: E501
        :type list_kind: str
        """

        self._list_kind = list_kind

    @property
    def plural(self):
        """Gets the plural of this V1CustomResourceDefinitionNames.  # noqa: E501

        plural is the plural name of the resource to serve. The custom resources are served under `/apis/<group>/<version>/.../<plural>`. Must match the name of the CustomResourceDefinition (in the form `<names.plural>.<group>`). Must be all lowercase.  # noqa: E501

        :return: The plural of this V1CustomResourceDefinitionNames.  # noqa: E501
        :rtype: str
        """
        return self._plural

    @plural.setter
    def plural(self, plural):
        """Sets the plural of this V1CustomResourceDefinitionNames.

        plural is the plural name of the resource to serve. The custom resources are served under `/apis/<group>/<version>/.../<plural>`. Must match the name of the CustomResourceDefinition (in the form `<names.plural>.<group>`). Must be all lowercase.  # noqa: E501

        :param plural: The plural of this V1CustomResourceDefinitionNames.  # noqa: E501
        :type plural: str
        """
        if self.local_vars_configuration.client_side_validation and plural is None:  # noqa: E501
            raise ValueError("Invalid value for `plural`, must not be `None`")  # noqa: E501

        self._plural = plural

    @property
    def short_names(self):
        """Gets the short_names of this V1CustomResourceDefinitionNames.  # noqa: E501

        shortNames are short names for the resource, exposed in API discovery documents, and used by clients to support invocations like `kubectl get <shortname>`. It must be all lowercase.  # noqa: E501

        :return: The short_names of this V1CustomResourceDefinitionNames.  # noqa: E501
        :rtype: list[str]
        """
        return self._short_names

    @short_names.setter
    def short_names(self, short_names):
        """Sets the short_names of this V1CustomResourceDefinitionNames.

        shortNames are short names for the resource, exposed in API discovery documents, and used by clients to support invocations like `kubectl get <shortname>`. It must be all lowercase.  # noqa: E501

        :param short_names: The short_names of this V1CustomResourceDefinitionNames.  # noqa: E501
        :type short_names: list[str]
        """

        self._short_names = short_names

    @property
    def singular(self):
        """Gets the singular of this V1CustomResourceDefinitionNames.  # noqa: E501

        singular is the singular name of the resource. It must be all lowercase. Defaults to lowercased `kind`.  # noqa: E501

        :return: The singular of this V1CustomResourceDefinitionNames.  # noqa: E501
        :rtype: str
        """
        return self._singular

    @singular.setter
    def singular(self, singular):
        """Sets the singular of this V1CustomResourceDefinitionNames.

        singular is the singular name of the resource. It must be all lowercase. Defaults to lowercased `kind`.  # noqa: E501

        :param singular: The singular of this V1CustomResourceDefinitionNames.  # noqa: E501
        :type singular: str
        """

        self._singular = singular

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
        if not isinstance(other, V1CustomResourceDefinitionNames):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1CustomResourceDefinitionNames):
            return True

        return self.to_dict() != other.to_dict()
