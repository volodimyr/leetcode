package kthlargestelementinanarray

import "testing"

func TestFindKthLargest(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		k    int
		want int
	}{
		{
			name: "example 1",
			nums: []int{3, 2, 1, 5, 6, 4},
			k:    2,
			want: 5,
		},
		{
			name: "example 2",
			nums: []int{3, 2, 3, 1, 2, 4, 5, 5, 6},
			k:    4,
			want: 4,
		},
		{
			name: "single element",
			nums: []int{1},
			k:    1,
			want: 1,
		},
		{
			name: "k equals 1",
			nums: []int{3, 2, 1, 5, 6, 4},
			k:    1,
			want: 6,
		},
		{
			name: "k equals array length",
			nums: []int{3, 2, 1, 5, 6, 4},
			k:    6,
			want: 1,
		},
		{
			name: "all same elements",
			nums: []int{5, 5, 5, 5, 5},
			k:    3,
			want: 5,
		},
		{
			name: "negative numbers",
			nums: []int{-1, -2, -3, -4, -5},
			k:    2,
			want: -2,
		},
		{
			name: "mixed positive and negative",
			nums: []int{-3, 2, -1, 5, -6, 4},
			k:    3,
			want: 2,
		},
		{
			name: "two elements",
			nums: []int{2, 1},
			k:    1,
			want: 2,
		},
		{
			name: "two elements k=2",
			nums: []int{2, 1},
			k:    2,
			want: 1,
		},
		{
			name: "already sorted ascending",
			nums: []int{1, 2, 3, 4, 5},
			k:    2,
			want: 4,
		},
		{
			name: "already sorted descending",
			nums: []int{5, 4, 3, 2, 1},
			k:    2,
			want: 4,
		},
		{
			name: "duplicates at boundaries",
			nums: []int{1, 1, 1, 2, 2, 3, 3, 3, 3},
			k:    4,
			want: 3,
		},
		{
			name: "large values",
			nums: []int{10000, 9999, 9998, 9997, 9996},
			k:    3,
			want: 9998,
		},
		{
			name: "small values",
			nums: []int{-10000, -9999, -9998, -9997, -9996},
			k:    3,
			want: -9998,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			numsCopy := make([]int, len(tt.nums))
			copy(numsCopy, tt.nums)

			got := findKthLargest(numsCopy, tt.k)
			if got != tt.want {
				t.Errorf("findKthLargest(%v, %d) = %d, want %d", tt.nums, tt.k, got, tt.want)
			}
		})
	}
}
