// 3. Longest substring without repeating characters
// Topics: 'Hash Table', 'String', 'Sliding window'
// Level: 'Medium'

// Given a string s, find the length of the longest

// without duplicate characters.

// Example 1:

// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

// Example 2:

// Input: s = "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.

// Example 3:

// Input: s = "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.
// Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

// Constraints:

//     0 <= s.length <= 5 * 104
//     s consists of English letters, digits, symbols and spaces.

package longestsubstringwithoutrepeatingcharacters

func lengthOfLongestSubstring(s string) int {
	m := map[byte]int{}
	var _max int
	var start int
	for i := 0; i < len(s); i++ {
		j, ok := m[s[i]]
		if ok {
			for start <= j {
				delete(m, s[start])
				start++
			}
		}
		m[s[i]] = i

		_max = max(_max, len(m))
	}
	return _max
}
