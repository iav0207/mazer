
class UnionFind:
    def __init__(self, items):
        self._items = items
        self._idx = {item: i for i, item in enumerate(items)}
        self._size = [1] * len(items)
        self._count = len(items)

    def count(self):
        return self._count

    def connect(self, p, q):
        root_p = self._root(p)
        root_q = self._root(q)
        if root_p == root_q:
            return
        heavy_root = max(root_p, root_q, key=self._size_of_subtree)
        light_root = root_q if heavy_root == root_p else root_p
        self._merge_p_to_q(light_root, heavy_root)
        self._increase_set_size_by(heavy_root, self._size_of_subtree(light_root))
        self._count -= 1

    def size_of_set_including(self, item):
        return self._size_of_subtree(self._root(item))

    def _size_of_subtree(self, root):
        return self._size[self._idx[root]]

    def _increase_set_size_by(self, root, increment):
        self._size[self._idx[root]] += increment

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        return self._idx[self._root(p)]

    def _merge_p_to_q(self, p, q):
        self._idx[q] = self._idx[p]

    def _root(self, p):
        while not self._is_root(p):
            self._idx[p] = self._idx[self._grandparent(p)]  # path compression
            p = self._parent(p)
        return p

    def _is_root(self, p):
        return p == self._parent(p)

    def _grandparent(self, p):
        return self._parent(self._parent(p))

    def _parent(self, p):
        return self._items[self._idx[p]]


if __name__ == '__main__':
    uf = UnionFind([c for c in 'abcdefghijklmn'])
    uf.connect('a', 'k')
    uf.connect('a', 'l')
    assert not uf.connected('a', 'b')
    assert uf.connected('k', 'l')
    assert uf.count() == 12
