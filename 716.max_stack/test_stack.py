import unittest
from stack import MaxStack


class TestMaxStack(unittest.TestCase):
    def test_example(self):
        stk = MaxStack()
        stk.push(5)
        stk.push(1)
        stk.push(5)
        self.assertEqual(stk.top(), 5)
        self.assertEqual(stk.popMax(), 5)
        self.assertEqual(stk.top(), 1)
        self.assertEqual(stk.peekMax(), 5)
        self.assertEqual(stk.pop(), 1)
        self.assertEqual(stk.top(), 5)

    def test_push_pop(self):
        stk = MaxStack()
        stk.push(1)
        stk.push(2)
        stk.push(3)
        self.assertEqual(stk.pop(), 3)
        self.assertEqual(stk.pop(), 2)
        self.assertEqual(stk.pop(), 1)

    def test_top_does_not_remove(self):
        stk = MaxStack()
        stk.push(7)
        self.assertEqual(stk.top(), 7)
        self.assertEqual(stk.top(), 7)

    def test_peek_max_does_not_remove(self):
        stk = MaxStack()
        stk.push(3)
        stk.push(1)
        self.assertEqual(stk.peekMax(), 3)
        self.assertEqual(stk.peekMax(), 3)

    def test_pop_max_removes_topmost_duplicate(self):
        stk = MaxStack()
        stk.push(5)
        stk.push(5)
        self.assertEqual(stk.popMax(), 5)
        self.assertEqual(stk.top(), 5)
        self.assertEqual(stk.popMax(), 5)

    def test_pop_max_not_on_top(self):
        stk = MaxStack()
        stk.push(10)
        stk.push(3)
        stk.push(7)
        self.assertEqual(stk.popMax(), 10)
        self.assertEqual(stk.top(), 7)
        self.assertEqual(stk.peekMax(), 7)

    def test_negative_values(self):
        stk = MaxStack()
        stk.push(-5)
        stk.push(-1)
        stk.push(-3)
        self.assertEqual(stk.peekMax(), -1)
        self.assertEqual(stk.popMax(), -1)
        self.assertEqual(stk.peekMax(), -3)

    def test_single_element(self):
        stk = MaxStack()
        stk.push(42)
        self.assertEqual(stk.top(), 42)
        self.assertEqual(stk.peekMax(), 42)
        self.assertEqual(stk.pop(), 42)

    def test_interleaved_operations(self):
        stk = MaxStack()
        stk.push(1)
        stk.push(3)
        stk.push(2)
        self.assertEqual(stk.popMax(), 3)
        self.assertEqual(stk.pop(), 2)
        self.assertEqual(stk.top(), 1)
        self.assertEqual(stk.peekMax(), 1)


if __name__ == "__main__":
    unittest.main()
