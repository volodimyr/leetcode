# 721. Accounts Merge
# Topics: 'Array', 'Hash Table', 'String', 'Depth-First Search', 'Breadth-First Search', 'Union Find', 'Sorting'
# Level: 'Medium'

# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

 

# Example 1:

# Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Explanation:
# The first and second John's are the same person as they have the common email "johnsmith@mail.com".
# The third John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

# Example 2:

# Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
# Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]

 

# Constraints:

#     1 <= accounts.length <= 1000
#     2 <= accounts[i].length <= 10
#     1 <= accounts[i][j].length <= 30
#     accounts[i][0] consists of English letters.
#     accounts[i][j] (for j > 0) is a valid email.

from typing import List

class UnionFind:
    def __init__(self, accounts: List[List[str]]):
        self.par = {}
        self.rank = {}
        self.names = {}

        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                self.names[accounts[i][j]] = accounts[i][0]
                self.par[accounts[i][j]] = accounts[i][j]
                self.rank[accounts[i][j]] = 0
    
    def find(self, x: str) -> str:
        p = self.par[x]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def add(self, x1: str, x2: str):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2]+=1



class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union = UnionFind(accounts)
        for i in range(len(accounts)):
            for j in range(2, len(accounts[i])):
                union.add(accounts[i][1], accounts[i][j])
        
        comps = {}
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                p = union.find(accounts[i][j])
                if p not in comps:
                    comps[p] = set()
                comps[p].add(accounts[i][j]) 

        res = []
        for p, emails in comps.items():
            name = union.names[p]
            sorted_emails = sorted(emails)
            res.append([name] + sorted_emails)

        return res

