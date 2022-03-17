import pprint
import re  # noqa: F401

import six

class Action(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'action': 'str',
        'start_workflow': 'StartWorkflow',
        'complete_task': 'TaskDetails',
        'fail_task': 'TaskDetails',
        'expand_inline_json': 'bool'
    }

    attribute_map = {
        'action': 'action',
        'start_workflow': 'start_workflow',
        'complete_task': 'complete_task',
        'fail_task': 'fail_task',
        'expand_inline_json': 'expandInlineJSON'
    }

    def __init__(self, action=None, start_workflow=None, complete_task=None, fail_task=None, expand_inline_json=None):  # noqa: E501
        """Action - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._start_workflow = None
        self._complete_task = None
        self._fail_task = None
        self._expand_inline_json = None
        self.discriminator = None
        if action is not None:
            self.action = action
        if start_workflow is not None:
            self.start_workflow = start_workflow
        if complete_task is not None:
            self.complete_task = complete_task
        if fail_task is not None:
            self.fail_task = fail_task
        if expand_inline_json is not None:
            self.expand_inline_json = expand_inline_json

    @property
    def action(self):
        """Gets the action of this Action.  # noqa: E501


        :return: The action of this Action.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this Action.


        :param action: The action of this Action.  # noqa: E501
        :type: str
        """
        allowed_values = ["start_workflow", "complete_task", "fail_task"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def start_workflow(self):
        """Gets the start_workflow of this Action.  # noqa: E501


        :return: The start_workflow of this Action.  # noqa: E501
        :rtype: StartWorkflow
        """
        return self._start_workflow

    @start_workflow.setter
    def start_workflow(self, start_workflow):
        """Sets the start_workflow of this Action.


        :param start_workflow: The start_workflow of this Action.  # noqa: E501
        :type: StartWorkflow
        """

        self._start_workflow = start_workflow

    @property
    def complete_task(self):
        """Gets the complete_task of this Action.  # noqa: E501


        :return: The complete_task of this Action.  # noqa: E501
        :rtype: TaskDetails
        """
        return self._complete_task

    @complete_task.setter
    def complete_task(self, complete_task):
        """Sets the complete_task of this Action.


        :param complete_task: The complete_task of this Action.  # noqa: E501
        :type: TaskDetails
        """

        self._complete_task = complete_task

    @property
    def fail_task(self):
        """Gets the fail_task of this Action.  # noqa: E501


        :return: The fail_task of this Action.  # noqa: E501
        :rtype: TaskDetails
        """
        return self._fail_task

    @fail_task.setter
    def fail_task(self, fail_task):
        """Sets the fail_task of this Action.


        :param fail_task: The fail_task of this Action.  # noqa: E501
        :type: TaskDetails
        """

        self._fail_task = fail_task

    @property
    def expand_inline_json(self):
        """Gets the expand_inline_json of this Action.  # noqa: E501


        :return: The expand_inline_json of this Action.  # noqa: E501
        :rtype: bool
        """
        return self._expand_inline_json

    @expand_inline_json.setter
    def expand_inline_json(self, expand_inline_json):
        """Sets the expand_inline_json of this Action.


        :param expand_inline_json: The expand_inline_json of this Action.  # noqa: E501
        :type: bool
        """

        self._expand_inline_json = expand_inline_json

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
        if issubclass(Action, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Action):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
