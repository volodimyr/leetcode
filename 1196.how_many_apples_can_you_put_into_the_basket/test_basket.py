import unittest
from basket import Solution

class TestMaxNumberOfApples(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_all_fit(self):
        self.assertEqual(self.s.maxNumberOfApples([100, 200, 150, 1000]), 4)

    def test_exceeds_limit(self):
        self.assertEqual(self.s.maxNumberOfApples([900, 950, 800, 1000, 700, 800]), 5)

    def test_single_apple_fits(self):
        self.assertEqual(self.s.maxNumberOfApples([5000]), 1)

    def test_single_apple_too_heavy(self):
        self.assertEqual(self.s.maxNumberOfApples([5001]), 0)

    def test_exact_limit(self):
        self.assertEqual(self.s.maxNumberOfApples([1000, 1000, 1000, 1000, 1000]), 5)

    def test_unsorted_input(self):
        self.assertEqual(self.s.maxNumberOfApples([1000, 1, 1, 1, 1]), 5)

if __name__ == "__main__":
    unittest.main()
