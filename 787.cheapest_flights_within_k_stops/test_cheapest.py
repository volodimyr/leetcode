import unittest
from cheapest import Solution

class TestCheapestFlightsWithinKStops(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        n = 4
        flights = [
            [0, 1, 100],
            [1, 2, 100],
            [2, 0, 100],
            [1, 3, 600],
            [2, 3, 200]
        ]
        self.assertEqual(
            self.solution.findCheapestPrice(n, flights, 0, 3, 1),
            700
        )

    def test_example_2(self):
        n = 3
        flights = [
            [0, 1, 100],
            [1, 2, 100],
            [0, 2, 500]
        ]
        self.assertEqual(
            self.solution.findCheapestPrice(n, flights, 0, 2, 1),
            200
        )

    def test_example_3(self):
        n = 3
        flights = [
            [0, 1, 100],
            [1, 2, 100],
            [0, 2, 500]
        ]
        self.assertEqual(
            self.solution.findCheapestPrice(n, flights, 0, 2, 0),
            500
        )

    def test_no_possible_route(self):
        n = 3
        flights = [
            [0, 1, 100]
        ]
        self.assertEqual(
            self.solution.findCheapestPrice(n, flights, 0, 2, 1),
            -1
        )

    def test_no_flights(self):
        n = 2
        flights = []
        self.assertEqual(
            self.solution.findCheapestPrice(n, flights, 0, 1, 1),
            -1
        )

    def test_exact_k_stops(self):
        n = 4
        flights = [
            [0, 1, 100],
            [1, 2, 100],
            [2, 3, 100]
        ]
        self.assertEqual(
            self.solution.findCheapestPrice(n, flights, 0, 3, 2),
            300
        )

    def test_cheaper_path_exceeds_k(self):
        n = 4
        flights = [
            [0, 1, 50],
            [1, 2, 50],
            [2, 3, 50],
            [0, 3, 300]
        ]
        self.assertEqual(
            self.solution.findCheapestPrice(n, flights, 0, 3, 1),
            300
        )

    def test_cycle_handling(self):
        n = 3
        flights = [
            [0, 1, 100],
            [1, 0, 50],
            [1, 2, 100]
        ]
        self.assertEqual(
            self.solution.findCheapestPrice(n, flights, 0, 2, 2),
            200
        )


if __name__ == "__main__":
    unittest.main()
