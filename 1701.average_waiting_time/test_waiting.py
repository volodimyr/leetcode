import unittest
from typing import List
from waiting import Solution


class TestAverageWaitingTime(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        customers = [[1, 2], [2, 5], [4, 3]]
        result = self.solution.averageWaitingTime(customers)
        self.assertAlmostEqual(result, 5.0, places=5)

    def test_example_2(self):
        customers = [[5, 2], [5, 4], [10, 3], [20, 1]]
        result = self.solution.averageWaitingTime(customers)
        self.assertAlmostEqual(result, 3.25, places=5)

    def test_single_customer(self):
        customers = [[10, 5]]
        result = self.solution.averageWaitingTime(customers)
        self.assertAlmostEqual(result, 5.0, places=5)

    def test_all_customers_arrive_same_time(self):
        customers = [[1, 1], [1, 2], [1, 3]]
        # finish times: 2, 4, 7
        # waits: 1, 3, 6 -> avg = 10/3
        result = self.solution.averageWaitingTime(customers)
        self.assertAlmostEqual(result, 10/3, places=5)

    def test_chef_idle_between_customers(self):
        customers = [[1, 2], [10, 3]]
        # waits: (3-1)=2, (13-10)=3 -> avg = 2.5
        result = self.solution.averageWaitingTime(customers)
        self.assertAlmostEqual(result, 2.5, places=5)

    def test_large_processing_time(self):
        customers = [[1, 10000], [2, 10000]]
        # finish times: 10001, 20001
        # waits: 10000, 19999
        result = self.solution.averageWaitingTime(customers)
        self.assertAlmostEqual(result, (10000 + 19999) / 2, places=5)


if __name__ == "__main__":
    unittest.main()
