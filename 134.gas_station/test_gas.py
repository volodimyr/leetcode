import unittest
from gas import Solution


class TestGasStation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), 3)

    def test_example_2(self):
        gas = [2, 3, 4]
        cost = [3, 4, 3]
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), -1)

    def test_single_station_success(self):
        gas = [5]
        cost = [4]
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), 0)

    def test_single_station_failure(self):
        gas = [3]
        cost = [4]
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), -1)

    def test_all_zero(self):
        gas = [0, 0, 0]
        cost = [0, 0, 0]
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), 0)

    def test_reset_logic(self):
        # total gas == total cost, but early stations fail
        gas = [1, 2, 3, 4]
        cost = [3, 4, 3, 0]
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), 3)

    def test_no_possible_start(self):
        gas = [1, 1, 1, 1]
        cost = [2, 2, 2, 2]
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), -1)

    def test_large_valid_case(self):
        gas = [5, 1, 2, 3, 4]
        cost = [4, 4, 1, 5, 1]
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), 4)


if __name__ == "__main__":
    unittest.main()
