package laststoneweight

import "testing"

func TestLastStoneWeight(t *testing.T) {
	tests := []struct {
		name   string
		stones []int
		want   int
	}{
		{
			name:   "example 1",
			stones: []int{2, 7, 4, 1, 8, 1},
			want:   1,
		},
		{
			name:   "example 2",
			stones: []int{1},
			want:   1,
		},
		{
			name:   "all stones destroyed",
			stones: []int{2, 2},
			want:   0,
		},
		{
			name:   "two different stones",
			stones: []int{3, 7},
			want:   4,
		},
		{
			name:   "multiple same weight stones",
			stones: []int{5, 5, 5, 5},
			want:   0,
		},
		{
			name:   "descending order",
			stones: []int{9, 7, 5, 3, 1},
			want:   1,
		},
		{
			name:   "ascending order",
			stones: []int{1, 3, 5, 7, 9},
			want:   1,
		},
		{
			name:   "three stones",
			stones: []int{2, 7, 4},
			want:   1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := lastStoneWeight(tt.stones)
			if got != tt.want {
				t.Errorf("lastStoneWeight(%v) = %v, want %v", tt.stones, got, tt.want)
			}
		})
	}
}
