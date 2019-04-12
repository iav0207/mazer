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
