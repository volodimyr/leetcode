package captoshippackageswithinddays

import "testing"

func TestShipWithinDays(t *testing.T) {
	tests := []struct {
		name    string
		weights []int
		days    int
		want    int
	}{
		{
			name:    "example 1",
			weights: []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
			days:    5,
			want:    15,
		},
		{
			name:    "example 2",
			weights: []int{3, 2, 2, 4, 1, 4},
			days:    3,
			want:    6,
		},
		{
			name:    "example 3",
			weights: []int{1, 2, 3, 1, 1},
			days:    4,
			want:    3,
		},
		{
			name:    "single package",
			weights: []int{10},
			days:    1,
			want:    10,
		},
		{
			name:    "days equal to number of packages",
			weights: []int{1, 2, 3, 4, 5},
			days:    5,
			want:    5,
		},
		{
			name:    "all packages same weight",
			weights: []int{5, 5, 5, 5, 5},
			days:    2,
			want:    15,
		},
		{
			name:    "ship all in one day",
			weights: []int{1, 2, 3, 4, 5},
			days:    1,
			want:    15,
		},
		{
			name:    "minimum days possible",
			weights: []int{10, 20, 30, 40, 50},
			days:    5,
			want:    50,
		},
		{
			name:    "two packages",
			weights: []int{100, 200},
			days:    1,
			want:    300,
		},
		{
			name:    "two packages two days",
			weights: []int{100, 200},
			days:    2,
			want:    200,
		},
		{
			name:    "large weights",
			weights: []int{500, 500, 500, 500},
			days:    2,
			want:    1000,
		},
		{
			name:    "mixed small weights",
			weights: []int{1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
			days:    3,
			want:    4,
		},
		{
			name:    "ascending order",
			weights: []int{1, 2, 3, 4, 5, 6, 7, 8, 9},
			days:    3,
			want:    17,
		},
		{
			name:    "descending order",
			weights: []int{9, 8, 7, 6, 5, 4, 3, 2, 1},
			days:    3,
			want:    17,
		},
		{
			name:    "one heavy package",
			weights: []int{1, 1, 1, 1, 500},
			days:    2,
			want:    500,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := shipWithinDays(tt.weights, tt.days)
			if got != tt.want {
				t.Errorf("shipWithinDays(%v, %d) = %d, want %d", tt.weights, tt.days, got, tt.want)
			}
		})
	}
}
