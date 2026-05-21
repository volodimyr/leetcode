import unittest
from strobogrammatic import Solution


class TestIsStrobogrammatic(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_69(self):
        self.assertTrue(self.s.isStrobogrammatic("69"))

    def test_88(self):
        self.assertTrue(self.s.isStrobogrammatic("88"))

    def test_962(self):
        self.assertFalse(self.s.isStrobogrammatic("962"))

    def test_single_0(self):
        self.assertTrue(self.s.isStrobogrammatic("0"))

    def test_single_1(self):
        self.assertTrue(self.s.isStrobogrammatic("1"))

    def test_single_8(self):
        self.assertTrue(self.s.isStrobogrammatic("8"))

    def test_single_invalid(self):
        self.assertFalse(self.s.isStrobogrammatic("2"))

    def test_818(self):
        self.assertTrue(self.s.isStrobogrammatic("818"))

    def test_619(self):
        self.assertTrue(self.s.isStrobogrammatic("619"))

    def test_1881(self):
        self.assertTrue(self.s.isStrobogrammatic("1881"))


if __name__ == "__main__":
    unittest.main()
