import unittest
from phone_directory import PhoneDirectory


class TestPhoneDirectory(unittest.TestCase):

    def test_get_returns_valid_number(self):
        pd = PhoneDirectory(3)
        num = pd.get()
        self.assertIn(num, [0, 1, 2])

    def test_get_exhausts_all_slots(self):
        pd = PhoneDirectory(3)
        nums = {pd.get(), pd.get(), pd.get()}
        self.assertEqual(nums, {0, 1, 2})

    def test_get_when_empty_returns_minus_one(self):
        pd = PhoneDirectory(1)
        pd.get()
        self.assertEqual(pd.get(), -1)

    def test_check_available(self):
        pd = PhoneDirectory(3)
        self.assertTrue(pd.check(2))

    def test_check_after_get(self):
        pd = PhoneDirectory(3)
        num = pd.get()
        self.assertFalse(pd.check(num))

    def test_release_makes_slot_available(self):
        pd = PhoneDirectory(3)
        num = pd.get()
        pd.release(num)
        self.assertTrue(pd.check(num))

    def test_release_allows_get(self):
        pd = PhoneDirectory(1)
        num = pd.get()
        self.assertEqual(pd.get(), -1)
        pd.release(num)
        self.assertEqual(pd.get(), num)

    def test_example_sequence(self):
        pd = PhoneDirectory(3)
        n1 = pd.get()
        n2 = pd.get()
        self.assertTrue(pd.check(2))
        n3 = pd.get()
        self.assertFalse(pd.check(n3))
        pd.release(n3)
        self.assertTrue(pd.check(n3))


if __name__ == "__main__":
    unittest.main()
