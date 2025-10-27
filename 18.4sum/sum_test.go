package sum

import (
	"reflect"
	"sort"
	"testing"
)

func TestFourSum(t *testing.T) {
	tests := []struct {
		name   string
		nums   []int
		target int
		want   [][]int
	}{
		{
			name:   "basic case",
			nums:   []int{1, 0, -1, 0, -2, 2},
			target: 0,
			want:   [][]int{{-2, -1, 1, 2}, {-2, 0, 0, 2}, {-1, 0, 0, 1}},
		},
		{
			name:   "no solution",
			nums:   []int{2, 2, 2, 2, 2},
			target: 9,
			want:   [][]int{},
		},
		{
			name:   "single solution",
			nums:   []int{1, 2, 3, 4},
			target: 10,
			want:   [][]int{{1, 2, 3, 4}},
		},
		{
			name:   "empty array",
			nums:   []int{},
			target: 0,
			want:   [][]int{},
		},
		{
			name:   "array too small",
			nums:   []int{1, 2, 3},
			target: 6,
			want:   [][]int{},
		},
		{
			name:   "all same values with solution",
			nums:   []int{2, 2, 2, 2, 2},
			target: 8,
			want:   [][]int{{2, 2, 2, 2}},
		},
		{
			name:   "duplicates test",
			nums:   []int{0, 0, 0, 0},
			target: 0,
			want:   [][]int{{0, 0, 0, 0}},
		},
		{
			name:   "negative target",
			nums:   []int{-3, -2, -1, 0, 1, 2, 3},
			target: -6,
			want:   [][]int{{-3, -2, -1, 0}},
		},
		{
			name:   "positive target",
			nums:   []int{-3, -2, -1, 0, 1, 2, 3},
			target: 6,
			want:   [][]int{{0, 1, 2, 3}},
		},
		{
			name:   "large target",
			nums:   []int{1, 2, 3, 4, 5, 6},
			target: 18,
			want:   [][]int{{3, 4, 5, 6}},
		},
		{
			name:   "multiple duplicates",
			nums:   []int{-1, -1, -1, 0, 0, 0, 1, 1, 1},
			target: 0,
			want:   [][]int{{-1, -1, 1, 1}, {-1, 0, 0, 1}},
		},
		{
			name:   "complex duplicates",
			nums:   []int{2, 2, 2, 2, 2, 2, 2, 2},
			target: 8,
			want:   [][]int{{2, 2, 2, 2}},
		},
		{
			name:   "exactly 4 elements",
			nums:   []int{1, 2, 3, 4},
			target: 100,
			want:   [][]int{},
		},
		{
			name:   "exactly 4 elements with solution",
			nums:   []int{1, 2, 3, 4},
			target: 10,
			want:   [][]int{{1, 2, 3, 4}},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := fourSum(tt.nums, tt.target)

			// Sort both slices for comparison
			sortQuadruplets(got)
			sortQuadruplets(tt.want)

			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("fourSum() = %v, want %v", got, tt.want)
			}
		})
	}
}

// Helper function to sort quadruplets for consistent comparison
func sortQuadruplets(quads [][]int) {
	// Sort each individual quadruplet
	for _, quad := range quads {
		sort.Ints(quad)
	}

	// Sort the slice of quadruplets
	sort.Slice(quads, func(i, j int) bool {
		for k := 0; k < 4 && k < len(quads[i]) && k < len(quads[j]); k++ {
			if quads[i][k] != quads[j][k] {
				return quads[i][k] < quads[j][k]
			}
		}
		return false
	})
}

// Test for no duplicates in results
func TestFourSumNoDuplicates(t *testing.T) {
	nums := []int{1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3}
	target := 8

	result := fourSum(nums, target)

	// Check for duplicate quadruplets
	seen := make(map[[4]int]bool)
	for _, quad := range result {
		if len(quad) != 4 {
			t.Errorf("Expected quadruplet of length 4, got %d", len(quad))
		}

		key := [4]int{quad[0], quad[1], quad[2], quad[3]}
		if seen[key] {
			t.Errorf("Found duplicate quadruplet: %v", quad)
		}
		seen[key] = true

		// Verify sum
		sum := quad[0] + quad[1] + quad[2] + quad[3]
		if sum != target {
			t.Errorf("Quadruplet %v sums to %d, expected %d", quad, sum, target)
		}
	}
}
