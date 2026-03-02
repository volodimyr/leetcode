import unittest
from cost import Solution


class TestConnectSticks(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.connectSticks([2, 4, 3]), 14)

    def test_example2(self):
        self.assertEqual(self.sol.connectSticks([1, 8, 3, 5]), 30)

    def test_example3_single_stick(self):
        self.assertEqual(self.sol.connectSticks([5]), 0)

    def test_two_sticks(self):
        self.assertEqual(self.sol.connectSticks([1, 2]), 3)

    def test_duplicate_values(self):
        # 4+4=8
        # 4+4=8
        # 8+8=16
        # total = 8 + 8 + 16 = 32
        self.assertEqual(self.sol.connectSticks([4, 4, 4, 4]), 32)

    def test_random_order(self):
        self.assertEqual(self.sol.connectSticks([5, 1, 8, 3]), 30)

    def test_large_balanced_case(self):
        sticks = [1] * 6
        # 1+1=2
        # 1+1=2
        # 1+1=2
        # 2+2=4
        # 2+4=6
        # total = 2+2+2+4+6 = 16
        self.assertEqual(self.sol.connectSticks(sticks), 16)


if __name__ == "__main__":
    unittest.main()