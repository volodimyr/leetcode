import unittest
from max_sum import Solution

s = Solution()

class TestMaxAscendingSum(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(s.maxAscendingSum([10, 20, 30, 5, 10, 50]), 65)

    def test_example2(self):
        self.assertEqual(s.maxAscendingSum([10, 20, 30, 40, 50]), 150)

    def test_example3(self):
        self.assertEqual(s.maxAscendingSum([12, 17, 15, 13, 10, 11, 12]), 33)

    def test_single_element(self):
        self.assertEqual(s.maxAscendingSum([5]), 5)

    def test_descending(self):
        self.assertEqual(s.maxAscendingSum([50, 40, 30, 20, 10]), 50)

    def test_all_equal(self):
        self.assertEqual(s.maxAscendingSum([5, 5, 5, 5]), 5)

    def test_ascending_at_end(self):
        self.assertEqual(s.maxAscendingSum([100, 1, 2, 3]), 100)

if __name__ == "__main__":
    unittest.main()
