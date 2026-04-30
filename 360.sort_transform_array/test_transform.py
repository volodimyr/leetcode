import unittest
from transform import Solution

class TestSortTransformedArray(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.sortTransformedArray([-4,-2,2,4], 1, 3, 5), [3,9,15,33])

    def test_example2(self):
        self.assertEqual(self.s.sortTransformedArray([-4,-2,2,4], -1, 3, 5), [-23,-5,1,7])

    def test_a_zero_positive_b(self):
        self.assertEqual(self.s.sortTransformedArray([-4,-2,2,4], 0, 1, 0), [-4,-2,2,4])

    def test_a_zero_negative_b(self):
        self.assertEqual(self.s.sortTransformedArray([-4,-2,2,4], 0, -1, 0), [-4,-2,2,4])

    def test_single_element(self):
        self.assertEqual(self.s.sortTransformedArray([1], 2, 3, 1), [6])

    def test_all_zeros(self):
        self.assertEqual(self.s.sortTransformedArray([-1,0,1], 0, 0, 0), [0,0,0])

    def test_large_parabola_up(self):
        self.assertEqual(self.s.sortTransformedArray([-3,-1,0,1,3], 1, 0, 0), [0,1,1,9,9])

    def test_large_parabola_down(self):
        self.assertEqual(self.s.sortTransformedArray([-3,-1,0,1,3], -1, 0, 0), [-9,-9,-1,-1,0])

if __name__ == "__main__":
    unittest.main()
