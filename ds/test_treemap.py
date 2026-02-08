import unittest
from treemap import TreeMap


class TestTreeMap(unittest.TestCase):

    def setUp(self):
        self.tm = TreeMap()

    def test_get_on_empty(self):
        self.assertEqual(self.tm.get(1), -1)
        self.assertEqual(self.tm.getMin(), -1)
        self.assertEqual(self.tm.getMax(), -1)
        self.assertEqual(self.tm.getInorderKeys(), [])

    def test_insert_and_get(self):
        self.tm.insert(5, 50)
        self.tm.insert(3, 30)
        self.tm.insert(7, 70)

        self.assertEqual(self.tm.get(5), 50)
        self.assertEqual(self.tm.get(3), 30)
        self.assertEqual(self.tm.get(7), 70)
        self.assertEqual(self.tm.get(10), -1)

    def test_insert_update_existing_key(self):
        self.tm.insert(5, 50)
        self.tm.insert(5, 99)

        self.assertEqual(self.tm.get(5), 99)
        self.assertEqual(self.tm.getInorderKeys(), [5])

    def test_get_min_and_max(self):
        self.tm.insert(10, 100)
        self.tm.insert(5, 50)
        self.tm.insert(20, 200)
        self.tm.insert(3, 30)

        self.assertEqual(self.tm.getMin(), 30)
        self.assertEqual(self.tm.getMax(), 200)

    def test_inorder_keys_sorted(self):
        keys = [10, 5, 15, 3, 7, 12, 18]
        for k in keys:
            self.tm.insert(k, k * 10)

        self.assertEqual(self.tm.getInorderKeys(), sorted(keys))

    def test_remove_leaf_node(self):
        self.tm.insert(5, 50)
        self.tm.insert(3, 30)
        self.tm.insert(7, 70)

        self.tm.remove(3)

        self.assertEqual(self.tm.get(3), -1)
        self.assertEqual(self.tm.getInorderKeys(), [5, 7])

    def test_remove_node_with_one_child(self):
        self.tm.insert(5, 50)
        self.tm.insert(3, 30)
        self.tm.insert(2, 20)

        self.tm.remove(3)

        self.assertEqual(self.tm.get(3), -1)
        self.assertEqual(self.tm.get(2), 20)
        self.assertEqual(self.tm.getInorderKeys(), [2, 5])

    def test_remove_node_with_two_children(self):
        self.tm.insert(10, 100)
        self.tm.insert(5, 50)
        self.tm.insert(15, 150)
        self.tm.insert(12, 120)
        self.tm.insert(18, 180)

        self.tm.remove(15)

        self.assertEqual(self.tm.get(15), -1)
        self.assertEqual(self.tm.getInorderKeys(), [5, 10, 12, 18])

    def test_remove_root(self):
        self.tm.insert(10, 100)
        self.tm.insert(5, 50)
        self.tm.insert(15, 150)

        self.tm.remove(10)

        self.assertEqual(self.tm.get(10), -1)
        self.assertEqual(self.tm.getInorderKeys(), [5, 15])

    def test_remove_non_existent_key(self):
        self.tm.insert(5, 50)
        self.tm.insert(3, 30)

        self.tm.remove(100)

        self.assertEqual(self.tm.getInorderKeys(), [3, 5])


if __name__ == "__main__":
    unittest.main()
