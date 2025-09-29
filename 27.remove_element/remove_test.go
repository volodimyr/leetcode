package removelement

import (
	"sort"
	"testing"
)

func TestRemoveElement(t *testing.T) {
	tests := []struct {
		name        string
		nums        []int
		val         int
		expectedK   int
		expectedSet []int // elements that should be in first k positions (order doesn't matter)
	}{
		{
			name:        "example 1: remove 3s",
			nums:        []int{3, 2, 2, 3},
			val:         3,
			expectedK:   2,
			expectedSet: []int{2, 2},
		},
		{
			name:        "example 2: remove 2s",
			nums:        []int{0, 1, 2, 2, 3, 0, 4, 2},
			val:         2,
			expectedK:   5,
			expectedSet: []int{0, 1, 3, 0, 4},
		},
		{
			name:        "no elements to remove",
			nums:        []int{1, 2, 3, 4, 5},
			val:         6,
			expectedK:   5,
			expectedSet: []int{1, 2, 3, 4, 5},
		},
		{
			name:        "all elements should be removed",
			nums:        []int{1, 1, 1, 1},
			val:         1,
			expectedK:   0,
			expectedSet: []int{},
		},
		{
			name:        "single element - keep",
			nums:        []int{1},
			val:         2,
			expectedK:   1,
			expectedSet: []int{1},
		},
		{
			name:        "single element - remove",
			nums:        []int{1},
			val:         1,
			expectedK:   0,
			expectedSet: []int{},
		},
		{
			name:        "two elements - remove first",
			nums:        []int{1, 2},
			val:         1,
			expectedK:   1,
			expectedSet: []int{2},
		},
		{
			name:        "two elements - remove second",
			nums:        []int{1, 2},
			val:         2,
			expectedK:   1,
			expectedSet: []int{1},
		},
		{
			name:        "two elements - remove both",
			nums:        []int{1, 1},
			val:         1,
			expectedK:   0,
			expectedSet: []int{},
		},
		{
			name:        "two elements - remove neither",
			nums:        []int{1, 2},
			val:         3,
			expectedK:   2,
			expectedSet: []int{1, 2},
		},
		{
			name:        "remove at start",
			nums:        []int{1, 1, 2, 3, 4},
			val:         1,
			expectedK:   3,
			expectedSet: []int{2, 3, 4},
		},
		{
			name:        "remove at end",
			nums:        []int{1, 2, 3, 4, 4},
			val:         4,
			expectedK:   3,
			expectedSet: []int{1, 2, 3},
		},
		{
			name:        "remove in middle",
			nums:        []int{1, 2, 3, 3, 4},
			val:         3,
			expectedK:   3,
			expectedSet: []int{1, 2, 4},
		},
		{
			name:        "alternating pattern",
			nums:        []int{1, 2, 1, 2, 1, 2},
			val:         1,
			expectedK:   3,
			expectedSet: []int{2, 2, 2},
		},
		{
			name:        "remove negative numbers",
			nums:        []int{-1, -2, 3, -1, 4},
			val:         -1,
			expectedK:   3,
			expectedSet: []int{-2, 3, 4},
		},
		{
			name:        "remove zeros",
			nums:        []int{0, 1, 0, 2, 0, 3},
			val:         0,
			expectedK:   3,
			expectedSet: []int{1, 2, 3},
		},
		{
			name:        "large numbers",
			nums:        []int{100, 200, 100, 300, 100},
			val:         100,
			expectedK:   2,
			expectedSet: []int{200, 300},
		},
		{
			name:        "consecutive values to remove",
			nums:        []int{1, 2, 2, 2, 3},
			val:         2,
			expectedK:   2,
			expectedSet: []int{1, 3},
		},
		{
			name:        "mixed positive and negative",
			nums:        []int{-3, -2, -1, 0, 1, 2, 3},
			val:         0,
			expectedK:   6,
			expectedSet: []int{-3, -2, -1, 1, 2, 3},
		},
		{
			name:        "empty array",
			nums:        []int{},
			val:         1,
			expectedK:   0,
			expectedSet: []int{},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			// Make a copy for error messages
			original := make([]int, len(tt.nums))
			copy(original, tt.nums)

			k := removeElement(tt.nums, tt.val)

			// Check if k matches expected
			if k != tt.expectedK {
				t.Errorf("removeElement(%v, %d) returned k = %d, want %d",
					original, tt.val, k, tt.expectedK)
				return
			}

			// Extract and sort first k elements
			actual := make([]int, k)
			copy(actual, tt.nums[:k])
			sort.Ints(actual)

			// Sort expected for comparison
			expected := make([]int, len(tt.expectedSet))
			copy(expected, tt.expectedSet)
			sort.Ints(expected)

			// Compare sorted arrays
			if !equal(actual, expected) {
				t.Errorf("removeElement(%v, %d) first %d elements = %v, want %v (order may vary)",
					original, tt.val, k, actual, expected)
			}

			// Verify no occurrence of val in first k elements
			for i := 0; i < k; i++ {
				if tt.nums[i] == tt.val {
					t.Errorf("removeElement(%v, %d) has val %d at index %d in first %d elements",
						original, tt.val, tt.val, i, k)
					break
				}
			}
		})
	}
}

