package twosumiiinputarrayissorted

import (
	"testing"
)

func TestTwoSum(t *testing.T) {
	tests := []struct {
		name     string
		numbers  []int
		target   int
		expected []int
	}{
		{
			name:     "example 1 - basic case",
			numbers:  []int{2, 7, 11, 15},
			target:   9,
			expected: []int{1, 2},
		},
		{
			name:     "example 2 - middle elements",
			numbers:  []int{2, 3, 4},
			target:   6,
			expected: []int{1, 3},
		},
		{
			name:     "example 3 - negative numbers",
			numbers:  []int{-1, 0},
			target:   -1,
			expected: []int{1, 2},
		},
		{
			name:     "two elements only",
			numbers:  []int{1, 2},
			target:   3,
			expected: []int{1, 2},
		},
		{
			name:     "large array first and last",
			numbers:  []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
			target:   11,
			expected: []int{1, 10},
		},
		{
			name:     "consecutive elements",
			numbers:  []int{5, 25, 75},
			target:   100,
			expected: []int{2, 3},
		},
		{
			name:     "all negative numbers",
			numbers:  []int{-10, -5, -3, -1},
			target:   -13,
			expected: []int{1, 3},
		},
		{
			name:     "mixed negative and positive",
			numbers:  []int{-5, -2, 0, 3, 7},
			target:   5,
			expected: []int{2, 5},
		},
		{
			name:     "large numbers",
			numbers:  []int{100, 200, 300, 400, 500},
			target:   700,
			expected: []int{2, 5},
		},
		{
			name:     "same number twice in sequence",
			numbers:  []int{0, 0, 3, 4},
			target:   0,
			expected: []int{1, 2},
		},
		{
			name:     "negative target",
			numbers:  []int{-10, -8, -5, -2},
			target:   -13,
			expected: []int{2, 3},
		},
		{
			name:     "minimum length array",
			numbers:  []int{5, 5},
			target:   10,
			expected: []int{1, 2},
		},
		{
			name:     "elements at beginning",
			numbers:  []int{1, 3, 5, 7, 9, 11},
			target:   4,
			expected: []int{1, 2},
		},
		{
			name:     "elements at end",
			numbers:  []int{1, 3, 5, 7, 9, 11},
			target:   20,
			expected: []int{5, 6},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := twoSum(tt.numbers, tt.target)

			if len(result) != 2 {
				t.Fatalf("expected result length 2, got %d", len(result))
			}

			if result[0] != tt.expected[0] || result[1] != tt.expected[1] {
				t.Errorf("twoSum(%v, %d) = %v, expected %v",
					tt.numbers, tt.target, result, tt.expected)
			}

			// Verify the sum is correct
			idx1 := result[0] - 1
			idx2 := result[1] - 1
			if idx1 >= 0 && idx1 < len(tt.numbers) && idx2 >= 0 && idx2 < len(tt.numbers) {
				sum := tt.numbers[idx1] + tt.numbers[idx2]
				if sum != tt.target {
					t.Errorf("sum of numbers[%d]=%d and numbers[%d]=%d is %d, expected %d",
						idx1, tt.numbers[idx1], idx2, tt.numbers[idx2], sum, tt.target)
				}
			}
		})
	}
}
