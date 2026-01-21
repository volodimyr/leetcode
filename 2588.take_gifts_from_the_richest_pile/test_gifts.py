import unittest
from gifts import Solution


class TestPickGifts(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        gifts = [25, 64, 9, 4, 100]
        k = 4
        self.assertEqual(self.solution.pickGifts(gifts, k), 29)

    def test_example_2(self):
        gifts = [1, 1, 1, 1]
        k = 4
        self.assertEqual(self.solution.pickGifts(gifts, k), 4)

    def test_single_pile(self):
        gifts = [100]
        k = 1
        # floor(sqrt(100)) = 10
        self.assertEqual(self.solution.pickGifts(gifts, k), 10)

    def test_single_pile_multiple_operations(self):
        gifts = [100]
        k = 3
        # 100 -> 10 -> 3 -> 1
        self.assertEqual(self.solution.pickGifts(gifts, k), 1)

    def test_all_equal_piles(self):
        gifts = [16, 16, 16]
        k = 3
        # each 16 -> 4 once
        self.assertEqual(self.solution.pickGifts(gifts, k), 12)

    def test_k_greater_than_needed(self):
        gifts = [2, 3]
        k = 10
        # 3 -> 1, 2 -> 1, then all stay at 1
        self.assertEqual(self.solution.pickGifts(gifts, k), 2)

    def test_large_values(self):
        gifts = [10**9, 10**9]
        k = 2
        # both piles reduced once
        expected = int((10**9) ** 0.5) * 2
        self.assertEqual(self.solution.pickGifts(gifts, k), expected)

    def test_no_modification_when_k_zero(self):
        gifts = [5, 10, 15]
        k = 0
        self.assertEqual(self.solution.pickGifts(gifts, k), sum(gifts))


if __name__ == "__main__":
    unittest.main()