func TestRemoveElementProperties(t *testing.T) {
	t.Run("modifies array in-place", func(t *testing.T) {
		nums := []int{1, 2, 3, 2, 4}
		ptr := &nums[0]

		k := removeElement(nums, 2)

		// Verify same underlying array
		if &nums[0] != ptr {
			t.Error("removeElement should modify array in-place")
		}

		// Verify result
		if k != 3 {
			t.Errorf("removeElement returned k = %d, want 3", k)
		}
	})

	t.Run("k equals count of non-val elements", func(t *testing.T) {
		testCases := []struct {
			nums []int
			val  int
		}{
			{[]int{1, 2, 3, 2, 4}, 2},
			{[]int{0, 1, 2, 2, 3, 0, 4, 2}, 2},
			{[]int{3, 3, 3, 3}, 3},
		}

		for _, tc := range testCases {
			nums := make([]int, len(tc.nums))
			copy(nums, tc.nums)

			// Count expected non-val elements
			expectedK := 0
			for _, num := range tc.nums {
				if num != tc.val {
					expectedK++
				}
			}

			k := removeElement(nums, tc.val)

			if k != expectedK {
				t.Errorf("removeElement(%v, %d) = %d, expected count %d",
					tc.nums, tc.val, k, expectedK)
			}
		}
	})

	t.Run("no val in first k elements", func(t *testing.T) {
		testCases := []struct {
			nums []int
			val  int
		}{
			{[]int{3, 2, 2, 3}, 3},
			{[]int{0, 1, 2, 2, 3, 0, 4, 2}, 2},
			{[]int{1, 1, 1, 2, 3}, 1},
		}

		for _, tc := range testCases {
			nums := make([]int, len(tc.nums))
			copy(nums, tc.nums)

			k := removeElement(nums, tc.val)

			for i := 0; i < k; i++ {
				if nums[i] == tc.val {
					t.Errorf("removeElement(%v, %d) has val %d at index %d",
						tc.nums, tc.val, tc.val, i)
					break
				}
			}
		}
	})

	t.Run("preserves all non-val elements", func(t *testing.T) {
		testCases := []struct {
			nums []int
			val  int
		}{
			{[]int{3, 2, 2, 3}, 3},
			{[]int{0, 1, 2, 2, 3, 0, 4, 2}, 2},
		}

		for _, tc := range testCases {
			// Collect expected non-val elements
			expected := []int{}
			for _, num := range tc.nums {
				if num != tc.val {
					expected = append(expected, num)
				}
			}
			sort.Ints(expected)

			nums := make([]int, len(tc.nums))
			copy(nums, tc.nums)

			k := removeElement(nums, tc.val)

			actual := make([]int, k)
			copy(actual, nums[:k])
			sort.Ints(actual)

			if !equal(actual, expected) {
				t.Errorf("removeElement(%v, %d) elements = %v, want %v",
					tc.nums, tc.val, actual, expected)
			}
		}
	})

	t.Run("k is valid length", func(t *testing.T) {
		testCases := [][]int{
			{1, 2, 3, 2, 4},
			{1, 1, 1},
			{1, 2, 3, 4, 5},
		}

		for _, tc := range testCases {
			nums := make([]int, len(tc))
			copy(nums, tc)

			k := removeElement(nums, 2)

			if k < 0 || k > len(nums) {
				t.Errorf("removeElement(%v, 2) returned invalid k = %d, should be between 0 and %d",
					tc, k, len(nums))
			}
		}
	})
}

// Helper function to compare slices
func equal(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}
