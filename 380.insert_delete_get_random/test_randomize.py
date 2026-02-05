import unittest
from randomize import RandomizedSet

class TestRandomizedSet(unittest.TestCase):

    def test_insert(self):
        rs = RandomizedSet()
        self.assertTrue(rs.insert(1))  # Insert 1, should return True
        self.assertFalse(rs.insert(1))  # Insert 1 again, should return False
        self.assertTrue(rs.insert(2))  # Insert 2, should return True

    def test_remove(self):
        rs = RandomizedSet()
        rs.insert(1)
        rs.insert(2)
        self.assertFalse(rs.remove(3))  # Remove non-existent, should return False
        self.assertTrue(rs.remove(1))   # Remove existing, should return True
        self.assertFalse(rs.remove(1))  # Remove again, should return False

    def test_getRandom(self):
        rs = RandomizedSet()
        rs.insert(10)
        rs.insert(20)
        rs.insert(30)
        # Run multiple times to ensure returned values are from the set
        for _ in range(10):
            val = rs.getRandom()
            self.assertIn(val, [10, 20, 30])

    def test_combined_operations(self):
        rs = RandomizedSet()
        self.assertTrue(rs.insert(1))
        self.assertFalse(rs.remove(2))
        self.assertTrue(rs.insert(2))
        self.assertIn(rs.getRandom(), [1, 2])
        self.assertTrue(rs.remove(1))
        self.assertFalse(rs.insert(2))
        self.assertEqual(rs.getRandom(), 2)  # Only 2 remains

if __name__ == "__main__":
    unittest.main()
