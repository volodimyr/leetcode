// 84. Largest Rectangle in Histogram
// Topics: 'Array', 'Stack', 'Monotonic Stack'
// Level: 'Hard'

// Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

// Example 1:

// Input: heights = [2,1,5,6,2,3]
// Output: 10
// Explanation: The above is a histogram where width of each bar is 1.
// The largest rectangle is shown in the red area, which has an area = 10 units.

// Example 2:

// Input: heights = [2,4]
// Output: 4

// Constraints:

//     1 <= heights.length <= 105
//     0 <= heights[i] <= 104

package largestrectangleinhistogram

// O(n*n)
func largestRectangleArea(heights []int) int {
	if len(heights) == 0 {
		return 0
	}
	maxarea := heights[0]
	for i, h := range heights[:len(heights)-1] {
		base := h
		for j := i + 1; j < len(heights); j++ {
			if heights[j] < base {
				base = heights[j]
			}
			maxarea = max(maxarea, (j-i+1)*base, heights[j])
		}
	}

	return maxarea
}
