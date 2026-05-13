import unittest
from unique import FirstUnique


class TestFirstUnique(unittest.TestCase):
    def test_example1(self):
        fu = FirstUnique([2, 3, 5])
        self.assertEqual(fu.showFirstUnique(), 2)
        fu.add(5)
        self.assertEqual(fu.showFirstUnique(), 2)
        fu.add(2)
        self.assertEqual(fu.showFirstUnique(), 3)
        fu.add(3)
        self.assertEqual(fu.showFirstUnique(), -1)

    def test_example2(self):
        fu = FirstUnique([7, 7, 7, 7, 7, 7])
        self.assertEqual(fu.showFirstUnique(), -1)
        fu.add(7)
        fu.add(3)
        fu.add(3)
        fu.add(7)
        fu.add(17)
        self.assertEqual(fu.showFirstUnique(), 17)

    def test_example3(self):
        fu = FirstUnique([809])
        self.assertEqual(fu.showFirstUnique(), 809)
        fu.add(809)
        self.assertEqual(fu.showFirstUnique(), -1)

    def test_single_element_stays_unique(self):
        fu = FirstUnique([1])
        self.assertEqual(fu.showFirstUnique(), 1)

    def test_all_duplicates_in_init(self):
        fu = FirstUnique([5, 5, 5])
        self.assertEqual(fu.showFirstUnique(), -1)

    def test_add_new_unique_after_empty(self):
        fu = FirstUnique([1, 1])
        self.assertEqual(fu.showFirstUnique(), -1)
        fu.add(42)
        self.assertEqual(fu.showFirstUnique(), 42)


if __name__ == "__main__":
    unittest.main()
