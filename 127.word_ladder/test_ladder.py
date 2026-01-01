import unittest
from ladder import Solution

class TestLadderLength(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        begin = "hit"
        end = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
        self.assertEqual(self.sol.ladderLength(begin, end, wordList), 5)

    def test_example2_no_path(self):
        begin = "hit"
        end = "cog"
        wordList = ["hot","dot","dog","lot","log"]
        self.assertEqual(self.sol.ladderLength(begin, end, wordList), 0)

    def test_single_step(self):
        begin = "a"
        end = "c"
        wordList = ["a","b","c"]
        self.assertEqual(self.sol.ladderLength(begin, end, wordList), 2)

    def test_two_steps(self):
        begin = "hit"
        end = "cog"
        wordList = ["hot","dot","cog"]
        self.assertEqual(self.sol.ladderLength(begin, end, wordList), 0)

    def test_beginword_not_in_list(self):
        begin = "hit"
        end = "hot"
        wordList = ["hot"]
        self.assertEqual(self.sol.ladderLength(begin, end, wordList), 2)

    def test_no_endword_in_list(self):
        begin = "hit"
        end = "xyz"
        wordList = ["hot","dot","dog"]
        self.assertEqual(self.sol.ladderLength(begin, end, wordList), 0)

    def test_longer_path(self):
        begin = "aaaa"
        end = "cccc"
        wordList = ["aaab","aabb","abbb","bbbb","bbbc","bbcc","bccc","cccc"]
        self.assertEqual(self.sol.ladderLength(begin, end, wordList), 9)

if __name__ == "__main__":
    unittest.main()
