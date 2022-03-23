from __future__ import annotations
from typing import Any
from Node import Node
class Stack:
    """Basic Stack Class 
    """
    def __init__(self, limit:int):
        """Initialize Stack object

        Args:
            limit (int): max size of Stack
        """
        self.size = 0
        self.top_item = None
        self.limit = limit

    def push(self, value:Any) -> int:
        """Put value on top of Stack

        Args:
            value (Any): Value to put in top node

        Returns:
            int: 1 if item was added, -1 if it wasn't (Stack is full)
        """
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
            return 1
        return -1
    
    def pop(self) -> int:
        """Remove top item in stack

        Returns:
            int: if any node was removed it returns that nodes value, otherwise return -1
        """
        if self.size > 0:
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        return -1

    def peek(self) -> int:
        """Get value of top item without deleting it from Stack

        Returns:
            int: Value of top node if it exists, otherwide -1
        """
        if self.size > 0:
            return self.top_item.get_value()
        return -1
    
    def has_space(self) -> bool:
        """Check if Stack has space left

        Returns:
            bool: True if there is more space, otherwise False
        """
        return self.limit > self.size

    def is_empty(self) -> bool:
        """Check if Stack has any items

        Returns:
            bool: True if Stack is empty, otherwise False
        """
        return self.size == 0

    def get_size(self) -> int:
        """Return current size of Stack (not max sixe)

        Returns:
            int: Size of Stack
        """
        return self.size
    