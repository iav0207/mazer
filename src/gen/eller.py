from collections import defaultdict
from random import Random

from gen.uf import UnionFind
from model import Vertex, Edge, Maze


class Eller:

    class PrevRowSummary:
        def __init__(self, vertices=None, uf=None):
            self.vertices = vertices or []
            self.uf = uf or UnionFind(self.vertices)
            self.map = defaultdict(list)
            self.get_connected = lambda v: self.map[uf.find(v)]
            for vtx in self.vertices:
                self.get_connected(vtx).append(vtx)

    class RowGenerator:
        def __init__(self, maze_gen, row_i, prev_row_summary):
            self.maze_gen = maze_gen
            self.i = row_i
            self.prev = prev_row_summary

            self.curr_row = self._create_vertices()
            self.uf = UnionFind([*self.prev.vertices, *self.curr_row])
            # restoring UF state of prev row
            for set_id, vertices in self.prev.map.items():
                for v in vertices[1:]:
                    self.uf.connect(vertices[0], v)

        def _create_vertices(self):
            return [Vertex(j, self.i) for j in range(self.maze_gen.maze.n)]

        def generate(self):
            self.create_vertical_connections_from_prev_row()
            self.generate_horizontal_connections_in_curr_row()

            return Eller.PrevRowSummary(self.curr_row, self.uf)

        def create_vertical_connections_from_prev_row(self):
            for vertices_set in self.prev.map.values():
                # decide how many vertices of a set will connect to the next row
                # important: at least one should have a bridge further to prevent isolated islands
                num_to_connect = max(1, sum([self.will_connect() for i in range(len(vertices_set))]))
                to_connect = self.maze_gen.random.sample(vertices_set, num_to_connect)
                for vtx in to_connect:
                    self.connect(vtx, self.curr_row[vtx.x])

        def generate_horizontal_connections_in_curr_row(self):
            for j in range(1, self.maze_gen.n):
                le, ri = self.curr_row[j - 1], self.curr_row[j]
                if not self.uf.connected(le, ri) and self.will_connect():
                    self.connect(le, ri)

        def connect(self, v1, v2):
            assert not self.uf.connected(v1, v2)    # preventing loops
            self.uf.connect(v1, v2)
            self.maze_gen.maze.add_edge(Edge(v1, v2))

        def will_connect(self):
            return self.maze_gen.will_connect()

    class MazeGenerator:
        def __init__(self, n, thresh=0.4):
            self.n = n
            self.thresh = thresh
            self.maze = Maze(n)
            self.random = Random()

        def generate(self):
            prev = Eller.PrevRowSummary()
            for i in range(self.n):
                prev = Eller.RowGenerator(self, i, prev).generate()

            self.finalize(prev)

            return self.maze

        def finalize(self, last_row_summary):
            """satisfying last row post-conditions: no isolated regions should be left"""
            row = last_row_summary
            for j in range(1, len(row.vertices)):
                le, ri = row.vertices[j - 1], row.vertices[j]
                if not row.uf.connected(le, ri):
                    row.uf.connect(le, ri)
                    self.maze.add_edge(Edge(le, ri))

        def will_connect(self):
            return self.random.random() > self.thresh

    @staticmethod
    def generate_maze_of_size(n):
        return Eller.MazeGenerator(n).generate()
