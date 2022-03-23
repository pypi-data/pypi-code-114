from __future__ import annotations
from typing import Any
class Node:
    """Basic Node CLass
    """
    
    def __init__(self, value, next_node:Node=None):
        """Initialize Node Object

        Args:
            value (Any): Node value.
            next_node (Node, optional): Next Node. Defaults to None.
        """
        self.value = value
        self.next_node = next_node

    def __repr__(self) -> str:
        return str(self.value)
    
    def __str__(self) -> str:
        return self.__repr__()

    def set_next_node(self, next_node:Node) -> None:
        """Set value for next_node

        Args:
            next_node (Node): Next node
        Returns:
            None
        """
        self.next_node = next_node

    def get_next_node(self) -> Node:
        """Return next node

        Returns:
            Node: Next node
        """
        return self.next_node

    def get_value(self) -> Any:
        """Return node value

        Returns:
            Any: Data node holds
        """
        return self.value

