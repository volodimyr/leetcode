import unittest
from merge import Solution


def sort_output(res):
    """
    Normalize output for comparison:
    - Emails sorted
    - Accounts sorted by (name, emails)
    """
    return sorted([ [acc[0]] + sorted(acc[1:]) for acc in res ])


class TestAccountsMerge(unittest.TestCase):

    def test_example_1(self):
        accounts = [
            ["John","johnsmith@mail.com","john_newyork@mail.com"],
            ["John","johnsmith@mail.com","john00@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]
        ]

        expected = [
            ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]
        ]

        sol = Solution()
        output = sol.accountsMerge(accounts)

        self.assertEqual(sort_output(output), sort_output(expected))

    def test_example_2(self):
        accounts = [
            ["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
            ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
            ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
            ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
            ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]
        ]

        expected = [
            ["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
            ["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
            ["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
            ["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
            ["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]
        ]

        sol = Solution()
        output = sol.accountsMerge(accounts)

        self.assertEqual(sort_output(output), sort_output(expected))

    def test_no_merge_same_name(self):
        accounts = [
            ["John","a@mail.com"],
            ["John","b@mail.com"],
            ["John","c@mail.com"]
        ]

        expected = [
            ["John","a@mail.com"],
            ["John","b@mail.com"],
            ["John","c@mail.com"]
        ]

        sol = Solution()
        output = sol.accountsMerge(accounts)

        self.assertEqual(sort_output(output), sort_output(expected))

    def test_multiple_chain_merging(self):
        accounts = [
            ["Alice","a@mail.com","b@mail.com"],
            ["Alice","b@mail.com","c@mail.com"],
            ["Alice","x@mail.com"]
        ]

        expected = [
            ["Alice","a@mail.com","b@mail.com","c@mail.com"],
            ["Alice","x@mail.com"]
        ]

        sol = Solution()
        output = sol.accountsMerge(accounts)

        self.assertEqual(sort_output(output), sort_output(expected))

    def test_cross_account_merge(self):
        # invalid according to problem but tests algorithm robustness
        accounts = [
            ["X","1@mail.com","2@mail.com"],
            ["Y","2@mail.com","3@mail.com"],
            ["Z","3@mail.com","4@mail.com"]
        ]
        sol = Solution()
        out = sol.accountsMerge(accounts)

        # just ensure no crash and something returned
        self.assertTrue(len(out) >= 1)

    def test_multiple_people_same_name_but_with_clusters(self):
        accounts = [
            ["Bob","a@mail.com","b@mail.com"],
            ["Bob","b@mail.com","c@mail.com"],
            ["Bob","x@mail.com"],
            ["Bob","y@mail.com","z@mail.com"],
            ["Bob","z@mail.com","t@mail.com"],
        ]

        expected = [
            ["Bob","a@mail.com","b@mail.com","c@mail.com"],
            ["Bob","x@mail.com"],
            ["Bob","t@mail.com","y@mail.com","z@mail.com"]
        ]

        sol = Solution()
        output = sol.accountsMerge(accounts)

        self.assertEqual(sort_output(output), sort_output(expected))

    def test_email_order_randomized(self):
        accounts = [
            ["John","c@mail.com","a@mail.com","b@mail.com"],
            ["John","b@mail.com","d@mail.com"]
        ]

        expected = [
            ["John","a@mail.com","b@mail.com","c@mail.com","d@mail.com"]
        ]

        sol = Solution()
        output = sol.accountsMerge(accounts)

        self.assertEqual(sort_output(output), sort_output(expected))

    def test_single_account(self):
        accounts = [["Alice","one@mail.com","two@mail.com"]]

        sol = Solution()
        output = sol.accountsMerge(accounts)

        self.assertEqual(output, [["Alice","one@mail.com","two@mail.com"]])

    def test_many_isolated_accounts(self):
        accounts = [["Name", f"{i}@mail.com"] for i in range(100)]

        sol = Solution()
        out = sol.accountsMerge(accounts)

        self.assertEqual(len(out), 100)
        self.assertTrue(all(len(acc) == 2 for acc in out))


if __name__ == "__main__":
    unittest.main()
