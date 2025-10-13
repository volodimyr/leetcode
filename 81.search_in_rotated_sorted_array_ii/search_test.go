package searchinrotatedsortedarrayii

import "testing"

func TestSearch(t *testing.T) {
	tests := []struct {
		name   string
		nums   []int
		target int
		want   bool
	}{
		// Basic examples from problem
		{
			name:   "Example 1: target exists",
			nums:   []int{2, 5, 6, 0, 0, 1, 2},
			target: 0,
			want:   true,
		},
		{
			name:   "Example 2: target doesn't exist",
			nums:   []int{2, 5, 6, 0, 0, 1, 2},
			target: 3,
			want:   false,
		},
		// Single element
		{
			name:   "Single element - found",
			nums:   []int{1},
			target: 1,
			want:   true,
		},
		{
			name:   "Single element - not found",
			nums:   []int{1},
			target: 0,
			want:   false,
		},
		// Two elements
		{
			name:   "Two elements - first",
			nums:   []int{1, 3},
			target: 1,
			want:   true,
		},
		{
			name:   "Two elements - second",
			nums:   []int{1, 3},
			target: 3,
			want:   true,
		},
		{
			name:   "Two elements - not found",
			nums:   []int{1, 3},
			target: 2,
			want:   false,
		},
		// All duplicates
		{
			name:   "All same elements - target exists",
			nums:   []int{1, 1, 1, 1, 1},
			target: 1,
			want:   true,
		},
		{
			name:   "All same elements - target doesn't exist",
			nums:   []int{1, 1, 1, 1, 1},
			target: 2,
			want:   false,
		},
		// Duplicates with rotation
		{
			name:   "Duplicates at boundaries",
			nums:   []int{1, 1, 1, 2, 1, 1, 1},
			target: 2,
			want:   true,
		},
		{
			name:   "Many duplicates - target at beginning",
			nums:   []int{2, 2, 2, 3, 4, 2},
			target: 3,
			want:   true,
		},
		{
			name:   "Many duplicates - target at end",
			nums:   []int{3, 1, 2, 2, 2, 2},
			target: 1,
			want:   true,
		},
		// No rotation (already sorted)
		{
			name:   "No rotation - sorted array",
			nums:   []int{1, 2, 3, 4, 5},
			target: 3,
			want:   true,
		},
		{
			name:   "No rotation - target not found",
			nums:   []int{1, 2, 3, 4, 5},
			target: 6,
			want:   false,
		},
		// Heavy rotation
		{
			name:   "Rotated at last position",
			nums:   []int{5, 1, 2, 3, 4},
			target: 1,
			want:   true,
		},
		{
			name:   "Rotated in middle",
			nums:   []int{4, 5, 6, 7, 0, 1, 2},
			target: 0,
			want:   true,
		},
		// Edge cases with duplicates
		{
			name:   "Target equals boundary duplicates",
			nums:   []int{1, 3, 1, 1, 1},
			target: 1,
			want:   true,
		},
		{
			name:   "Two distinct values with duplicates",
			nums:   []int{1, 1, 3, 1},
			target: 3,
			want:   true,
		},
		// Negative numbers
		{
			name:   "Negative numbers - found",
			nums:   []int{-5, -3, -1, 0, 2, 4},
			target: -3,
			want:   true,
		},
		{
			name:   "Negative numbers - not found",
			nums:   []int{-5, -3, -1, 0, 2, 4},
			target: -2,
			want:   false,
		},
		{
			name:   "Mixed negative and positive",
			nums:   []int{3, 4, 5, -5, -3, -1, 0, 1},
			target: -3,
			want:   true,
		},
		// Target at different positions
		{
			name:   "Target at beginning",
			nums:   []int{3, 4, 5, 1, 2},
			target: 3,
			want:   true,
		},
		{
			name:   "Target at end",
			nums:   []int{3, 4, 5, 1, 2},
			target: 2,
			want:   true,
		},
		{
			name:   "Target in middle",
			nums:   []int{4, 5, 6, 7, 0, 1, 2},
			target: 6,
			want:   true,
		},
		// Complex duplicate patterns
		{
			name:   "Duplicates everywhere",
			nums:   []int{2, 2, 2, 3, 2, 2, 2},
			target: 3,
			want:   true,
		},
		{
			name:   "Duplicates everywhere - not found",
			nums:   []int{2, 2, 2, 3, 2, 2, 2},
			target: 4,
			want:   false,
		},
		// Boundary values
		{
			name:   "Max constraint values",
			nums:   []int{10000, -10000, 0},
			target: -10000,
			want:   true,
		},
		{
			name:   "Zero in array",
			nums:   []int{0, 0, 1, 2, 0},
			target: 0,
			want:   true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := search(tt.nums, tt.target)
			if got != tt.want {
				t.Errorf("search(%v, %d) = %v, want %v", tt.nums, tt.target, got, tt.want)
			}
		})
	}
}

func TestSkipDuplicates(t *testing.T) {
	tests := []struct {
		name  string
		nums  []int
		L     int
		R     int
		wantL int
		wantR int
	}{
		{
			name:  "No duplicates",
			nums:  []int{1, 2, 3, 4, 5},
			L:     0,
			R:     4,
			wantL: 0,
			wantR: 4,
		},
		{
			name:  "Duplicates at left",
			nums:  []int{1, 1, 1, 2, 3},
			L:     0,
			R:     4,
			wantL: 2,
			wantR: 4,
		},
		{
			name:  "Duplicates at right",
			nums:  []int{1, 2, 3, 3, 3},
			L:     0,
			R:     4,
			wantL: 0,
			wantR: 2,
		},
		{
			name:  "Duplicates at both ends",
			nums:  []int{1, 1, 2, 1, 1},
			L:     0,
			R:     4,
			wantL: 1,
			wantR: 2,
		},
		{
			name:  "All same elements",
			nums:  []int{1, 1, 1, 1, 1},
			L:     0,
			R:     4,
			wantL: 4,
			wantR: 4,
		},
		{
			name:  "Two elements - same",
			nums:  []int{1, 1},
			L:     0,
			R:     1,
			wantL: 1,
			wantR: 1,
		},
		{
			name:  "Two elements - different",
			nums:  []int{1, 2},
			L:     0,
			R:     1,
			wantL: 0,
			wantR: 1,
		},
		{
			name:  "Complex pattern",
			nums:  []int{1, 1, 1, 2, 1, 1, 1},
			L:     0,
			R:     6,
			wantL: 2,
			wantR: 3,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			gotL, gotR := skipDuplicates(tt.nums, tt.L, tt.R)
			if gotL != tt.wantL || gotR != tt.wantR {
				t.Errorf("skipDuplicates(%v, %d, %d) = (%d, %d), want (%d, %d)",
					tt.nums, tt.L, tt.R, gotL, gotR, tt.wantL, tt.wantR)
			}
		})
	}
}
