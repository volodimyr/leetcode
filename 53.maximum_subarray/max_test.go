package maximumsubarray

import "testing"

func TestMaxSubArray(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want int
	}{
		{
			name: "Example 1",
			nums: []int{-2, 1, -3, 4, -1, 2, 1, -5, 4},
			want: 6,
		},
		{
			name: "Example 2",
			nums: []int{1},
			want: 1,
		},
		{
			name: "Example 3",
			nums: []int{5, 4, -1, 7, 8},
			want: 23,
		},
		{
			name: "All negative numbers",
			nums: []int{-8, -3, -6, -2, -5, -4},
			want: -2,
		},
		{
			name: "Single negative number",
			nums: []int{-10},
			want: -10,
		},
		{
			name: "All positives",
			nums: []int{1, 2, 3, 4, 5},
			want: 15,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := maxSubArray(tt.nums)
			if got != tt.want {
				t.Errorf("maxSubArray(%v) = %d; want %d", tt.nums, got, tt.want)
			}
		})
	}
}
