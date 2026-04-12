import unittest
from province import Solution


class TestFindCircleNum(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_two_provinces(self):
        self.assertEqual(self.s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]), 2)

    def test_three_provinces(self):
        self.assertEqual(self.s.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]), 3)

    def test_single_city(self):
        self.assertEqual(self.s.findCircleNum([[1]]), 1)

    def test_all_connected(self):
        self.assertEqual(self.s.findCircleNum([[1,1,1],[1,1,1],[1,1,1]]), 1)


if __name__ == "__main__":
    unittest.main()
