package boatstosavepeople

import "testing"

func TestNumRescueBoats(t *testing.T) {
	tests := []struct {
		name   string
		people []int
		limit  int
		want   int
	}{
		{
			name:   "Example 1: two light people fit in one boat",
			people: []int{1, 2},
			limit:  3,
			want:   1,
		},
		{
			name:   "Example 2: mixed weights",
			people: []int{3, 2, 2, 1},
			limit:  3,
			want:   3,
		},
		{
			name:   "Example 3: all need separate boats",
			people: []int{3, 5, 3, 4},
			limit:  5,
			want:   4,
		},
		{
			name:   "single person",
			people: []int{5},
			limit:  5,
			want:   1,
		},
		{
			name:   "all people at limit",
			people: []int{5, 5, 5, 5},
			limit:  5,
			want:   4,
		},
		{
			name:   "two people at limit",
			people: []int{5, 5},
			limit:  5,
			want:   2,
		},
		{
			name:   "light and heavy people",
			people: []int{1, 1, 1, 5, 5, 5},
			limit:  5,
			want:   5,
		},
		{
			name:   "all very light people",
			people: []int{1, 1, 1, 1},
			limit:  5,
			want:   2,
		},
		{
			name:   "three people with various weights",
			people: []int{2, 2, 3},
			limit:  5,
			want:   2,
		},
		{
			name:   "large array with mixed weights",
			people: []int{5, 1, 4, 2, 3, 3, 2, 1},
			limit:  5,
			want:   5,
		},
		{
			name:   "pairs that exactly match limit",
			people: []int{2, 3, 2, 3},
			limit:  5,
			want:   2,
		},
		{
			name:   "minimum constraints",
			people: []int{1},
			limit:  1,
			want:   1,
		},
		{
			name:   "all people can pair up",
			people: []int{1, 1, 2, 2},
			limit:  3,
			want:   2,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			// Create a copy since sort.Ints modifies the slice
			peopleCopy := make([]int, len(tt.people))
			copy(peopleCopy, tt.people)

			got := numRescueBoats(peopleCopy, tt.limit)
			if got != tt.want {
				t.Errorf("numRescueBoats(%v, %d) = %d, want %d", tt.people, tt.limit, got, tt.want)
			}
		})
	}
}
