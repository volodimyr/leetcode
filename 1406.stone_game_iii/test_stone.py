import unittest
from stone import Solution


class TestStoneGameIII(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.stoneGameIII([1, 2, 3, 7]), "Bob")

    def test_example_2(self):
        self.assertEqual(self.solution.stoneGameIII([1, 2, 3, -9]), "Alice")

    def test_example_3(self):
        self.assertEqual(self.solution.stoneGameIII([1, 2, 3, 6]), "Tie")

    def test_single_positive(self):
        self.assertEqual(self.solution.stoneGameIII([1]), "Alice")

    def test_single_negative(self):
        self.assertEqual(self.solution.stoneGameIII([-1]), "Bob")

    def test_single_zero(self):
        self.assertEqual(self.solution.stoneGameIII([0]), "Tie")

    def test_all_negative(self):
        self.assertEqual(self.solution.stoneGameIII([-1, -2, -3]), "Tie")

    def test_alice_takes_all_three(self):
        self.assertEqual(self.solution.stoneGameIII([1, 2, 3]), "Alice")

    def test_two_stones(self):
        self.assertEqual(self.solution.stoneGameIII([7, 7]), "Alice")

    def test_large_last_stone(self):
        # Bob gets 7, Alice can only get 6
        self.assertEqual(self.solution.stoneGameIII([1, 2, 3, 7]), "Bob")


if __name__ == "__main__":
    unittest.main(verbosity=2)
