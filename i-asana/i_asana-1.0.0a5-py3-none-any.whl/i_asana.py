"""Class module to interface with Asana.
"""
from datetime import date, datetime, time
import os
from typing import Union

from aracnid_logger import Logger
import asana
from pytz import timezone, utc

# initialize logging
logger = Logger(__name__).get_logger()


class AsanaInterface:
    """Asana interface class.

    Environment Variables:
        ASANA_ACCESS_TOKEN: Access token for Asana.

    Attributes:
        client: Asana client.

    Exceptions:
        TBD
    """

    def __init__(self) -> None:
        """Initializes the interface.
        """
        # read environment variables
        asana_access_token = os.environ.get('ASANA_ACCESS_TOKEN')

        # initialize asana client
        self._client = asana.Client.access_token(asana_access_token)

    @property
    def client(self) -> asana.client.Client:
        """Returns the Asana Client object.

        Returns:
            Asana Client object.
        """
        return self._client

    def create_task(
        self,
        name: str,
        project_id: str,
        start: Union[date, datetime]=None,
        due: Union[date, datetime]=None,
        section_id: str=None,
        parent_id: str=None
    ) -> dict:
        """Create a task in the specified project and section

        Start is only set if due is set.

        Args:
            name: Name of the task to create.
            project_id: Project identifier.
            start: Date or date-time when the task will start
            due: Date or date-time when the task is due.
            section_id: (Optional) Section identifier.
            parent_id: (Optional) Parent identifier.
        """
        # create the task body
        body = {
            'name': name,
            'projects': [project_id]
        }
        if due:
            if isinstance(due, datetime):
                body['due_at'] = self.convert_asana_datetime(due)
            elif isinstance(due, date):
                body['due_on'] = due.isoformat()

            if start:
                if isinstance(start, datetime):
                    body['start_at'] = self.convert_asana_datetime(start)
                elif isinstance(start, date):
                    body['start_on'] = start.isoformat()

        # create the task/subtask
        if parent_id:
            task = self._client.tasks.create_subtask_for_task(parent_id, body)
        else:
            task = self._client.tasks.create_task(body)

        # add task to the specified section
        if task and section_id:
            result = self._client.sections.add_task_for_section(
                section_gid=section_id,
                params={
                    'task': task['gid']
                }
            )

            # retrieve the updated task
            task = self._client.tasks.get_task(task_gid=task['gid'])

        return task

    def read_task(self, task_id: str) -> dict:
        """Read a task with the specified task id.

        Args:
            task_id: Task identifier.
        
        Returns:
            Specified task as a dictionary.
        """
        task = self._client.tasks.get_task(task_gid=task_id)

        return task

    def update_task(self, task_id: str, fields: dict) -> dict:
        """Update the specified task with the new fields.

        Args:
            task_id: Task identifier.
            fields: Fields to updated.

        Returns:
            Updated task as a dictionary.
        """
        task = self._client.tasks.update_task(
            task_gid=task_id,
            params=fields
        )

        return task

    def delete_task(self, task_id: str) -> None:
        """Delete a task with the specified task id.

        Args:
            task_id: Task identifier.
        
        Returns:
            None.
        """
        self._client.tasks.delete_task(task_gid=task_id)

        return None

    @staticmethod
    def convert_asana_datetime(datetime_obj: datetime) -> str:
        """Convert a datetime object to a string usable by Asana.

        Make sure that the input date-time is timezone-aware.

        Args:
            datetime_obj: Datetime object.

        Returns:
            Date-time as a string.
        """
        datetime_str = datetime_obj.strftime(
            '%Y-%m-%dT%H:%M:%S%z'
        )

        return datetime_str

    @classmethod
    def get_due_date(cls, task: dict) -> date:
        """Retrieve the date due.

        Args:
            task: Task object as a dictionary.

        Returns:
            Date due as a date object.
        """
        # get the due date string
        due_date_str = task.get('due_on')

        # convert string to date
        due_date = date.fromisoformat(due_date_str)

        return due_date

    @classmethod
    def get_due_datetime(cls, task: dict) -> datetime:
        """Retrieve the date-time due.

        If the due time is not specified in the task, noon local is used.

        Args:
            task: Task object as a dictionary.

        Returns:
            Date-time due as a datetime object.
        """
        # get the due date string and convert
        due_datetime_str = task.get('due_at')
        if due_datetime_str:
            due_datetime_utc = utc.localize(datetime.fromisoformat(due_datetime_str[0:-1]))
            due_datetime = due_datetime_utc.astimezone()
        else:
            due_date = cls.get_due_date(task)
            if due_date:
                due_datetime = datetime.combine(due_date, time(12, 0)).astimezone()

        return due_datetime

    def read_subtasks(self, task_id: str) -> list:
        """Read subtasks for a task with the specified task id.

        Args:
            task_id: Task identifier.
        
        Returns:
            List of subtasks.
        """
        # get the compact list of subtasks
        subtasks = self._client.tasks.get_subtasks_for_task(task_gid=task_id)

        # read each full subtask
        subtask_list = []
        for summary_task in subtasks:
            subtask_list.append(self.read_task(summary_task['gid']))

        return subtask_list

    def read_subtask_by_name(self, task_id: str, name: str) -> dict:
        """Read subtask by name for a task with the specified task id.

        Args:
            task_id: Task identifier.
            name: Name of the subtask to read.
        
        Returns:
            Subtask as a dictionary.
        """
        # get the compact list of subtasks
        subtasks = self._client.tasks.get_subtasks_for_task(task_gid=task_id)

        # read each full subtask
        subtask = None
        for summary_task in subtasks:
            if summary_task['name'] == name:
                subtask = self.read_task(summary_task['gid'])
                break

        return subtask
