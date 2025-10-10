package searcha2dmatrix

import "testing"

func TestSearchMatrix(t *testing.T) {
	tests := []struct {
		name   string
		matrix [][]int
		target int
		want   bool
	}{
		{
			name:   "example 1 - target exists in first row",
			matrix: [][]int{{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}},
			target: 3,
			want:   true,
		},
		{
			name:   "example 2 - target does not exist",
			matrix: [][]int{{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}},
			target: 13,
			want:   false,
		},
		{
			name:   "target at beginning of matrix",
			matrix: [][]int{{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}},
			target: 1,
			want:   true,
		},
		{
			name:   "target at end of matrix",
			matrix: [][]int{{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}},
			target: 60,
			want:   true,
		},
		{
			name:   "target in middle row",
			matrix: [][]int{{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}},
			target: 16,
			want:   true,
		},
		{
			name:   "target in last row",
			matrix: [][]int{{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}},
			target: 30,
			want:   true,
		},
		{
			name:   "single element matrix - target exists",
			matrix: [][]int{{5}},
			target: 5,
			want:   true,
		},
		{
			name:   "single element matrix - target does not exist",
			matrix: [][]int{{5}},
			target: 1,
			want:   false,
		},
		{
			name:   "single row matrix - target exists",
			matrix: [][]int{{1, 3, 5, 7, 9}},
			target: 7,
			want:   true,
		},
		{
			name:   "single row matrix - target does not exist",
			matrix: [][]int{{1, 3, 5, 7, 9}},
			target: 4,
			want:   false,
		},
		{
			name:   "single column matrix - target exists",
			matrix: [][]int{{1}, {3}, {5}, {7}, {9}},
			target: 5,
			want:   true,
		},
		{
			name:   "single column matrix - target does not exist",
			matrix: [][]int{{1}, {3}, {5}, {7}, {9}},
			target: 4,
			want:   false,
		},
		{
			name:   "target less than all elements",
			matrix: [][]int{{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}},
			target: 0,
			want:   false,
		},
		{
			name:   "target greater than all elements",
			matrix: [][]int{{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}},
			target: 100,
			want:   false,
		},
		{
			name:   "target at end of first row",
			matrix: [][]int{{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}},
			target: 7,
			want:   true,
		},
		{
			name:   "target at beginning of second row",
			matrix: [][]int{{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}},
			target: 10,
			want:   true,
		},
		{
			name:   "target at end of second row",
			matrix: [][]int{{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}},
			target: 20,
			want:   true,
		},
		{
			name:   "target at beginning of last row",
			matrix: [][]int{{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}},
			target: 23,
			want:   true,
		},
		{
			name:   "negative numbers - target exists",
			matrix: [][]int{{-10, -5, -1}, {0, 5, 10}, {15, 20, 25}},
			target: -5,
			want:   true,
		},
		{
			name:   "negative numbers - target does not exist",
			matrix: [][]int{{-10, -5, -1}, {0, 5, 10}, {15, 20, 25}},
			target: -3,
			want:   false,
		},
		{
			name:   "all negative numbers",
			matrix: [][]int{{-100, -90, -80}, {-70, -60, -50}, {-40, -30, -20}},
			target: -60,
			want:   true,
		},
		{
			name:   "large matrix - target in middle",
			matrix: [][]int{{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}},
			target: 11,
			want:   true,
		},
		{
			name:   "two row matrix - target in first row",
			matrix: [][]int{{1, 3, 5}, {7, 9, 11}},
			target: 3,
			want:   true,
		},
		{
			name:   "two row matrix - target in second row",
			matrix: [][]int{{1, 3, 5}, {7, 9, 11}},
			target: 9,
			want:   true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := searchMatrix(tt.matrix, tt.target)
			if got != tt.want {
				t.Errorf("searchMatrix() = %v, want %v", got, tt.want)
			}
		})
	}
}
