from model import Maze, Vertex


class MazeAcyclicityChecker:
    def __init__(self, maze: Maze):
        self.loops_count = 0
        i = 0
        visited = set()

        def visit(vtx: Vertex, prev: Vertex = None):
            nonlocal self, i
            self.loops_count += vtx in visited
            i += 1
            print(self.loops_count)
            print(i)
            visited.add(vtx)
            [visit(n, prev=vtx) for n in maze.get_accessible_neighbours(vtx) if not prev or n != prev]

        import sys
        recursion_limit = sys.getrecursionlimit()
        sys.setrecursionlimit(maze.n ** 2 + 100)

        visit(Vertex(0, 0))

        sys.setrecursionlimit(recursion_limit)

        assert len(visited) == maze.n**2

    def is_acyclic(self):
        return self.loops_count == 0
