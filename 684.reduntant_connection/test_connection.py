import unittest
from connection import Solution, UnionFind
class TestUnionFind(unittest.TestCase):

    def test_initial_parents(self):
        uf = UnionFind(5)
        # Parents should initially point to themselves
        for i in range(1, 6):
            self.assertEqual(uf.find(i), i)

    def test_union_simple(self):
        uf = UnionFind(3)
        uf.add(1, 2)
        self.assertEqual(uf.find(1), uf.find(2))
        uf.add(2, 3)
        self.assertEqual(uf.find(1), uf.find(3))

    def test_rank_and_union(self):
        uf = UnionFind(4)
        uf.add(1, 2)
        uf.add(3, 4)
        uf.add(2, 3)
        # all should be in same set
        root = uf.find(1)
        for i in [2, 3, 4]:
            self.assertEqual(uf.find(i), root)

    def test_cycle_detection(self):
        uf = UnionFind(3)
        uf.add(1, 2)
        uf.add(2, 3)
        # Adding edge 1-3 should detect a cycle (return False)
        self.assertFalse(uf.add(1, 3))


class TestRedundantConnection(unittest.TestCase):

    def test_example1(self):
        sol = Solution()
        edges = [[1,2],[1,3],[2,3]]
        self.assertEqual(sol.findRedundantConnection(edges), [2,3])

    def test_example2(self):
        sol = Solution()
        edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
        self.assertEqual(sol.findRedundantConnection(edges), [1,4])

    def test_last_edge_cycle(self):
        sol = Solution()
        edges = [[1,2],[2,3],[3,1]]   # cycle formed only at last edge
        self.assertEqual(sol.findRedundantConnection(edges), [3,1])

    def test_no_cycle_until_end(self):
        sol = Solution()
        edges = [[1,2],[2,3],[3,4],[4,1]]
        self.assertEqual(sol.findRedundantConnection(edges), [4,1])

    def test_larger_graph(self):
        sol = Solution()
        edges = [
            [1,2],[2,3],[3,4],[4,5],
            [2,6],[6,7],[7,3]  # redundant edge
        ]
        self.assertEqual(sol.findRedundantConnection(edges), [7,3])


if __name__ == "__main__":
    unittest.main()
