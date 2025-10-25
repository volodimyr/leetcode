package besttimetobuyandsellstock

import "testing"

func TestMaxProfit(t *testing.T) {
	tests := []struct {
		name   string
		prices []int
		want   int
	}{
		{
			name:   "example 1: profit possible",
			prices: []int{7, 1, 5, 3, 6, 4},
			want:   5,
		},
		{
			name:   "example 2: no profit possible",
			prices: []int{7, 6, 4, 3, 1},
			want:   0,
		},
		{
			name:   "single element",
			prices: []int{5},
			want:   0,
		},
		{
			name:   "two elements increasing",
			prices: []int{1, 5},
			want:   4,
		},
		{
			name:   "two elements decreasing",
			prices: []int{5, 1},
			want:   0,
		},
		{
			name:   "all same prices",
			prices: []int{3, 3, 3, 3},
			want:   0,
		},
		{
			name:   "buy at minimum sell at maximum",
			prices: []int{2, 4, 1, 7, 5, 11},
			want:   10,
		},
		{
			name:   "profit at the end",
			prices: []int{3, 2, 6, 5, 0, 3},
			want:   4,
		},
		{
			name:   "minimum price at the end",
			prices: []int{5, 4, 3, 2, 1},
			want:   0,
		},
		{
			name:   "maximum profit with multiple peaks",
			prices: []int{1, 2, 4, 2, 5, 7, 2, 4, 9, 0},
			want:   8,
		},
		{
			name:   "prices with zeros",
			prices: []int{0, 5, 3, 8, 1},
			want:   8,
		},
		{
			name:   "large price values",
			prices: []int{10000, 1, 10000},
			want:   9999,
		},
		{
			name:   "alternating high low",
			prices: []int{10, 1, 10, 1, 10},
			want:   9,
		},
		{
			name:   "increasing sequence",
			prices: []int{1, 2, 3, 4, 5},
			want:   4,
		},
		{
			name:   "profit in middle section",
			prices: []int{5, 1, 3, 6, 2, 4},
			want:   5,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := maxProfit(tt.prices)
			if got != tt.want {
				t.Errorf("maxProfit(%v) = %d, want %d", tt.prices, got, tt.want)
			}
		})
	}
}
