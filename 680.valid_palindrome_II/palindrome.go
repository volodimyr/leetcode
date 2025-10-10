// 680. Valid Palindrome II
// Topics: 'String', 'Two Pointers', 'Greedy'
// Given a string s, return true if the s can be palindrome after deleting at most one character from it.

// Example 1:

// Input: s = "aba"
// Output: true

// Example 2:

// Input: s = "abca"
// Output: true
// Explanation: You could delete the character 'c'.

// Example 3:

// Input: s = "abc"
// Output: false

// Constraints:

//     1 <= s.length <= 105
//     s consists of lowercase English letters.

package validpalindromeii

func validPalindrome(s string) bool {
	return valid(s, false)
}

func valid(str string, skipped bool) bool {
	s, e := 0, len(str)-1
	for s < e {
		if str[s] != str[e] {
			if skipped {
				return false
			}
			return valid(str[s+1:e+1], true) || valid(str[s:e], true)
		}
		s++
		e--
	}

	return true
}
