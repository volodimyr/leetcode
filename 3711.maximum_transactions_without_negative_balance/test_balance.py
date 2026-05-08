import unittest
from balance import Solution

class TestMaxTransactions(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.maxTransactions([2, -5, 3, -1, -2]), 4)

    def test_example2(self):
        self.assertEqual(self.s.maxTransactions([-1, -2, -3]), 0)

    def test_example3(self):
        self.assertEqual(self.s.maxTransactions([3, -2, 3, -2, 1, -1]), 6)

    def test_all_positive(self):
        self.assertEqual(self.s.maxTransactions([1, 2, 3]), 3)

    def test_single_negative(self):
        self.assertEqual(self.s.maxTransactions([-1]), 0)

    def test_single_positive(self):
        self.assertEqual(self.s.maxTransactions([5]), 1)

if __name__ == "__main__":
    unittest.main()
