from collections import deque


class Node(object):
    def __init__(self, value=None, children=None, parent=None):
        if children is None:
            children = []
        self.value = value
        self.children = children
        self.parent = parent
        self.depth = 0
        self.flags = []

    def add_children(self, children):
        for child in children:
            child.depth = self.depth + 1
            self.children.append(child)

    def get_value(self):
        return self.value

    def get_parent(self):
        return self.parent

    def flag(self, flag):
        self.flags.append(flag)

    @staticmethod
    def breadth_first_search(root, consumer):
        queue = deque([root])

        while len(queue) > 0:
            n = queue.popleft()
            can_continue = consumer(n)
            if can_continue:
                queue.extend(n.children)
            else:
                return
