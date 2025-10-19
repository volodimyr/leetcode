package rangesumquery2dimmutable

import "testing"

func TestNumMatrix(t *testing.T) {
	tests := []struct {
		name     string
		matrix   [][]int
		queries  [][]int
		expected []int
	}{
		{
			name: "example 1",
			matrix: [][]int{
				{3, 0, 1, 4, 2},
				{5, 6, 3, 2, 1},
				{1, 2, 0, 1, 5},
				{4, 1, 0, 1, 7},
				{1, 0, 3, 0, 5},
			},
			queries: [][]int{
				{2, 1, 4, 3},
				{1, 1, 2, 2},
				{1, 2, 2, 4},
			},
			expected: []int{8, 11, 12},
		},
		{
			name: "single element",
			matrix: [][]int{
				{5},
			},
			queries: [][]int{
				{0, 0, 0, 0},
			},
			expected: []int{5},
		},
		{
			name: "single row",
			matrix: [][]int{
				{1, 2, 3, 4, 5},
			},
			queries: [][]int{
				{0, 0, 0, 4},
				{0, 1, 0, 3},
				{0, 2, 0, 2},
			},
			expected: []int{15, 9, 3},
		},
		{
			name: "single column",
			matrix: [][]int{
				{1},
				{2},
				{3},
				{4},
				{5},
			},
			queries: [][]int{
				{0, 0, 4, 0},
				{1, 0, 3, 0},
				{2, 0, 2, 0},
			},
			expected: []int{15, 9, 3},
		},
		{
			name: "negative numbers",
			matrix: [][]int{
				{-1, -2, -3},
				{-4, -5, -6},
				{-7, -8, -9},
			},
			queries: [][]int{
				{0, 0, 2, 2},
				{1, 1, 2, 2},
				{0, 0, 1, 1},
			},
			expected: []int{-45, -28, -12},
		},
		{
			name: "mixed positive and negative",
			matrix: [][]int{
				{1, -2, 3},
				{-4, 5, -6},
				{7, -8, 9},
			},
			queries: [][]int{
				{0, 0, 2, 2},
				{1, 1, 1, 1},
				{0, 0, 0, 2},
			},
			expected: []int{5, 5, 2},
		},
		{
			name: "all zeros",
			matrix: [][]int{
				{0, 0, 0},
				{0, 0, 0},
				{0, 0, 0},
			},
			queries: [][]int{
				{0, 0, 2, 2},
				{1, 1, 2, 2},
			},
			expected: []int{0, 0},
		},
		{
			name: "query top-left corner",
			matrix: [][]int{
				{1, 2, 3},
				{4, 5, 6},
				{7, 8, 9},
			},
			queries: [][]int{
				{0, 0, 0, 0},
			},
			expected: []int{1},
		},
		{
			name: "query bottom-right corner",
			matrix: [][]int{
				{1, 2, 3},
				{4, 5, 6},
				{7, 8, 9},
			},
			queries: [][]int{
				{2, 2, 2, 2},
			},
			expected: []int{9},
		},
		{
			name: "full matrix query",
			matrix: [][]int{
				{1, 2, 3},
				{4, 5, 6},
				{7, 8, 9},
			},
			queries: [][]int{
				{0, 0, 2, 2},
			},
			expected: []int{45},
		},
		{
			name: "multiple non-overlapping queries",
			matrix: [][]int{
				{1, 2, 3, 4},
				{5, 6, 7, 8},
				{9, 10, 11, 12},
			},
			queries: [][]int{
				{0, 0, 1, 1},
				{0, 2, 1, 3},
				{2, 0, 2, 3},
			},
			expected: []int{14, 22, 42},
		},
		{
			name: "rectangular matrix more rows",
			matrix: [][]int{
				{1, 2},
				{3, 4},
				{5, 6},
				{7, 8},
			},
			queries: [][]int{
				{0, 0, 3, 1},
				{1, 0, 2, 1},
			},
			expected: []int{36, 18},
		},
		{
			name: "rectangular matrix more cols",
			matrix: [][]int{
				{1, 2, 3, 4},
				{5, 6, 7, 8},
			},
			queries: [][]int{
				{0, 0, 1, 3},
				{0, 1, 1, 2},
			},
			expected: []int{36, 18},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			nm := Constructor(tt.matrix)
			for i, query := range tt.queries {
				result := nm.SumRegion(query[0], query[1], query[2], query[3])
				if result != tt.expected[i] {
					t.Errorf("query %d: SumRegion(%d, %d, %d, %d) = %d, expected %d",
						i, query[0], query[1], query[2], query[3], result, tt.expected[i])
				}
			}
		})
	}
}
