from flowers import Solution

s = Solution()

def test_example1():
    assert s.canPlaceFlowers([1,0,0,0,1], 1) == True

def test_example2():
    assert s.canPlaceFlowers([1,0,0,0,1], 2) == False

def test_single_zero():
    assert s.canPlaceFlowers([0], 1) == True

def test_single_one():
    assert s.canPlaceFlowers([1], 1) == False

def test_all_zeros():
    assert s.canPlaceFlowers([0,0,0,0,0], 3) == True

def test_all_zeros_too_many():
    assert s.canPlaceFlowers([0,0,0,0,0], 4) == False

def test_n_zero():
    assert s.canPlaceFlowers([1,0,0,0,1], 0) == True

def test_adjacent_constraint():
    assert s.canPlaceFlowers([0,0,1,0,0], 1) == True

def test_full():
    assert s.canPlaceFlowers([1,0,1,0,1], 0) == True
