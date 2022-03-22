'''Provides Base Functions for Nawah modules.'''

from ._delete_lock import delete_lock
from ._obtain_lock import obtain_lock

__all__ = [
    'delete_lock',
    'obtain_lock',
]
