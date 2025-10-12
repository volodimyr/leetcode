package findmininrotatedsortedarray

import "testing"

func TestFindMin(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want int
	}{
		{
			name: "example 1 - rotated 3 times",
			nums: []int{3, 4, 5, 1, 2},
			want: 1,
		},
		{
			name: "example 2 - rotated 4 times",
			nums: []int{4, 5, 6, 7, 0, 1, 2},
			want: 0,
		},
		{
			name: "example 3 - not rotated or fully rotated",
			nums: []int{11, 13, 15, 17},
			want: 11,
		},
		{
			name: "single element",
			nums: []int{1},
			want: 1,
		},
		{
			name: "two elements rotated",
			nums: []int{2, 1},
			want: 1,
		},
		{
			name: "two elements not rotated",
			nums: []int{1, 2},
			want: 1,
		},
		{
			name: "rotated once",
			nums: []int{2, 3, 4, 5, 1},
			want: 1,
		},
		{
			name: "negative numbers rotated",
			nums: []int{3, 4, 5, -1, 0, 1, 2},
			want: -1,
		},
		{
			name: "all negative numbers",
			nums: []int{-3, -2, -1, -5, -4},
			want: -5,
		},
		{
			name: "large rotation",
			nums: []int{7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 6},
			want: 1,
		},
		{
			name: "minimum at start",
			nums: []int{1, 2, 3, 4, 5},
			want: 1,
		},
		{
			name: "minimum at end",
			nums: []int{2, 1},
			want: 1,
		},
		{
			name: "three elements rotated once",
			nums: []int{3, 1, 2},
			want: 1,
		},
		{
			name: "three elements rotated twice",
			nums: []int{2, 3, 1},
			want: 1,
		},
		{
			name: "three elements not rotated",
			nums: []int{1, 2, 3},
			want: 1,
		},
		{
			name: "zero in array",
			nums: []int{5, 6, 7, 0, 1, 2, 3, 4},
			want: 0,
		},
		{
			name: "large values",
			nums: []int{4000, 5000, -5000, -4000, -3000},
			want: -5000,
		},
		{
			name: "minimum at middle",
			nums: []int{5, 6, 7, 8, 1, 2, 3, 4},
			want: 1,
		},
		{
			name: "rotated n-1 times (almost not rotated)",
			nums: []int{2, 3, 4, 5, 6, 1},
			want: 1,
		},
		{
			name: "small rotated array",
			nums: []int{4, 5, 1, 2, 3},
			want: 1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := findMin(tt.nums)
			if got != tt.want {
				t.Errorf("findMin(%v) = %d, want %d", tt.nums, got, tt.want)
			}
		})
	}
}
