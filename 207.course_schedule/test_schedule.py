from typing import List
from collections import deque
from schedule import Solution

def test_course_schedule():
    solution = Solution()
    
    # Test 1: Example 1 - Simple valid case
    assert solution.canFinish(2, [[1, 0]]) == True, "Test 1 failed"
    print("✓ Test 1 passed: Simple valid case")
    
    # Test 2: Example 2 - Simple cycle
    assert solution.canFinish(2, [[1, 0], [0, 1]]) == False, "Test 2 failed"
    print("✓ Test 2 passed: Simple cycle")
    
    # Test 3: No prerequisites
    assert solution.canFinish(3, []) == True, "Test 3 failed"
    print("✓ Test 3 passed: No prerequisites")
    
    # Test 4: Single course
    assert solution.canFinish(1, []) == True, "Test 4 failed"
    print("✓ Test 4 passed: Single course")
    
    # Test 5: Linear dependency chain
    assert solution.canFinish(4, [[1, 0], [2, 1], [3, 2]]) == True, "Test 5 failed"
    print("✓ Test 5 passed: Linear dependency chain")
    
    # Test 6: Complex valid dependencies
    assert solution.canFinish(5, [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3]]) == True, "Test 6 failed"
    print("✓ Test 6 passed: Complex valid dependencies")
    
    # Test 7: Cycle in middle of chain
    assert solution.canFinish(3, [[0, 1], [1, 2], [2, 1]]) == False, "Test 7 failed"
    print("✓ Test 7 passed: Cycle in middle of chain")
    
    # Test 8: Self-loop
    assert solution.canFinish(2, [[0, 0]]) == False, "Test 8 failed"
    print("✓ Test 8 passed: Self-loop")
    
    # Test 9: Multiple disconnected components, all valid
    assert solution.canFinish(4, [[1, 0], [3, 2]]) == True, "Test 9 failed"
    print("✓ Test 9 passed: Multiple disconnected components (valid)")
    
    # Test 10: Multiple components, one has cycle
    assert solution.canFinish(4, [[1, 0], [3, 2], [2, 3]]) == False, "Test 10 failed"
    print("✓ Test 10 passed: Multiple components with cycle")
    
    # Test 11: Large cycle
    assert solution.canFinish(5, [[1, 0], [2, 1], [3, 2], [4, 3], [0, 4]]) == False, "Test 11 failed"
    print("✓ Test 11 passed: Large cycle")
    
    # Test 12: Diamond dependency (valid)
    assert solution.canFinish(4, [[2, 0], [2, 1], [3, 2]]) == True, "Test 12 failed"
    print("✓ Test 12 passed: Diamond dependency")
    
    # Test 13: Course with multiple prerequisites
    assert solution.canFinish(3, [[2, 0], [2, 1]]) == True, "Test 13 failed"
    print("✓ Test 13 passed: Course with multiple prerequisites")
    
    # Test 14: Complex cycle detection
    assert solution.canFinish(6, [[1, 0], [2, 1], [3, 2], [1, 3], [4, 3], [5, 4]]) == False, "Test 14 failed"
    print("✓ Test 14 passed: Complex cycle detection")
    
    # Test 15: All courses depend on one course
    assert solution.canFinish(5, [[1, 0], [2, 0], [3, 0], [4, 0]]) == True, "Test 15 failed"
    print("✓ Test 15 passed: All courses depend on one")
    
    # Test 16: Many courses, no prerequisites
    assert solution.canFinish(100, []) == True, "Test 16 failed"
    print("✓ Test 16 passed: Many courses, no prerequisites")
    
    # Test 17: Duplicate prerequisites (should still work)
    assert solution.canFinish(2, [[1, 0], [1, 0]]) == True, "Test 17 failed"
    print("✓ Test 17 passed: Duplicate prerequisites")
    
    # Test 18: Course 0 depending on itself through chain
    assert solution.canFinish(3, [[1, 0], [2, 1], [0, 2]]) == False, "Test 18 failed"
    print("✓ Test 18 passed: Indirect self-dependency")
    
    print("\n" + "="*50)
    print("All tests passed! ✓")
    print("="*50)


if __name__ == "__main__":
    test_course_schedule()