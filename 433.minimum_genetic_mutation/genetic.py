# 433. Minumum Genetic Mutation
# Topics: 'Hash Table', 'String', 'Breadth-First Search'
# Level: 'Medium'


# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

# Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

#     For example, "AACCGGTT" --> "AACCGGTA" is one mutation.

# There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

# Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

# Note that the starting point is assumed to be valid, so it might not be included in the bank.

 

# Example 1:

# Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
# Output: 1

# Example 2:

# Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2

 

# Constraints:

#     0 <= bank.length <= 10
#     startGene.length == endGene.length == bank[i].length == 8
#     startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].

from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        set_bank = set(bank)
        if startGene == endGene:
            return 0
        if endGene not in set_bank:
            return -1
        
        q = deque()
        q.append((startGene, 0))
        genes = ['A', 'C', 'G', 'T']
        visit = set()
        visit.add(startGene)
        
        while q:
            pop, steps = q.popleft()
            if pop == endGene:
                return steps

            for i in range(8):
                for char in genes:
                    if char == pop[i]:
                        continue
                    mutation = pop[:i] + char + pop[i+1:]
                    if mutation not in visit and mutation in set_bank:
                        visit.add(mutation)
                        q.append((mutation, steps+1))
        return -1

# class Solution:
#     def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
#         if startGene == endGene:
#             return 0
#         if endGene not in bank:
#             return -1
#         adj = {}
#         adj[startGene] = []
#         for i in range(len(bank)):
#             adj[bank[i]] = []
#             if self.has_edge(startGene, bank[i]):
#                 adj[startGene].append(bank[i])
#                 adj[bank[i]].append(startGene)
        
#         for i in range(len(bank)-1):
#             for j in range(i+1, len(bank)):
#                 if self.has_edge(bank[i], bank[j]):
#                     adj[bank[i]].append(bank[j])
#                     adj[bank[j]].append(bank[i])
        
#         q = deque()
#         visit = set()
#         visit.add(startGene)
#         for dst in adj[startGene]:
#             visit.add(dst)
#             q.append(dst)
        
#         count = 0
#         while q:
#             count+=1
#             for i in range(len(q)):
#                 pop = q.popleft()
#                 if pop == endGene:
#                     return count
#                 for dst in adj[pop]:
#                     if dst not in visit:
#                         visit.add(dst)
#                         q.append(dst)

                
#         return -1
    
#     def has_edge(self, g1: str, g2: str) -> bool:
#         if g1 == g2:
#             return False
#         count = 0
#         for i in range(8):
#             if g1[i] != g2[i]:
#                 count+=1
#             if count > 1:
#                 return False

#         return True