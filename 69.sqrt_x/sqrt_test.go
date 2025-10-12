package sqrtx

import "testing"

func TestMySqrt(t *testing.T) {
	tests := []struct {
		name string
		x    int
		want int
	}{
		{
			name: "example 1 - perfect square",
			x:    4,
			want: 2,
		},
		{
			name: "example 2 - rounded down",
			x:    8,
			want: 2,
		},
		{
			name: "zero",
			x:    0,
			want: 0,
		},
		{
			name: "one",
			x:    1,
			want: 1,
		},
		{
			name: "two",
			x:    2,
			want: 1,
		},
		{
			name: "three",
			x:    3,
			want: 1,
		},
		{
			name: "perfect square 9",
			x:    9,
			want: 3,
		},
		{
			name: "perfect square 16",
			x:    16,
			want: 4,
		},
		{
			name: "perfect square 25",
			x:    25,
			want: 5,
		},
		{
			name: "perfect square 100",
			x:    100,
			want: 10,
		},
		{
			name: "non-perfect square 15",
			x:    15,
			want: 3,
		},
		{
			name: "non-perfect square 24",
			x:    24,
			want: 4,
		},
		{
			name: "non-perfect square 99",
			x:    99,
			want: 9,
		},
		{
			name: "large perfect square 10000",
			x:    10000,
			want: 100,
		},
		{
			name: "large non-perfect square 10001",
			x:    10001,
			want: 100,
		},
		{
			name: "large number 2147395599",
			x:    2147395599,
			want: 46339,
		},
		{
			name: "max value 2147483647",
			x:    2147483647,
			want: 46340,
		},
		{
			name: "just below perfect square",
			x:    80,
			want: 8,
		},
		{
			name: "just above perfect square",
			x:    65,
			want: 8,
		},
		{
			name: "small non-perfect 5",
			x:    5,
			want: 2,
		},
		{
			name: "small non-perfect 6",
			x:    6,
			want: 2,
		},
		{
			name: "small non-perfect 7",
			x:    7,
			want: 2,
		},
		{
			name: "144",
			x:    144,
			want: 12,
		},
		{
			name: "143",
			x:    143,
			want: 11,
		},
		{
			name: "145",
			x:    145,
			want: 12,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := mySqrt(tt.x)
			if got != tt.want {
				t.Errorf("mySqrt(%d) = %d, want %d", tt.x, got, tt.want)
			}
		})
	}
}
