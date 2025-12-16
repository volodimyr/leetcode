import unittest
from cost import Solution

class TestMinCostConnectPoints(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
        self.assertEqual(self.sol.minCostConnectPoints(points), 20)

    def test_example2(self):
        points = [[3,12],[-2,5],[-4,1]]
        self.assertEqual(self.sol.minCostConnectPoints(points), 18)

    def test_single_point(self):
        points = [[0,0]]
        self.assertEqual(self.sol.minCostConnectPoints(points), 0)

    def test_two_points(self):
        points = [[0,0],[1,1]]
        self.assertEqual(self.sol.minCostConnectPoints(points), 2)

    def test_negative_coordinates(self):
        points = [[-1,-2],[3,4],[-5,6]]
        self.assertEqual(self.sol.minCostConnectPoints(points), 20)

if __name__ == '__main__':
    unittest.main()
