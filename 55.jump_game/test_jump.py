import unittest
from jump import Solution

class TestCanJump(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_single_element(self):
        self.assertTrue(self.sol.canJump([0]))

    def test_simple_true(self):
        self.assertTrue(self.sol.canJump([2,3,1,1,4]))

    def test_simple_false(self):
        self.assertFalse(self.sol.canJump([3,2,1,0,4]))

    def test_all_ones(self):
        self.assertTrue(self.sol.canJump([1,1,1,1,1]))

    def test_zero_at_end(self):
        self.assertTrue(self.sol.canJump([2,3,1,0,0]))

    def test_large_jump(self):
        self.assertTrue(self.sol.canJump([5,0,0,0,0,0]))

    def test_trailing_zeros_blocking(self):
        self.assertFalse(self.sol.canJump([1,2,3,0,0,0,1]))

    def test_long_chain_true(self):
        nums = [1]*100
        self.assertTrue(self.sol.canJump(nums))

if __name__ == "__main__":
    unittest.main()
