package sortcolors

import (
	"reflect"
	"testing"
)

func TestSortColors(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want []int
	}{
		{
			name: "example 1",
			nums: []int{2, 0, 2, 1, 1, 0},
			want: []int{0, 0, 1, 1, 2, 2},
		},
		{
			name: "example 2",
			nums: []int{2, 0, 1},
			want: []int{0, 1, 2},
		},
		{
			name: "already sorted",
			nums: []int{0, 0, 1, 1, 2, 2},
			want: []int{0, 0, 1, 1, 2, 2},
		},
		{
			name: "all same color - red",
			nums: []int{0, 0, 0},
			want: []int{0, 0, 0},
		},
		{
			name: "all same color - blue",
			nums: []int{2, 2, 2},
			want: []int{2, 2, 2},
		},
		{
			name: "single element",
			nums: []int{1},
			want: []int{1},
		},
		{
			name: "mixed small input",
			nums: []int{1, 0, 2},
			want: []int{0, 1, 2},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			// Copy input to check in-place modification
			original := append([]int(nil), tt.nums...)

			sortColors(tt.nums)

			if !reflect.DeepEqual(tt.nums, tt.want) {
				t.Errorf("sortColors(%v) = %v, want %v", original, tt.nums, tt.want)
			}
		})
	}
}
