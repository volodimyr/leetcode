// 49. Group Anagrams
// Topics: 'Array', 'Hash Table', 'String', 'Sorting'
// Level: 'Medium'

// Given an array of strings strs, group the

// together. You can return the answer in any order.

// Example 1:

// Input: strs = ["eat","tea","tan","ate","nat","bat"]

// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

// Explanation:

//     There is no string in strs that can be rearranged to form "bat".
//     The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
//     The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

// Example 2:

// Input: strs = [""]

// Output: [[""]]

// Example 3:

// Input: strs = ["a"]

// Output: [["a"]]

// Constraints:

//     1 <= strs.length <= 104
//     0 <= strs[i].length <= 100
//     strs[i] consists of lowercase English letters.

package groupanagrams

func groupAnagrams(strs []string) [][]string {
	m := map[[26]int][]string{}
	for _, str := range strs {
		arr := [26]int{}
		for _, s := range str {
			arr[s-'a'] += 1
		}
		m[arr] = append(m[arr], str)
	}
	res := make([][]string, len(m))
	var index int
	for _, arr := range m {
		res[index] = arr
		index++
	}
	return res
}
