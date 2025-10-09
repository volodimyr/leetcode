package longestcommonprefix

import "testing"

func TestLongestCommonPrefix(t *testing.T) {
	tests := []struct {
		name string
		strs []string
		want string
	}{
		{
			name: "example 1 - common prefix fl",
			strs: []string{"flower", "flow", "flight"},
			want: "fl",
		},
		{
			name: "example 2 - no common prefix",
			strs: []string{"dog", "racecar", "car"},
			want: "",
		},
		{
			name: "single string",
			strs: []string{"alone"},
			want: "alone",
		},
		{
			name: "all strings identical",
			strs: []string{"test", "test", "test"},
			want: "test",
		},
		{
			name: "empty string in array",
			strs: []string{"flower", "", "flight"},
			want: "",
		},
		{
			name: "empty string at beginning",
			strs: []string{"", "flow", "flight"},
			want: "",
		},
		{
			name: "array with only empty strings",
			strs: []string{"", "", ""},
			want: "",
		},
		{
			name: "single empty string",
			strs: []string{""},
			want: "",
		},
		{
			name: "one character common prefix",
			strs: []string{"apple", "ape", "april"},
			want: "ap",
		},
		{
			name: "full string is prefix of others",
			strs: []string{"ab", "abc", "abcd"},
			want: "ab",
		},
		{
			name: "no common prefix at all",
			strs: []string{"abc", "def", "ghi"},
			want: "",
		},
		{
			name: "two strings with common prefix",
			strs: []string{"hello", "heaven"},
			want: "he",
		},
		{
			name: "two strings no common prefix",
			strs: []string{"abc", "xyz"},
			want: "",
		},
		{
			name: "common prefix is entire shortest string",
			strs: []string{"a", "a", "ab"},
			want: "a",
		},
		{
			name: "single character strings all same",
			strs: []string{"a", "a", "a"},
			want: "a",
		},
		{
			name: "single character strings all different",
			strs: []string{"a", "b", "c"},
			want: "",
		},
		{
			name: "long common prefix",
			strs: []string{"international", "internet", "internal"},
			want: "intern",
		},
		{
			name: "prefix stops at first difference",
			strs: []string{"prefix", "prefab", "preface"},
			want: "pref",
		},
		{
			name: "very similar strings",
			strs: []string{"aaaa", "aaab", "aaac"},
			want: "aaa",
		},
		{
			name: "mixed length strings short first",
			strs: []string{"a", "abc", "abcdef"},
			want: "a",
		},
		{
			name: "mixed length strings long first",
			strs: []string{"abcdef", "abc", "a"},
			want: "a",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := longestCommonPrefix(tt.strs)
			if got != tt.want {
				t.Errorf("longestCommonPrefix(%v) = %q, want %q", tt.strs, got, tt.want)
			}
		})
	}
}

// TestLongestCommonPrefixConstraints tests boundary conditions
func TestLongestCommonPrefixConstraints(t *testing.T) {
	tests := []struct {
		name string
		strs []string
		want string
	}{
		{
			name: "minimum array size (1 element)",
			strs: []string{"test"},
			want: "test",
		},
		{
			name: "maximum individual string length (200 chars) - all same",
			strs: []string{
				"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
				"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
			},
			want: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
		},
		{
			name: "long strings with short common prefix",
			strs: []string{
				"abcdefghijklmnopqrstuvwxyz",
				"abcdefghijklmnopqrstuvwxyzaaa",
				"abcdefghijklmnopqrstuvwxyzz",
			},
			want: "abcdefghijklmnopqrstuvwxyz",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := longestCommonPrefix(tt.strs)
			if got != tt.want {
				t.Errorf("longestCommonPrefix() = %q (len=%d), want %q (len=%d)",
					got, len(got), tt.want, len(tt.want))
			}
		})
	}
}

// TestLongestCommonPrefixSpecialCases tests special scenarios
func TestLongestCommonPrefixSpecialCases(t *testing.T) {
	tests := []struct {
		name string
		strs []string
		want string
	}{
		{
			name: "strings with only one character each - same",
			strs: []string{"z", "z", "z", "z"},
			want: "z",
		},
		{
			name: "strings with only one character each - different",
			strs: []string{"a", "b", "c", "d"},
			want: "",
		},
		{
			name: "progressively shorter strings",
			strs: []string{"abcdefg", "abcdef", "abcde", "abcd", "abc"},
			want: "abc",
		},
		{
			name: "progressively longer strings",
			strs: []string{"abc", "abcd", "abcde", "abcdef", "abcdefg"},
			want: "abc",
		},
		{
			name: "one string is prefix of all others",
			strs: []string{"pre", "prefix", "prepare", "preview"},
			want: "pre",
		},
		{
			name: "common prefix with repeating characters",
			strs: []string{"aaabbb", "aaaccc", "aaaddd"},
			want: "aaa",
		},
		{
			name: "strings differ at first character",
			strs: []string{"apple", "banana", "cherry"},
			want: "",
		},
		{
			name: "strings differ at last matched character",
			strs: []string{"testing", "tester", "tested"},
			want: "test",
		},
		{
			name: "all lowercase letters as required",
			strs: []string{"abcdefghijklmnopqrstuvwxyz", "abcdefghijklm"},
			want: "abcdefghijklm",
		},
		{
			name: "two element array - same strings",
			strs: []string{"hello", "hello"},
			want: "hello",
		},
		{
			name: "two element array - completely different",
			strs: []string{"start", "end"},
			want: "",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := longestCommonPrefix(tt.strs)
			if got != tt.want {
				t.Errorf("longestCommonPrefix(%v) = %q, want %q", tt.strs, got, tt.want)
			}
		})
	}
}

// TestLongestCommonPrefixMultipleStrings tests arrays with many strings
func TestLongestCommonPrefixMultipleStrings(t *testing.T) {
	tests := []struct {
		name string
		strs []string
		want string
	}{
		{
			name: "many strings with common prefix",
			strs: []string{"prefix1", "prefix2", "prefix3", "prefix4", "prefix5"},
			want: "prefix",
		},
		{
			name: "many strings without common prefix",
			strs: []string{"apple", "banana", "cherry", "date", "elderberry"},
			want: "",
		},
		{
			name: "many strings all identical",
			strs: []string{"same", "same", "same", "same", "same", "same"},
			want: "same",
		},
		{
			name: "many strings with single char prefix",
			strs: []string{"apple", "apricot", "avocado", "almond", "artichoke"},
			want: "a",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := longestCommonPrefix(tt.strs)
			if got != tt.want {
				t.Errorf("longestCommonPrefix(%v) = %q, want %q", tt.strs, got, tt.want)
			}
		})
	}
}
