import unittest
from remove import Solution


class TestRemoveDuplicates(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_no_duplicates(self):
        self.assertEqual(self.s.removeDuplicates("abcd", 2), "abcd")

    def test_example2(self):
        self.assertEqual(self.s.removeDuplicates("deeedbbcccbdaa", 3), "aa")

    def test_example3(self):
        self.assertEqual(self.s.removeDuplicates("pbbcggttciiippooaais", 2), "ps")

    def test_single_char(self):
        self.assertEqual(self.s.removeDuplicates("a", 2), "a")

    def test_all_removed(self):
        self.assertEqual(self.s.removeDuplicates("aaa", 3), "")

    def test_chain_reaction(self):
        self.assertEqual(self.s.removeDuplicates("abbbac", 3), "aac")


if __name__ == "__main__":
    unittest.main()
