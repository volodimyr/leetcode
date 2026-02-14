import unittest
from hand import Solution


class TestHandOfStraights(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    # Example 1
    def test_example_true(self):
        hand = [1,2,3,6,2,3,4,7,8]
        groupSize = 3
        self.assertTrue(self.sol.isNStraightHand(hand, groupSize))

    # Example 2
    def test_example_false(self):
        hand = [1,2,3,4,5]
        groupSize = 4
        self.assertFalse(self.sol.isNStraightHand(hand, groupSize))

    # Single group valid
    def test_single_group_valid(self):
        hand = [5,6,7,8]
        groupSize = 4
        self.assertTrue(self.sol.isNStraightHand(hand, groupSize))

    # Single group invalid (not consecutive)
    def test_single_group_invalid(self):
        hand = [1,2,4,5]
        groupSize = 4
        self.assertFalse(self.sol.isNStraightHand(hand, groupSize))

    # Duplicates forming multiple valid groups
    def test_duplicates_valid(self):
        hand = [1,2,3,1,2,3]
        groupSize = 3
        self.assertTrue(self.sol.isNStraightHand(hand, groupSize))

    # Duplicates but impossible grouping
    def test_duplicates_invalid(self):
        hand = [1,2,3,4,4,5]
        groupSize = 3
        self.assertFalse(self.sol.isNStraightHand(hand, groupSize))

    # groupSize == 1 (always true)
    def test_group_size_one(self):
        hand = [10,20,30]
        groupSize = 1
        self.assertTrue(self.sol.isNStraightHand(hand, groupSize))

    # Large gaps invalid
    def test_large_gap(self):
        hand = [1,10,20,30]
        groupSize = 2
        self.assertFalse(self.sol.isNStraightHand(hand, groupSize))

    # Large numbers
    def test_large_numbers(self):
        hand = [10**9, 10**9 - 1, 10**9 - 2]
        groupSize = 3
        self.assertTrue(self.sol.isNStraightHand(hand, groupSize))

    # Empty counter edge behavior (minimal input)
    def test_single_card(self):
        hand = [7]
        groupSize = 1
        self.assertTrue(self.sol.isNStraightHand(hand, groupSize))

    # Length not divisible by groupSize
    def test_not_divisible(self):
        hand = [1,2,3,4,5,6,7]
        groupSize = 3
        self.assertFalse(self.sol.isNStraightHand(hand, groupSize))


if __name__ == "__main__":
    unittest.main()
