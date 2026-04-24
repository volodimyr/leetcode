import unittest
from origin import Solution


class TestFurthestDistanceFromOrigin(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.furthestDistanceFromOrigin("L_RL__R"), 3)

    def test_example2(self):
        self.assertEqual(self.s.furthestDistanceFromOrigin("_R__LL_"), 5)

    def test_example3(self):
        self.assertEqual(self.s.furthestDistanceFromOrigin("_______"), 7)

    def test_only_right(self):
        self.assertEqual(self.s.furthestDistanceFromOrigin("RRR"), 3)

    def test_only_left(self):
        self.assertEqual(self.s.furthestDistanceFromOrigin("LLL"), 3)

    def test_single_blank(self):
        self.assertEqual(self.s.furthestDistanceFromOrigin("_"), 1)

    def test_balanced_lr(self):
        self.assertEqual(self.s.furthestDistanceFromOrigin("LR"), 0)


if __name__ == "__main__":
    unittest.main()
