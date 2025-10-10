package validpalindromeii

import "testing"

func TestValidPalindromeBasicCases(t *testing.T) {
	tests := []struct {
		name   string
		s      string
		expect bool
	}{
		{
			name:   "example 1 - already palindrome",
			s:      "aba",
			expect: true,
		},
		{
			name:   "example 2 - delete one char",
			s:      "abca",
			expect: true,
		},
		{
			name:   "example 3 - cannot form palindrome",
			s:      "abc",
			expect: false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := validPalindrome(tt.s)
			if result != tt.expect {
				t.Errorf("validPalindrome(%q) = %v, want %v", tt.s, result, tt.expect)
			}
		})
	}
}

func TestValidPalindromeSingleCharacter(t *testing.T) {
	tests := []struct {
		name   string
		s      string
		expect bool
	}{
		{
			name:   "single character",
			s:      "a",
			expect: true,
		},
		{
			name:   "two same characters",
			s:      "aa",
			expect: true,
		},
		{
			name:   "two different characters",
			s:      "ab",
			expect: true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := validPalindrome(tt.s)
			if result != tt.expect {
				t.Errorf("validPalindrome(%q) = %v, want %v", tt.s, result, tt.expect)
			}
		})
	}
}

func TestValidPalindromeAlreadyPalindrome(t *testing.T) {
	tests := []struct {
		name   string
		s      string
		expect bool
	}{
		{
			name:   "short palindrome",
			s:      "racecar",
			expect: true,
		},
		{
			name:   "even length palindrome",
			s:      "abba",
			expect: true,
		},
		{
			name:   "odd length palindrome",
			s:      "abcba",
			expect: true,
		},
		{
			name:   "all same characters",
			s:      "aaaa",
			expect: true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := validPalindrome(tt.s)
			if result != tt.expect {
				t.Errorf("validPalindrome(%q) = %v, want %v", tt.s, result, tt.expect)
			}
		})
	}
}

func TestValidPalindromeDeleteOneChar(t *testing.T) {
	tests := []struct {
		name   string
		s      string
		expect bool
	}{
		{
			name:   "delete from beginning",
			s:      "xaba",
			expect: true,
		},
		{
			name:   "delete from end",
			s:      "abax",
			expect: true,
		},
		{
			name:   "delete duplicate",
			s:      "aabaa",
			expect: true,
		},
		{
			name:   "delete to form even palindrome",
			s:      "abcba",
			expect: true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := validPalindrome(tt.s)
			if result != tt.expect {
				t.Errorf("validPalindrome(%q) = %v, want %v", tt.s, result, tt.expect)
			}
		})
	}
}

func TestValidPalindromeCannotFormPalindrome(t *testing.T) {
	tests := []struct {
		name   string
		s      string
		expect bool
	}{
		{
			name:   "need to delete two chars",
			s:      "abcd",
			expect: false,
		},
		{
			name:   "completely reversed",
			s:      "abcdef",
			expect: false,
		},
		{
			name:   "alternating pattern",
			s:      "ababab",
			expect: true,
		},
		{
			name:   "close but not valid",
			s:      "abcde",
			expect: false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := validPalindrome(tt.s)
			if result != tt.expect {
				t.Errorf("validPalindrome(%q) = %v, want %v", tt.s, result, tt.expect)
			}
		})
	}
}

func TestValidPalindromeLongStrings(t *testing.T) {
	tests := []struct {
		name   string
		s      string
		expect bool
	}{
		{
			name:   "long palindrome with one extra",
			s:      "raceacar",
			expect: true,
		},
		{
			name:   "long valid case",
			s:      "abcdefgfedcba",
			expect: true,
		},
		{
			name:   "many repeated characters",
			s:      "aaaaabaaaa",
			expect: true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := validPalindrome(tt.s)
			if result != tt.expect {
				t.Errorf("validPalindrome(%q) = %v, want %v", tt.s, result, tt.expect)
			}
		})
	}
}

func TestValidPalindromeEdgeCases(t *testing.T) {
	tests := []struct {
		name   string
		s      string
		expect bool
	}{
		{
			name:   "three chars - delete middle",
			s:      "axa",
			expect: true,
		},
		{
			name:   "three chars - no palindrome",
			s:      "xyz",
			expect: false,
		},
		{
			name:   "four chars palindrome",
			s:      "abba",
			expect: true,
		},
		{
			name:   "four chars with one extra",
			s:      "abbxa",
			expect: true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := validPalindrome(tt.s)
			if result != tt.expect {
				t.Errorf("validPalindrome(%q) = %v, want %v", tt.s, result, tt.expect)
			}
		})
	}
}

func TestValidPalindromeSpecialPatterns(t *testing.T) {
	tests := []struct {
		name   string
		s      string
		expect bool
	}{
		{
			name:   "mirror with extra in middle",
			s:      "abxba",
			expect: true,
		},
		{
			name:   "almost symmetric",
			s:      "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga",
			expect: true,
		},
		{
			name:   "delete last for palindrome",
			s:      "deeee",
			expect: true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := validPalindrome(tt.s)
			if result != tt.expect {
				t.Errorf("validPalindrome(%q) = %v, want %v", tt.s, result, tt.expect)
			}
		})
	}
}
