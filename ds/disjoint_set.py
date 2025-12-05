# Design Disjoint Set (Union-Find)

# Design a Disjoint Set (aka Union-Find) class.

# Your UnionFind class should support the following operations:

#     UnionFind(int n) will initialize a disjoint set of size n.
#     int find(int x) will return the root of the component that x belongs to.
#     bool isSameComponent(int x, int y) will return whether x and y belong to the same component.
#     bool union(int x, int y) will union the components that x and y belong to. If they are already in the same component, return false, otherwise return true.
#     int getNumComponents() will return the number of components in the disjoint set.

# Example 1:

# Input:
# ["UnionFind", 10, "isSameComponent", 1, 3, "union", 1, 2, "union", 2, 3, "getNumComponents", "isSameComponent", 1, 3]

# Output:
# [null, 1, false, true, true, 8, true]

# Note: The find method will not be directly tested, but you will need to use it in the implementation of the other methods. Thus, it will be tested indirectly.


class UnionFind:
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}
        self.n = n
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        p = self.parent[x]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        return True

    def getNumComponents(self) -> int:
        c = set()
        for i in range(self.n):
            c.add(self.find(i))
        return len(c)