import unittest
from system import FileSystem


class TestFileSystem(unittest.TestCase):

    def test_example1(self):
        fs = FileSystem()
        self.assertTrue(fs.createPath("/a", 1))
        self.assertEqual(fs.get("/a"), 1)

    def test_example2(self):
        fs = FileSystem()
        self.assertTrue(fs.createPath("/neet", 1))
        self.assertTrue(fs.createPath("/neet/code", 2))
        self.assertEqual(fs.get("/neet/code"), 2)
        self.assertFalse(fs.createPath("/c/d", 1))
        self.assertEqual(fs.get("/c"), -1)

    def test_duplicate_path(self):
        fs = FileSystem()
        self.assertTrue(fs.createPath("/a", 1))
        self.assertFalse(fs.createPath("/a", 2))

    def test_get_nonexistent(self):
        fs = FileSystem()
        self.assertEqual(fs.get("/missing"), -1)

    def test_nested_path(self):
        fs = FileSystem()
        self.assertTrue(fs.createPath("/a", 1))
        self.assertTrue(fs.createPath("/a/b", 2))
        self.assertTrue(fs.createPath("/a/b/c", 3))
        self.assertEqual(fs.get("/a"), 1)
        self.assertEqual(fs.get("/a/b"), 2)
        self.assertEqual(fs.get("/a/b/c"), 3)

    def test_missing_parent(self):
        fs = FileSystem()
        self.assertFalse(fs.createPath("/a/b", 1))

    def test_root_path_invalid(self):
        fs = FileSystem()
        self.assertFalse(fs.createPath("/", 1))
        self.assertEqual(fs.get("/"), -1)

    def test_sibling_paths(self):
        fs = FileSystem()
        self.assertTrue(fs.createPath("/a", 1))
        self.assertTrue(fs.createPath("/b", 2))
        self.assertEqual(fs.get("/a"), 1)
        self.assertEqual(fs.get("/b"), 2)


if __name__ == "__main__":
    unittest.main()
