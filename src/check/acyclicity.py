from collections import deque

from model import Maze, Vertex


class MazeAcyclicityChecker:
    def __init__(self, maze: Maze):
        self.loops_count = 0

        visited = set()
        stack = deque()

        def visit(vtx: Vertex, prev: Vertex):
            if vtx in visited:
                self.loops_count += 1
                return
            visited.add(vtx)
            for nxt in maze.get_accessible_neighbours(vtx):
                if nxt != prev:
                    stack.append((nxt, vtx))

        stack.append((Vertex(0, 0), Vertex(0, 0)))

        while stack:
            visit(*stack.pop())

    def is_acyclic(self):
        return self.loops_count == 0
