package findtheduplicatenumber

import "testing"

func TestFindDuplicate_Example1(t *testing.T) {
	nums := []int{1, 3, 4, 2, 2}
	result := findDuplicate(nums)

	if result != 2 {
		t.Errorf("Expected 2, got %d", result)
	}
}

func TestFindDuplicate_Example2(t *testing.T) {
	nums := []int{3, 1, 3, 4, 2}
	result := findDuplicate(nums)

	if result != 3 {
		t.Errorf("Expected 3, got %d", result)
	}
}

func TestFindDuplicate_Example3(t *testing.T) {
	nums := []int{3, 3, 3, 3, 3}
	result := findDuplicate(nums)

	if result != 3 {
		t.Errorf("Expected 3, got %d", result)
	}
}

func TestFindDuplicate_TwoElements(t *testing.T) {
	nums := []int{1, 1}
	result := findDuplicate(nums)

	if result != 1 {
		t.Errorf("Expected 1, got %d", result)
	}
}

func TestFindDuplicate_Complex(t *testing.T) {
	nums := []int{2, 5, 9, 6, 9, 3, 8, 9, 7, 1}
	result := findDuplicate(nums)

	if result != 9 {
		t.Errorf("Expected 9, got %d", result)
	}
}

func TestFindDuplicate_DuplicateAtEnd(t *testing.T) {
	nums := []int{1, 2, 3, 4, 4}
	result := findDuplicate(nums)

	if result != 4 {
		t.Errorf("Expected 4, got %d", result)
	}
}

func TestFindDuplicate_DuplicateInMiddle(t *testing.T) {
	nums := []int{1, 2, 5, 3, 5, 4}
	result := findDuplicate(nums)

	if result != 5 {
		t.Errorf("Expected 5, got %d", result)
	}
}

func TestFindDuplicate_ThreeElements(t *testing.T) {
	nums := []int{2, 1, 2}
	result := findDuplicate(nums)

	if result != 2 {
		t.Errorf("Expected 2, got %d", result)
	}
}

func TestFindDuplicate_FourElements(t *testing.T) {
	nums := []int{4, 3, 1, 4, 2}
	result := findDuplicate(nums)

	if result != 4 {
		t.Errorf("Expected 4, got %d", result)
	}
}

func TestFindDuplicate_LargerArray(t *testing.T) {
	nums := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 5}
	result := findDuplicate(nums)

	if result != 5 {
		t.Errorf("Expected 5, got %d", result)
	}
}

func TestFindDuplicate_DuplicateOne(t *testing.T) {
	nums := []int{1, 1, 2, 3, 4}
	result := findDuplicate(nums)

	if result != 1 {
		t.Errorf("Expected 1, got %d", result)
	}
}

func TestFindDuplicate_MultipleDuplicates(t *testing.T) {
	nums := []int{2, 5, 9, 6, 9, 3, 8, 9, 7, 1, 4}
	result := findDuplicate(nums)

	if result != 9 {
		t.Errorf("Expected 9, got %d", result)
	}
}

func TestFindDuplicate_AdjacentDuplicates(t *testing.T) {
	nums := []int{1, 2, 3, 3, 4, 5}
	result := findDuplicate(nums)

	if result != 3 {
		t.Errorf("Expected 3, got %d", result)
	}
}

func TestFindDuplicate_NonAdjacentDuplicates(t *testing.T) {
	nums := []int{5, 1, 2, 3, 4, 5}
	result := findDuplicate(nums)

	if result != 5 {
		t.Errorf("Expected 5, got %d", result)
	}
}

func TestFindDuplicate_LargeN(t *testing.T) {
	nums := make([]int, 101)
	for i := 1; i <= 100; i++ {
		nums[i-1] = i
	}
	nums[100] = 50

	result := findDuplicate(nums)

	if result != 50 {
		t.Errorf("Expected 50, got %d", result)
	}
}

func TestFindDuplicate_MaxValue(t *testing.T) {
	nums := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10}
	result := findDuplicate(nums)

	if result != 10 {
		t.Errorf("Expected 10, got %d", result)
	}
}

func TestFindDuplicate_SequentialWithGap(t *testing.T) {
	nums := []int{2, 5, 1, 3, 4, 6, 7, 3}
	result := findDuplicate(nums)

	if result != 3 {
		t.Errorf("Expected 3, got %d", result)
	}
}

func TestFindDuplicate_ReverseOrder(t *testing.T) {
	nums := []int{5, 4, 3, 2, 1, 3}
	result := findDuplicate(nums)

	if result != 3 {
		t.Errorf("Expected 3, got %d", result)
	}
}
