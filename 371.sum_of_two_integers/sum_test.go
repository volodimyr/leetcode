package sum

import "testing"

func TestGetSum(t *testing.T) {
	tests := []struct {
		name string
		a    int
		b    int
		want int
	}{
		{"both positive small", 1, 2, 3},
		{"both positive", 2, 3, 5},
		{"one zero", 0, 5, 5},
		{"both zero", 0, 0, 0},
		{"positive and negative", 5, -3, 2},
		{"negative and positive", -3, 5, 2},
		{"both negative", -4, -6, -10},
		{"negative result", -10, 3, -7},
		{"large positive bounds", 1000, 1000, 2000},
		{"large negative bounds", -1000, -1000, -2000},
		{"mixed bounds", 1000, -1000, 0},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := getSum(tt.a, tt.b)
			if got != tt.want {
				t.Errorf("getSum(%d, %d) = %d; want %d", tt.a, tt.b, got, tt.want)
			}
		})
	}
}
