package findpivotindex

import "testing"

func TestPivotIndex(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected int
	}{
		{
			name:     "example 1 - pivot in middle",
			nums:     []int{1, 7, 3, 6, 5, 6},
			expected: 3,
		},
		{
			name:     "example 2 - no pivot exists",
			nums:     []int{1, 2, 3},
			expected: -1,
		},
		{
			name:     "example 3 - pivot at start",
			nums:     []int{2, 1, -1},
			expected: 0,
		},
		{
			name:     "single element",
			nums:     []int{1},
			expected: 0,
		},
		{
			name:     "two elements - no pivot",
			nums:     []int{1, 2},
			expected: -1,
		},
		{
			name:     "two elements - pivot at start",
			nums:     []int{0, 0},
			expected: 0,
		},
		{
			name:     "all zeros",
			nums:     []int{0, 0, 0, 0},
			expected: 0,
		},
		{
			name:     "pivot at end",
			nums:     []int{-1, -1, 0, 1, 1, 0},
			expected: 5,
		},
		{
			name:     "negative numbers - pivot exists",
			nums:     []int{-1, -1, -1, 0, 1, 1},
			expected: 0,
		},
		{
			name:     "mixed positive and negative",
			nums:     []int{1, -1, 2, -1, 1},
			expected: 2,
		},
		{
			name:     "large positive sum on left",
			nums:     []int{100, -99, -1, 0},
			expected: 3,
		},
		{
			name:     "leftmost pivot when multiple exist",
			nums:     []int{0, 0, 0},
			expected: 0,
		},
		{
			name:     "larger array no pivot",
			nums:     []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
			expected: -1,
		},
		{
			name:     "array with zero in middle as pivot",
			nums:     []int{5, 5, 0, 5, 5},
			expected: 2,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := pivotIndex(tt.nums)
			if result != tt.expected {
				t.Errorf("pivotIndex(%v) = %d; expected %d", tt.nums, result, tt.expected)
			}
		})
	}
}
