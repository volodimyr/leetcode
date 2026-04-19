import unittest
from ocean import Solution

class TestFindBuildings(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.findBuildings([4,2,3,2,1]), [0,2,3,4])

    def test_example2(self):
        self.assertEqual(self.s.findBuildings([1,3,2,4,2,5,1]), [5,6])

    def test_example3(self):
        self.assertEqual(self.s.findBuildings([9,8,7,7,6,5,4,3]), [0,1,3,4,5,6,7])

    def test_single_building(self):
        self.assertEqual(self.s.findBuildings([5]), [0])

    def test_ascending(self):
        self.assertEqual(self.s.findBuildings([1,2,3,4,5]), [4])

    def test_equal_heights(self):
        self.assertEqual(self.s.findBuildings([3,3,3]), [2])

if __name__ == "__main__":
    unittest.main()
