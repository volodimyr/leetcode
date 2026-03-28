import unittest
from game import Solution


class TestStoneGame(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertTrue(self.s.stoneGame([5, 3, 4, 5]))

    def test_example2(self):
        self.assertTrue(self.s.stoneGame([3, 7, 2, 3]))

    def test_two_piles_alice_wins(self):
        # Alice always picks the larger of two piles
        self.assertTrue(self.s.stoneGame([1, 2]))

    def test_two_piles_alice_wins_reversed(self):
        self.assertTrue(self.s.stoneGame([2, 1]))

    def test_four_piles_large_middle(self):
        # Alice wins by strategy, not just taking endpoints greedily
        self.assertTrue(self.s.stoneGame([1, 100, 1, 3]))

    def test_alice_always_wins(self):
        # Mathematical insight: Alice always wins with even piles
        # since she can always choose odd-indexed or even-indexed piles
        self.assertTrue(self.s.stoneGame([2, 1, 4, 3]))

    def test_minimal_piles(self):
        # Smallest valid input: 2 piles, odd total
        self.assertTrue(self.s.stoneGame([1, 2]))

    def test_uniform_piles(self):
        # All same value — odd total requires odd number of piles total value
        # [1,1,1,3]: total=6 — violates odd constraint, skip
        # [1,2,1,3]: total=7 odd, 4 piles even
        self.assertTrue(self.s.stoneGame([1, 2, 1, 3]))

    def test_large_first_and_last(self):
        self.assertTrue(self.s.stoneGame([500, 1, 1, 499]))

    def test_returns_bool(self):
        result = self.s.stoneGame([5, 3, 4, 5])
        self.assertIsInstance(result, bool)


if __name__ == "__main__":
    unittest.main()
