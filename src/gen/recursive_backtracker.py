from collections import deque
from random import Random

from model import Maze, Vertex, Edge


class RecursiveBacktrackerGenerator:
    def __init__(self, n):
        self.n = n
        self.maze = Maze(n)
        self.random = Random()

    def generate(self):
        stack = deque([Vertex(0, 0)])
        visited = set()

        def dive(vtx):
            next_candidates = [n for n in self._get_neighbours(vtx) if n not in visited]
            if not next_candidates:
                return
            nxt = self.random.choice(next_candidates)
            self.maze.add_edge(Edge(vtx, nxt))
            visited.add(nxt)
            stack.append(nxt)
            dive(nxt)

        while stack:
            dive(stack.pop())

        return self.maze

    def _get_neighbours(self, vtx: Vertex):
        adj = []
        for delta in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            adj.append(Vertex(vtx.x + delta[0], vtx.y + delta[1]))
            if not self.maze.contains(adj[-1]):
                del adj[-1]
        return adj
