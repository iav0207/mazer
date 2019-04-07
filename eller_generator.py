from collections import defaultdict
from random import Random

from uf import UnionFind
from vo import Vertex, Edge, Maze


class EllerGenerator:
    def __init__(self, n, thresh=0.8):
        self.n = n
        self.thresh = thresh
        self.maze = Maze(n)
        self.random = Random()

    class PrevRowSummary:
        def __init__(self, vertices=None, uf=None):
            self.vertices = vertices or []
            self.uf = uf or UnionFind(self.vertices)
            self.map = defaultdict(list)
            self.get_set_of = lambda v: self.map[uf.find(v)]
            for vtx in self.vertices:
                self.get_set_of(vtx).append(vtx)

    def generate(self):
        prev = EllerGenerator.PrevRowSummary()
        for i in range(self.n):
            prev = self.generate_row(i, prev)
        # finalization: last row post-conditions
        # for j in range(1, len(prev.vertices)):
        #     le, ri = prev.vertices[j - 1], prev.vertices[j]
        #     if not prev.uf.connected(le, ri):
        #         prev.uf.connect(le, ri)
        #         self.maze.add_edge(Edge(le, ri))
        return self.maze

    def generate_row(self, i, prev: PrevRowSummary):
        curr_row = self.create_vertices(i)
        uf = UnionFind([*prev.vertices, *curr_row])

        # restoring UF state of prev row
        if len(prev.map):
            for set_id, vertices in prev.map.items():
                for v in vertices[1:]:
                    uf.connect(vertices[0], v)

        def connect(v1, v2):
            uf.connect(v1, v2)
            self.maze.add_edge(Edge(v1, v2))

        # vertical binding
        if i > 0:
            for vtx in prev.vertices:
                if len(prev.get_set_of(vtx)) == 1:
                    connect(vtx, curr_row[vtx.x])

        # horizontal binding
        for j in range(1, self.n):
            le, ri = curr_row[j-1], curr_row[j]
            if not uf.connected(le, ri) and self.will_connect():
                # print(f'horizontal binding on i={i} j={j}')
                connect(le, ri)

        return EllerGenerator.PrevRowSummary(curr_row, uf)

    def create_vertices(self, row_i):
        return [Vertex(j, row_i) for j in range(self.n)]

    def will_connect(self):
        return self.random.random() > self.thresh
