package reverse

import (
	"reflect"
	"testing"
)

func TestReverseString(t *testing.T) {
	tests := []struct {
		name     string
		input    []byte
		expected []byte
	}{
		{
			name:     "example 1: hello",
			input:    []byte{'h', 'e', 'l', 'l', 'o'},
			expected: []byte{'o', 'l', 'l', 'e', 'h'},
		},
		{
			name:     "example 2: Hannah",
			input:    []byte{'H', 'a', 'n', 'n', 'a', 'h'},
			expected: []byte{'h', 'a', 'n', 'n', 'a', 'H'},
		},
		{
			name:     "single character",
			input:    []byte{'a'},
			expected: []byte{'a'},
		},
		{
			name:     "two characters",
			input:    []byte{'a', 'b'},
			expected: []byte{'b', 'a'},
		},
		{
			name:     "empty string",
			input:    []byte{},
			expected: []byte{},
		},
		{
			name:     "palindrome",
			input:    []byte{'r', 'a', 'c', 'e', 'c', 'a', 'r'},
			expected: []byte{'r', 'a', 'c', 'e', 'c', 'a', 'r'},
		},
		{
			name:     "even length string",
			input:    []byte{'a', 'b', 'c', 'd'},
			expected: []byte{'d', 'c', 'b', 'a'},
		},
		{
			name:     "odd length string",
			input:    []byte{'a', 'b', 'c', 'd', 'e'},
			expected: []byte{'e', 'd', 'c', 'b', 'a'},
		},
		{
			name:     "string with spaces",
			input:    []byte{'h', 'i', ' ', 't', 'h', 'e', 'r', 'e'},
			expected: []byte{'e', 'r', 'e', 'h', 't', ' ', 'i', 'h'},
		},
		{
			name:     "string with numbers",
			input:    []byte{'1', '2', '3', '4', '5'},
			expected: []byte{'5', '4', '3', '2', '1'},
		},
		{
			name:     "string with special characters",
			input:    []byte{'!', '@', '#', '$', '%'},
			expected: []byte{'%', '$', '#', '@', '!'},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			// Make a copy for comparison since function modifies in-place
			input := make([]byte, len(tt.input))
			copy(input, tt.input)

			reverseString(input)

			if !reflect.DeepEqual(input, tt.expected) {
				t.Errorf("reverseString() = %v, want %v", input, tt.expected)
			}
		})
	}
}
