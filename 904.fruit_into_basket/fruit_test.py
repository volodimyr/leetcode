import unittest
from fruit import Solution


class TestTotalFruit(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.totalFruit([1, 2, 1]), 3)

    def test_example2(self):
        self.assertEqual(self.s.totalFruit([0, 1, 2, 2]), 3)

    def test_example3(self):
        self.assertEqual(self.s.totalFruit([1, 2, 3, 2, 2]), 4)

    def test_single_element(self):
        self.assertEqual(self.s.totalFruit([5]), 1)

    def test_all_same(self):
        self.assertEqual(self.s.totalFruit([3, 3, 3, 3]), 4)

    def test_two_types(self):
        self.assertEqual(self.s.totalFruit([1, 2, 1, 2, 1]), 5)

    def test_long_tail(self):
        self.assertEqual(self.s.totalFruit([1, 0, 1, 4, 1, 4, 1, 2, 3]), 5)

    def test_all_distinct(self):
        self.assertEqual(self.s.totalFruit([1, 2, 3, 4, 5]), 2)


if __name__ == "__main__":
    unittest.main()
