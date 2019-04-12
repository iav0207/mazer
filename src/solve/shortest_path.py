from collections import deque

from model import Maze


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
            path.appendleft(node)
            node = node.parent
        return path

    def __eq__(self, other):
        return (self.val, self.parent) == (other.val, other.parent)

    def __hash__(self):
        return hash((self.val, self.parent))


def flat_list(lst):
    return [item for sublist in lst for item in sublist]


class ShortestPathFinder:
    def __init__(self, maze: Maze):
        front = [Node(maze.start)]
        seen = {maze.start}
        finish = None

        def step_fw(node):
            new_sub_front = []
            for vtx in maze.get_accessible_neighbours(node.val):
                if not node.is_parent_val(vtx) and vtx not in seen:
                    new_node = node.create_child(vtx)
                    seen.add(vtx)
                    new_sub_front.append(new_node)
                    if vtx == maze.end:
                        nonlocal finish
                        finish = new_node
            return new_sub_front

        while not finish:
            front = flat_list([step_fw(n) for n in front])

        self.path = finish.as_path()
