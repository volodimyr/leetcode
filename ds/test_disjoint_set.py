import unittest
from disjoint_set import UnionFind


class TestUnionFind(unittest.TestCase):
    def test_initial_components(self):
        uf = UnionFind(5)
        for i in range(5):
            self.assertEqual(uf.find(i), i)
        self.assertEqual(uf.getNumComponents(), 5)

    def test_union_basic(self):
        uf = UnionFind(5)

        self.assertTrue(uf.union(0, 1))
        self.assertTrue(uf.isSameComponent(0, 1))
        self.assertEqual(uf.getNumComponents(), 4)

        # union of the same set returns False
        self.assertFalse(uf.union(0, 1))

    def test_chain_and_path_compression(self):
        uf = UnionFind(5)

        uf.union(0, 1)
        uf.union(1, 2)
        uf.union(2, 3)

        root_before = uf.find(3)
        self.assertEqual(root_before, uf.find(0))

        # After find(), path should compress
        self.assertEqual(uf.parent[3], root_before)

    def test_rank_updates(self):
        uf = UnionFind(4)

        uf.union(0, 1)  # rank[1] increases
        self.assertEqual(uf.rank[uf.find(1)], 1)

        uf.union(2, 3)  # rank[3] increases
        self.assertEqual(uf.rank[uf.find(3)], 1)

        # merging two trees with equal rank increases rank by 1
        uf.union(1, 3)
        root = uf.find(1)
        self.assertEqual(uf.rank[root], 2)

    def test_multiple_unions(self):
        uf = UnionFind(6)

        uf.union(0, 1)
        uf.union(2, 3)
        uf.union(4, 5)

        self.assertEqual(uf.getNumComponents(), 3)

        uf.union(1, 2)
        self.assertEqual(uf.getNumComponents(), 2)

        uf.union(3, 4)
        self.assertEqual(uf.getNumComponents(), 1)

    def test_same_component(self):
        uf = UnionFind(3)

        uf.union(0, 1)

        self.assertTrue(uf.isSameComponent(0, 1))
        self.assertFalse(uf.isSameComponent(1, 2))


if __name__ == "__main__":
    unittest.main()
