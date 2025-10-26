package besttimetobuyandsellstockii

import "testing"

func TestMaxProfit(t *testing.T) {
	tests := []struct {
		name   string
		prices []int
		want   int
	}{
		{
			name:   "example 1 - multiple transactions",
			prices: []int{7, 1, 5, 3, 6, 4},
			want:   7,
		},
		{
			name:   "example 2 - continuous upward trend",
			prices: []int{1, 2, 3, 4, 5},
			want:   4,
		},
		{
			name:   "example 3 - continuous downward trend",
			prices: []int{7, 6, 4, 3, 1},
			want:   0,
		},
		{
			name:   "single day",
			prices: []int{5},
			want:   0,
		},
		{
			name:   "two days - profit",
			prices: []int{1, 5},
			want:   4,
		},
		{
			name:   "two days - loss",
			prices: []int{5, 1},
			want:   0,
		},
		{
			name:   "two days - same price",
			prices: []int{5, 5},
			want:   0,
		},
		{
			name:   "zigzag pattern",
			prices: []int{1, 7, 2, 8, 3, 9},
			want:   18, // (7-1) + (8-2) + (9-3) = 6 + 6 + 6
		},
		{
			name:   "valley and peak",
			prices: []int{3, 2, 1, 4, 5, 6},
			want:   5, // buy at 1, sell at 6
		},
		{
			name:   "multiple small gains",
			prices: []int{1, 2, 1, 2, 1, 2},
			want:   3, // three gains of 1 each
		},
		{
			name:   "flat then up",
			prices: []int{5, 5, 5, 10},
			want:   5,
		},
		{
			name:   "up then flat",
			prices: []int{1, 10, 10, 10},
			want:   9,
		},
		{
			name:   "all zeros",
			prices: []int{0, 0, 0, 0},
			want:   0,
		},
		{
			name:   "starting from zero",
			prices: []int{0, 1, 2, 3},
			want:   3,
		},
		{
			name:   "large single jump",
			prices: []int{1, 10000},
			want:   9999,
		},
		{
			name:   "many small ups and downs",
			prices: []int{5, 1, 5, 1, 5, 1, 5},
			want:   12, // three cycles of 4 profit each
		},
		{
			name:   "peak in middle",
			prices: []int{1, 5, 3, 7, 2},
			want:   8, // (5-1) + (7-3) = 4 + 4
		},
		{
			name:   "alternating by one",
			prices: []int{1, 2, 1, 2, 1, 2, 1},
			want:   3,
		},
		{
			name:   "max constraint values",
			prices: []int{10000, 0, 10000, 0, 10000},
			want:   20000,
		},
		{
			name:   "gradual increase then decrease",
			prices: []int{1, 2, 3, 4, 3, 2, 1},
			want:   3, // sell at peak (day 4)
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

// Test to verify the greedy approach
func TestMaxProfitGreedyLogic(t *testing.T) {
	// This test verifies that capturing every upward movement
	// is equivalent to the optimal strategy
	prices := []int{1, 3, 2, 4, 1, 5}
	// Upward movements: (3-1)=2, (4-2)=2, (5-1)=4
	// Total: 2 + 2 + 4 = 8
	want := 8
	got := maxProfit(prices)

	if got != want {
		t.Errorf("maxProfit(%v) = %d, want %d (sum of all positive diffs)", prices, got, want)
	}
}
