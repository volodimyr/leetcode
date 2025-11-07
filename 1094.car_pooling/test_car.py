import heapq
from typing import List
from car import Solution

def test_car_pooling():
    solution = Solution()
    
    # Test 1: Example 1 - Should fail (capacity exceeded)
    trips1 = [[2,1,5],[3,3,7]]
    capacity1 = 4
    assert solution.carPooling(trips1, capacity1) == False, "Test 1 Failed"
    print("✓ Test 1 passed: Capacity exceeded correctly detected")
    
    # Test 2: Example 2 - Should pass
    trips2 = [[2,1,5],[3,3,7]]
    capacity2 = 5
    assert solution.carPooling(trips2, capacity2) == True, "Test 2 Failed"
    print("✓ Test 2 passed: Sufficient capacity")
    
    # Test 3: Single trip
    trips3 = [[5,1,3]]
    capacity3 = 5
    assert solution.carPooling(trips3, capacity3) == True, "Test 3 Failed"
    print("✓ Test 3 passed: Single trip fits exactly")
    
    # Test 4: Single trip exceeds capacity
    trips4 = [[6,1,3]]
    capacity4 = 5
    assert solution.carPooling(trips4, capacity4) == False, "Test 4 Failed"
    print("✓ Test 4 passed: Single trip exceeds capacity")
    
    # Test 5: Drop off before pickup at same location
    trips5 = [[3,2,5],[2,5,7]]
    capacity5 = 3
    assert solution.carPooling(trips5, capacity5) == True, "Test 5 Failed"
    print("✓ Test 5 passed: Dropoff at same location as pickup")
    
    # Test 6: Multiple overlapping trips
    trips6 = [[2,1,5],[3,3,7],[4,6,8]]
    capacity6 = 6
    assert solution.carPooling(trips6, capacity6) == False, "Test 6 Failed"
    print("✓ Test 6 passed: Multiple overlapping trips exceed capacity")
    
    # Test 7: Sequential trips (no overlap)
    trips7 = [[2,1,3],[3,3,5],[4,5,7]]
    capacity7 = 4
    assert solution.carPooling(trips7, capacity7) == True, "Test 7 Failed"
    print("✓ Test 7 passed: Sequential non-overlapping trips")
    
    # Test 8: All passengers get off before last pickup
    trips8 = [[9,0,1],[3,3,7]]
    capacity8 = 9
    assert solution.carPooling(trips8, capacity8) == True, "Test 8 Failed"
    print("✓ Test 8 passed: Early passengers dropped off")
    
    # Test 9: Edge case - capacity of 1
    trips9 = [[1,1,2],[1,2,3]]
    capacity9 = 1
    assert solution.carPooling(trips9, capacity9) == True, "Test 9 Failed"
    print("✓ Test 9 passed: Minimum capacity sequential trips")
    
    # Test 11: Large capacity
    trips11 = [[1,1,100],[1,50,150],[1,100,200]]
    capacity11 = 3
    assert solution.carPooling(trips11, capacity11) == True, "Test 11 Failed"
    print("✓ Test 11 passed: Long distance trips with overlaps")
    
    # Test 12: Exact capacity match throughout
    trips12 = [[2,1,3],[2,2,4],[1,3,5]]
    capacity12 = 5
    assert solution.carPooling(trips12, capacity12) == True, "Test 12 Failed"
    print("✓ Test 12 passed: Exact capacity never exceeded")
    
    print("\n🎉 All tests passed!")


if __name__ == "__main__":
    test_car_pooling()