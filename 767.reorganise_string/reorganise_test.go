package reorganisestring

import "testing"

func TestReorganizeString(t *testing.T) {
	tests := []struct {
		name  string
		input string
		valid bool
	}{
		{
			name:  "custom",
			input: "aaabc",
			valid: true,
		},
		{
			name:  "example 1 - aab",
			input: "aab",
			valid: true,
		},
		{
			name:  "example 2 - aaab",
			input: "aaab",
			valid: false,
		},
		{
			name:  "single character",
			input: "a",
			valid: true,
		},
		{
			name:  "two same characters",
			input: "aa",
			valid: false,
		},
		{
			name:  "two different characters",
			input: "ab",
			valid: true,
		},
		{
			name:  "all different characters",
			input: "abcde",
			valid: true,
		},
		{
			name:  "valid rearrangement possible",
			input: "aaabbc",
			valid: true,
		},
		{
			name:  "longer valid string",
			input: "aabbcc",
			valid: true,
		},
		{
			name:  "edge case - barely possible",
			input: "aaab",
			valid: false,
		},
		{
			name:  "edge case - just possible",
			input: "aabb",
			valid: true,
		},
		{
			name:  "multiple different frequencies",
			input: "aaabbbbccd",
			valid: true,
		},
		{
			name:  "long string with valid distribution",
			input: "aaaaabbbbbccccc",
			valid: true,
		},
		{
			name:  "impossible case - one char dominates",
			input: "aaaaabbc",
			valid: false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := reorganizeString(tt.input)

			if tt.valid {
				if result == "" {
					t.Errorf("Expected valid rearrangement but got empty string")
					return
				}

				if len(result) != len(tt.input) {
					t.Errorf("Result length %d doesn't match input length %d", len(result), len(tt.input))
					return
				}

				charCount := make(map[byte]int)
				for i := range tt.input {
					charCount[tt.input[i]]++
				}
				for i := range result {
					charCount[result[i]]--
				}
				for char, count := range charCount {
					if count != 0 {
						t.Errorf("Character %c count mismatch: %d", char, count)
					}
				}

				for i := 0; i < len(result)-1; i++ {
					if result[i] == result[i+1] {
						t.Errorf("Found adjacent same characters at position %d: %c", i, result[i])
					}
				}
			} else {
				if result != "" {
					t.Errorf("Expected empty string but got: %s", result)
				}
			}
		})
	}
}

func TestReorganizeStringCharacterFrequency(t *testing.T) {
	input := "aabbcc"
	result := reorganizeString(input)

	if result == "" {
		t.Fatal("Expected non-empty result")
	}

	freq := make(map[byte]int)
	for i := range input {
		freq[input[i]]++
	}

	for i := range result {
		freq[result[i]]--
	}

	for char, count := range freq {
		if count != 0 {
			t.Errorf("Character frequency mismatch for %c: %d", char, count)
		}
	}
}

func TestReorganizeStringNoAdjacentDuplicates(t *testing.T) {
	testCases := []string{"aab", "aabbcc", "aaabbbbccccc"}

	for _, input := range testCases {
		result := reorganizeString(input)
		if result == "" {
			continue
		}

		for i := 0; i < len(result)-1; i++ {
			if result[i] == result[i+1] {
				t.Errorf("Input %s: Found adjacent duplicates in result %s at position %d", input, result, i)
			}
		}
	}
}
