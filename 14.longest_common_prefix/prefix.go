// 14. Longest common prefix
// Topics: 'Array', 'String', 'Trie'

// Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".

// Example 1:

// Input: strs = ["flower","flow","flight"]
// Output: "fl"

// Example 2:

// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.

// Constraints:

//     1 <= strs.length <= 200
//     0 <= strs[i].length <= 200
//     strs[i] consists of only lowercase English letters if it is non-empty.

package longestcommonprefix

func longestCommonPrefix(strs []string) string {
	if len(strs) == 1 {
		return strs[0]
	}
	prefix := len(strs[0])
	for _, str := range strs[1:] {
		var tempPref int
		for i, s := range strs[0][:prefix] {
			if i >= len(str) {
				break
			}
			if byte(s) == str[i] {
				tempPref++
			} else {
				break
			}
		}
		if tempPref == 0 {
			return ""
		}
		if prefix > tempPref {
			prefix = tempPref
		}
	}

	return strs[0][:prefix]
}
