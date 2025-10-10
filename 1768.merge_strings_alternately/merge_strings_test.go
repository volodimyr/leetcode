package mergestringsalternately

import "testing"

func TestMergeAlternately(t *testing.T) {
	tests := []struct {
		name  string
		word1 string
		word2 string
		want  string
	}{
		{
			name:  "equal length strings",
			word1: "abc",
			word2: "pqr",
			want:  "apbqcr",
		},
		{
			name:  "word2 longer than word1",
			word1: "ab",
			word2: "pqrs",
			want:  "apbqrs",
		},
		{
			name:  "word1 longer than word2",
			word1: "abcd",
			word2: "pq",
			want:  "apbqcd",
		},
		{
			name:  "word1 is empty",
			word1: "",
			word2: "pqr",
			want:  "pqr",
		},
		{
			name:  "word2 is empty",
			word1: "abc",
			word2: "",
			want:  "abc",
		},
		{
			name:  "both strings empty",
			word1: "",
			word2: "",
			want:  "",
		},
		{
			name:  "single character each",
			word1: "a",
			word2: "b",
			want:  "ab",
		},
		{
			name:  "word1 much longer",
			word1: "abcdefgh",
			word2: "xy",
			want:  "axbycdefgh",
		},
		{
			name:  "word2 much longer",
			word1: "xy",
			word2: "abcdefgh",
			want:  "xaybcdefgh",
		},
		{
			name:  "single char word1, empty word2",
			word1: "z",
			word2: "",
			want:  "z",
		},
		{
			name:  "empty word1, single char word2",
			word1: "",
			word2: "z",
			want:  "z",
		},
		{
			name:  "longer strings with different lengths",
			word1: "abcdefghijklmno",
			word2: "pqrstuvwxyz",
			want:  "apbqcrdsetfugvhwixjykzlmno",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := mergeAlternately(tt.word1, tt.word2)
			if got != tt.want {
				t.Errorf("mergeAlternately(%q, %q) = %q, want %q", tt.word1, tt.word2, got, tt.want)
			}
		})
	}
}

func TestMergeAlternatelyEdgeCases(t *testing.T) {
	t.Run("alternation pattern verification", func(t *testing.T) {
		word1 := "aaa"
		word2 := "bbb"
		want := "ababab"
		got := mergeAlternately(word1, word2)
		if got != want {
			t.Errorf("mergeAlternately(%q, %q) = %q, want %q", word1, word2, got, want)
		}
	})

	t.Run("verify starting with word1", func(t *testing.T) {
		word1 := "x"
		word2 := "y"
		want := "xy"
		got := mergeAlternately(word1, word2)
		if got != want {
			t.Errorf("mergeAlternately(%q, %q) = %q, want %q - should start with word1", word1, word2, got, want)
		}
	})

	t.Run("remaining characters appended correctly", func(t *testing.T) {
		word1 := "a"
		word2 := "bcde"
		want := "abcde"
		got := mergeAlternately(word1, word2)
		if got != want {
			t.Errorf("mergeAlternately(%q, %q) = %q, want %q", word1, word2, got, want)
		}
	})
}

func TestMergeAlternatelyLength(t *testing.T) {
	tests := []struct {
		name  string
		word1 string
		word2 string
	}{
		{"equal lengths", "abc", "def"},
		{"word1 longer", "abcde", "xy"},
		{"word2 longer", "xy", "abcde"},
		{"empty word1", "", "abc"},
		{"empty word2", "abc", ""},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := mergeAlternately(tt.word1, tt.word2)
			expectedLen := len(tt.word1) + len(tt.word2)
			if len(got) != expectedLen {
				t.Errorf("mergeAlternately(%q, %q) length = %d, want %d", tt.word1, tt.word2, len(got), expectedLen)
			}
		})
	}
}
