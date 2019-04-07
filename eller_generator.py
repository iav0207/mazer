from collections import defaultdict
from random import Random

from uf import UnionFind
from vo import Vertex, Edge, Maze


def create_vertices(row_i, maze_n):
    return [Vertex(j, row_i) for j in range(maze_n)]


class Eller:

    class _PrevRowSummary:
        def __init__(self, vertices=None, uf=None):
            self.vertices = vertices or []
            self.uf = uf or UnionFind(self.vertices)
            self.map = defaultdict(list)
            self.get_connected = lambda v: self.map[uf.find(v)]
            for vtx in self.vertices:
                self.get_connected(vtx).append(vtx)

    class _RowGenerator:
        def __init__(self, maze_gen, row_i, prev_row_summary):
            self.maze_gen = maze_gen
            self.i = row_i
            self.prev = prev_row_summary

            self.curr_row = create_vertices(self.i, self.maze_gen.n)
            self.uf = UnionFind([*self.prev.vertices, *self.curr_row])
            # restoring UF state of prev row
            for set_id, vertices in self.prev.map.items():
                for v in vertices[1:]:
                    self.uf.connect(vertices[0], v)

        def generate(self):
            self.create_vertical_connections_from_prev_row()
            self.generate_horizontal_connections_in_curr_row()

            return Eller._PrevRowSummary(self.curr_row, self.uf)

        def create_vertical_connections_from_prev_row(self):
            for vertices_set in self.prev.map.values():
                vtx = self.maze_gen.random.choice(vertices_set)
                self.connect(vtx, self.curr_row[vtx.x])

        def generate_horizontal_connections_in_curr_row(self):
            for j in range(1, self.maze_gen.n):
                le, ri = self.curr_row[j - 1], self.curr_row[j]
                if not self.uf.connected(le, ri) and self.will_connect():
                    self.connect(le, ri)

        def connect(self, v1, v2):
            self.uf.connect(v1, v2)
            self.maze_gen.maze.add_edge(Edge(v1, v2))

        def will_connect(self):
            return self.maze_gen.will_connect()

    class MazeGenerator:
        def __init__(self, n, thresh=0.7):
            self.n = n
            self.thresh = thresh
            self.maze = Maze(n)
            self.random = Random()

        def generate(self):
            prev = Eller._PrevRowSummary()
            for i in range(self.n):
                prev = Eller._RowGenerator(self, i, prev).generate()

            self.finalize(prev)

            return self.maze

        def finalize(self, last_row_summary):
            """satisfying last row post-conditions: no isolated regions should be left"""
            row = last_row_summary
            for j in range(1, len(row.vertices)):
                le, ri = row.vertices[j - 1], row.vertices[j]
                if row.uf.connected(le, ri):
                    continue
                # this is wrong i suppose, but it kinda works
                sizes = [row.uf.size_of_set_including(v) for v in [le, ri]]
                if any(size < 3 for size in sizes):
                    row.uf.connect(le, ri)
                    self.maze.add_edge(Edge(le, ri))

        def will_connect(self):
            return self.random.random() > self.thresh
