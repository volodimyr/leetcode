package validpalindrome

import "testing"

func TestIsPalindrome(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected bool
	}{
		{
			name:     "example 1 - valid palindrome with punctuation",
			input:    "A man, a plan, a canal: Panama",
			expected: true,
		},
		{
			name:     "example 2 - not a palindrome",
			input:    "race a car",
			expected: false,
		},
		{
			name:     "example 3 - empty after removing non-alphanumeric",
			input:    " ",
			expected: true,
		},
		{
			name:     "single character",
			input:    "a",
			expected: true,
		},
		{
			name:     "single non-alphanumeric character",
			input:    ".",
			expected: true,
		},
		{
			name:     "two same characters",
			input:    "aa",
			expected: true,
		},
		{
			name:     "two different characters",
			input:    "ab",
			expected: false,
		},
		{
			name:     "palindrome with numbers",
			input:    "A1b2B1a",
			expected: true,
		},
		{
			name:     "not palindrome with numbers",
			input:    "A1b2B3a",
			expected: false,
		},
		{
			name:     "all uppercase palindrome",
			input:    "ABBA",
			expected: true,
		},
		{
			name:     "mixed case palindrome",
			input:    "AbBa",
			expected: true,
		},
		{
			name:     "palindrome with special characters",
			input:    "!@#$$#@!",
			expected: true,
		},
		{
			name:     "palindrome with spaces",
			input:    "a b a",
			expected: true,
		},
		{
			name:     "only numbers palindrome",
			input:    "12321",
			expected: true,
		},
		{
			name:     "only numbers not palindrome",
			input:    "12345",
			expected: false,
		},
		{
			name:     "complex palindrome",
			input:    "Madam, I'm Adam",
			expected: true,
		},
		{
			name:     "palindrome with many special chars",
			input:    ":::a:::b:::a:::",
			expected: true,
		},
		{
			name:     "not palindrome with many special chars",
			input:    ":::a:::b:::c:::",
			expected: false,
		},
		{
			name:     "empty string",
			input:    "",
			expected: true,
		},
		{
			name:     "only special characters",
			input:    ".,;!?",
			expected: true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := isPalindrome(tt.input)
			if result != tt.expected {
				t.Errorf("isPalindrome(%q) = %v; want %v", tt.input, result, tt.expected)
			}
		})
	}
}
