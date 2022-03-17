import pprint
import re  # noqa: F401

import six

class TaskDetails(object):
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
        'workflow_id': 'str',
        'task_ref_name': 'str',
        'output': 'dict(str, object)',
        'task_id': 'str'
    }

    attribute_map = {
        'workflow_id': 'workflowId',
        'task_ref_name': 'taskRefName',
        'output': 'output',
        'task_id': 'taskId'
    }

    def __init__(self, workflow_id=None, task_ref_name=None, output=None, task_id=None):  # noqa: E501
        """TaskDetails - a model defined in Swagger"""  # noqa: E501
        self._workflow_id = None
        self._task_ref_name = None
        self._output = None
        self._task_id = None
        self.discriminator = None
        if workflow_id is not None:
            self.workflow_id = workflow_id
        if task_ref_name is not None:
            self.task_ref_name = task_ref_name
        if output is not None:
            self.output = output
        if task_id is not None:
            self.task_id = task_id

    @property
    def workflow_id(self):
        """Gets the workflow_id of this TaskDetails.  # noqa: E501


        :return: The workflow_id of this TaskDetails.  # noqa: E501
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this TaskDetails.


        :param workflow_id: The workflow_id of this TaskDetails.  # noqa: E501
        :type: str
        """

        self._workflow_id = workflow_id

    @property
    def task_ref_name(self):
        """Gets the task_ref_name of this TaskDetails.  # noqa: E501


        :return: The task_ref_name of this TaskDetails.  # noqa: E501
        :rtype: str
        """
        return self._task_ref_name

    @task_ref_name.setter
    def task_ref_name(self, task_ref_name):
        """Sets the task_ref_name of this TaskDetails.


        :param task_ref_name: The task_ref_name of this TaskDetails.  # noqa: E501
        :type: str
        """

        self._task_ref_name = task_ref_name

    @property
    def output(self):
        """Gets the output of this TaskDetails.  # noqa: E501


        :return: The output of this TaskDetails.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this TaskDetails.


        :param output: The output of this TaskDetails.  # noqa: E501
        :type: dict(str, object)
        """

        self._output = output

    @property
    def task_id(self):
        """Gets the task_id of this TaskDetails.  # noqa: E501


        :return: The task_id of this TaskDetails.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this TaskDetails.


        :param task_id: The task_id of this TaskDetails.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

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
        if issubclass(TaskDetails, dict):
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
        if not isinstance(other, TaskDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
