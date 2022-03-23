from __future__ import annotations
from Node import Node
from typing import Any

class LinkedList:
    """Basic LinkedList Class
    """
    def __init__(self, head:Node):
        self.head = head
        self.iterNode = self.head
        self.len = 1
    
    def __iter__(self) -> LinkedList:
        return self
    
    def __next__(self) -> Node:
        """Return next node in interation

        Returns:
            Node: Node at iteration
        """
        if self.iterNode:
            iteration = self.iterNode
            self.iterNode = self.iterNode.get_next_node()
            
            return iteration
        else:
            self.iterNode = self.head
            raise StopIteration
            
    def __add__(self, new_val:Any) -> int:
        """add value at end of list

        Args:
            new_val (Any): new value to store

        Returns:
            int: return value that was added
        """
        return self.append(new_val)
    
    def __len__(self) -> int:
        """Return length of LinkedList

        Returns:
            int: length of LinkedList
        """
        return self.len
    
    def push(self, new_val:Any) -> int:
        """Insert value at beginning of list

        Args:
            new_val (Any): new value to insert to list

        Returns:
            int: value that was added
        """
        new = Node(new_val)
        new.set_next_node(self.head)
        self.head = new
    
    def append(self, new_val:Any) -> int:
        """Append value at end of list

        Args:
            new_val (Any): new value to add

        Returns:
            int: value that was added
        """
        node = self.head
        new = Node(new_val)
        while node:
            if not node.get_next_node():
                node.set_next_node(new)
                return new_val
            node = node.get_next_node()


if __name__ == '__main__':
    myList = LinkedList(Node(0))
    for i in range(5):
        myList.append(i)
    
    node = myList.head
    i = 0
    while node:
        print(f'iter: {i}')
        print(node)
        node = node.get_next_node()
        i+=1
    
    for node in myList:
        print(node)