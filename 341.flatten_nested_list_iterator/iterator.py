# 341. Flatter Nested List Iterator
# Topics: 'Stack', 'Tree', 'Depth-First Search', 'Design', 'Queue', 'Iterator'
# Level: 'Medium'

# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

# Implement the NestedIterator class:

#     NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
#     int next() Returns the next integer in the nested list.
#     boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.

# Your code will be tested with the following pseudocode:

# initialize iterator with nestedList
# res = []
# while iterator.hasNext()
#     append iterator.next() to the end of res
# return res

# If res matches the expected flattened list, then your code will be judged as correct.

 

# Example 1:

# Input: nestedList = [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

# Example 2:

# Input: nestedList = [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].

 

# Constraints:

#     1 <= nestedList.length <= 500
#     The values of the integers in the nested list is in the range [-106, 106].

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """

#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """

#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
# #        """

# crazy good solution
# extend stack if not a number
# lazy initialization
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]

    def next(self) -> int:
        return self.stack.pop().getInteger()
            
    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.extend(self.stack.pop().getList()[::-1])
        return False


# Lazy initialization each NestedInteger tree
# class NestedIterator:
#     def __init__(self, nestedList: [NestedInteger]):
#         self.i = 0
#         self.nestedList = nestedList
#         self.q = deque()

#     def next(self) -> int:
#         return self.q.popleft()
            
#     def hasNext(self) -> bool:
#         while not self.q:
#             if self.i >= len(self.nestedList):
#                 break
#             self.dfs(self.nestedList[self.i])
#             self.i+=1
#         return self.q

#     def dfs(self, root: NestedInteger):
#         if not root:
#             return
#         else:
#             if root.isInteger():
#                 self.q.append(root.getInteger())
#             else:
#                 for ni in root.getList():
#                     self.dfs(ni)

# Eager initialization
# class NestedIterator:
#     def __init__(self, nestedList: [NestedInteger]):
#         self.arr = []
#         self.i = 0
#         def dfs(root: NestedInteger):
#             if not root:
#                 return
#             if root.isInteger():
#                 self.arr.append(root.getInteger())
#             else:
#                 for ni in root.getList():
#                     dfs(ni)
#         for ni in nestedList:
#             dfs(ni)
            

#     def next(self) -> int:
#         v = self.arr[self.i]
#         self.i+=1
#         return v
    
#     def hasNext(self) -> bool:
#         return self.i < len(self.arr)
         
