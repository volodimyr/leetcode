import unittest
from number import Solution


class TestMinOperations(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.minOperations([2, 3, 3, 2, 2, 4, 2, 3, 4]), 4)

    def test_example2(self):
        self.assertEqual(self.s.minOperations([2, 1, 2, 2, 3, 3]), -1)

    def test_all_same(self):
        self.assertEqual(self.s.minOperations([1, 1, 1]), 1)

    def test_pairs_only(self):
        self.assertEqual(self.s.minOperations([1, 1, 2, 2]), 2)

    def test_singleton_returns_minus_one(self):
        self.assertEqual(self.s.minOperations([1, 1, 2]), -1)

    def test_count_of_four(self):
        # 4 = 2+2, so 2 operations
        self.assertEqual(self.s.minOperations([5, 5, 5, 5]), 2)

    def test_count_of_five(self):
        # 5 = 3+2, so 2 operations
        self.assertEqual(self.s.minOperations([7, 7, 7, 7, 7]), 2)


if __name__ == "__main__":
    unittest.main()
