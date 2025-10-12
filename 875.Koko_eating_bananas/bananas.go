// 875. Koko eating bananas
// Topics: 'Array', 'Binary Search'
// Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

// Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

// Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

// Return the minimum integer k such that she can eat all the bananas within h hours.

// Example 1:

// Input: piles = [3,6,7,11], h = 8
// Output: 4

// Example 2:

// Input: piles = [30,11,23,4,20], h = 5
// Output: 30

// Example 3:

// Input: piles = [30,11,23,4,20], h = 6
// Output: 23

// Constraints:

//     1 <= piles.length <= 104
//     piles.length <= h <= 109
//     1 <= piles[i] <= 109

package kokoeatingbananas

import (
	"math"
)

func minEatingSpeed(piles []int, h int) int {
	var R int
	for _, pile := range piles {
		if pile >= R {
			//max
			R = pile
		}
	}
	if len(piles) == h {
		return R
	}

	L := 1
	var k int

	for L <= R {
		var total int
		speed := (L + R) / 2

		for _, pile := range piles {
			total += int(math.Ceil(float64(pile) / float64(speed)))
		}
		if total <= h {
			k = speed
			R = speed - 1
		} else {
			L = speed + 1
		}
	}
	return k
}
