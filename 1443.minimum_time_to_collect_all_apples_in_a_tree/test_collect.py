import unittest
from collect import Solution


class TestMinTime(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,True,True,False]), 8)

    def test_example2(self):
        self.assertEqual(self.s.minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,False,True,False]), 6)

    def test_example3(self):
        self.assertEqual(self.s.minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,False,False,False,False,False]), 0)

    def test_single_node_no_apple(self):
        self.assertEqual(self.s.minTime(1, [], [False]), 0)

    def test_single_node_with_apple(self):
        self.assertEqual(self.s.minTime(1, [], [True]), 0)

    def test_root_only_has_apple(self):
        self.assertEqual(self.s.minTime(3, [[0,1],[0,2]], [True,False,False]), 0)

    def test_all_apples(self):
        self.assertEqual(self.s.minTime(4, [[0,1],[1,2],[1,3]], [False,True,True,True]), 6)


if __name__ == "__main__":
    unittest.main()
