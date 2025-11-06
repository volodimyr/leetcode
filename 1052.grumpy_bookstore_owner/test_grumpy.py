import unittest
from typing import List
from grumpy import Solution

class TestMaxSatisfied(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        customers = [1, 0, 1, 2, 1, 1, 7, 5]
        grumpy =    [0, 1, 0, 1, 0, 1, 0, 1]
        minutes = 3
        self.assertEqual(self.s.maxSatisfied(customers, grumpy, minutes), 16)

    def test_example2(self):
        customers = [1]
        grumpy = [0]
        minutes = 1
        self.assertEqual(self.s.maxSatisfied(customers, grumpy, minutes), 1)

    def test_all_not_grumpy(self):
        customers = [2, 3, 4, 5]
        grumpy = [0, 0, 0, 0]
        minutes = 2
        self.assertEqual(self.s.maxSatisfied(customers, grumpy, minutes), 14)

    def test_all_grumpy(self):
        customers = [1, 2, 3, 4]
        grumpy = [1, 1, 1, 1]
        minutes = 2
        # Best 2-minute window: last two (3 + 4) = 7, total = 7
        self.assertEqual(self.s.maxSatisfied(customers, grumpy, minutes), 7)

    def test_single_window_best_in_middle(self):
        customers = [1, 10, 2, 5, 1]
        grumpy = [1, 0, 1, 1, 0]
        minutes = 2
        # Not grumpy: 10 + 1 = 11; best window = [2,5] = 7
        self.assertEqual(self.s.maxSatisfied(customers, grumpy, minutes), 18)

    def test_window_length_equals_array(self):
        customers = [4, 2, 3]
        grumpy = [1, 1, 1]
        minutes = 3
        self.assertEqual(self.s.maxSatisfied(customers, grumpy, minutes), 9)

    def test_edge_case_empty(self):
        customers = []
        grumpy = []
        minutes = 0
        # technically invalid by constraints, but just to check behavior
        self.assertEqual(self.s.maxSatisfied(customers, grumpy, minutes), 0)


if __name__ == "__main__":
    unittest.main()
