import unittest
from typing import List


class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        N, M = len(sentence1), len(sentence2)
        if N != M:
            return False

        present = set()
        for p1, p2 in similarPairs:
            present.add((p1, p2))

        for i in range(len(sentence1)):
            p1, p2 = sentence1[i], sentence2[i]
            if p1 == p2:
                continue
            if (p1, p2) in present or (p2, p1) in present:
                continue
            return False

        return True


class TestSentenceSimilarity(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        sentence1 = ["great", "acting", "skills"]
        sentence2 = ["fine", "drama", "talent"]
        pairs = [["great", "fine"], ["drama", "acting"], ["skills", "talent"]]
        self.assertTrue(self.sol.areSentencesSimilar(sentence1, sentence2, pairs))

    def test_example_2_same_word(self):
        sentence1 = ["great"]
        sentence2 = ["great"]
        pairs = []
        self.assertTrue(self.sol.areSentencesSimilar(sentence1, sentence2, pairs))

    def test_example_3_different_length(self):
        sentence1 = ["great"]
        sentence2 = ["doubleplus", "good"]
        pairs = [["great", "doubleplus"]]
        self.assertFalse(self.sol.areSentencesSimilar(sentence1, sentence2, pairs))

    def test_not_similar(self):
        sentence1 = ["great", "acting"]
        sentence2 = ["fine", "skills"]
        pairs = [["great", "fine"]]
        self.assertFalse(self.sol.areSentencesSimilar(sentence1, sentence2, pairs))

    def test_reverse_pair(self):
        sentence1 = ["fine"]
        sentence2 = ["great"]
        pairs = [["great", "fine"]]
        self.assertTrue(self.sol.areSentencesSimilar(sentence1, sentence2, pairs))

    def test_transitive_not_allowed(self):
        sentence1 = ["a"]
        sentence2 = ["c"]
        pairs = [["a", "b"], ["b", "c"]]
        self.assertFalse(self.sol.areSentencesSimilar(sentence1, sentence2, pairs))


if __name__ == "__main__":
    unittest.main()