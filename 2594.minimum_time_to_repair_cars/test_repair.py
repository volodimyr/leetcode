import math
from typing import List
import unittest
from repair import Solution

class TestRepairCars(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_simple_example_1(self):
        # Expected: Rank 1 repairs 4 cars in 16. Total cars repaired at time 16 >= 10.
        self.assertEqual(self.solution.repairCars([4, 2, 3, 1], 10), 16)

    def test_simple_example_2(self):
        # Expected: Rank 1 repairs 5 cars in 25. Total cars repaired at time 25 >= 6.
        self.assertEqual(self.solution.repairCars([5, 1, 8], 6), 16)

    def test_single_mechanic(self):
        # Expected: 10 * 5^2 = 250
        self.assertEqual(self.solution.repairCars([10], 5), 250)

    def test_single_car(self):
        # Expected: Min rank 1 * 1^2 = 1
        self.assertEqual(self.solution.repairCars([10, 1, 5], 1), 1)

    def test_all_same_rank(self):
        # Expected: 3 mechanics each repair 3 cars. 3 * 3^2 = 27.
        self.assertEqual(self.solution.repairCars([3, 3, 3], 9), 27)

    def test_min_rank_dominates(self):
        # Expected: Rank 1 repairs 10 cars in 1 * 10^2 = 100.
        self.assertEqual(self.solution.repairCars([100, 1, 100], 10), 100)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)