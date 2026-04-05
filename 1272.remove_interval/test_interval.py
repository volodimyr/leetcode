import unittest
from interval import Solution


class TestRemoveInterval(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.removeInterval([[0,2],[3,4],[5,7]], [1,6]), [[0,1],[6,7]])

    def test_example2(self):
        self.assertEqual(self.s.removeInterval([[0,5]], [2,3]), [[0,2],[3,5]])

    def test_example3(self):
        self.assertEqual(self.s.removeInterval([[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], [-1,4]), [[-5,-4],[-3,-2],[4,5],[8,9]])

    def test_no_overlap(self):
        self.assertEqual(self.s.removeInterval([[0,2],[3,4]], [5,7]), [[0,2],[3,4]])

    def test_remove_entire_interval(self):
        self.assertEqual(self.s.removeInterval([[1,3]], [0,5]), [])

    def test_remove_touches_boundary(self):
        self.assertEqual(self.s.removeInterval([[0,2],[3,4]], [2,3]), [[0,2],[3,4]])


if __name__ == "__main__":
    unittest.main()
