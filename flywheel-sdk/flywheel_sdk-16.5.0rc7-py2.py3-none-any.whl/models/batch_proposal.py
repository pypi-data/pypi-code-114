# coding: utf-8

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


## NOTE: This file is auto generated by the swagger code generator program.
## Do not edit the file manually.

import pprint
import re  # noqa: F401

import six

from flywheel.models.batch_proposal_detail import BatchProposalDetail  # noqa: F401,E501
from flywheel.models.container_output_with_files import ContainerOutputWithFiles  # noqa: F401,E501
from flywheel.models.job_config import JobConfig  # noqa: F401,E501
from flywheel.models.job_origin import JobOrigin  # noqa: F401,E501

# NOTE: This file is auto generated by the swagger code generator program.
# Do not edit the class manually.

from .mixins import BatchProposalMixin

class BatchProposal(BatchProposalMixin):

    swagger_types = {
        'id': 'str',
        'gear_id': 'str',
        'state': 'str',
        'config': 'JobConfig',
        'origin': 'JobOrigin',
        'proposal': 'BatchProposalDetail',
        'ambiguous': 'list[ContainerOutputWithFiles]',
        'matched': 'list[ContainerOutputWithFiles]',
        'not_matched': 'list[ContainerOutputWithFiles]',
        'optional_input_policy': 'str',
        'improper_permissions': 'list[str]',
        'created': 'datetime',
        'modified': 'datetime'
    }

    attribute_map = {
        'id': '_id',
        'gear_id': 'gear_id',
        'state': 'state',
        'config': 'config',
        'origin': 'origin',
        'proposal': 'proposal',
        'ambiguous': 'ambiguous',
        'matched': 'matched',
        'not_matched': 'not_matched',
        'optional_input_policy': 'optional_input_policy',
        'improper_permissions': 'improper_permissions',
        'created': 'created',
        'modified': 'modified'
    }

    rattribute_map = {
        '_id': 'id',
        'gear_id': 'gear_id',
        'state': 'state',
        'config': 'config',
        'origin': 'origin',
        'proposal': 'proposal',
        'ambiguous': 'ambiguous',
        'matched': 'matched',
        'not_matched': 'not_matched',
        'optional_input_policy': 'optional_input_policy',
        'improper_permissions': 'improper_permissions',
        'created': 'created',
        'modified': 'modified'
    }

    def __init__(self, id=None, gear_id=None, state=None, config=None, origin=None, proposal=None, ambiguous=None, matched=None, not_matched=None, optional_input_policy=None, improper_permissions=None, created=None, modified=None):  # noqa: E501
        """BatchProposal - a model defined in Swagger"""
        super(BatchProposal, self).__init__()

        self._id = None
        self._gear_id = None
        self._state = None
        self._config = None
        self._origin = None
        self._proposal = None
        self._ambiguous = None
        self._matched = None
        self._not_matched = None
        self._optional_input_policy = None
        self._improper_permissions = None
        self._created = None
        self._modified = None
        self.discriminator = None
        self.alt_discriminator = None

        if id is not None:
            self.id = id
        if gear_id is not None:
            self.gear_id = gear_id
        if state is not None:
            self.state = state
        if config is not None:
            self.config = config
        if origin is not None:
            self.origin = origin
        if proposal is not None:
            self.proposal = proposal
        if ambiguous is not None:
            self.ambiguous = ambiguous
        if matched is not None:
            self.matched = matched
        if not_matched is not None:
            self.not_matched = not_matched
        if optional_input_policy is not None:
            self.optional_input_policy = optional_input_policy
        if improper_permissions is not None:
            self.improper_permissions = improper_permissions
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified

    @property
    def id(self):
        """Gets the id of this BatchProposal.

        Unique database ID

        :return: The id of this BatchProposal.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BatchProposal.

        Unique database ID

        :param id: The id of this BatchProposal.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def gear_id(self):
        """Gets the gear_id of this BatchProposal.


        :return: The gear_id of this BatchProposal.
        :rtype: str
        """
        return self._gear_id

    @gear_id.setter
    def gear_id(self, gear_id):
        """Sets the gear_id of this BatchProposal.


        :param gear_id: The gear_id of this BatchProposal.  # noqa: E501
        :type: str
        """

        self._gear_id = gear_id

    @property
    def state(self):
        """Gets the state of this BatchProposal.


        :return: The state of this BatchProposal.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BatchProposal.


        :param state: The state of this BatchProposal.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def config(self):
        """Gets the config of this BatchProposal.


        :return: The config of this BatchProposal.
        :rtype: JobConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this BatchProposal.


        :param config: The config of this BatchProposal.  # noqa: E501
        :type: JobConfig
        """

        self._config = config

    @property
    def origin(self):
        """Gets the origin of this BatchProposal.


        :return: The origin of this BatchProposal.
        :rtype: JobOrigin
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this BatchProposal.


        :param origin: The origin of this BatchProposal.  # noqa: E501
        :type: JobOrigin
        """

        self._origin = origin

    @property
    def proposal(self):
        """Gets the proposal of this BatchProposal.


        :return: The proposal of this BatchProposal.
        :rtype: BatchProposalDetail
        """
        return self._proposal

    @proposal.setter
    def proposal(self, proposal):
        """Sets the proposal of this BatchProposal.


        :param proposal: The proposal of this BatchProposal.  # noqa: E501
        :type: BatchProposalDetail
        """

        self._proposal = proposal

    @property
    def ambiguous(self):
        """Gets the ambiguous of this BatchProposal.


        :return: The ambiguous of this BatchProposal.
        :rtype: list[ContainerOutputWithFiles]
        """
        return self._ambiguous

    @ambiguous.setter
    def ambiguous(self, ambiguous):
        """Sets the ambiguous of this BatchProposal.


        :param ambiguous: The ambiguous of this BatchProposal.  # noqa: E501
        :type: list[ContainerOutputWithFiles]
        """

        self._ambiguous = ambiguous

    @property
    def matched(self):
        """Gets the matched of this BatchProposal.


        :return: The matched of this BatchProposal.
        :rtype: list[ContainerOutputWithFiles]
        """
        return self._matched

    @matched.setter
    def matched(self, matched):
        """Sets the matched of this BatchProposal.


        :param matched: The matched of this BatchProposal.  # noqa: E501
        :type: list[ContainerOutputWithFiles]
        """

        self._matched = matched

    @property
    def not_matched(self):
        """Gets the not_matched of this BatchProposal.


        :return: The not_matched of this BatchProposal.
        :rtype: list[ContainerOutputWithFiles]
        """
        return self._not_matched

    @not_matched.setter
    def not_matched(self, not_matched):
        """Sets the not_matched of this BatchProposal.


        :param not_matched: The not_matched of this BatchProposal.  # noqa: E501
        :type: list[ContainerOutputWithFiles]
        """

        self._not_matched = not_matched

    @property
    def optional_input_policy(self):
        """Gets the optional_input_policy of this BatchProposal.

        ignored: Ignore all optional inputs, flexible: match a file if it's there, otherwise still match the container, required: treat all optional inputs as required inputs.

        :return: The optional_input_policy of this BatchProposal.
        :rtype: str
        """
        return self._optional_input_policy

    @optional_input_policy.setter
    def optional_input_policy(self, optional_input_policy):
        """Sets the optional_input_policy of this BatchProposal.

        ignored: Ignore all optional inputs, flexible: match a file if it's there, otherwise still match the container, required: treat all optional inputs as required inputs.

        :param optional_input_policy: The optional_input_policy of this BatchProposal.  # noqa: E501
        :type: str
        """

        self._optional_input_policy = optional_input_policy

    @property
    def improper_permissions(self):
        """Gets the improper_permissions of this BatchProposal.


        :return: The improper_permissions of this BatchProposal.
        :rtype: list[str]
        """
        return self._improper_permissions

    @improper_permissions.setter
    def improper_permissions(self, improper_permissions):
        """Sets the improper_permissions of this BatchProposal.


        :param improper_permissions: The improper_permissions of this BatchProposal.  # noqa: E501
        :type: list[str]
        """

        self._improper_permissions = improper_permissions

    @property
    def created(self):
        """Gets the created of this BatchProposal.

        Creation time (automatically set)

        :return: The created of this BatchProposal.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this BatchProposal.

        Creation time (automatically set)

        :param created: The created of this BatchProposal.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this BatchProposal.

        Last modification time (automatically updated)

        :return: The modified of this BatchProposal.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this BatchProposal.

        Last modification time (automatically updated)

        :param modified: The modified of this BatchProposal.  # noqa: E501
        :type: datetime
        """

        self._modified = modified


    @staticmethod
    def positional_to_model(value):
        """Converts a positional argument to a model value"""
        return value

    def return_value(self):
        """Unwraps return value from model"""
        return self

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchProposal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

    # Container emulation
    def __getitem__(self, key):
        """Returns the value of key"""
        key = self._map_key(key)
        return getattr(self, key)

    def __setitem__(self, key, value):
        """Sets the value of key"""
        key = self._map_key(key)
        setattr(self, key, value)

    def __contains__(self, key):
        """Checks if the given value is a key in this object"""
        key = self._map_key(key, raise_on_error=False)
        return key is not None

    def keys(self):
        """Returns the list of json properties in the object"""
        return self.__class__.rattribute_map.keys()

    def values(self):
        """Returns the list of values in the object"""
        for key in self.__class__.attribute_map.keys():
            yield getattr(self, key)

    def items(self):
        """Returns the list of json property to value mapping"""
        for key, prop in self.__class__.rattribute_map.items():
            yield key, getattr(self, prop)

    def get(self, key, default=None):
        """Get the value of the provided json property, or default"""
        key = self._map_key(key, raise_on_error=False)
        if key:
            return getattr(self, key, default)
        return default

    def _map_key(self, key, raise_on_error=True):
        result = self.__class__.rattribute_map.get(key)
        if result is None:
            if raise_on_error:
                raise AttributeError('Invalid attribute name: {}'.format(key))
            return None
        return '_' + result
