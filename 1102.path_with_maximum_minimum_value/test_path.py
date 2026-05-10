import unittest
from path import Solution


class TestMaximumMinimumPath(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.maximumMinimumPath([[5,4,5],[1,2,6],[7,4,6]]), 4)

    def test_example2(self):
        self.assertEqual(self.s.maximumMinimumPath([[2,2,1,2,2,2],[1,2,2,2,1,2]]), 2)

    def test_example3(self):
        self.assertEqual(self.s.maximumMinimumPath([[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]), 3)

    def test_single_cell(self):
        self.assertEqual(self.s.maximumMinimumPath([[7]]), 7)

    def test_single_row(self):
        self.assertEqual(self.s.maximumMinimumPath([[3, 1, 5, 4]]), 1)

    def test_single_col(self):
        self.assertEqual(self.s.maximumMinimumPath([[4],[2],[6],[3]]), 2)

    def test_all_same_values(self):
        self.assertEqual(self.s.maximumMinimumPath([[5,5],[5,5]]), 5)

    def test_zero_in_path(self):
        self.assertEqual(self.s.maximumMinimumPath([[0,2],[2,2]]), 0)


if __name__ == "__main__":
    unittest.main()
