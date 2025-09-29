package concatenationofarray

import (
	"reflect"
	"testing"
)

func TestGetConcatenation(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want []int
	}{
		{
			name: "example 1",
			nums: []int{1, 2, 1},
			want: []int{1, 2, 1, 1, 2, 1},
		},
		{
			name: "example 2",
			nums: []int{1, 3, 2, 1},
			want: []int{1, 3, 2, 1, 1, 3, 2, 1},
		},
		{
			name: "single element",
			nums: []int{5},
			want: []int{5, 5},
		},
		{
			name: "two elements",
			nums: []int{7, 8},
			want: []int{7, 8, 7, 8},
		},
		{
			name: "increasing sequence",
			nums: []int{1, 2, 3, 4, 5},
			want: []int{1, 2, 3, 4, 5, 1, 2, 3, 4, 5},
		},
		{
			name: "all same elements",
			nums: []int{9, 9, 9},
			want: []int{9, 9, 9, 9, 9, 9},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := getConcatenation(tt.nums)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("getConcatenation(%v) = %v, want %v", tt.nums, got, tt.want)
			}
		})
	}
}
