package missingnumber

import "testing"

func TestMissingNumber(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want int
	}{
		{
			name: "example1",
			nums: []int{3, 0, 1},
			want: 2,
		},
		{
			name: "example2",
			nums: []int{0, 1},
			want: 2,
		},
		{
			name: "example3",
			nums: []int{9, 6, 4, 2, 3, 5, 7, 0, 1},
			want: 8,
		},
		{
			name: "missing zero",
			nums: []int{1, 2, 3},
			want: 0,
		},
		{
			name: "missing n",
			nums: []int{0, 1, 2, 3},
			want: 4,
		},
		{
			name: "single element 0",
			nums: []int{1},
			want: 0,
		},
		{
			name: "single element 1",
			nums: []int{0},
			want: 1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := missingNumber(tt.nums)
			if got != tt.want {
				t.Fatalf("missingNumber(%v) = %v, want %v", tt.nums, got, tt.want)
			}
		})
	}
}
