import heapq
from typing import List
from cpu import Solution

# Test Suite
def run_tests():
    sol = Solution()
    
    # Test 1: Example 1 from problem
    tasks = [[1,2],[2,4],[3,2],[4,1]]
    result = sol.getOrder(tasks)
    expected = [0,2,3,1]
    assert result == expected, f"Test 1 failed: expected {expected}, got {result}"
    print("[PASS] Test 1 passed: Example 1")
    
    # Test 2: Example 2 from problem
    tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
    result = sol.getOrder(tasks)
    expected = [4,3,2,0,1]
    assert result == expected, f"Test 2 failed: expected {expected}, got {result}"
    print("[PASS] Test 2 passed: Example 2 (all tasks at same time)")
    
    # Test 3: Single task
    tasks = [[1,5]]
    result = sol.getOrder(tasks)
    expected = [0]
    assert result == expected, f"Test 3 failed: expected {expected}, got {result}"
    print("[PASS] Test 3 passed: Single task")
    
    # Test 4: Tasks with same processing time (tie-breaker by index)
    tasks = [[0,3],[0,3],[0,3]]
    result = sol.getOrder(tasks)
    expected = [0,1,2]
    assert result == expected, f"Test 4 failed: expected {expected}, got {result}"
    print("[PASS] Test 4 passed: Same processing time, sorted by index")
    
    # Test 5: Sequential tasks (no overlap)
    tasks = [[1,2],[5,3],[10,1]]
    result = sol.getOrder(tasks)
    expected = [0,1,2]
    assert result == expected, f"Test 5 failed: expected {expected}, got {result}"
    print("[PASS] Test 5 passed: Sequential non-overlapping tasks")
    
    # Test 6: Tasks with gaps (CPU idle periods)
    tasks = [[1,2],[10,3],[20,1]]
    result = sol.getOrder(tasks)
    expected = [0,1,2]
    assert result == expected, f"Test 6 failed: expected {expected}, got {result}"
    print("[PASS] Test 6 passed: Tasks with idle gaps")
    
    # Test 7: All tasks start at time 0
    tasks = [[0,5],[0,3],[0,4]]
    result = sol.getOrder(tasks)
    expected = [1,2,0]
    assert result == expected, f"Test 7 failed: expected {expected}, got {result}"
    print("[PASS] Test 7 passed: All tasks at time 0")
    
    # Test 8: Tasks arrive while processing
    tasks = [[0,10],[1,1],[2,1],[3,1]]
    result = sol.getOrder(tasks)
    expected = [0,1,2,3]
    assert result == expected, f"Test 8 failed: expected {expected}, got {result}"
    print("[PASS] Test 8 passed: Tasks arrive during long processing")
    
    # Test 9: Later task has shorter processing time
    tasks = [[0,5],[1,2]]
    result = sol.getOrder(tasks)
    expected = [0,1]
    assert result == expected, f"Test 9 failed: expected {expected}, got {result}"
    print("[PASS] Test 9 passed: Later task can't interrupt")
    
    # Test 10: Multiple tasks become available, choose shortest
    tasks = [[1,5],[2,2],[2,3],[2,1]]
    result = sol.getOrder(tasks)
    expected = [0,3,1,2]
    assert result == expected, f"Test 10 failed: expected {expected}, got {result}"
    print("[PASS] Test 10 passed: Choose shortest among available")
    
    # Test 11: Large enqueue times (testing time jump)
    tasks = [[1000000000,1],[1000000001,1]]
    result = sol.getOrder(tasks)
    expected = [0,1]
    assert result == expected, f"Test 11 failed: expected {expected}, got {result}"
    print("[PASS] Test 11 passed: Large enqueue times")
    
    # Test 12: Same enqueue and processing, different indices
    tasks = [[5,5],[5,5],[5,5]]
    result = sol.getOrder(tasks)
    expected = [0,1,2]
    assert result == expected, f"Test 12 failed: expected {expected}, got {result}"
    print("[PASS] Test 12 passed: Identical tasks, sorted by index")
    
    # Test 13: Reverse order arrival
    tasks = [[10,1],[5,1],[1,1]]
    result = sol.getOrder(tasks)
    expected = [2,1,0]
    assert result == expected, f"Test 13 failed: expected {expected}, got {result}"
    print("[PASS] Test 13 passed: Tasks arrive in reverse order")
    
    # Test 14: Mix of short and long tasks
    tasks = [[1,100],[2,1],[3,1],[4,1]]
    result = sol.getOrder(tasks)
    expected = [0,1,2,3]
    assert result == expected, f"Test 14 failed: expected {expected}, got {result}"
    print("[PASS] Test 14 passed: Long task followed by short tasks")
    
    # Test 15: Tasks that pile up during processing
    tasks = [[0,50],[10,1],[20,1],[30,1],[40,1]]
    result = sol.getOrder(tasks)
    expected = [0,1,2,3,4]
    assert result == expected, f"Test 15 failed: expected {expected}, got {result}"
    print("[PASS] Test 15 passed: Tasks pile up during long processing")
    
    # Test 16: Edge case - two tasks, second has same enqueue as first finishes
    tasks = [[1,2],[3,1]]
    result = sol.getOrder(tasks)
    expected = [0,1]
    assert result == expected, f"Test 16 failed: expected {expected}, got {result}"
    print("[PASS] Test 16 passed: Task arrives exactly when CPU becomes free")
    
    # Test 17: Multiple tasks with complex tie-breaking
    tasks = [[0,5],[0,5],[0,3],[0,3]]
    result = sol.getOrder(tasks)
    expected = [2,3,0,1]
    assert result == expected, f"Test 17 failed: expected {expected}, got {result}"
    print("[PASS] Test 17 passed: Complex tie-breaking scenario")
    
    print("\n" + "="*50)
    print("All 17 tests passed! [PASS]")
    print("="*50)

if __name__ == "__main__":
    run_tests()