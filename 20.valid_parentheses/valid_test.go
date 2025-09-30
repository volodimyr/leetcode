package validparentheses

import "testing"

func TestIsValid(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected bool
	}{
		{
			name:     "Example 1: simple parentheses",
			input:    "()",
			expected: true,
		},
		{
			name:     "Example 2: all bracket types",
			input:    "()[]{}",
			expected: true,
		},
		{
			name:     "Example 3: mismatched brackets",
			input:    "(]",
			expected: false,
		},
		{
			name:     "Example 4: nested brackets",
			input:    "([])",
			expected: true,
		},
		{
			name:     "Example 5: wrong order",
			input:    "([)]",
			expected: false,
		},
		{
			name:     "single open bracket",
			input:    "(",
			expected: false,
		},
		{
			name:     "single close bracket",
			input:    ")",
			expected: false,
		},
		{
			name:     "empty string",
			input:    "",
			expected: true,
		},
		{
			name:     "only open brackets",
			input:    "(((",
			expected: false,
		},
		{
			name:     "only close brackets",
			input:    ")))",
			expected: false,
		},
		{
			name:     "nested parentheses",
			input:    "((()))",
			expected: true,
		},
		{
			name:     "nested mixed brackets",
			input:    "{[()]}",
			expected: true,
		},
		{
			name:     "mismatched nested",
			input:    "{[}",
			expected: false,
		},
		{
			name:     "extra closing bracket",
			input:    "())",
			expected: false,
		},
		{
			name:     "extra opening bracket",
			input:    "(()",
			expected: false,
		},
		{
			name:     "all bracket types sequential",
			input:    "(){}[]",
			expected: true,
		},
		{
			name:     "complex valid nesting",
			input:    "{[()(){}]}",
			expected: true,
		},
		{
			name:     "wrong order closing",
			input:    "[(])",
			expected: false,
		},
		{
			name:     "square brackets",
			input:    "[]",
			expected: true,
		},
		{
			name:     "curly braces",
			input:    "{}",
			expected: true,
		},
		{
			name:     "mismatch paren to square",
			input:    "(]",
			expected: false,
		},
		{
			name:     "mismatch square to curly",
			input:    "[}",
			expected: false,
		},
		{
			name:     "mismatch curly to paren",
			input:    "{)",
			expected: false,
		},
		{
			name:     "long valid string",
			input:    "()[]{}()[]{}()[]{}",
			expected: true,
		},
		{
			name:     "closing before opening",
			input:    ")(",
			expected: false,
		},
		{
			name:     "deeply nested valid",
			input:    "((((((()))))))",
			expected: true,
		},
		{
			name:     "deeply nested invalid",
			input:    "((((((())))",
			expected: false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := isValid(tt.input)
			if result != tt.expected {
				t.Errorf("isValid(%q) = %v, expected %v", tt.input, result, tt.expected)
			}
		})
	}
}
