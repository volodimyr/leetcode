import unittest

from remove import Solution

class TestMinRemoveToMakeValid(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def is_valid(self, s: str) -> bool:
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

    def test_example1(self):
        result = self.s.minRemoveToMakeValid("lee(t(c)o)de)")
        self.assertTrue(self.is_valid(result))
        self.assertEqual(len(result), 12)

    def test_example2(self):
        result = self.s.minRemoveToMakeValid("a)b(c)d")
        self.assertTrue(self.is_valid(result))
        self.assertEqual(len(result), 6)

    def test_example3(self):
        result = self.s.minRemoveToMakeValid("))((" )
        self.assertEqual(result, "")

    def test_already_valid(self):
        result = self.s.minRemoveToMakeValid("(a)(b)")
        self.assertTrue(self.is_valid(result))
        self.assertEqual(result, "(a)(b)")

    def test_no_parentheses(self):
        result = self.s.minRemoveToMakeValid("abc")
        self.assertEqual(result, "abc")

    def test_all_open(self):
        result = self.s.minRemoveToMakeValid("(((")
        self.assertEqual(result, "")

    def test_all_close(self):
        result = self.s.minRemoveToMakeValid(")))")
        self.assertEqual(result, "")

    def test_nested_valid(self):
        result = self.s.minRemoveToMakeValid("((a))")
        self.assertTrue(self.is_valid(result))
        self.assertEqual(result, "((a))")

    def test_extra_open_at_end(self):
        result = self.s.minRemoveToMakeValid("(a(b)")
        self.assertTrue(self.is_valid(result))
        self.assertEqual(len(result), 4)

    def test_single_char(self):
        self.assertEqual(self.s.minRemoveToMakeValid("a"), "a")
        self.assertEqual(self.s.minRemoveToMakeValid("("), "")
        self.assertEqual(self.s.minRemoveToMakeValid(")"), "")

if __name__ == "__main__":
    unittest.main()
