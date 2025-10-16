package carfleet

import "testing"

func TestCarFleet(t *testing.T) {
	tests := []struct {
		name     string
		target   int
		position []int
		speed    []int
		expected int
	}{
		{
			name:     "one-by-one",
			target:   10,
			position: []int{8, 3, 7, 4, 6, 5},
			speed:    []int{4, 4, 4, 4, 4, 4},
			expected: 6,
		},
		{
			name:     "Example 1: Multiple fleets form",
			target:   12,
			position: []int{10, 8, 0, 5, 3},
			speed:    []int{2, 4, 1, 1, 3},
			expected: 3,
		},
		{
			name:     "Example 2: Single car",
			target:   10,
			position: []int{3},
			speed:    []int{3},
			expected: 1,
		},
		{
			name:     "Example 3: All cars merge into one fleet",
			target:   100,
			position: []int{0, 2, 4},
			speed:    []int{4, 2, 1},
			expected: 1,
		},
		{
			name:     "Two cars, no merge",
			target:   10,
			position: []int{0, 5},
			speed:    []int{1, 1},
			expected: 2,
		},
		{
			name:     "Two cars merge into one fleet",
			target:   10,
			position: []int{0, 5},
			speed:    []int{2, 1},
			expected: 1,
		},
		{
			name:     "Car already at target",
			target:   10,
			position: []int{9},
			speed:    []int{1},
			expected: 1,
		},
		{
			name:     "All cars at different positions, same speed",
			target:   10,
			position: []int{1, 3, 5, 7},
			speed:    []int{1, 1, 1, 1},
			expected: 4,
		},
		{
			name:     "Cars with varying speeds, closer car is faster",
			target:   10,
			position: []int{8, 6, 4},
			speed:    []int{1, 2, 3},
			expected: 1,
		},
		{
			name:     "Fast car catches slow car exactly at target",
			target:   12,
			position: []int{10, 8},
			speed:    []int{2, 4},
			expected: 1,
		},
		{
			name:     "Large target with close cars",
			target:   1000000,
			position: []int{999999, 999998},
			speed:    []int{1, 1},
			expected: 2,
		},
		{
			name:     "Three separate fleets",
			target:   10,
			position: []int{0, 3, 5, 8},
			speed:    []int{1, 1, 1, 1},
			expected: 4,
		},
		{
			name:     "Cars with high speeds",
			target:   100,
			position: []int{10, 20, 30},
			speed:    []int{1000000, 1000000, 1000000},
			expected: 3,
		},
		{
			name:     "Edge case: car at position 0",
			target:   10,
			position: []int{0},
			speed:    []int{5},
			expected: 1,
		},
		{
			name:     "Slower car ahead catches faster car behind",
			target:   10,
			position: []int{5, 2},
			speed:    []int{1, 5},
			expected: 1,
		},
		{
			name:     "Random order positions",
			target:   10,
			position: []int{6, 2, 8, 4},
			speed:    []int{2, 3, 1, 4},
			expected: 2,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := carFleet(tt.target, tt.position, tt.speed)
			if result != tt.expected {
				t.Errorf("carFleet(%d, %v, %v) = %d; expected %d",
					tt.target, tt.position, tt.speed, result, tt.expected)
			}
		})
	}
}
