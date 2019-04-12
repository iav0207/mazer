from collections import defaultdict


class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def adj(self, other):
        dx, dy = abs(self.x - other.x), abs(self.y - other.y)
        return {dx, dy} == {0, 1}

    def neighbour_by(self, edge):
        return edge.other(self)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f'vtx({self.x}:{self.y})'


class Edge:
    def __init__(self, v1: Vertex, v2: Vertex):
        assert v1.adj(v2)
        self.v = {v1, v2}

    def other(self, vertex: Vertex):
        assert vertex in self.v
        for vtx in self.v:
            if vtx != vertex:
                return vtx

    def __eq__(self, other):
        return self.v == other.v

    def __hash__(self):
        return hash(tuple(self.v))

    def __str__(self):
        v = tuple(self.v)
        return f'<{v[0]}-{v[1]}>'


class Maze:
    def __init__(self, n, start=Vertex(0, 0), end=None):
        self.n = n
        self.start = self._validated(start)
        self.end = self._validated(end or Vertex(n - 1, n - 1))
        self.map = defaultdict(set)

    def add_edge(self, e: Edge):
        for vtx in e.v:
            self.map[self._validated(vtx)].add(e)

    def get_all_edges(self):
        return {edge for edges in self.map.values() for edge in edges}

    def get_accessible_neighbours(self, vertex):
        return [edge.other(vertex) for edge in self._edges(vertex)]

    def get_edges(self, vertex):
        return self._edges(vertex).copy()

    def _edges(self, v: Vertex):
        return self.map[self._validated(v)]

    def _validated(self, v: Vertex):
        assert self.contains(v)
        return v

    def contains(self, v: Vertex):
        return 0 <= v.x < self.n and 0 <= v.y < self.n


class Solution:

    @staticmethod
    def from_vertices(vertices):
        edges = []
        for i in range(1, len(vertices)):
            edges.append(Edge(vertices[i - 1], vertices[i]))
        return Solution(vertices, edges)

    @staticmethod
    def from_edges(edges):
        vertices = []
        second_v = edges[0].v.intersection(edges[1].v)
        vertices.append(edges[0].other(second_v))
        vertices.append(second_v)
        v = second_v
        for e in edges[2:]:
            v = e.other(v)
            vertices.append(v)
        return Solution(vertices, edges)

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    def _validate(self):
        assert len(self.vertices) == len(self.edges) + 1
        assert len(self.edges) == len({self.edges})
        v_set = {self.vertices}
        for e in self.edges:
            for v in e.v:
                assert v in v_set

    def __len__(self):
        return len(self.vertices)
