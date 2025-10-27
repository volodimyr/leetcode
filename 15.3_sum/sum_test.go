package sum

import (
	"reflect"
	"sort"
	"testing"
)

// Helper function to sort triplets for comparison
func sortTriplets(triplets [][]int) {
	// Sort each individual triplet
	for _, triplet := range triplets {
		sort.Ints(triplet)
	}
	// Sort the slice of triplets
	sort.Slice(triplets, func(i, j int) bool {
		for k := 0; k < 3; k++ {
			if triplets[i][k] != triplets[j][k] {
				return triplets[i][k] < triplets[j][k]
			}
		}
		return false
	})
}

func TestThreeSum(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected [][]int
	}{
		{
			name:     "Example 1 - Multiple triplets",
			nums:     []int{-1, 0, 1, 2, -1, -4},
			expected: [][]int{{-1, -1, 2}, {-1, 0, 1}},
		},
		{
			name:     "Example 2 - No valid triplets",
			nums:     []int{0, 1, 1},
			expected: [][]int{},
		},
		{
			name:     "Example 3 - All zeros",
			nums:     []int{0, 0, 0},
			expected: [][]int{{0, 0, 0}},
		},
		{
			name:     "Minimum length array",
			nums:     []int{-1, 0, 1},
			expected: [][]int{{-1, 0, 1}},
		},
		{
			name:     "All negative numbers",
			nums:     []int{-5, -4, -3, -2, -1},
			expected: [][]int{},
		},
		{
			name:     "All positive numbers",
			nums:     []int{1, 2, 3, 4, 5},
			expected: [][]int{},
		},
		{
			name:     "Multiple duplicates",
			nums:     []int{-2, 0, 0, 2, 2},
			expected: [][]int{{-2, 0, 2}},
		},
		{
			name:     "Complex case with duplicates",
			nums:     []int{-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6},
			expected: [][]int{{-4, -2, 6}, {-4, 0, 4}, {-4, 1, 3}, {-4, 2, 2}, {-2, -2, 4}, {-2, 0, 2}},
		},
		{
			name:     "Two zeros with negatives and positives",
			nums:     []int{-1, 0, 0, 1},
			expected: [][]int{{-1, 0, 1}},
		},
		{
			name:     "Single triplet with duplicates",
			nums:     []int{1, 1, -2},
			expected: [][]int{{-2, 1, 1}},
		},
		{
			name:     "Multiple zeros",
			nums:     []int{0, 0, 0, 0},
			expected: [][]int{{0, 0, 0}},
		},
		{
			name:     "Empty result with exact 3 elements",
			nums:     []int{1, 2, 3},
			expected: [][]int{},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			// Make a copy to avoid modifying test data
			numsCopy := make([]int, len(tt.nums))
			copy(numsCopy, tt.nums)

			result := threeSum(numsCopy)

			// Sort both result and expected for comparison
			sortTriplets(result)
			sortTriplets(tt.expected)

			if !reflect.DeepEqual(result, tt.expected) {
				t.Errorf("threeSum(%v) = %v, want %v", tt.nums, result, tt.expected)
			}
		})
	}
}

func TestThreeSumNoDuplicates(t *testing.T) {
	nums := []int{-1, 0, 1, 2, -1, -4}
	result := threeSum(nums)

	// Check for duplicate triplets
	seen := make(map[[3]int]bool)
	for _, triplet := range result {
		sort.Ints(triplet)
		key := [3]int{triplet[0], triplet[1], triplet[2]}
		if seen[key] {
			t.Errorf("Found duplicate triplet: %v", triplet)
		}
		seen[key] = true
	}
}

func TestThreeSumValidSums(t *testing.T) {
	testCases := [][]int{
		{-1, 0, 1, 2, -1, -4},
		{0, 0, 0},
		{-2, 0, 1, 1, 2},
	}

	for _, nums := range testCases {
		result := threeSum(nums)
		for _, triplet := range result {
			sum := triplet[0] + triplet[1] + triplet[2]
			if sum != 0 {
				t.Errorf("Triplet %v does not sum to 0, got sum = %d", triplet, sum)
			}
		}
	}
}
