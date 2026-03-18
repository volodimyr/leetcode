import unittest
from triangle import Solution

s = Solution()

class TestMinimumTotal(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]), 11)

    def test_example2(self):
        self.assertEqual(s.minimumTotal([[-10]]), -10)

    def test_single_row(self):
        self.assertEqual(s.minimumTotal([[5]]), 5)

    def test_two_rows(self):
        self.assertEqual(s.minimumTotal([[1],[2,3]]), 3)

    def test_negative_values(self):
        self.assertEqual(s.minimumTotal([[-1],[-2,-3]]), -4)

    def test_all_same(self):
        self.assertEqual(s.minimumTotal([[1],[1,1],[1,1,1]]), 3)

if __name__ == "__main__":
    unittest.main()
