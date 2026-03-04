import unittest
from jump import Solution


class TestCanReach(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        s = "011010"
        minJump = 2
        maxJump = 3
        self.assertTrue(self.sol.canReach(s, minJump, maxJump))

    def test_example_2(self):
        s = "01101110"
        minJump = 2
        maxJump = 3
        self.assertFalse(self.sol.canReach(s, minJump, maxJump))

    def test_direct_jump(self):
        s = "00"
        minJump = 1
        maxJump = 1
        self.assertTrue(self.sol.canReach(s, minJump, maxJump))

    def test_large_gap(self):
        s = "0000000"
        minJump = 2
        maxJump = 5
        self.assertTrue(self.sol.canReach(s, minJump, maxJump))

    def test_last_is_one(self):
        s = "00001"
        minJump = 1
        maxJump = 3
        self.assertFalse(self.sol.canReach(s, minJump, maxJump))

    def test_min_equals_max(self):
        s = "010001000"
        minJump = 3
        maxJump = 3
        self.assertFalse(self.sol.canReach(s, minJump, maxJump))

    def test_single_possible_path(self):
        s = "000100010000"
        minJump = 2
        maxJump = 3
        self.assertTrue(self.sol.canReach(s, minJump, maxJump))


if __name__ == "__main__":
    unittest.main()