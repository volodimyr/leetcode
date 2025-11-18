import unittest
from collections import deque
from clone import Node, Solution

# Assuming Node and Solution are already defined above

class TestCloneGraph(unittest.TestCase):
    def build_graph(self, adj):
        if not adj:
            return None
        nodes = {i+1: Node(i+1) for i in range(len(adj))}
        for i, neighbors in enumerate(adj, start=1):
            nodes[i].neighbors = [nodes[n] for n in neighbors]
        return nodes[1]

    def graph_to_adj(self, node):
        if not node:
            return []
        adj = {}
        q = deque([node])
        seen = set()
        while q:
            cur = q.popleft()
            if cur.val in seen:
                continue
            seen.add(cur.val)
            adj[cur.val] = [n.val for n in cur.neighbors]
            for n in cur.neighbors:
                q.append(n)
        return [adj[i] for i in sorted(adj.keys())]

    def test_empty_graph(self):
        sol = Solution()
        self.assertIsNone(sol.cloneGraph(None))

    def test_single_node(self):
        start = self.build_graph([[]])
        sol = Solution()
        cloned = sol.cloneGraph(start)
        self.assertEqual(self.graph_to_adj(cloned), [[]])
        self.assertIsNot(cloned, start)

    def test_two_nodes_connected(self):
        start = self.build_graph([[2], [1]])
        sol = Solution()
        cloned = sol.cloneGraph(start)
        self.assertEqual(self.graph_to_adj(cloned), [[2], [1]])
        self.assertIsNot(cloned, start)

    def test_four_cycle(self):
        start = self.build_graph([[2,4],[1,3],[2,4],[1,3]])
        sol = Solution()
        cloned = sol.cloneGraph(start)
        self.assertEqual(
            self.graph_to_adj(cloned),
            [[2,4],[1,3],[2,4],[1,3]]
        )
        self.assertIsNot(cloned, start)

    def test_branch_graph(self):
        start = self.build_graph([[2,3], [4], [4], []])
        sol = Solution()
        cloned = sol.cloneGraph(start)
        self.assertEqual(
            self.graph_to_adj(cloned),
            [[2,3], [4], [4], []]
        )
        self.assertIsNot(cloned, start)

class TestCloneGraph1(unittest.TestCase):
    def build_diamond_graph(self):
        # 1-2-3
        #  \ | /
        #    4
        
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)

        n1.neighbors = [n2, n3]
        n2.neighbors = [n1, n4, n3]
        n3.neighbors = [n1, n2, n4]
        n4.neighbors = [n2, n3]

        return n1

    def collect_edges(self, node):
        # helper to serialize the graph for comparison
        visited = set()
        q = deque([node])
        edges = {}

        while q:
            cur = q.popleft()
            if cur.val in visited:
                continue
            visited.add(cur.val)
            edges[cur.val] = sorted([n.val for n in cur.neighbors])
            for n in cur.neighbors:
                q.append(n)

        return edges

    def test_diamond_graph(self):
        sol = Solution()
        original = self.build_diamond_graph()
        cloned = sol.cloneGraph(original)

        original_edges = self.collect_edges(original)
        cloned_edges = self.collect_edges(cloned)

        self.assertEqual(original_edges, cloned_edges)


if __name__ == "__main__":
    unittest.main()
