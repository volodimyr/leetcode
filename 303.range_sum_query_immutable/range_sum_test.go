package rangesumqueryimmutable

import "testing"

func TestNumArray(t *testing.T) {
	tests := []struct {
		name    string
		nums    []int
		queries []struct {
			left  int
			right int
			want  int
		}
	}{
		{
			name: "example case",
			nums: []int{-2, 0, 3, -5, 2, -1},
			queries: []struct {
				left  int
				right int
				want  int
			}{
				{0, 2, 1},
				{2, 5, -1},
				{0, 5, -3},
			},
		},
		{
			name: "single element",
			nums: []int{5},
			queries: []struct {
				left  int
				right int
				want  int
			}{
				{0, 0, 5},
			},
		},
		{
			name: "all positive numbers",
			nums: []int{1, 2, 3, 4, 5},
			queries: []struct {
				left  int
				right int
				want  int
			}{
				{0, 4, 15},
				{1, 3, 9},
				{2, 2, 3},
			},
		},
		{
			name: "all negative numbers",
			nums: []int{-1, -2, -3, -4, -5},
			queries: []struct {
				left  int
				right int
				want  int
			}{
				{0, 4, -15},
				{1, 3, -9},
				{3, 4, -9},
			},
		},
		{
			name: "zeros",
			nums: []int{0, 0, 0, 0},
			queries: []struct {
				left  int
				right int
				want  int
			}{
				{0, 3, 0},
				{1, 2, 0},
			},
		},
		{
			name: "left equals right",
			nums: []int{10, 20, 30, 40},
			queries: []struct {
				left  int
				right int
				want  int
			}{
				{0, 0, 10},
				{2, 2, 30},
				{3, 3, 40},
			},
		},
		{
			name: "full range",
			nums: []int{1, 2, 3},
			queries: []struct {
				left  int
				right int
				want  int
			}{
				{0, 2, 6},
			},
		},
		{
			name: "mixed positive and negative",
			nums: []int{5, -3, 4, -1, 2},
			queries: []struct {
				left  int
				right int
				want  int
			}{
				{0, 1, 2},
				{1, 3, 0},
				{2, 4, 5},
			},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			numArray := Constructor(tt.nums)
			for i, q := range tt.queries {
				got := numArray.SumRange(q.left, q.right)
				if got != q.want {
					t.Errorf("query %d: SumRange(%d, %d) = %d, want %d", i, q.left, q.right, got, q.want)
				}
			}
		})
	}
}
