// 621. Task scheduler
// Topics: 'Greedy', 'Hash Table', 'Array', 'Sorting', 'Heap (Priority Queue)', 'Counting'
// level: 'Medium'

// You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

// Return the minimum number of CPU intervals required to complete all tasks.

// Example 1:

// Input: tasks = ["A","A","A","B","B","B"], n = 2

// Output: 8

// Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

// After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

// Example 2:

// Input: tasks = ["A","C","A","B","D","B"], n = 1

// Output: 6

// Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

// With a cooling interval of 1, you can repeat a task after just one other task.

// Example 3:

// Input: tasks = ["A","A","A", "B","B","B"], n = 3

// Output: 10

// Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

// There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

// Constraints:

//     1 <= tasks.length <= 104
//     tasks[i] is an uppercase English letter.
//     0 <= n <= 100

package taskscheduler

import (
	"container/heap"
)

func leastInterval(ts []byte, n int) int {
	m := map[byte]int{}
	for _, t := range ts {
		m[t]++
	}
	var scheduler tasks
	for k, v := range m {
		heap.Push(&scheduler, sumTask{task: k, times: v})
	}

	var cycles int
	for {
		var (
			executed tasks
		)
		for scheduler.Len() > 0 && len(executed) < n+1 {
			task := heap.Pop(&scheduler).(sumTask)
			task.times--
			executed = append(executed, task)
		}
		if len(executed) == 0 {
			break
		}
		for _, e := range executed {
			if e.times > 0 {
				heap.Push(&scheduler, e)
			}
		}
		if scheduler.Len() > 0 {
			cycles += n + 1
		} else {
			cycles += len(executed)
		}
	}

	return cycles
}

type sumTask struct {
	task  byte
	times int
}

type tasks []sumTask

func (t tasks) Less(i, j int) bool {
	return t[i].times > t[j].times
}

func (t tasks) Swap(i, j int) {
	t[i], t[j] = t[j], t[i]
}

func (t tasks) Len() int {
	return len(t)
}

func (t *tasks) Push(task interface{}) {
	*t = append(*t, task.(sumTask))
}

func (t *tasks) Pop() interface{} {
	old := *t
	x := old[len(old)-1]
	*t = old[:len(old)-1]
	return x
}
