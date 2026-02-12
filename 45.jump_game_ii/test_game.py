import unittest
from game import Solution


class TestJumpGameII(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        nums = [2, 3, 1, 1, 4]
        self.assertEqual(self.sol.jump(nums), 2)

    def test_example_2(self):
        nums = [2, 3, 0, 1, 4]
        self.assertEqual(self.sol.jump(nums), 2)

    def test_single_element(self):
        nums = [0]
        self.assertEqual(self.sol.jump(nums), 0)

    def test_two_elements(self):
        nums = [1, 0]
        self.assertEqual(self.sol.jump(nums), 1)

    def test_all_ones(self):
        nums = [1, 1, 1, 1]
        self.assertEqual(self.sol.jump(nums), 3)

    def test_direct_jump(self):
        nums = [5, 0, 0, 0, 0]
        self.assertEqual(self.sol.jump(nums), 1)

    def test_zero_in_middle(self):
        nums = [2, 0, 2, 0, 1]
        self.assertEqual(self.sol.jump(nums), 2)

    def test_longer_case(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.sol.jump(nums), 3)


if __name__ == "__main__":
    unittest.main()
