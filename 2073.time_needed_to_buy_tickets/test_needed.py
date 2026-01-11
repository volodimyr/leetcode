import unittest
from needed import Solution

class TestTimeRequiredToBuy(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        tickets = [2, 3, 2]
        k = 2
        self.assertEqual(
            self.sol.timeRequiredToBuy(tickets.copy(), k),
            6
        )

    def test_example_2(self):
        tickets = [5, 1, 1, 1]
        k = 0
        self.assertEqual(
            self.sol.timeRequiredToBuy(tickets.copy(), k),
            8
        )

    def test_single_person(self):
        tickets = [1]
        k = 0
        self.assertEqual(
            self.sol.timeRequiredToBuy(tickets.copy(), k),
            1
        )

    def test_all_same_tickets(self):
        tickets = [3, 3, 3]
        k = 1
        # Each person buys 3 tickets → 3 full rounds → 9 seconds
        self.assertEqual(
            self.sol.timeRequiredToBuy(tickets.copy(), k),
            8
        )

    def test_k_at_end(self):
        tickets = [1, 2, 3]
        k = 2
        self.assertEqual(
            self.sol.timeRequiredToBuy(tickets.copy(), k),
            6
        )

    def test_large_values(self):
        tickets = [100] * 100
        k = 50
        self.assertEqual(
            self.sol.timeRequiredToBuy(tickets.copy(), k),
            100 * 100 - (99 - k)
        )


if __name__ == "__main__":
    unittest.main()
