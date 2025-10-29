package simplifypath

import "testing"

func TestSimplifyPath(t *testing.T) {
	tests := []struct {
		name     string
		path     string
		expected string
	}{
		{
			name:     "trailing slash",
			path:     "/home/",
			expected: "/home",
		},
		{
			name:     "multiple slashes",
			path:     "/home//foo/",
			expected: "/home/foo",
		},
		{
			name:     "parent directory",
			path:     "/home/user/Documents/../Pictures",
			expected: "/home/user/Pictures",
		},
		{
			name:     "parent from root",
			path:     "/../",
			expected: "/",
		},
		{
			name:     "three dots directory",
			path:     "/.../a/../b/c/../d/./",
			expected: "/.../b/d",
		},
		{
			name:     "root directory",
			path:     "/",
			expected: "/",
		},
		{
			name:     "current directory",
			path:     "/./",
			expected: "/",
		},
		{
			name:     "multiple parent directories",
			path:     "/a/b/c/../../..",
			expected: "/",
		},
		{
			name:     "complex path",
			path:     "/a/./b/../../c/",
			expected: "/c",
		},
		{
			name:     "underscore in path",
			path:     "/..//_home/a/b/..///",
			expected: "/_home/a",
		},
		{
			name:     "all current directories",
			path:     "/./././.",
			expected: "/",
		},
		{
			name:     "valid multi-dot names",
			path:     "/home/.../files/..../",
			expected: "/home/.../files/....",
		},
		{
			name:     "mix of everything",
			path:     "//home/.//foo/../bar//./baz/",
			expected: "/home/bar/baz",
		},
		{
			name:     "parent at various levels",
			path:     "/a/b/../c/./d/../e",
			expected: "/a/c/e",
		},
		{
			name:     "multiple parents from root",
			path:     "/../../home",
			expected: "/home",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := simplifyPath(tt.path)
			if result != tt.expected {
				t.Errorf("simplifyPath(%q) = %q; expected %q", tt.path, result, tt.expected)
			}
		})
	}
}
