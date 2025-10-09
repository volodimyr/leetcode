package majorityelement

import "testing"

func TestMajorityElement(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want int
	}{
		{
			name: "example 1 - simple case with 3 elements",
			nums: []int{3, 2, 3},
			want: 3,
		},
		{
			name: "example 2 - seven elements",
			nums: []int{2, 2, 1, 1, 1, 2, 2},
			want: 2,
		},
		{
			name: "single element",
			nums: []int{1},
			want: 1,
		},
		{
			name: "two identical elements",
			nums: []int{5, 5},
			want: 5,
		},
		{
			name: "majority element at beginning",
			nums: []int{1, 1, 1, 2, 3},
			want: 1,
		},
		{
			name: "majority element at end",
			nums: []int{2, 3, 1, 1, 1},
			want: 1,
		},
		{
			name: "majority element in middle",
			nums: []int{3, 3, 4, 4, 4},
			want: 4,
		},
		{
			name: "all elements are the same",
			nums: []int{7, 7, 7, 7, 7},
			want: 7,
		},
		{
			name: "negative numbers",
			nums: []int{-1, -1, -1, 2, 2},
			want: -1,
		},
		{
			name: "mixed positive and negative",
			nums: []int{-5, 3, -5, -5, 3},
			want: -5,
		},
		{
			name: "large majority count",
			nums: []int{1, 1, 1, 1, 1, 2, 3, 4, 5},
			want: 1,
		},
		{
			name: "exact majority threshold (n/2 + 1)",
			nums: []int{1, 2, 3, 1, 1},
			want: 1,
		},
		{
			name: "alternating pattern with majority",
			nums: []int{1, 2, 1, 2, 1, 2, 1},
			want: 1,
		},
		{
			name: "zero as majority element",
			nums: []int{0, 0, 1, 1, 0},
			want: 0,
		},
		{
			name: "large values",
			nums: []int{1000000000, 1000000000, -1000000000},
			want: 1000000000,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := majorityElement(tt.nums)
			if got != tt.want {
				t.Errorf("majorityElement(%v) = %v, want %v", tt.nums, got, tt.want)
			}
		})
	}
}

// TestMajorityElementAlgorithm verifies the Boyer-Moore Voting Algorithm behavior
func TestMajorityElementAlgorithm(t *testing.T) {
	t.Run("algorithm handles multiple candidates correctly", func(t *testing.T) {
		// The algorithm should correctly find the majority even when
		// other elements temporarily become candidates
		nums := []int{4, 5, 4, 5, 4, 5, 4, 4, 4}
		want := 4
		got := majorityElement(nums)
		if got != want {
			t.Errorf("majorityElement(%v) = %v, want %v", nums, got, want)
		}
	})

	t.Run("algorithm with count reaching zero multiple times", func(t *testing.T) {
		// Tests case where count hits zero and candidate changes
		nums := []int{1, 2, 3, 3, 3, 3, 3}
		want := 3
		got := majorityElement(nums)
		if got != want {
			t.Errorf("majorityElement(%v) = %v, want %v", nums, got, want)
		}
	})
}

// TestMajorityElementEdgeCases tests boundary conditions
func TestMajorityElementEdgeCases(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want int
	}{
		{
			name: "minimum array size",
			nums: []int{42},
			want: 42,
		},
		{
			name: "two elements same",
			nums: []int{99, 99},
			want: 99,
		},
		{
			name: "minimum constraint value",
			nums: []int{-1000000000, -1000000000, 0},
			want: -1000000000,
		},
		{
			name: "maximum constraint value",
			nums: []int{1000000000, 1000000000, 0},
			want: 1000000000,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := majorityElement(tt.nums)
			if got != tt.want {
				t.Errorf("majorityElement(%v) = %v, want %v", tt.nums, got, tt.want)
			}
		})
	}
}
