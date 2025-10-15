package onlinestockspan

import "testing"

func TestStockSpanner_SinglePrice(t *testing.T) {
	ss := Constructor()
	got := ss.Next(100)
	want := 1
	if got != want {
		t.Errorf("Next(100) = %d, want %d", got, want)
	}
}

func TestStockSpanner_DecreasingPrices(t *testing.T) {
	ss := Constructor()

	tests := []struct {
		price int
		want  int
	}{
		{100, 1},
		{80, 1},
		{60, 1},
	}

	for _, tt := range tests {
		got := ss.Next(tt.price)
		if got != tt.want {
			t.Errorf("Next(%d) = %d, want %d", tt.price, got, tt.want)
		}
	}
}

func TestStockSpanner_IncreasingPrices(t *testing.T) {
	ss := Constructor()

	tests := []struct {
		price int
		want  int
	}{
		{60, 1},
		{70, 2},
		{80, 3},
		{100, 4},
	}

	for _, tt := range tests {
		got := ss.Next(tt.price)
		if got != tt.want {
			t.Errorf("Next(%d) = %d, want %d", tt.price, got, tt.want)
		}
	}
}

func TestStockSpanner_ExampleCase(t *testing.T) {
	ss := Constructor()

	tests := []struct {
		price int
		want  int
	}{
		{100, 1},
		{80, 1},
		{60, 1},
		{70, 2},
		{60, 1},
		{75, 4},
		{85, 6},
	}

	for i, tt := range tests {
		got := ss.Next(tt.price)
		if got != tt.want {
			t.Errorf("Call %d: Next(%d) = %d, want %d", i+1, tt.price, got, tt.want)
		}
	}
}

func TestStockSpanner_MixedPrices(t *testing.T) {
	ss := Constructor()

	tests := []struct {
		price int
		want  int
	}{
		{50, 1},
		{40, 1},
		{30, 1},
		{35, 2},
		{32, 1},
		{45, 5},
		{60, 7},
	}

	for i, tt := range tests {
		got := ss.Next(tt.price)
		if got != tt.want {
			t.Errorf("Call %d: Next(%d) = %d, want %d", i+1, tt.price, got, tt.want)
		}
	}
}

func TestStockSpanner_AllSamePrices(t *testing.T) {
	ss := Constructor()

	for i := 1; i <= 5; i++ {
		got := ss.Next(50)
		want := i
		if got != want {
			t.Errorf("Call %d: Next(50) = %d, want %d", i, got, want)
		}
	}
}

func TestStockSpanner_LargePriceJump(t *testing.T) {
	ss := Constructor()

	tests := []struct {
		price int
		want  int
	}{
		{10, 1},
		{20, 2},
		{30, 3},
		{40, 4},
		{100000, 5},
	}

	for i, tt := range tests {
		got := ss.Next(tt.price)
		if got != tt.want {
			t.Errorf("Call %d: Next(%d) = %d, want %d", i+1, tt.price, got, tt.want)
		}
	}
}
