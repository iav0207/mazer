from collections import deque


class Node:
    def __init__(self, val, parent=None):
        self.val = val
        self.parent = parent

    def create_child(self, val):
        return Node(val, self)

    def is_parent_val(self, val):
        return self.parent and self.parent.val == val

    def as_path(self):
        path = deque()
        node = self
        while node:
            path.appendleft(node.val)
            node = node.parent
        return path

    def __eq__(self, other):
        return (self.val, self.parent) == (other.val, other.parent)

    def __hash__(self):
        return hash((self.val, self.parent))

    def __str__(self):
        par_str = f'{self.parent.val.x}:{self.parent.val.y}' if self.parent else 'None'
        return f'node_{self.val}<<({par_str})'
