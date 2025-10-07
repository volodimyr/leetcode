package fibonacci

import "testing"

func TestFind(t *testing.T) {
	tests := []struct {
		name     string
		input    int
		expected int
	}{
		{"base case 0", 0, 0},
		{"base case 1", 1, 1},
		{"n equals 2", 2, 1},
		{"n equals 3", 3, 2},
		{"n equals 4", 4, 3},
		{"n equals 5", 5, 5},
		{"n equals 6", 6, 8},
		{"n equals 10", 10, 55},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := find(tt.input)
			if result != tt.expected {
				t.Errorf("find(%d) = %d; want %d", tt.input, result, tt.expected)
			}
		})
	}
}
