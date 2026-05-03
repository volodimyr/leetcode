import unittest
from paint import Solution


class TestMinCost(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.minCost([[17,2,17],[16,16,5],[14,3,19]]), 10)

    def test_example2(self):
        self.assertEqual(self.s.minCost([[7,6,2]]), 2)

    def test_example3(self):
        self.assertEqual(self.s.minCost([[15,10,16],[10,1,11]]), 16)

    def test_single_house(self):
        self.assertEqual(self.s.minCost([[5,8,3]]), 3)

    def test_all_same_cost(self):
        self.assertEqual(self.s.minCost([[1,1,1],[1,1,1]]), 2)

    def test_forces_alternation(self):
        self.assertEqual(self.s.minCost([[1,100,100],[100,1,100],[100,100,1]]), 3)


if __name__ == "__main__":
    unittest.main()
