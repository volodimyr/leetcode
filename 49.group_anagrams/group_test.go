package groupanagrams

import (
	"reflect"
	"sort"
	"testing"
)

func TestGroupAnagrams(t *testing.T) {
	tests := []struct {
		name string
		strs []string
		want [][]string
	}{
		{
			name: "example 1 - multiple anagram groups",
			strs: []string{"eat", "tea", "tan", "ate", "nat", "bat"},
			want: [][]string{{"bat"}, {"nat", "tan"}, {"ate", "eat", "tea"}},
		},
		{
			name: "example 2 - empty string",
			strs: []string{""},
			want: [][]string{{""}},
		},
		{
			name: "example 3 - single character",
			strs: []string{"a"},
			want: [][]string{{"a"}},
		},
		{
			name: "all same anagrams",
			strs: []string{"abc", "bca", "cab"},
			want: [][]string{{"abc", "bca", "cab"}},
		},
		{
			name: "no anagrams",
			strs: []string{"a", "b", "c"},
			want: [][]string{{"a"}, {"b"}, {"c"}},
		},
		{
			name: "mix of lengths",
			strs: []string{"a", "aa", "aaa"},
			want: [][]string{{"a"}, {"aa"}, {"aaa"}},
		},
		{
			name: "longer words",
			strs: []string{"listen", "silent", "enlist", "hello", "world"},
			want: [][]string{{"listen", "silent", "enlist"}, {"hello"}, {"world"}},
		},
		{
			name: "duplicate strings",
			strs: []string{"abc", "abc", "def"},
			want: [][]string{{"abc", "abc"}, {"def"}},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := groupAnagrams(tt.strs)

			// Sort for comparison since order doesn't matter
			sortGroups(got)
			sortGroups(tt.want)

			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("groupAnagrams() = %v, want %v", got, tt.want)
			}
		})
	}
}

// Helper to sort groups for comparison
func sortGroups(groups [][]string) {
	for _, group := range groups {
		sort.Strings(group)
	}
	sort.Slice(groups, func(i, j int) bool {
		if len(groups[i]) != len(groups[j]) {
			return len(groups[i]) < len(groups[j])
		}
		return groups[i][0] < groups[j][0]
	})
}
