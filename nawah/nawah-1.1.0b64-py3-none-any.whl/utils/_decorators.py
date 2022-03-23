'''Provides nawah_func decorator.'''
import inspect

from nawah.classes import Query
from nawah.enums import Event


def nawah_func(func):
    '''Processes args passed to a function as Nawah call.'''

    def _(**kwargs):
        check_permissions = check_args_query = check_args_doc = check_cache = True
        if 'skip_events' in kwargs and isinstance(kwargs['skip_events'], list):
            check_permissions = Event.PERM not in kwargs['skip_events']
            check_cache = Event.CACHE not in kwargs['skip_events']
            check_args_query = check_args_doc = Event.ARGS not in kwargs['skip_events']
            if check_args_query:
                check_args_query = Event.ARGS_QUERY not in kwargs['skip_events']
            if check_args_doc:
                check_args_doc = Event.ARGS_DOC not in kwargs['skip_events']

        if check_permissions:
            # [TODO] Implement
            pass

        if check_args_query:
            # [TODO] Implement
            pass

        if check_args_doc:
            # [TODO] Implement
            pass

        if check_cache:
            # [TODO] Implement
            pass

        if 'query' in kwargs:
            kwargs['query'] = Query(kwargs['query'])

        return func(
            **{
                param: kwargs[param]
                for param in inspect.signature(func).parameters
                if param in kwargs
            }
        )

    return _
