package longestconsecutivesequence

import "testing"

func TestLongestConsecutive_TableDriven(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected int
	}{
		{"empty", []int{}, 0},
		{"single", []int{5}, 1},
		{"pair consecutive", []int{1, 2}, 2},
		{"pair non-consecutive", []int{1, 3}, 1},
		{"all same", []int{7, 7, 7}, 1},
		{"scattered", []int{9, 1, 4, 7, 3, 2, 8, 5, 6}, 9},
		{"with negatives", []int{-5, -4, -3, 0, 1}, 3},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := longestConsecutive(tt.nums)
			if result != tt.expected {
				t.Errorf("longestConsecutive(%v) = %d; expected %d",
					tt.nums, result, tt.expected)
			}
		})
	}
}

func TestLongestConsecutive_EmptyArray(t *testing.T) {
	nums := []int{}
	expected := 0
	result := longestConsecutive(nums)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestLongestConsecutive_SingleElement(t *testing.T) {
	nums := []int{100}
	expected := 1
	result := longestConsecutive(nums)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestLongestConsecutive_AllDuplicates(t *testing.T) {
	nums := []int{1, 1, 1, 1}
	expected := 1
	result := longestConsecutive(nums)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestLongestConsecutive_Example1(t *testing.T) {
	nums := []int{2, 20, 4, 10, 3, 4, 5}
	expected := 4 // [2, 3, 4, 5]
	result := longestConsecutive(nums)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestLongestConsecutive_Example2(t *testing.T) {
	nums := []int{0, 3, 2, 5, 4, 6, 1, 1}
	expected := 7 // [0, 1, 2, 3, 4, 5, 6]
	result := longestConsecutive(nums)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestLongestConsecutive_NoConsecutive(t *testing.T) {
	nums := []int{10, 5, 100, 200}
	expected := 1
	result := longestConsecutive(nums)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestLongestConsecutive_AlreadySorted(t *testing.T) {
	nums := []int{1, 2, 3, 4, 5}
	expected := 5
	result := longestConsecutive(nums)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestLongestConsecutive_ReverseSorted(t *testing.T) {
	nums := []int{5, 4, 3, 2, 1}
	expected := 5
	result := longestConsecutive(nums)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestLongestConsecutive_NegativeNumbers(t *testing.T) {
	nums := []int{-3, -2, -1, 0, 1}
	expected := 5
	result := longestConsecutive(nums)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestLongestConsecutive_MixedPositiveNegative(t *testing.T) {
	nums := []int{-1, -2, 0, 1, 2, 10, 11}
	expected := 5 // [-2, -1, 0, 1, 2]
	result := longestConsecutive(nums)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestLongestConsecutive_MultipleSequences(t *testing.T) {
	nums := []int{100, 4, 200, 1, 3, 2}
	expected := 4 // [1, 2, 3, 4]
	result := longestConsecutive(nums)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestLongestConsecutive_WithGaps(t *testing.T) {
	nums := []int{1, 2, 3, 5, 6, 7, 9}
	expected := 3 // Either [1,2,3] or [5,6,7]
	result := longestConsecutive(nums)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestLongestConsecutive_LargeNumbers(t *testing.T) {
	nums := []int{1000000000, 999999999, 1000000001}
	expected := 3
	result := longestConsecutive(nums)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestLongestConsecutive_DuplicatesInSequence(t *testing.T) {
	nums := []int{1, 2, 2, 3, 4, 4, 5}
	expected := 5 // [1, 2, 3, 4, 5]
	result := longestConsecutive(nums)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestLongestConsecutive_TwoElement(t *testing.T) {
	nums := []int{1, 2}
	expected := 2
	result := longestConsecutive(nums)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}

func TestLongestConsecutive_TwoElementNonConsecutive(t *testing.T) {
	nums := []int{1, 3}
	expected := 1
	result := longestConsecutive(nums)
	if result != expected {
		t.Errorf("Expected %d, got %d", expected, result)
	}
}
