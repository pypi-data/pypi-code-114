"""Helpers for `mcli get` displays"""

import json
from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Dict, List, Tuple

from rich.table import Table

from mcli.utils.utils_rich import console, create_table


class OutputDisplay(Enum):
    TABLE = 'table'
    NAME = 'name'
    JSON = 'json'

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self.value)


class MCLIGetDisplay(ABC):
    """ABC for all `mcli get` lists
    """

    def print(self, output: OutputDisplay):
        if output == OutputDisplay.TABLE:
            disp = self.to_table()
        elif output == OutputDisplay.NAME:
            names = self.to_name()
            disp = '\n'.join(names)
        elif output == OutputDisplay.JSON:
            json_list = self.to_json()
            disp = json.dumps(json_list)
        else:
            raise ValueError(f'output is not a known display type. It must be one of {list(OutputDisplay)}')
        console.print(disp)

    @abstractmethod
    def to_table(self) -> Table:
        raise NotImplementedError(
            f'Table outputs are not yet implemented for displaying mcli {self.__class__.__name__} objects.')

    @abstractmethod
    def to_name(self) -> List[str]:
        raise NotImplementedError(
            f'Name outputs are not yet implemented for displaying mcli {self.__class__.__name__} objects.')

    @abstractmethod
    def to_json(self) -> List[Dict[str, Any]]:
        raise NotImplementedError(
            f'JSON outputs are not yet implemented for displaying mcli {self.__class__.__name__} objects.')


def create_display_table(names: List[str], columns: List[Tuple[Any, ...]], column_names: List[str]) -> Table:

    output_table = create_table(data=columns,
                                indices=names,
                                index_label='NAME',
                                columns=[ss.upper() for ss in column_names],
                                table_kwargs={
                                    'box': None,
                                    'pad_edge': False
                                },
                                index_kwargs={
                                    'justify': 'left',
                                    'no_wrap': True
                                })
    return output_table
