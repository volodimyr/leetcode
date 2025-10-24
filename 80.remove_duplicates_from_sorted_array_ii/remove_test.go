package removeduplicatesfromsortedarrayii

import (
	"testing"
)

func TestRemoveDuplicates(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected int
		result   []int
	}{
		{
			name:     "Example 1",
			nums:     []int{1, 1, 1, 2, 2, 3},
			expected: 5,
			result:   []int{1, 1, 2, 2, 3},
		},
		{
			name:     "Example 2",
			nums:     []int{0, 0, 1, 1, 1, 1, 2, 3, 3},
			expected: 7,
			result:   []int{0, 0, 1, 1, 2, 3, 3},
		},
		{
			name:     "Single element",
			nums:     []int{1},
			expected: 1,
			result:   []int{1},
		},
		{
			name:     "Two identical elements",
			nums:     []int{1, 1},
			expected: 2,
			result:   []int{1, 1},
		},
		{
			name:     "Three identical elements",
			nums:     []int{1, 1, 1},
			expected: 2,
			result:   []int{1, 1},
		},
		{
			name:     "All different elements",
			nums:     []int{1, 2, 3, 4, 5},
			expected: 5,
			result:   []int{1, 2, 3, 4, 5},
		},
		{
			name:     "All same elements",
			nums:     []int{2, 2, 2, 2, 2, 2},
			expected: 2,
			result:   []int{2, 2},
		},
		{
			name:     "Pairs only",
			nums:     []int{1, 1, 2, 2, 3, 3},
			expected: 6,
			result:   []int{1, 1, 2, 2, 3, 3},
		},
		{
			name:     "Multiple groups with different counts",
			nums:     []int{1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3},
			expected: 6,
			result:   []int{1, 1, 2, 2, 3, 3},
		},
		{
			name:     "Negative numbers",
			nums:     []int{-5, -5, -5, -3, -3, -1},
			expected: 5,
			result:   []int{-5, -5, -3, -3, -1},
		},
		{
			name:     "Mix of negative and positive",
			nums:     []int{-2, -2, -1, -1, -1, 0, 0, 1, 1, 1},
			expected: 8,
			result:   []int{-2, -2, -1, -1, 0, 0, 1, 1},
		},
		{
			name:     "Two elements different",
			nums:     []int{1, 2},
			expected: 2,
			result:   []int{1, 2},
		},
		{
			name:     "Large numbers",
			nums:     []int{10000, 10000, 10000, 10001, 10001},
			expected: 4,
			result:   []int{10000, 10000, 10001, 10001},
		},
		{
			name:     "Starting with many duplicates",
			nums:     []int{1, 1, 1, 1, 1, 1, 1, 2, 3},
			expected: 4,
			result:   []int{1, 1, 2, 3},
		},
		{
			name:     "Ending with many duplicates",
			nums:     []int{1, 2, 3, 3, 3, 3, 3, 3, 3},
			expected: 4,
			result:   []int{1, 2, 3, 3},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			// Make a copy for error messages
			original := make([]int, len(tt.nums))
			copy(original, tt.nums)

			k := removeDuplicates(tt.nums)

			if k != tt.expected {
				t.Errorf("removeDuplicates(%v) returned k = %d, expected %d", original, k, tt.expected)
			}

			// Verify the first k elements match the expected result
			for i := 0; i < k; i++ {
				if tt.nums[i] != tt.result[i] {
					t.Errorf("removeDuplicates(%v) at index %d: got %d, expected %d", original, i, tt.nums[i], tt.result[i])
				}
			}
		})
	}
}

func TestRemoveDuplicatesProperties(t *testing.T) {
	t.Run("Result is sorted", func(t *testing.T) {
		nums := []int{1, 1, 1, 2, 2, 3, 3, 3, 3}
		k := removeDuplicates(nums)

		for i := 1; i < k; i++ {
			if nums[i] < nums[i-1] {
				t.Errorf("Result is not sorted: nums[%d]=%d < nums[%d]=%d", i, nums[i], i-1, nums[i-1])
			}
		}
	})

	t.Run("No element appears more than twice", func(t *testing.T) {
		nums := []int{1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3}
		k := removeDuplicates(nums)

		counts := make(map[int]int)
		for i := 0; i < k; i++ {
			counts[nums[i]]++
			if counts[nums[i]] > 2 {
				t.Errorf("Element %d appears more than twice in result", nums[i])
			}
		}
	})
}
