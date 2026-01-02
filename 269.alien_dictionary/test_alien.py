import unittest
from alien import Solution 

class TestAlienDictionary(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        words = ["z","o"]
        expected = "zo"
        result = self.sol.foreignDictionary(words)
        # result can be any valid order that satisfies constraints
        self.assertIn(result, ["zo", "oz"])  # both valid

    def test_example2(self):
        words = ["hrn","hrf","er","enn","rfnn"]
        result = self.sol.foreignDictionary(words)
        # expected one possible solution
        expected_set = set("hernf")
        self.assertEqual(set(result), expected_set)
        self.assertEqual(len(result), len(expected_set))

    def test_prefix_invalid(self):
        words = ["wrtkj", "wrt"]
        result = self.sol.foreignDictionary(words)
        self.assertEqual(result, "")

    def test_single_word(self):
        words = ["abc"]
        result = self.sol.foreignDictionary(words)
        self.assertEqual(set(result), set("abc"))

    def test_cycle(self):
        words = ["z","x","z"]
        result = self.sol.foreignDictionary(words)
        self.assertEqual(result, "")

    def test_all_letters_chain(self):
        words = [
            "mnop","nopq","opqr","pqrs","qrst","rstu","stuv","tuvw","uvwx","vwxy",
            "wxyz","xyz","yz","z","mnopqr","nopqrs","opqrst","pqrstu","qrstuv",
            "rstuvw","stuvwx","tuvwxy","uvwxyz","vwxyz","wxyza","xyzab","yzabc","zabcd"
        ]
        result = self.sol.foreignDictionary(words)
        # should be invalid due to cycle
        self.assertEqual(result, "")

    def test_no_constraints(self):
        words = ["abc", "abc", "abc"]
        result = self.sol.foreignDictionary(words)
        self.assertEqual(set(result), set("abc"))

if __name__ == "__main__":
    unittest.main()
