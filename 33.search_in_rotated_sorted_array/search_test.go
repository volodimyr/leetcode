package searchinrotatedsortedarray

import "testing"

func TestSearch(t *testing.T) {
	tests := []struct {
		name   string
		nums   []int
		target int
		want   int
	}{
		{
			name:   "example 1: target found in rotated array",
			nums:   []int{4, 5, 6, 7, 0, 1, 2},
			target: 0,
			want:   4,
		},
		{
			name:   "example 2: target not in array",
			nums:   []int{4, 5, 6, 7, 0, 1, 2},
			target: 3,
			want:   -1,
		},
		{
			name:   "example 3: single element array, target not found",
			nums:   []int{1},
			target: 0,
			want:   -1,
		},
		{
			name:   "single element array, target found",
			nums:   []int{5},
			target: 5,
			want:   0,
		},
		{
			name:   "no rotation, target at beginning",
			nums:   []int{1, 2, 3, 4, 5},
			target: 1,
			want:   0,
		},
		{
			name:   "no rotation, target at end",
			nums:   []int{1, 2, 3, 4, 5},
			target: 5,
			want:   4,
		},
		{
			name:   "no rotation, target in middle",
			nums:   []int{1, 2, 3, 4, 5},
			target: 3,
			want:   2,
		},
		{
			name:   "rotated by 1, target at beginning",
			nums:   []int{2, 3, 4, 5, 1},
			target: 2,
			want:   0,
		},
		{
			name:   "rotated by 1, target at end",
			nums:   []int{2, 3, 4, 5, 1},
			target: 1,
			want:   4,
		},
		{
			name:   "rotated by 1, target in middle",
			nums:   []int{2, 3, 4, 5, 1},
			target: 4,
			want:   2,
		},
		{
			name:   "heavily rotated, target in first half",
			nums:   []int{6, 7, 8, 1, 2, 3, 4, 5},
			target: 7,
			want:   1,
		},
		{
			name:   "heavily rotated, target in second half",
			nums:   []int{6, 7, 8, 1, 2, 3, 4, 5},
			target: 3,
			want:   5,
		},
		{
			name:   "two elements, not rotated, target first",
			nums:   []int{1, 3},
			target: 1,
			want:   0,
		},
		{
			name:   "two elements, not rotated, target second",
			nums:   []int{1, 3},
			target: 3,
			want:   1,
		},
		{
			name:   "two elements, rotated, target first",
			nums:   []int{3, 1},
			target: 3,
			want:   0,
		},
		{
			name:   "two elements, rotated, target second",
			nums:   []int{3, 1},
			target: 1,
			want:   1,
		},
		{
			name:   "target is negative number",
			nums:   []int{-5, -3, -1, 0, 2, 4},
			target: -3,
			want:   1,
		},
		{
			name:   "all negative numbers, rotated",
			nums:   []int{-2, -1, -10, -9, -8, -5, -4, -3},
			target: -5,
			want:   5,
		},
		{
			name:   "target smaller than all elements",
			nums:   []int{4, 5, 6, 7, 0, 1, 2},
			target: -1,
			want:   -1,
		},
		{
			name:   "target larger than all elements",
			nums:   []int{4, 5, 6, 7, 0, 1, 2},
			target: 10,
			want:   -1,
		},
		{
			name:   "large array, no rotation, target in middle",
			nums:   []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
			target: 5,
			want:   4,
		},
		{
			name:   "large array, rotated at middle, target before rotation",
			nums:   []int{6, 7, 8, 9, 10, 1, 2, 3, 4, 5},
			target: 8,
			want:   2,
		},
		{
			name:   "large array, rotated at middle, target after rotation",
			nums:   []int{6, 7, 8, 9, 10, 1, 2, 3, 4, 5},
			target: 3,
			want:   7,
		},
		{
			name:   "rotated array, target at rotation point",
			nums:   []int{5, 6, 7, 1, 2, 3, 4},
			target: 1,
			want:   3,
		},
		{
			name:   "rotated array, target just before rotation",
			nums:   []int{5, 6, 7, 1, 2, 3, 4},
			target: 7,
			want:   2,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := search(tt.nums, tt.target)
			if got != tt.want {
				t.Errorf("search(%v, %d) = %d, want %d", tt.nums, tt.target, got, tt.want)
			}
		})
	}
}
