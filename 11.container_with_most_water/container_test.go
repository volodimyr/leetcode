package containerwithmostwater

import "testing"

func TestMaxArea(t *testing.T) {
	tests := []struct {
		name   string
		height []int
		want   int
	}{
		{
			name:   "example 1",
			height: []int{1, 8, 6, 2, 5, 4, 8, 3, 7},
			want:   49,
		},
		{
			name:   "example 2",
			height: []int{1, 1},
			want:   1,
		},
		{
			name:   "two lines with different heights",
			height: []int{1, 2},
			want:   1,
		},
		{
			name:   "increasing heights",
			height: []int{1, 2, 3, 4, 5},
			want:   6,
		},
		{
			name:   "decreasing heights",
			height: []int{5, 4, 3, 2, 1},
			want:   6,
		},
		{
			name:   "all same heights",
			height: []int{5, 5, 5, 5, 5},
			want:   20,
		},
		{
			name:   "tall lines at ends",
			height: []int{8, 1, 1, 1, 1, 8},
			want:   40,
		},
		{
			name:   "one tall line and one short",
			height: []int{100, 1},
			want:   1,
		},
		{
			name:   "zero heights included",
			height: []int{0, 5, 0, 5, 0},
			want:   10,
		},
		{
			name:   "large array with max values",
			height: []int{10000, 1, 1, 1, 1, 10000},
			want:   50000,
		},
		{
			name:   "zigzag pattern",
			height: []int{1, 3, 2, 5, 4, 6, 5, 7},
			want:   20,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := maxArea(tt.height)
			if got != tt.want {
				t.Errorf("maxArea(%v) = %d, want %d", tt.height, got, tt.want)
			}
		})
	}
}
