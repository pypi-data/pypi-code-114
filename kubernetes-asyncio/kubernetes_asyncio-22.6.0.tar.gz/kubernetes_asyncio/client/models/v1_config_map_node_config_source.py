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


class V1ConfigMapNodeConfigSource(object):
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
        'kubelet_config_key': 'str',
        'name': 'str',
        'namespace': 'str',
        'resource_version': 'str',
        'uid': 'str'
    }

    attribute_map = {
        'kubelet_config_key': 'kubeletConfigKey',
        'name': 'name',
        'namespace': 'namespace',
        'resource_version': 'resourceVersion',
        'uid': 'uid'
    }

    def __init__(self, kubelet_config_key=None, name=None, namespace=None, resource_version=None, uid=None, local_vars_configuration=None):  # noqa: E501
        """V1ConfigMapNodeConfigSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._kubelet_config_key = None
        self._name = None
        self._namespace = None
        self._resource_version = None
        self._uid = None
        self.discriminator = None

        self.kubelet_config_key = kubelet_config_key
        self.name = name
        self.namespace = namespace
        if resource_version is not None:
            self.resource_version = resource_version
        if uid is not None:
            self.uid = uid

    @property
    def kubelet_config_key(self):
        """Gets the kubelet_config_key of this V1ConfigMapNodeConfigSource.  # noqa: E501

        KubeletConfigKey declares which key of the referenced ConfigMap corresponds to the KubeletConfiguration structure This field is required in all cases.  # noqa: E501

        :return: The kubelet_config_key of this V1ConfigMapNodeConfigSource.  # noqa: E501
        :rtype: str
        """
        return self._kubelet_config_key

    @kubelet_config_key.setter
    def kubelet_config_key(self, kubelet_config_key):
        """Sets the kubelet_config_key of this V1ConfigMapNodeConfigSource.

        KubeletConfigKey declares which key of the referenced ConfigMap corresponds to the KubeletConfiguration structure This field is required in all cases.  # noqa: E501

        :param kubelet_config_key: The kubelet_config_key of this V1ConfigMapNodeConfigSource.  # noqa: E501
        :type kubelet_config_key: str
        """
        if self.local_vars_configuration.client_side_validation and kubelet_config_key is None:  # noqa: E501
            raise ValueError("Invalid value for `kubelet_config_key`, must not be `None`")  # noqa: E501

        self._kubelet_config_key = kubelet_config_key

    @property
    def name(self):
        """Gets the name of this V1ConfigMapNodeConfigSource.  # noqa: E501

        Name is the metadata.name of the referenced ConfigMap. This field is required in all cases.  # noqa: E501

        :return: The name of this V1ConfigMapNodeConfigSource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1ConfigMapNodeConfigSource.

        Name is the metadata.name of the referenced ConfigMap. This field is required in all cases.  # noqa: E501

        :param name: The name of this V1ConfigMapNodeConfigSource.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this V1ConfigMapNodeConfigSource.  # noqa: E501

        Namespace is the metadata.namespace of the referenced ConfigMap. This field is required in all cases.  # noqa: E501

        :return: The namespace of this V1ConfigMapNodeConfigSource.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this V1ConfigMapNodeConfigSource.

        Namespace is the metadata.namespace of the referenced ConfigMap. This field is required in all cases.  # noqa: E501

        :param namespace: The namespace of this V1ConfigMapNodeConfigSource.  # noqa: E501
        :type namespace: str
        """
        if self.local_vars_configuration.client_side_validation and namespace is None:  # noqa: E501
            raise ValueError("Invalid value for `namespace`, must not be `None`")  # noqa: E501

        self._namespace = namespace

    @property
    def resource_version(self):
        """Gets the resource_version of this V1ConfigMapNodeConfigSource.  # noqa: E501

        ResourceVersion is the metadata.ResourceVersion of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.  # noqa: E501

        :return: The resource_version of this V1ConfigMapNodeConfigSource.  # noqa: E501
        :rtype: str
        """
        return self._resource_version

    @resource_version.setter
    def resource_version(self, resource_version):
        """Sets the resource_version of this V1ConfigMapNodeConfigSource.

        ResourceVersion is the metadata.ResourceVersion of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.  # noqa: E501

        :param resource_version: The resource_version of this V1ConfigMapNodeConfigSource.  # noqa: E501
        :type resource_version: str
        """

        self._resource_version = resource_version

    @property
    def uid(self):
        """Gets the uid of this V1ConfigMapNodeConfigSource.  # noqa: E501

        UID is the metadata.UID of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.  # noqa: E501

        :return: The uid of this V1ConfigMapNodeConfigSource.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this V1ConfigMapNodeConfigSource.

        UID is the metadata.UID of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.  # noqa: E501

        :param uid: The uid of this V1ConfigMapNodeConfigSource.  # noqa: E501
        :type uid: str
        """

        self._uid = uid

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
        if not isinstance(other, V1ConfigMapNodeConfigSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ConfigMapNodeConfigSource):
            return True

        return self.to_dict() != other.to_dict()
