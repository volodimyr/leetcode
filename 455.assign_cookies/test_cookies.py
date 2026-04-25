import unittest
from cookies import Solution

class TestFindContentChildren(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.findContentChildren([1,2,3], [1,1]), 1)

    def test_example2(self):
        self.assertEqual(self.s.findContentChildren([1,2], [1,2,3]), 2)

    def test_no_cookies(self):
        self.assertEqual(self.s.findContentChildren([1,2,3], []), 0)

    def test_no_children(self):
        self.assertEqual(self.s.findContentChildren([], [1,2,3]), 0)

    def test_all_satisfied(self):
        self.assertEqual(self.s.findContentChildren([1,2,3], [1,2,3]), 3)

    def test_none_satisfied(self):
        self.assertEqual(self.s.findContentChildren([5,6,7], [1,2,3]), 0)

    def test_single_child_satisfied(self):
        self.assertEqual(self.s.findContentChildren([3], [3]), 1)

    def test_single_child_not_satisfied(self):
        self.assertEqual(self.s.findContentChildren([4], [3]), 0)

if __name__ == '__main__':
    unittest.main()
