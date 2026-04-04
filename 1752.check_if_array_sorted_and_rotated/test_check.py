from check import Solution

def test_example_1():
    assert Solution().check([3,4,5,1,2]) == True

def test_example_2():
    assert Solution().check([2,1,3,4]) == False

def test_example_3():
    assert Solution().check([1,2,3]) == True

def test_single_element():
    assert Solution().check([1]) == True

def test_all_equal():
    assert Solution().check([2,2,2]) == True

def test_rotated_with_duplicates():
    assert Solution().check([2,2,3,1,2]) == True

def test_not_valid():
    assert Solution().check([1,3,2]) == False

def test_full_rotation():
    assert Solution().check([1,2,3,4,5]) == True

def test_rotation_at_end():
    assert Solution().check([2,3,4,5,1]) == True

def test_multiple_drops():
    assert Solution().check([3,1,2,0]) == False
