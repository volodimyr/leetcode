# 716. Max Stack
# Topics: 'Linked List', 'Stack', 'Design', 'Doubly-Linked List', 'Ordered Set'
# Level: 'Hard'

# Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

# Implement the MaxStack class:

#     MaxStack() Initializes the stack object.

#     void push(int x) Pushes element x onto the stack.

#     int pop() Removes the element on top of the stack and returns it.

#     int top() Gets the element on the top of the stack without removing it.

#     int peekMax() Retrieves the maximum element in the stack without removing it.

#     int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.

# You should come up with a solution that supports O(1) for each top call and O(logn) for each other call.

# Example 1:

# Input:
# ["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
# [[], [5], [1], [5], [], [], [], [], [], []]

# Output:
# [null, null, null, null, 5, 5, 1, 5, 1, 5]

# Explanation:
# MaxStack stk = new MaxStack();
# stk.push(5);   // [5] the top of the stack and the maximum number is 5.
# stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
# stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
# stk.top();     // return 5, [5, 1, 5] the stack did not change.
# stk.popMax();  // return 5, [5, 1] the stack is changed now, and the top is different from the max.
# stk.top();     // return 1, [5, 1] the stack did not change.
# stk.peekMax(); // return 5, [5, 1] the stack did not change.
# stk.pop();     // return 1, [5] the top of the stack and the max element is now 5.
# stk.top();     // return 5, [5] the stack did not change.


# Constraints:

#     -10⁷ <= x <= 10⁷
#     At most 10⁵ calls will be made to push, pop, top, peekMax, and popMax.
#     There will be at least one element in the stack when pop, top, peekMax, or popMax is called.


import heapq

class MaxStack:
    def __init__(self):
        self.max_heap = []
        self.stack = []
        self.generation = 0

    def push(self, x: int) -> None:
        self.generation += 1
        n = Node(x, self.generation)

        self.stack.append(n)
        heapq.heappush(self.max_heap, n)

    def pop(self) -> int:
        while self.stack and not self.stack[-1].valid:
            self.stack.pop()

        n = self.stack.pop()
        n.valid = False

        return n.x

    def top(self) -> int:
        while self.stack and not self.stack[-1].valid:
            self.stack.pop()

        return self.stack[-1].x

    def peekMax(self) -> int:
        while self.max_heap and not self.max_heap[0].valid:
            heapq.heappop(self.max_heap)

        return self.max_heap[0].x

    def popMax(self) -> int:
        while self.max_heap and not self.max_heap[0].valid:
            heapq.heappop(self.max_heap)

        n = heapq.heappop(self.max_heap)
        n.valid = False

        return n.x


class Node:
    def __init__(self, x, generation):
        self.x = x
        self.generation = generation
        self.valid = True

    def __lt__(self, other):
        if self.x == other.x:
            return self.generation > other.generation

        return self.x > other.x