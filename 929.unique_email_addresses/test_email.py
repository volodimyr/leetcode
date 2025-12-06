import unittest
from typing import List
from email import Solution

class TestUniqueEmails(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        emails = [
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com"
        ]
        self.assertEqual(self.sol.numUniqueEmails(emails), 2)

    def test_example_2(self):
        emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
        self.assertEqual(self.sol.numUniqueEmails(emails), 3)

    def test_same_local_different_domain(self):
        emails = [
            "user.name+tag@leetcode.com",
            "username@leet.code.com"
        ]
        self.assertEqual(self.sol.numUniqueEmails(emails), 2)

    def test_plus_handling(self):
        emails = [
            "abc+foo@leetcode.com",
            "abc+bar@leetcode.com",
            "abc@leetcode.com"
        ]
        self.assertEqual(self.sol.numUniqueEmails(emails), 1)

    def test_dot_handling(self):
        emails = [
            "a.b.c@leetcode.com",
            "abc@leetcode.com",
            "a.b.c+d.e.f@leetcode.com"
        ]
        self.assertEqual(self.sol.numUniqueEmails(emails), 1)

    def test_no_plus_no_dot(self):
        emails = [
            "simple@leetcode.com",
            "simple@leetcode.com"
        ]
        self.assertEqual(self.sol.numUniqueEmails(emails), 1)

    def test_mixed_domains(self):
        emails = [
            "test.email+alex@leetcode.com",
            "test.email@lee.tcode.com",
            "testemail@lee.tcode.com"
        ]
        self.assertEqual(self.sol.numUniqueEmails(emails), 2)


if __name__ == "__main__":
    unittest.main()
