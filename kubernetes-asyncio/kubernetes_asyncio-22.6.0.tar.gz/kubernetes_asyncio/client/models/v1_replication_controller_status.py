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


class V1ReplicationControllerStatus(object):
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
        'available_replicas': 'int',
        'conditions': 'list[V1ReplicationControllerCondition]',
        'fully_labeled_replicas': 'int',
        'observed_generation': 'int',
        'ready_replicas': 'int',
        'replicas': 'int'
    }

    attribute_map = {
        'available_replicas': 'availableReplicas',
        'conditions': 'conditions',
        'fully_labeled_replicas': 'fullyLabeledReplicas',
        'observed_generation': 'observedGeneration',
        'ready_replicas': 'readyReplicas',
        'replicas': 'replicas'
    }

    def __init__(self, available_replicas=None, conditions=None, fully_labeled_replicas=None, observed_generation=None, ready_replicas=None, replicas=None, local_vars_configuration=None):  # noqa: E501
        """V1ReplicationControllerStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._available_replicas = None
        self._conditions = None
        self._fully_labeled_replicas = None
        self._observed_generation = None
        self._ready_replicas = None
        self._replicas = None
        self.discriminator = None

        if available_replicas is not None:
            self.available_replicas = available_replicas
        if conditions is not None:
            self.conditions = conditions
        if fully_labeled_replicas is not None:
            self.fully_labeled_replicas = fully_labeled_replicas
        if observed_generation is not None:
            self.observed_generation = observed_generation
        if ready_replicas is not None:
            self.ready_replicas = ready_replicas
        self.replicas = replicas

    @property
    def available_replicas(self):
        """Gets the available_replicas of this V1ReplicationControllerStatus.  # noqa: E501

        The number of available replicas (ready for at least minReadySeconds) for this replication controller.  # noqa: E501

        :return: The available_replicas of this V1ReplicationControllerStatus.  # noqa: E501
        :rtype: int
        """
        return self._available_replicas

    @available_replicas.setter
    def available_replicas(self, available_replicas):
        """Sets the available_replicas of this V1ReplicationControllerStatus.

        The number of available replicas (ready for at least minReadySeconds) for this replication controller.  # noqa: E501

        :param available_replicas: The available_replicas of this V1ReplicationControllerStatus.  # noqa: E501
        :type available_replicas: int
        """

        self._available_replicas = available_replicas

    @property
    def conditions(self):
        """Gets the conditions of this V1ReplicationControllerStatus.  # noqa: E501

        Represents the latest available observations of a replication controller's current state.  # noqa: E501

        :return: The conditions of this V1ReplicationControllerStatus.  # noqa: E501
        :rtype: list[V1ReplicationControllerCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V1ReplicationControllerStatus.

        Represents the latest available observations of a replication controller's current state.  # noqa: E501

        :param conditions: The conditions of this V1ReplicationControllerStatus.  # noqa: E501
        :type conditions: list[V1ReplicationControllerCondition]
        """

        self._conditions = conditions

    @property
    def fully_labeled_replicas(self):
        """Gets the fully_labeled_replicas of this V1ReplicationControllerStatus.  # noqa: E501

        The number of pods that have labels matching the labels of the pod template of the replication controller.  # noqa: E501

        :return: The fully_labeled_replicas of this V1ReplicationControllerStatus.  # noqa: E501
        :rtype: int
        """
        return self._fully_labeled_replicas

    @fully_labeled_replicas.setter
    def fully_labeled_replicas(self, fully_labeled_replicas):
        """Sets the fully_labeled_replicas of this V1ReplicationControllerStatus.

        The number of pods that have labels matching the labels of the pod template of the replication controller.  # noqa: E501

        :param fully_labeled_replicas: The fully_labeled_replicas of this V1ReplicationControllerStatus.  # noqa: E501
        :type fully_labeled_replicas: int
        """

        self._fully_labeled_replicas = fully_labeled_replicas

    @property
    def observed_generation(self):
        """Gets the observed_generation of this V1ReplicationControllerStatus.  # noqa: E501

        ObservedGeneration reflects the generation of the most recently observed replication controller.  # noqa: E501

        :return: The observed_generation of this V1ReplicationControllerStatus.  # noqa: E501
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """Sets the observed_generation of this V1ReplicationControllerStatus.

        ObservedGeneration reflects the generation of the most recently observed replication controller.  # noqa: E501

        :param observed_generation: The observed_generation of this V1ReplicationControllerStatus.  # noqa: E501
        :type observed_generation: int
        """

        self._observed_generation = observed_generation

    @property
    def ready_replicas(self):
        """Gets the ready_replicas of this V1ReplicationControllerStatus.  # noqa: E501

        The number of ready replicas for this replication controller.  # noqa: E501

        :return: The ready_replicas of this V1ReplicationControllerStatus.  # noqa: E501
        :rtype: int
        """
        return self._ready_replicas

    @ready_replicas.setter
    def ready_replicas(self, ready_replicas):
        """Sets the ready_replicas of this V1ReplicationControllerStatus.

        The number of ready replicas for this replication controller.  # noqa: E501

        :param ready_replicas: The ready_replicas of this V1ReplicationControllerStatus.  # noqa: E501
        :type ready_replicas: int
        """

        self._ready_replicas = ready_replicas

    @property
    def replicas(self):
        """Gets the replicas of this V1ReplicationControllerStatus.  # noqa: E501

        Replicas is the most recently oberved number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller  # noqa: E501

        :return: The replicas of this V1ReplicationControllerStatus.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this V1ReplicationControllerStatus.

        Replicas is the most recently oberved number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller  # noqa: E501

        :param replicas: The replicas of this V1ReplicationControllerStatus.  # noqa: E501
        :type replicas: int
        """
        if self.local_vars_configuration.client_side_validation and replicas is None:  # noqa: E501
            raise ValueError("Invalid value for `replicas`, must not be `None`")  # noqa: E501

        self._replicas = replicas

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
        if not isinstance(other, V1ReplicationControllerStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ReplicationControllerStatus):
            return True

        return self.to_dict() != other.to_dict()
