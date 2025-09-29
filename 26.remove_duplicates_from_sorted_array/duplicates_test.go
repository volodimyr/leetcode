package removeduplicatesfromsortedarray

import (
	"reflect"
	"testing"
)

func TestRemoveDuplicates(t *testing.T) {
	tests := []struct {
		name         string
		nums         []int
		expectedK    int
		expectedNums []int // first k elements that should be in nums
	}{
		{
			name:         "example 1: simple duplicates",
			nums:         []int{1, 1, 2},
			expectedK:    2,
			expectedNums: []int{1, 2},
		},
		{
			name:         "example 2: multiple duplicates",
			nums:         []int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4},
			expectedK:    5,
			expectedNums: []int{0, 1, 2, 3, 4},
		},
		{
			name:         "no duplicates",
			nums:         []int{1, 2, 3, 4, 5},
			expectedK:    5,
			expectedNums: []int{1, 2, 3, 4, 5},
		},
		{
			name:         "all duplicates",
			nums:         []int{1, 1, 1, 1, 1},
			expectedK:    1,
			expectedNums: []int{1},
		},
		{
			name:         "single element",
			nums:         []int{1},
			expectedK:    1,
			expectedNums: []int{1},
		},
		{
			name:         "two identical elements",
			nums:         []int{1, 1},
			expectedK:    1,
			expectedNums: []int{1},
		},
		{
			name:         "two different elements",
			nums:         []int{1, 2},
			expectedK:    2,
			expectedNums: []int{1, 2},
		},
		{
			name:         "duplicates at start",
			nums:         []int{1, 1, 1, 2, 3, 4},
			expectedK:    4,
			expectedNums: []int{1, 2, 3, 4},
		},
		{
			name:         "duplicates at end",
			nums:         []int{1, 2, 3, 4, 4, 4},
			expectedK:    4,
			expectedNums: []int{1, 2, 3, 4},
		},
		{
			name:         "duplicates in middle",
			nums:         []int{1, 2, 2, 2, 3, 4},
			expectedK:    4,
			expectedNums: []int{1, 2, 3, 4},
		},
		{
			name:         "pairs of duplicates",
			nums:         []int{1, 1, 2, 2, 3, 3, 4, 4},
			expectedK:    4,
			expectedNums: []int{1, 2, 3, 4},
		},
		{
			name:         "negative numbers",
			nums:         []int{-3, -3, -2, -1, -1, 0, 0, 1},
			expectedK:    5,
			expectedNums: []int{-3, -2, -1, 0, 1},
		},
		{
			name:         "all negative duplicates",
			nums:         []int{-5, -5, -5, -5},
			expectedK:    1,
			expectedNums: []int{-5},
		},
		{
			name:         "large numbers with duplicates",
			nums:         []int{100, 100, 200, 300, 300, 300},
			expectedK:    3,
			expectedNums: []int{100, 200, 300},
		},
		{
			name:         "consecutive duplicates varying length",
			nums:         []int{1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5},
			expectedK:    5,
			expectedNums: []int{1, 2, 3, 4, 5},
		},
		{
			name:         "zeros with duplicates",
			nums:         []int{0, 0, 0, 1, 1, 2},
			expectedK:    3,
			expectedNums: []int{0, 1, 2},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			// Make a copy for error messages
			original := make([]int, len(tt.nums))
			copy(original, tt.nums)

			k := removeDuplicates(tt.nums)

			// Check if k matches expected
			if k != tt.expectedK {
				t.Errorf("removeDuplicates(%v) returned k = %d, want %d",
					original, k, tt.expectedK)
				return
			}

			// Check if first k elements match expected
			actual := tt.nums[:k]
			if !reflect.DeepEqual(actual, tt.expectedNums) {
				t.Errorf("removeDuplicates(%v) first %d elements = %v, want %v",
					original, k, actual, tt.expectedNums)
			}
		})
	}
}

