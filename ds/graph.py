from collections import deque

class Graph:
    def __init__(self):
        self.nodes = {}

    def addEdge(self, src: int, dst: int) -> None:
        neighbours = []
        if src in self.nodes:
            neighbours = self.nodes[src]
        if dst not in neighbours:
            neighbours.append(dst)
            self.nodes[src] = neighbours
        if dst not in self.nodes:
            self.nodes[dst] = []

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.nodes:
            return False
        neighbours = self.nodes[src]
        if dst not in neighbours:
            return False
        neighbours.remove(dst)
        self.nodes[src] = neighbours
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        if src == dst:
            return True
        visit = set()
        q = deque(self.nodes[src])
        while q:
            neighbour = q.popleft()
            if neighbour in visit:
                continue
            if neighbour == dst:
                return True
            visit.add(neighbour)
            for n in self.nodes[neighbour]:
                q.append(n)
        return False
        

# Test Cases

def test_basic_operations():
    """Test basic add edge and has path operations"""
    g = Graph()
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    assert g.hasPath(1, 3) == True, "Should have path 1->2->3"
    assert g.hasPath(3, 1) == False, "Should not have path 3->1 (directed)"
    print("✓ Basic operations test passed")

def test_remove_edge():
    """Test edge removal"""
    g = Graph()
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    assert g.removeEdge(1, 2) == True, "Should successfully remove edge 1->2"
    assert g.hasPath(1, 3) == False, "Should not have path after removing edge"
    assert g.removeEdge(1, 2) == False, "Should return False when removing non-existent edge"
    print("✓ Remove edge test passed")

def test_cycle_detection():
    """Test graph with cycles"""
    g = Graph()
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    assert g.hasPath(1, 3) == True, "Should have path 1->2->3"
    assert g.hasPath(3, 1) == True, "Should have path 3->1 (cycle exists)"
    assert g.hasPath(2, 2) == True, "Should have path to itself through cycle"
    print("✓ Cycle detection test passed")

def test_disconnected_components():
    """Test graph with disconnected components"""
    g = Graph()
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(4, 5)
    g.addEdge(5, 6)
    assert g.hasPath(1, 3) == True, "Should have path in first component"
    assert g.hasPath(4, 6) == True, "Should have path in second component"
    assert g.hasPath(1, 6) == False, "Should not have path between components"
    assert g.hasPath(4, 2) == False, "Should not have path between components"
    print("✓ Disconnected components test passed")

def test_remove_nonexistent_edge():
    """Test removing edges from non-existent vertices"""
    g = Graph()
    g.addEdge(1, 2)
    assert g.removeEdge(3, 4) == False, "Should return False for non-existent vertices"
    assert g.removeEdge(1, 3) == False, "Should return False when dst doesn't exist"
    assert g.removeEdge(3, 2) == False, "Should return False when src doesn't exist"
    print("✓ Remove nonexistent edge test passed")

def test_duplicate_edge():
    """Test adding duplicate edges"""
    g = Graph()
    g.addEdge(1, 2)
    g.addEdge(1, 2)  # Duplicate - should not create multiple edges
    g.addEdge(1, 2)  # Another duplicate
    assert g.hasPath(1, 2) == True, "Should have path"
    assert g.removeEdge(1, 2) == True, "Should remove edge"
    assert g.hasPath(1, 2) == False, "Should not have path after single removal"
    print("✓ Duplicate edge test passed")

def test_single_vertex():
    """Test operations with single vertex"""
    g = Graph()
    g.addEdge(1, 2)
    g.removeEdge(1, 2)
    # After removal, vertices still exist but no edges
    # hasPath assumes both vertices exist
    print("✓ Single vertex test passed")

def test_complex_graph():
    """Test more complex graph structure"""
    g = Graph()
    # Create a diamond shape: 1->2, 1->3, 2->4, 3->4
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 4)
    g.addEdge(3, 4)
    assert g.hasPath(1, 4) == True, "Should have path 1->2->4"
    g.removeEdge(2, 4)
    assert g.hasPath(1, 4) == True, "Should still have path 1->3->4"
    g.removeEdge(3, 4)
    assert g.hasPath(1, 4) == False, "Should not have path after removing both edges to 4"
    print("✓ Complex graph test passed")

def test_long_path():
    """Test longer paths"""
    g = Graph()
    # Create chain: 1->2->3->4->5->6->7->8->9->10
    for i in range(1, 10):
        g.addEdge(i, i + 1)
    assert g.hasPath(1, 10) == True, "Should have long path"
    assert g.hasPath(10, 1) == False, "Should not have reverse path"
    g.removeEdge(5, 6)  # Break the chain
    assert g.hasPath(1, 10) == False, "Should not have path after breaking chain"
    assert g.hasPath(1, 5) == True, "Should have path to middle"
    assert g.hasPath(6, 10) == True, "Should have path from middle to end"
    print("✓ Long path test passed")

def test_empty_graph():
    """Test operations on empty graph"""
    g = Graph()
    assert g.removeEdge(1, 2) == False, "Should return False on empty graph"
    print("✓ Empty graph test passed")

def test_bidirectional_edges():
    """Test that directed edges work correctly"""
    g = Graph()
    g.addEdge(1, 2)
    g.addEdge(2, 1)  # Add reverse edge
    assert g.hasPath(1, 2) == True, "Should have path 1->2"
    assert g.hasPath(2, 1) == True, "Should have path 2->1"
    g.removeEdge(1, 2)
    assert g.hasPath(1, 2) == False, "Should not have path 1->2 after removal"
    assert g.hasPath(2, 1) == True, "Should still have path 2->1"
    print("✓ Bidirectional edges test passed")

# Run all tests
if __name__ == "__main__":
    test_basic_operations()
    test_remove_edge()
    test_cycle_detection()
    test_disconnected_components()
    test_remove_nonexistent_edge()
    test_duplicate_edge()
    test_single_vertex()
    test_complex_graph()
    test_long_path()
    test_empty_graph()
    test_bidirectional_edges()
    print("\n✅ All tests passed!")