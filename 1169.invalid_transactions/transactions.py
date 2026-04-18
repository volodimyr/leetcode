# 1169. Invalid Transactions
# Topics: 'Array', 'Hash Table', 'String', 'Sorting'
# Level: 'Medium'

# A transaction is possibly invalid if:

#     the amount exceeds $1000, or;
#     if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.

# You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

# Return a list of transactions that are possibly invalid. You may return the answer in any order.

 

# Example 1:

# Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
# Output: ["alice,20,800,mtv","alice,50,100,beijing"]
# Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.

# Example 2:

# Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
# Output: ["alice,50,1200,mtv"]

# Example 3:

# Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
# Output: ["bob,50,1200,mtv"]

 

# Constraints:

#     transactions.length <= 1000
#     Each transactions[i] takes the form "{name},{time},{amount},{city}"
#     Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
#     Each {time} consist of digits, and represent an integer between 0 and 1000.
#     Each {amount} consist of digits, and represent an integer between 0 and 2000.

from collections import deque

class Solution:
    def invalidTransactions(self, transactions):
        transactions = sorted(transactions, key=lambda x: int(x.split(",")[1]))
        
        q = deque()
        res = []
        added = set()
        for tnum, t in enumerate(transactions):
            name, time, amount, city = t.split(',')
            time = int(time)
            amount = int(amount)

            while q and q[0][1] + 60 < time:
                q.popleft()

            if amount > 1000:
                res.append(t)
                added.add(tnum)

            for name1, _, city1, tnum1, t1 in q:
                if name1 == name and city1 != city:
                    if tnum not in added:
                        res.append(t)
                        added.add(tnum)
                    if tnum1 not in added:
                        res.append(t1)
                        added.add(tnum1)

            q.append((name, time, city, tnum, t))

        return res