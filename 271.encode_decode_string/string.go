// 271. Encode and decode string
// Topics: 'Arrays', 'Hash Table'
// Level: 'Medium'

// Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

// Please implement encode and decode

// Example 1:

// Input: ["neet","code","love","you"]

// Output:["neet","code","love","you"]

// Example 2:

// Input: ["we","say",":","yes"]

// Output: ["we","say",":","yes"]

// Constraints:

//     0 <= strs.length < 100
//     0 <= strs[i].length < 200
//     strs[i] contains only UTF-8 characters.

package encodedecodestring

import (
	"strings"
)

type Solution struct {
	whitespaces []int
}

func (s *Solution) Encode(strs []string) string {
	builder := strings.Builder{}
	s.whitespaces = []int{}
	for _, str := range strs {
		s.whitespaces = append(s.whitespaces, len(str))
		builder.WriteString(str)
	}
	return builder.String()
}

func (s *Solution) Decode(str string) []string {
	var curr int
	var arr []string
	for _, ws := range s.whitespaces {
		end := ws + curr
		builder := strings.Builder{}
		for ; curr < end; curr++ {
			builder.WriteByte(str[curr])
		}
		arr = append(arr, builder.String())
	}
	return arr
}

//func Encode(strs []string) string {
// 	var builder strings.Builder
// 	for _, str := range strs {
// 		builder.WriteString(strconv.Itoa(len(str)))
// 		builder.WriteByte('#') // delimiter
// 		builder.WriteString(str)
// 	}
// 	return builder.String()
// }

// func Decode(s string) []string {
// 	var res []string
// 	for i := 0; i < len(s); {
// 		// find delimiter
// 		j := i
// 		for s[j] != '#' {
// 			j++
// 		}
// 		length, _ := strconv.Atoi(s[i:j])
// 		start := j + 1
// 		end := start + length
// 		res = append(res, s[start:end])
// 		i = end
// 	}
// 	return res
// }
