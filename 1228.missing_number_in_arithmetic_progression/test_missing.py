import unittest
from missing import Solution

class TestMissingNumber(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.missingNumber([5, 7, 11, 13]), 9)

    def test_example2(self):
        self.assertEqual(self.s.missingNumber([15, 13, 12]), 14)

    def test_all_same(self):
        self.assertEqual(self.s.missingNumber([3, 3, 3, 3]), 3)

    def test_missing_at_start(self):
        self.assertEqual(self.s.missingNumber([0, 4, 6, 8, 10]), 2)

    def test_missing_at_end(self):
        self.assertEqual(self.s.missingNumber([0, 2, 4, 6, 10]), 8)

    def test_descending(self):
        self.assertEqual(self.s.missingNumber([10, 6, 4, 2, 0]), 8)

if __name__ == "__main__":
    unittest.main()
