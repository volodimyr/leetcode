// 42. Trapping Rain Water
// Topics: 'Array', 'Two Pointers', 'Dynamic Programming', 'Stack', 'Monotonic Stack'
// Level: 'Hard'

// Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

// Example 1:

// Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
// Output: 6
// Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

// Example 2:

// Input: height = [4,2,0,3,2,5]
// Output: 9

// Constraints:

//     n == height.length
//     1 <= n <= 2 * 104
//     0 <= height[i] <= 105

package trappingrainwater

func trap(height []int) int {
	if len(height) < 2 {
		return 0
	}
	R := len(height) - 1
	L := 0
	var sum int

	maxr, maxl := R-1, L+1
	for L < R {
		if height[L] < height[R] {
			var ocuppied int
			for height[maxl] < height[L] && maxl != R {
				ocuppied += height[maxl]
				maxl++
			}
			sum += min(height[L], height[maxl]) * (maxl - L - 1)
			sum -= ocuppied
			L = maxl
			maxl++
		} else {
			var occupied int
			for height[maxr] < height[R] && maxr != L {
				occupied += height[maxr]
				maxr--
			}
			sum += min(height[R], height[maxr]) * (R - maxr - 1)
			sum -= occupied
			R = maxr
			maxr--
		}
	}
	return sum
}
