package rotatearray

import (
	"reflect"
	"testing"
)

func TestRotate(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		k    int
		want []int
	}{
		{
			name: "example 1 - rotate by 3",
			nums: []int{1, 2, 3, 4, 5, 6, 7},
			k:    3,
			want: []int{5, 6, 7, 1, 2, 3, 4},
		},
		{
			name: "example 2 - rotate by 2",
			nums: []int{-1, -100, 3, 99},
			k:    2,
			want: []int{3, 99, -1, -100},
		},
		{
			name: "k equals array length",
			nums: []int{1, 2, 3, 4},
			k:    4,
			want: []int{1, 2, 3, 4},
		},
		{
			name: "k greater than array length",
			nums: []int{1, 2, 3},
			k:    5,
			want: []int{2, 3, 1},
		},
		{
			name: "k is zero",
			nums: []int{1, 2, 3, 4},
			k:    0,
			want: []int{1, 2, 3, 4},
		},
		{
			name: "single element array",
			nums: []int{1},
			k:    3,
			want: []int{1},
		},
		{
			name: "two element array rotate by 1",
			nums: []int{1, 2},
			k:    1,
			want: []int{2, 1},
		},
		{
			name: "rotate by 1",
			nums: []int{1, 2, 3, 4, 5},
			k:    1,
			want: []int{5, 1, 2, 3, 4},
		},
		{
			name: "rotate entire array multiple times",
			nums: []int{1, 2, 3},
			k:    9,
			want: []int{1, 2, 3},
		},
		{
			name: "array with negative numbers",
			nums: []int{-5, -3, -1, 0, 2, 4},
			k:    2,
			want: []int{2, 4, -5, -3, -1, 0},
		},
		{
			name: "array with duplicates",
			nums: []int{1, 1, 2, 2, 3, 3},
			k:    3,
			want: []int{2, 3, 3, 1, 1, 2},
		},
		{
			name: "large k value",
			nums: []int{1, 2, 3, 4, 5},
			k:    100003,
			want: []int{3, 4, 5, 1, 2},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			// Make a copy since rotate modifies in-place
			nums := make([]int, len(tt.nums))
			copy(nums, tt.nums)

			rotate(nums, tt.k)

			if !reflect.DeepEqual(nums, tt.want) {
				t.Errorf("rotate() = %v, want %v", nums, tt.want)
			}
		})
	}
}

func TestReverse(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want []int
	}{
		{
			name: "reverse odd length array",
			nums: []int{1, 2, 3, 4, 5},
			want: []int{5, 4, 3, 2, 1},
		},
		{
			name: "reverse even length array",
			nums: []int{1, 2, 3, 4},
			want: []int{4, 3, 2, 1},
		},
		{
			name: "reverse single element",
			nums: []int{1},
			want: []int{1},
		},
		{
			name: "reverse two elements",
			nums: []int{1, 2},
			want: []int{2, 1},
		},
		{
			name: "reverse empty array",
			nums: []int{},
			want: []int{},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			nums := make([]int, len(tt.nums))
			copy(nums, tt.nums)

			reverse(nums)

			if !reflect.DeepEqual(nums, tt.want) {
				t.Errorf("reverse() = %v, want %v", nums, tt.want)
			}
		})
	}
}
