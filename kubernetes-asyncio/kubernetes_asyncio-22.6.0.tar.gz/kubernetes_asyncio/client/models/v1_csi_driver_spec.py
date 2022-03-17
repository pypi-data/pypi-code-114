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


class V1CSIDriverSpec(object):
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
        'attach_required': 'bool',
        'fs_group_policy': 'str',
        'pod_info_on_mount': 'bool',
        'requires_republish': 'bool',
        'storage_capacity': 'bool',
        'token_requests': 'list[StorageV1TokenRequest]',
        'volume_lifecycle_modes': 'list[str]'
    }

    attribute_map = {
        'attach_required': 'attachRequired',
        'fs_group_policy': 'fsGroupPolicy',
        'pod_info_on_mount': 'podInfoOnMount',
        'requires_republish': 'requiresRepublish',
        'storage_capacity': 'storageCapacity',
        'token_requests': 'tokenRequests',
        'volume_lifecycle_modes': 'volumeLifecycleModes'
    }

    def __init__(self, attach_required=None, fs_group_policy=None, pod_info_on_mount=None, requires_republish=None, storage_capacity=None, token_requests=None, volume_lifecycle_modes=None, local_vars_configuration=None):  # noqa: E501
        """V1CSIDriverSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._attach_required = None
        self._fs_group_policy = None
        self._pod_info_on_mount = None
        self._requires_republish = None
        self._storage_capacity = None
        self._token_requests = None
        self._volume_lifecycle_modes = None
        self.discriminator = None

        if attach_required is not None:
            self.attach_required = attach_required
        if fs_group_policy is not None:
            self.fs_group_policy = fs_group_policy
        if pod_info_on_mount is not None:
            self.pod_info_on_mount = pod_info_on_mount
        if requires_republish is not None:
            self.requires_republish = requires_republish
        if storage_capacity is not None:
            self.storage_capacity = storage_capacity
        if token_requests is not None:
            self.token_requests = token_requests
        if volume_lifecycle_modes is not None:
            self.volume_lifecycle_modes = volume_lifecycle_modes

    @property
    def attach_required(self):
        """Gets the attach_required of this V1CSIDriverSpec.  # noqa: E501

        attachRequired indicates this CSI volume driver requires an attach operation (because it implements the CSI ControllerPublishVolume() method), and that the Kubernetes attach detach controller should call the attach volume interface which checks the volumeattachment status and waits until the volume is attached before proceeding to mounting. The CSI external-attacher coordinates with CSI volume driver and updates the volumeattachment status when the attach operation is complete. If the CSIDriverRegistry feature gate is enabled and the value is specified to false, the attach operation will be skipped. Otherwise the attach operation will be called.  This field is immutable.  # noqa: E501

        :return: The attach_required of this V1CSIDriverSpec.  # noqa: E501
        :rtype: bool
        """
        return self._attach_required

    @attach_required.setter
    def attach_required(self, attach_required):
        """Sets the attach_required of this V1CSIDriverSpec.

        attachRequired indicates this CSI volume driver requires an attach operation (because it implements the CSI ControllerPublishVolume() method), and that the Kubernetes attach detach controller should call the attach volume interface which checks the volumeattachment status and waits until the volume is attached before proceeding to mounting. The CSI external-attacher coordinates with CSI volume driver and updates the volumeattachment status when the attach operation is complete. If the CSIDriverRegistry feature gate is enabled and the value is specified to false, the attach operation will be skipped. Otherwise the attach operation will be called.  This field is immutable.  # noqa: E501

        :param attach_required: The attach_required of this V1CSIDriverSpec.  # noqa: E501
        :type attach_required: bool
        """

        self._attach_required = attach_required

    @property
    def fs_group_policy(self):
        """Gets the fs_group_policy of this V1CSIDriverSpec.  # noqa: E501

        Defines if the underlying volume supports changing ownership and permission of the volume before being mounted. Refer to the specific FSGroupPolicy values for additional details. This field is beta, and is only honored by servers that enable the CSIVolumeFSGroupPolicy feature gate.  This field is immutable.  Defaults to ReadWriteOnceWithFSType, which will examine each volume to determine if Kubernetes should modify ownership and permissions of the volume. With the default policy the defined fsGroup will only be applied if a fstype is defined and the volume's access mode contains ReadWriteOnce.  # noqa: E501

        :return: The fs_group_policy of this V1CSIDriverSpec.  # noqa: E501
        :rtype: str
        """
        return self._fs_group_policy

    @fs_group_policy.setter
    def fs_group_policy(self, fs_group_policy):
        """Sets the fs_group_policy of this V1CSIDriverSpec.

        Defines if the underlying volume supports changing ownership and permission of the volume before being mounted. Refer to the specific FSGroupPolicy values for additional details. This field is beta, and is only honored by servers that enable the CSIVolumeFSGroupPolicy feature gate.  This field is immutable.  Defaults to ReadWriteOnceWithFSType, which will examine each volume to determine if Kubernetes should modify ownership and permissions of the volume. With the default policy the defined fsGroup will only be applied if a fstype is defined and the volume's access mode contains ReadWriteOnce.  # noqa: E501

        :param fs_group_policy: The fs_group_policy of this V1CSIDriverSpec.  # noqa: E501
        :type fs_group_policy: str
        """

        self._fs_group_policy = fs_group_policy

    @property
    def pod_info_on_mount(self):
        """Gets the pod_info_on_mount of this V1CSIDriverSpec.  # noqa: E501

        If set to true, podInfoOnMount indicates this CSI volume driver requires additional pod information (like podName, podUID, etc.) during mount operations. If set to false, pod information will not be passed on mount. Default is false. The CSI driver specifies podInfoOnMount as part of driver deployment. If true, Kubelet will pass pod information as VolumeContext in the CSI NodePublishVolume() calls. The CSI driver is responsible for parsing and validating the information passed in as VolumeContext. The following VolumeConext will be passed if podInfoOnMount is set to true. This list might grow, but the prefix will be used. \"csi.storage.k8s.io/pod.name\": pod.Name \"csi.storage.k8s.io/pod.namespace\": pod.Namespace \"csi.storage.k8s.io/pod.uid\": string(pod.UID) \"csi.storage.k8s.io/ephemeral\": \"true\" if the volume is an ephemeral inline volume                                 defined by a CSIVolumeSource, otherwise \"false\"  \"csi.storage.k8s.io/ephemeral\" is a new feature in Kubernetes 1.16. It is only required for drivers which support both the \"Persistent\" and \"Ephemeral\" VolumeLifecycleMode. Other drivers can leave pod info disabled and/or ignore this field. As Kubernetes 1.15 doesn't support this field, drivers can only support one mode when deployed on such a cluster and the deployment determines which mode that is, for example via a command line parameter of the driver.  This field is immutable.  # noqa: E501

        :return: The pod_info_on_mount of this V1CSIDriverSpec.  # noqa: E501
        :rtype: bool
        """
        return self._pod_info_on_mount

    @pod_info_on_mount.setter
    def pod_info_on_mount(self, pod_info_on_mount):
        """Sets the pod_info_on_mount of this V1CSIDriverSpec.

        If set to true, podInfoOnMount indicates this CSI volume driver requires additional pod information (like podName, podUID, etc.) during mount operations. If set to false, pod information will not be passed on mount. Default is false. The CSI driver specifies podInfoOnMount as part of driver deployment. If true, Kubelet will pass pod information as VolumeContext in the CSI NodePublishVolume() calls. The CSI driver is responsible for parsing and validating the information passed in as VolumeContext. The following VolumeConext will be passed if podInfoOnMount is set to true. This list might grow, but the prefix will be used. \"csi.storage.k8s.io/pod.name\": pod.Name \"csi.storage.k8s.io/pod.namespace\": pod.Namespace \"csi.storage.k8s.io/pod.uid\": string(pod.UID) \"csi.storage.k8s.io/ephemeral\": \"true\" if the volume is an ephemeral inline volume                                 defined by a CSIVolumeSource, otherwise \"false\"  \"csi.storage.k8s.io/ephemeral\" is a new feature in Kubernetes 1.16. It is only required for drivers which support both the \"Persistent\" and \"Ephemeral\" VolumeLifecycleMode. Other drivers can leave pod info disabled and/or ignore this field. As Kubernetes 1.15 doesn't support this field, drivers can only support one mode when deployed on such a cluster and the deployment determines which mode that is, for example via a command line parameter of the driver.  This field is immutable.  # noqa: E501

        :param pod_info_on_mount: The pod_info_on_mount of this V1CSIDriverSpec.  # noqa: E501
        :type pod_info_on_mount: bool
        """

        self._pod_info_on_mount = pod_info_on_mount

    @property
    def requires_republish(self):
        """Gets the requires_republish of this V1CSIDriverSpec.  # noqa: E501

        RequiresRepublish indicates the CSI driver wants `NodePublishVolume` being periodically called to reflect any possible change in the mounted volume. This field defaults to false.  Note: After a successful initial NodePublishVolume call, subsequent calls to NodePublishVolume should only update the contents of the volume. New mount points will not be seen by a running container.  # noqa: E501

        :return: The requires_republish of this V1CSIDriverSpec.  # noqa: E501
        :rtype: bool
        """
        return self._requires_republish

    @requires_republish.setter
    def requires_republish(self, requires_republish):
        """Sets the requires_republish of this V1CSIDriverSpec.

        RequiresRepublish indicates the CSI driver wants `NodePublishVolume` being periodically called to reflect any possible change in the mounted volume. This field defaults to false.  Note: After a successful initial NodePublishVolume call, subsequent calls to NodePublishVolume should only update the contents of the volume. New mount points will not be seen by a running container.  # noqa: E501

        :param requires_republish: The requires_republish of this V1CSIDriverSpec.  # noqa: E501
        :type requires_republish: bool
        """

        self._requires_republish = requires_republish

    @property
    def storage_capacity(self):
        """Gets the storage_capacity of this V1CSIDriverSpec.  # noqa: E501

        If set to true, storageCapacity indicates that the CSI volume driver wants pod scheduling to consider the storage capacity that the driver deployment will report by creating CSIStorageCapacity objects with capacity information.  The check can be enabled immediately when deploying a driver. In that case, provisioning new volumes with late binding will pause until the driver deployment has published some suitable CSIStorageCapacity object.  Alternatively, the driver can be deployed with the field unset or false and it can be flipped later when storage capacity information has been published.  This field is immutable.  This is a beta field and only available when the CSIStorageCapacity feature is enabled. The default is false.  # noqa: E501

        :return: The storage_capacity of this V1CSIDriverSpec.  # noqa: E501
        :rtype: bool
        """
        return self._storage_capacity

    @storage_capacity.setter
    def storage_capacity(self, storage_capacity):
        """Sets the storage_capacity of this V1CSIDriverSpec.

        If set to true, storageCapacity indicates that the CSI volume driver wants pod scheduling to consider the storage capacity that the driver deployment will report by creating CSIStorageCapacity objects with capacity information.  The check can be enabled immediately when deploying a driver. In that case, provisioning new volumes with late binding will pause until the driver deployment has published some suitable CSIStorageCapacity object.  Alternatively, the driver can be deployed with the field unset or false and it can be flipped later when storage capacity information has been published.  This field is immutable.  This is a beta field and only available when the CSIStorageCapacity feature is enabled. The default is false.  # noqa: E501

        :param storage_capacity: The storage_capacity of this V1CSIDriverSpec.  # noqa: E501
        :type storage_capacity: bool
        """

        self._storage_capacity = storage_capacity

    @property
    def token_requests(self):
        """Gets the token_requests of this V1CSIDriverSpec.  # noqa: E501

        TokenRequests indicates the CSI driver needs pods' service account tokens it is mounting volume for to do necessary authentication. Kubelet will pass the tokens in VolumeContext in the CSI NodePublishVolume calls. The CSI driver should parse and validate the following VolumeContext: \"csi.storage.k8s.io/serviceAccount.tokens\": {   \"<audience>\": {     \"token\": <token>,     \"expirationTimestamp\": <expiration timestamp in RFC3339>,   },   ... }  Note: Audience in each TokenRequest should be different and at most one token is empty string. To receive a new token after expiry, RequiresRepublish can be used to trigger NodePublishVolume periodically.  # noqa: E501

        :return: The token_requests of this V1CSIDriverSpec.  # noqa: E501
        :rtype: list[StorageV1TokenRequest]
        """
        return self._token_requests

    @token_requests.setter
    def token_requests(self, token_requests):
        """Sets the token_requests of this V1CSIDriverSpec.

        TokenRequests indicates the CSI driver needs pods' service account tokens it is mounting volume for to do necessary authentication. Kubelet will pass the tokens in VolumeContext in the CSI NodePublishVolume calls. The CSI driver should parse and validate the following VolumeContext: \"csi.storage.k8s.io/serviceAccount.tokens\": {   \"<audience>\": {     \"token\": <token>,     \"expirationTimestamp\": <expiration timestamp in RFC3339>,   },   ... }  Note: Audience in each TokenRequest should be different and at most one token is empty string. To receive a new token after expiry, RequiresRepublish can be used to trigger NodePublishVolume periodically.  # noqa: E501

        :param token_requests: The token_requests of this V1CSIDriverSpec.  # noqa: E501
        :type token_requests: list[StorageV1TokenRequest]
        """

        self._token_requests = token_requests

    @property
    def volume_lifecycle_modes(self):
        """Gets the volume_lifecycle_modes of this V1CSIDriverSpec.  # noqa: E501

        volumeLifecycleModes defines what kind of volumes this CSI volume driver supports. The default if the list is empty is \"Persistent\", which is the usage defined by the CSI specification and implemented in Kubernetes via the usual PV/PVC mechanism. The other mode is \"Ephemeral\". In this mode, volumes are defined inline inside the pod spec with CSIVolumeSource and their lifecycle is tied to the lifecycle of that pod. A driver has to be aware of this because it is only going to get a NodePublishVolume call for such a volume. For more information about implementing this mode, see https://kubernetes-csi.github.io/docs/ephemeral-local-volumes.html A driver can support one or more of these modes and more modes may be added in the future. This field is beta.  This field is immutable.  # noqa: E501

        :return: The volume_lifecycle_modes of this V1CSIDriverSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._volume_lifecycle_modes

    @volume_lifecycle_modes.setter
    def volume_lifecycle_modes(self, volume_lifecycle_modes):
        """Sets the volume_lifecycle_modes of this V1CSIDriverSpec.

        volumeLifecycleModes defines what kind of volumes this CSI volume driver supports. The default if the list is empty is \"Persistent\", which is the usage defined by the CSI specification and implemented in Kubernetes via the usual PV/PVC mechanism. The other mode is \"Ephemeral\". In this mode, volumes are defined inline inside the pod spec with CSIVolumeSource and their lifecycle is tied to the lifecycle of that pod. A driver has to be aware of this because it is only going to get a NodePublishVolume call for such a volume. For more information about implementing this mode, see https://kubernetes-csi.github.io/docs/ephemeral-local-volumes.html A driver can support one or more of these modes and more modes may be added in the future. This field is beta.  This field is immutable.  # noqa: E501

        :param volume_lifecycle_modes: The volume_lifecycle_modes of this V1CSIDriverSpec.  # noqa: E501
        :type volume_lifecycle_modes: list[str]
        """

        self._volume_lifecycle_modes = volume_lifecycle_modes

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
        if not isinstance(other, V1CSIDriverSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1CSIDriverSpec):
            return True

        return self.to_dict() != other.to_dict()
