package trappingrainwater

import "testing"

func TestTrap(t *testing.T) {
	tests := []struct {
		name   string
		height []int
		want   int
	}{
		{
			name:   "example 0",
			height: []int{5, 4, 1, 2},
			want:   1,
		},
		{
			name:   "example 1",
			height: []int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1},
			want:   6,
		},
		{
			name:   "example 2",
			height: []int{4, 2, 0, 3, 2, 5},
			want:   9,
		},
		{
			name:   "no water trapped - flat",
			height: []int{0, 0, 0, 0},
			want:   0,
		},
		{
			name:   "no water trapped - ascending",
			height: []int{1, 2, 3, 4, 5},
			want:   0,
		},
		{
			name:   "no water trapped - descending",
			height: []int{5, 4, 3, 2, 1},
			want:   0,
		},
		{
			name:   "single element",
			height: []int{5},
			want:   0,
		},
		{
			name:   "two elements",
			height: []int{3, 0},
			want:   0,
		},
		{
			name:   "simple valley",
			height: []int{3, 0, 3},
			want:   3,
		},
		{
			name:   "multiple valleys",
			height: []int{3, 0, 2, 0, 4},
			want:   7,
		},
		{
			name:   "complex pattern",
			height: []int{5, 2, 1, 2, 1, 5},
			want:   14,
		},
		{
			name:   "all zeros",
			height: []int{0, 0, 0},
			want:   0,
		},
		{
			name:   "peak in middle",
			height: []int{2, 0, 2},
			want:   2,
		},
		{
			name:   "asymmetric walls",
			height: []int{5, 1, 3},
			want:   2,
		},
		{
			name:   "long flat section",
			height: []int{3, 0, 0, 6, 0, 0, 3},
			want:   12,
		},
		{
			name:   "water at different levels",
			height: []int{4, 2, 3},
			want:   1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := trap(tt.height)
			if got != tt.want {
				t.Errorf("trap(%v) = %v, want %v", tt.height, got, tt.want)
			}
		})
	}
}
