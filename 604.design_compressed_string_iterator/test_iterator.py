import unittest
from iterator import StringIterator


class TestStringIterator(unittest.TestCase):

    def test_example(self):
        it = StringIterator("L1e2t1C1o1d1e1")
        self.assertEqual(it.next(), "L")
        self.assertEqual(it.next(), "e")
        self.assertEqual(it.next(), "e")
        self.assertEqual(it.next(), "t")
        self.assertEqual(it.next(), "C")
        self.assertEqual(it.next(), "o")
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), "d")
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), "e")
        self.assertFalse(it.hasNext())

    def test_next_after_exhaustion_returns_space(self):
        it = StringIterator("a1")
        self.assertEqual(it.next(), "a")
        self.assertFalse(it.hasNext())
        self.assertEqual(it.next(), " ")
        self.assertEqual(it.next(), " ")

    def test_multi_digit_count(self):
        it = StringIterator("a10")
        for _ in range(10):
            self.assertTrue(it.hasNext())
            self.assertEqual(it.next(), "a")
        self.assertFalse(it.hasNext())
        self.assertEqual(it.next(), " ")

    def test_large_count_single_char(self):
        it = StringIterator("z1000000000")
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), "z")
        self.assertTrue(it.hasNext())

    def test_multiple_chars_varying_counts(self):
        it = StringIterator("x1y2z3")
        result = []
        while it.hasNext():
            result.append(it.next())
        self.assertEqual(result, ["x", "y", "y", "z", "z", "z"])

    def test_has_next_false_on_empty_like(self):
        it = StringIterator("a1b1")
        self.assertTrue(it.hasNext())
        it.next()
        self.assertTrue(it.hasNext())
        it.next()
        self.assertFalse(it.hasNext())

    def test_single_char_single_count(self):
        it = StringIterator("A1")
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), "A")
        self.assertFalse(it.hasNext())

    def test_uppercase_and_lowercase(self):
        it = StringIterator("A2b3")
        result = []
        while it.hasNext():
            result.append(it.next())
        self.assertEqual(result, ["A", "A", "b", "b", "b"])

    def test_two_digit_count_transition(self):
        it = StringIterator("a12b1")
        for _ in range(12):
            self.assertEqual(it.next(), "a")
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), "b")
        self.assertFalse(it.hasNext())


if __name__ == "__main__":
    unittest.main()
