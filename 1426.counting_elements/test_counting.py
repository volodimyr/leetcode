import unittest
from counting import Solution


class TestCountElements(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.countElements([1, 2, 3]), 2)

    def test_example2(self):
        self.assertEqual(self.s.countElements([1, 1, 3, 3, 5, 5, 7, 7]), 0)

    def test_duplicates_counted_separately(self):
        self.assertEqual(self.s.countElements([1, 1, 2]), 2)

    def test_single_element(self):
        self.assertEqual(self.s.countElements([5]), 0)

    def test_all_consecutive(self):
        self.assertEqual(self.s.countElements([1, 2, 3, 4]), 3)

    def test_no_consecutive(self):
        self.assertEqual(self.s.countElements([2, 4, 6, 8]), 0)


if __name__ == "__main__":
    unittest.main()
