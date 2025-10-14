package asteroidcollision

import (
	"reflect"
	"testing"
)

func TestAsteroidCollision(t *testing.T) {
	tests := []struct {
		name      string
		asteroids []int
		expected  []int
	}{
		{
			name:      "negative all after single collision",
			asteroids: []int{-2, -2, 1, -2},
			expected:  []int{-2, -2, -2},
		},
		{
			name:      "example 1: right moving asteroids with one left",
			asteroids: []int{5, 10, -5},
			expected:  []int{5, 10},
		},
		{
			name:      "example 2: equal size collision",
			asteroids: []int{8, -8},
			expected:  []int{},
		},
		{
			name:      "example 3: chain collisions",
			asteroids: []int{10, 2, -5},
			expected:  []int{10},
		},
		{
			name:      "all moving right",
			asteroids: []int{5, 10, 15},
			expected:  []int{5, 10, 15},
		},
		{
			name:      "all moving left",
			asteroids: []int{-5, -10, -15},
			expected:  []int{-5, -10, -15},
		},
		{
			name:      "left then right - no collision",
			asteroids: []int{-5, -10, 15, 20},
			expected:  []int{-5, -10, 15, 20},
		},
		{
			name:      "multiple collisions with survivor going left",
			asteroids: []int{5, 10, -15},
			expected:  []int{-15},
		},
		{
			name:      "left asteroid destroys multiple right asteroids",
			asteroids: []int{1, 2, 3, -10},
			expected:  []int{-10},
		},
		{
			name:      "complex scenario with multiple collisions",
			asteroids: []int{-2, -1, 1, 2},
			expected:  []int{-2, -1, 1, 2},
		},
		{
			name:      "single asteroid moving right",
			asteroids: []int{10},
			expected:  []int{10},
		},
		{
			name:      "single asteroid moving left",
			asteroids: []int{-10},
			expected:  []int{-10},
		},
		{
			name:      "two asteroids same direction",
			asteroids: []int{5, 10},
			expected:  []int{5, 10},
		},
		{
			name:      "larger left asteroid wins",
			asteroids: []int{10, -15},
			expected:  []int{-15},
		},
		{
			name:      "larger right asteroid wins",
			asteroids: []int{15, -10},
			expected:  []int{15},
		},
		{
			name:      "multiple equal collisions",
			asteroids: []int{5, -5, 10, -10},
			expected:  []int{},
		},
		{
			name:      "cascade destruction",
			asteroids: []int{1, 1, 1, -3},
			expected:  []int{-3},
		},
		{
			name:      "left asteroids followed by larger right",
			asteroids: []int{-5, -10, 20},
			expected:  []int{-5, -10, 20},
		},
		{
			name:      "alternating pattern",
			asteroids: []int{10, -5, 10, -5},
			expected:  []int{10, 10},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := asteroidCollision(tt.asteroids)
			if !reflect.DeepEqual(result, tt.expected) {
				t.Errorf("asteroidCollision(%v) = %v, want %v", tt.asteroids, result, tt.expected)
			}
		})
	}
}
