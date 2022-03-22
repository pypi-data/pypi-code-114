from cakemail_openapi import TaskApi
from cakemail.wrapper import WrappedApi


class Task(WrappedApi):
    delete: TaskApi.delete_task
    get: TaskApi.get_task
    list: TaskApi.list_tasks

    def __init__(self, superclass):
        super().__init__(
            superclass=superclass,
            namemap={
                'delete': 'delete_task',
                'get': 'get_task',
                'list': 'list_tasks',
            }
        )
