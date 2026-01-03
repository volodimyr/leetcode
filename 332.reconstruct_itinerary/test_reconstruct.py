import unittest
from reconstruct import Solution


class TestReconstructItinerary(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        tickets = [
            ["MUC", "LHR"],
            ["JFK", "MUC"],
            ["SFO", "SJC"],
            ["LHR", "SFO"]
        ]
        expected = ["JFK", "MUC", "LHR", "SFO", "SJC"]
        self.assertEqual(self.sol.findItinerary(tickets), expected)

    def test_example_2(self):
        tickets = [
            ["JFK", "SFO"],
            ["JFK", "ATL"],
            ["SFO", "ATL"],
            ["ATL", "JFK"],
            ["ATL", "SFO"]
        ]
        expected = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
        self.assertEqual(self.sol.findItinerary(tickets), expected)


    def test_duplicate_tickets(self):
        tickets = [
            ["JFK", "ATL"],
            ["JFK", "ATL"],
            ["ATL", "JFK"]
        ]
        expected = ["JFK", "ATL", "JFK", "ATL"]
        self.assertEqual(self.sol.findItinerary(tickets), expected)

    def test_linear_path(self):
        tickets = [
            ["JFK", "A"],
            ["A", "B"],
            ["B", "C"]
        ]
        expected = ["JFK", "A", "B", "C"]
        self.assertEqual(self.sol.findItinerary(tickets), expected)

    def test_cycle(self):
        tickets = [
            ["JFK", "A"],
            ["A", "JFK"]
        ]
        expected = ["JFK", "A", "JFK"]
        self.assertEqual(self.sol.findItinerary(tickets), expected)

    def test_single_ticket(self):
        tickets = [["JFK", "SFO"]]
        expected = ["JFK", "SFO"]
        self.assertEqual(self.sol.findItinerary(tickets), expected)


if __name__ == "__main__":
    unittest.main()
