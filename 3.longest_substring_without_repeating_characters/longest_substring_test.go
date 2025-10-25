package longestsubstringwithoutrepeatingcharacters

import "testing"

func TestLengthOfLongestSubstring_BasicCases(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected int
	}{
		{
			name:     "example 1 - multiple unique substrings",
			input:    "abcabcbb",
			expected: 3,
		},
		{
			name:     "example 2 - all same characters",
			input:    "bbbbb",
			expected: 1,
		},
		{
			name:     "example 3 - mixed pattern",
			input:    "pwwkew",
			expected: 3,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := lengthOfLongestSubstring(tt.input)
			if result != tt.expected {
				t.Errorf("lengthOfLongestSubstring(%q) = %d, want %d", tt.input, result, tt.expected)
			}
		})
	}
}

func TestLengthOfLongestSubstring_EdgeCases(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected int
	}{
		{
			name:     "empty string",
			input:    "",
			expected: 0,
		},
		{
			name:     "single character",
			input:    "a",
			expected: 1,
		},
		{
			name:     "two same characters",
			input:    "aa",
			expected: 1,
		},
		{
			name:     "two different characters",
			input:    "ab",
			expected: 2,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := lengthOfLongestSubstring(tt.input)
			if result != tt.expected {
				t.Errorf("lengthOfLongestSubstring(%q) = %d, want %d", tt.input, result, tt.expected)
			}
		})
	}
}

func TestLengthOfLongestSubstring_AllUniqueCharacters(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected int
	}{
		{
			name:     "all unique lowercase",
			input:    "abcdefg",
			expected: 7,
		},
		{
			name:     "all unique mixed case",
			input:    "abcABC",
			expected: 6,
		},
		{
			name:     "all unique with numbers",
			input:    "abc123",
			expected: 6,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := lengthOfLongestSubstring(tt.input)
			if result != tt.expected {
				t.Errorf("lengthOfLongestSubstring(%q) = %d, want %d", tt.input, result, tt.expected)
			}
		})
	}
}

func TestLengthOfLongestSubstring_RepeatingPatterns(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected int
	}{
		{
			name:     "alternating pattern",
			input:    "abba",
			expected: 2,
		},
		{
			name:     "pattern at end",
			input:    "abcda",
			expected: 4,
		},
		{
			name:     "pattern at beginning",
			input:    "aabcdef",
			expected: 6,
		},
		{
			name:     "complex repeating",
			input:    "tmmzuxt",
			expected: 5,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := lengthOfLongestSubstring(tt.input)
			if result != tt.expected {
				t.Errorf("lengthOfLongestSubstring(%q) = %d, want %d", tt.input, result, tt.expected)
			}
		})
	}
}

func TestLengthOfLongestSubstring_SpecialCharacters(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected int
	}{
		{
			name:     "with spaces",
			input:    "a b c a",
			expected: 3,
		},
		{
			name:     "with symbols",
			input:    "!@#$%!",
			expected: 5,
		},
		{
			name:     "mixed symbols and letters",
			input:    "a!b@c#a",
			expected: 6,
		},
		{
			name:     "digits only",
			input:    "0123401",
			expected: 5,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := lengthOfLongestSubstring(tt.input)
			if result != tt.expected {
				t.Errorf("lengthOfLongestSubstring(%q) = %d, want %d", tt.input, result, tt.expected)
			}
		})
	}
}

func TestLengthOfLongestSubstring_LongStrings(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected int
	}{
		{
			name:     "long repeating",
			input:    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
			expected: 1,
		},
		{
			name:     "long unique then repeat",
			input:    "abcdefghijklmnopqrstuvwxyza",
			expected: 26,
		},
		{
			name:     "alphabet repeated",
			input:    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",
			expected: 26,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := lengthOfLongestSubstring(tt.input)
			if result != tt.expected {
				t.Errorf("lengthOfLongestSubstring(%q) = %d, want %d", tt.input, result, tt.expected)
			}
		})
	}
}

func TestLengthOfLongestSubstring_WindowShifting(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected int
	}{
		{
			name:     "window shifts forward",
			input:    "abcdefabc",
			expected: 6,
		},
		{
			name:     "multiple window shifts",
			input:    "abcabcbb",
			expected: 3,
		},
		{
			name:     "immediate repeat",
			input:    "aab",
			expected: 2,
		},
		{
			name:     "dvdf case",
			input:    "dvdf",
			expected: 3,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := lengthOfLongestSubstring(tt.input)
			if result != tt.expected {
				t.Errorf("lengthOfLongestSubstring(%q) = %d, want %d", tt.input, result, tt.expected)
			}
		})
	}
}
