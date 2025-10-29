package largestrectangleinhistogram

import "testing"

func TestLargestRectangleArea(t *testing.T) {
	tests := []struct {
		name     string
		heights  []int
		expected int
	}{
		{
			name:     "long ones",
			heights:  []int{2, 1, 5, 6, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1},
			expected: 14,
		},
		{
			name:     "example 1",
			heights:  []int{2, 1, 5, 6, 2, 3},
			expected: 10,
		},
		{
			name:     "example 2",
			heights:  []int{2, 4},
			expected: 4,
		},
		{
			name:     "custom test case",
			heights:  []int{7, 1, 7, 2, 2, 4},
			expected: 8,
		},
		{
			name:     "single bar",
			heights:  []int{5},
			expected: 5,
		},
		{
			name:     "ascending heights",
			heights:  []int{1, 2, 3, 4, 5},
			expected: 9,
		},
		{
			name:     "descending heights",
			heights:  []int{5, 4, 3, 2, 1},
			expected: 9,
		},
		{
			name:     "all same height",
			heights:  []int{3, 3, 3, 3},
			expected: 12,
		},
		{
			name:     "zero height",
			heights:  []int{0},
			expected: 0,
		},
		{
			name:     "with zeros",
			heights:  []int{2, 0, 2},
			expected: 2,
		},
		{
			name:     "tall bar in middle",
			heights:  []int{1, 10, 1},
			expected: 10,
		},
		{
			name:     "two bars",
			heights:  []int{1, 1},
			expected: 2,
		},
		{
			name:     "peak in middle",
			heights:  []int{2, 1, 2},
			expected: 3,
		},
		{
			name:     "valley in middle",
			heights:  []int{3, 1, 3, 2, 2},
			expected: 6,
		},
		{
			name:     "large heights",
			heights:  []int{10000, 10000, 10000},
			expected: 30000,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := largestRectangleArea(tt.heights)
			if result != tt.expected {
				t.Errorf("largestRectangleArea(%v) = %d; expected %d", tt.heights, result, tt.expected)
			}
		})
	}
}
