// 242. Valid Anagram
// Topics: 'Hash Table', 'String', 'Sorting'

// Given two strings s and t, return true if t is an

// of s, and false otherwise.

// Example 1:

// Input: s = "anagram", t = "nagaram"

// Output: true

// Example 2:

// Input: s = "rat", t = "car"

// Output: false

// Constraints:

//     1 <= s.length, t.length <= 5 * 104
//     s and t consist of lowercase English letters.

package validanagram

func isAnagram(s string, t string) bool {
	m := map[rune]int{}
	for _, r := range s {
		found, ok := m[r]
		if ok {
			m[r] = found + 1
		} else {
			m[r] = 1
		}
	}
	for _, r := range t {
		found, ok := m[r]
		if !ok {
			return false
		}
		found = found - 1
		if found == 0 {
			delete(m, r)
		} else {
			m[r] = found
		}
	}

	return len(m) == 0
}