func TestRemoveDuplicatesProperties(t *testing.T) {
	t.Run("modifies array in-place", func(t *testing.T) {
		nums := []int{1, 1, 2, 2, 3}
		ptr := &nums[0]

		k := removeDuplicates(nums)

		// Verify same underlying array
		if &nums[0] != ptr {
			t.Error("removeDuplicates should modify array in-place")
		}

		// Verify result
		if k != 3 || !reflect.DeepEqual(nums[:k], []int{1, 2, 3}) {
			t.Errorf("removeDuplicates modified in-place incorrectly")
		}
	})

	t.Run("first k elements are sorted", func(t *testing.T) {
		testCases := [][]int{
			{1, 1, 2, 3, 3, 4},
			{0, 0, 1, 1, 1, 2, 2, 3, 3, 4},
			{1, 2, 3, 4, 5},
		}

		for _, tc := range testCases {
			nums := make([]int, len(tc))
			copy(nums, tc)

			k := removeDuplicates(nums)

			// Check if first k elements are sorted
			for i := 1; i < k; i++ {
				if nums[i] < nums[i-1] {
					t.Errorf("removeDuplicates(%v) first %d elements not sorted: %v",
						tc, k, nums[:k])
					break
				}
			}
		}
	})

	t.Run("first k elements are unique", func(t *testing.T) {
		testCases := [][]int{
			{1, 1, 2, 3, 3, 4},
			{0, 0, 1, 1, 1, 2, 2, 3, 3, 4},
			{5, 5, 5, 5, 5},
		}

		for _, tc := range testCases {
			nums := make([]int, len(tc))
			copy(nums, tc)

			k := removeDuplicates(nums)

			// Check if first k elements are unique
			seen := make(map[int]bool)
			for i := 0; i < k; i++ {
				if seen[nums[i]] {
					t.Errorf("removeDuplicates(%v) has duplicate in first %d elements: %v",
						tc, k, nums[:k])
					break
				}
				seen[nums[i]] = true
			}
		}
	})

	t.Run("k is valid length", func(t *testing.T) {
		testCases := [][]int{
			{1, 1, 2},
			{0, 0, 1, 1, 1, 2, 2, 3, 3, 4},
			{1},
		}

		for _, tc := range testCases {
			nums := make([]int, len(tc))
			copy(nums, tc)

			k := removeDuplicates(nums)

			// k should be between 1 and len(nums)
			if k < 1 || k > len(nums) {
				t.Errorf("removeDuplicates(%v) returned invalid k = %d, should be between 1 and %d",
					tc, k, len(nums))
			}
		}
	})

	t.Run("relative order preserved", func(t *testing.T) {
		nums := []int{1, 1, 2, 3, 3, 4, 5, 5}
		expected := []int{1, 2, 3, 4, 5}

		k := removeDuplicates(nums)

		if !reflect.DeepEqual(nums[:k], expected) {
			t.Errorf("removeDuplicates did not preserve relative order: got %v, want %v",
				nums[:k], expected)
		}
	})

	t.Run("handles empty-like edge cases", func(t *testing.T) {
		// Single element
		nums := []int{42}
		k := removeDuplicates(nums)

		if k != 1 || nums[0] != 42 {
			t.Errorf("removeDuplicates([42]) = k:%d, nums:%v, want k:1, nums:[42]", k, nums)
		}
	})
}

func TestRemoveDuplicatesEdgeCases(t *testing.T) {
	t.Run("all same values from 1 to n", func(t *testing.T) {
		for n := 1; n <= 10; n++ {
			nums := make([]int, n)
			for i := range nums {
				nums[i] = 5 // all same value
			}

			k := removeDuplicates(nums)

			if k != 1 || nums[0] != 5 {
				t.Errorf("removeDuplicates([]int with %d fives) = k:%d, want k:1", n, k)
			}
		}
	})

	t.Run("no duplicates from 1 to n", func(t *testing.T) {
		for n := 1; n <= 10; n++ {
			nums := make([]int, n)
			for i := range nums {
				nums[i] = i
			}

			expected := make([]int, n)
			copy(expected, nums)

			k := removeDuplicates(nums)

			if k != n || !reflect.DeepEqual(nums[:k], expected) {
				t.Errorf("removeDuplicates(no dups, len %d) = k:%d, want k:%d", n, k, n)
			}
		}
	})
}
