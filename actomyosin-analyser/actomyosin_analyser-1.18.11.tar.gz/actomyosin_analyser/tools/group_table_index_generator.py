from typing import List, Any

from actomyosin_analyser.tools.experiment_iterator import GroupIterator


class GroupTableIndexGenerator:

    def __init__(self, group: GroupIterator):
        self.group = group

    def __call__(self) -> List[Any]:
        parameters = self.group.values
        keys = parameters.keys()
        index_list = []
        for k in keys:
            index_list.append(parameters[k])
        return index_list

