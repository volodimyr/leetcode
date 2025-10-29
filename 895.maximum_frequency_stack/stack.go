// 895. Maximum Frequency Stack
// Topics: 'Array', 'Stack'
// Level: 'Hard'

// Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

// Implement the FreqStack class:

//     FreqStack() constructs an empty frequency stack.
//     void push(int val) pushes an integer val onto the top of the stack.
//     int pop() removes and returns the most frequent element in the stack.
//         If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

// Example 1:

// Input
// ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
// [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
// Output
// [null, null, null, null, null, null, null, 5, 7, 5, 4]

// Explanation
// FreqStack freqStack = new FreqStack();
// freqStack.push(5); // The stack is [5]
// freqStack.push(7); // The stack is [5,7]
// freqStack.push(5); // The stack is [5,7,5]
// freqStack.push(7); // The stack is [5,7,5,7]
// freqStack.push(4); // The stack is [5,7,5,7,4]
// freqStack.push(5); // The stack is [5,7,5,7,4,5]
// freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
// freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
// freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
// freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].

// Constraints:

//     0 <= val <= 109
//     At most 2 * 104 calls will be made to push and pop.
//     It is guaranteed that there will be at least one element in the stack before calling pop.

package maximumfrequencystack

type FreqStack struct {
	max    int
	stacks map[int][]int
	freq   map[int]int
}

func Constructor() FreqStack {
	return FreqStack{
		max:    1,
		freq:   map[int]int{},
		stacks: map[int][]int{},
	}
}

func (f *FreqStack) Push(val int) {
	fq, ok := f.freq[val]
	if !ok {
		fq = 1
	} else {
		fq++
	}
	f.freq[val] = fq
	stack, ok := f.stacks[fq]
	if !ok {
		stack = []int{val}
	} else {
		stack = append(stack, val)
	}
	f.stacks[fq] = stack
	if fq > f.max {
		f.max = fq
	}
}

func (f *FreqStack) Pop() int {
	stack := f.stacks[f.max]
	v := stack[len(stack)-1]
	f.stacks[f.max] = stack[:len(stack)-1]
	if len(f.stacks[f.max]) == 0 {
		delete(f.stacks, f.max)
		f.max--
	}
	f.freq[v]--
	return v
}
