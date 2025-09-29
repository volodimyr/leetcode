package squaresofasortedarray

import (
	"reflect"
	"testing"
)

func TestSortedSquares(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected []int
	}{
		{
			name:     "example 1: mixed negative and positive",
			nums:     []int{-4, -1, 0, 3, 10},
			expected: []int{0, 1, 9, 16, 100},
		},
		{
			name:     "example 2: mixed with duplicates",
			nums:     []int{-7, -3, 2, 3, 11},
			expected: []int{4, 9, 9, 49, 121},
		},
		{
			name:     "all negative numbers",
			nums:     []int{-5, -4, -3, -2, -1},
			expected: []int{1, 4, 9, 16, 25},
		},
		{
			name:     "all positive numbers",
			nums:     []int{1, 2, 3, 4, 5},
			expected: []int{1, 4, 9, 16, 25},
		},
		{
			name:     "single element positive",
			nums:     []int{5},
			expected: []int{25},
		},
		{
			name:     "single element negative",
			nums:     []int{-5},
			expected: []int{25},
		},
		{
			name:     "single element zero",
			nums:     []int{0},
			expected: []int{0},
		},
		{
			name:     "two elements both negative",
			nums:     []int{-3, -1},
			expected: []int{1, 9},
		},
		{
			name:     "two elements both positive",
			nums:     []int{1, 3},
			expected: []int{1, 9},
		},
		{
			name:     "two elements negative and positive",
			nums:     []int{-1, 1},
			expected: []int{1, 1},
		},
		{
			name:     "contains zero at start",
			nums:     []int{0, 1, 2, 3},
			expected: []int{0, 1, 4, 9},
		},
		{
			name:     "contains zero in middle",
			nums:     []int{-3, -2, 0, 1, 2},
			expected: []int{0, 1, 4, 4, 9},
		},
		{
			name:     "contains zero at end",
			nums:     []int{-3, -2, -1, 0},
			expected: []int{0, 1, 4, 9},
		},
		{
			name:     "multiple zeros",
			nums:     []int{-2, 0, 0, 3},
			expected: []int{0, 0, 4, 9},
		},
		{
			name:     "all zeros",
			nums:     []int{0, 0, 0, 0},
			expected: []int{0, 0, 0, 0},
		},
		{
			name:     "large negative values",
			nums:     []int{-10000, -5000, -1},
			expected: []int{1, 25000000, 100000000},
		},
		{
			name:     "equal absolute values",
			nums:     []int{-5, -5, -3, 3, 5, 5},
			expected: []int{9, 9, 25, 25, 25, 25},
		},
		{
			name:     "mostly negative with few positive",
			nums:     []int{-10, -9, -8, -7, 1, 2},
			expected: []int{1, 4, 49, 64, 81, 100},
		},
		{
			name:     "mostly positive with few negative",
			nums:     []int{-2, -1, 3, 4, 5, 6},
			expected: []int{1, 4, 9, 16, 25, 36},
		},
		{
			name:     "negative to positive symmetric",
			nums:     []int{-3, -2, -1, 0, 1, 2, 3},
			expected: []int{0, 1, 1, 4, 4, 9, 9},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			// Make a copy to avoid modifying the test case
			input := make([]int, len(tt.nums))
			copy(input, tt.nums)

			result := sortedSquares(input)

			if !reflect.DeepEqual(result, tt.expected) {
				t.Errorf("sortedSquares(%v) = %v, want %v", tt.nums, result, tt.expected)
			}
		})
	}
}

func TestSortedSquaresProperties(t *testing.T) {
	t.Run("result length equals input length", func(t *testing.T) {
		testCases := [][]int{
			{-4, -1, 0, 3, 10},
			{1, 2, 3},
			{-5, -4, -3, -2, -1},
		}

		for _, tc := range testCases {
			result := sortedSquares(tc)
			if len(result) != len(tc) {
				t.Errorf("sortedSquares(%v) length = %d, want %d", tc, len(result), len(tc))
			}
		}
	})

	t.Run("result is sorted in non-decreasing order", func(t *testing.T) {
		testCases := [][]int{
			{-4, -1, 0, 3, 10},
			{-7, -3, 2, 3, 11},
			{-5, -4, -3, -2, -1},
		}

		for _, tc := range testCases {
			result := sortedSquares(tc)
			for i := 1; i < len(result); i++ {
				if result[i] < result[i-1] {
					t.Errorf("sortedSquares(%v) = %v is not sorted", tc, result)
					break
				}
			}
		}
	})

	t.Run("all values are non-negative", func(t *testing.T) {
		testCases := [][]int{
			{-4, -1, 0, 3, 10},
			{-7, -3, 2, 3, 11},
		}

		for _, tc := range testCases {
			result := sortedSquares(tc)
			for _, val := range result {
				if val < 0 {
					t.Errorf("sortedSquares(%v) contains negative value %d", tc, val)
				}
			}
		}
	})

	t.Run("does not modify input array", func(t *testing.T) {
		input := []int{-4, -1, 0, 3, 10}
		original := make([]int, len(input))
		copy(original, input)

		sortedSquares(input)

		if !reflect.DeepEqual(input, original) {
			t.Errorf("sortedSquares modified input array: got %v, original was %v", input, original)
		}
	})
}
