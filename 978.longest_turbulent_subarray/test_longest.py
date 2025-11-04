import unittest

from longest import Solution

class TestMaxTurbulenceSize(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.maxTurbulenceSize([9,4,2,10,7,8,8,1,9]), 5)

    def test_example2(self):
        self.assertEqual(self.s.maxTurbulenceSize([4,8,12,16]), 2)

    def test_example3(self):
        self.assertEqual(self.s.maxTurbulenceSize([100]), 1)

    def test_all_equal(self):
        self.assertEqual(self.s.maxTurbulenceSize([100,100,100]), 1)

    def test_simple_flip(self):
        self.assertEqual(self.s.maxTurbulenceSize([4,8]), 2)
        self.assertEqual(self.s.maxTurbulenceSize([8,4]), 2)

    def test_long_increase(self):
        self.assertEqual(self.s.maxTurbulenceSize([1,2,3,4,5,6]), 2)

    def test_long_decrease(self):
        self.assertEqual(self.s.maxTurbulenceSize([6,5,4,3,2,1]), 2)

    def test_alternating(self):
        self.assertEqual(self.s.maxTurbulenceSize([1,3,2,4,3,5,4,6]), 8)

    def test_edge_two_flips(self):
        self.assertEqual(self.s.maxTurbulenceSize([4,8,12]), 2)
        self.assertEqual(self.s.maxTurbulenceSize([9,9,4]), 2)
        self.assertEqual(self.s.maxTurbulenceSize([9,4,9]), 3)

if __name__ == "__main__":
    unittest.main()
