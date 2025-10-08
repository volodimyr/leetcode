// 706. Design HashMap
// Topics: 'Array', 'HashTable', 'Linked List', 'Design', 'Hash Function'

// Design a HashMap without using any built-in hash table libraries.

// Implement the MyHashMap class:

//     MyHashMap() initializes the object with an empty map.
//     void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
//     int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
//     void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

// Example 1:

// Input
// ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
// [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
// Output
// [null, null, null, 1, -1, null, 1, null, -1]

// Explanation
// MyHashMap myHashMap = new MyHashMap();
// myHashMap.put(1, 1); // The map is now [[1,1]]
// myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
// myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
// myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
// myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
// myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
// myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
// myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

// Constraints:

//     0 <= key, value <= 106
//     At most 104 calls will be made to put, get, and remove.

package designhashmap

import (
	"fmt"
	"math"
)

type MyHashMap struct {
	values []*linkedList
	cap    int
	size   int
}

func Constructor() MyHashMap {
	values := make([]*linkedList, 11)
	for i := range 11 {
		values[i] = newLinkedList()
	}
	return MyHashMap{
		values: values,
		size:   0,
		cap:    11,
	}
}

func (m *MyHashMap) Put(key int, value int) {
	index := m.hash(key)
	if m.values[index].insert(key, value) {
		m.size++
	}
	if m.shouldResize() {
		m.resize()
	}
}

func (m *MyHashMap) shouldResize() bool {
	return float64(m.size)/float64(m.cap) >= 0.75
}

func (m *MyHashMap) resize() {
	oldValues := m.values
	nValues := make([]*linkedList, findNextPrime(m.cap*2))
	for i := range nValues {
		nValues[i] = newLinkedList()
	}

	m.cap = len(nValues)
	m.size = 0
	m.values = nValues

	for i := 0; i < len(oldValues); i++ {
		curr := oldValues[i].head
		for curr != nil {
			index := m.hash(curr.key)
			nValues[index].insertHead(curr.key, curr.val)
			m.size++
			curr = curr.next
		}
	}
}

func (m *MyHashMap) Get(key int) int {
	index := m.hash(key)
	return m.values[index].find(key)
}

func (m *MyHashMap) Remove(key int) {
	index := m.hash(key)
	if m.values[index].remove(key) {
		m.size--
	}
}

func (m *MyHashMap) String() string {
	var s string
	for i, v := range m.values {
		s += fmt.Sprintf("[%d] = %s\n", i, v)
	}
	return s
}

func (m *MyHashMap) hash(key int) int {
	return key % m.cap
}

type linkedList struct {
	head *node
}

type node struct {
	val  int
	key  int
	next *node
}

func newLinkedList() *linkedList {
	return &linkedList{}
}

func (ll *linkedList) String() string {
	var s string
	curr := ll.head
	for curr != nil {
		if s == "" {
			s = fmt.Sprintf("[key = %d value = %d]", curr.key, curr.val)
		} else {
			s += fmt.Sprintf("->[key = %d value = %d]", curr.key, curr.val)
		}
		curr = curr.next
	}
	return s
}

func (ll *linkedList) insertHead(key, val int) {
	ll.head = &node{val: val, key: key, next: ll.head}
}

func (ll *linkedList) insert(key, val int) bool {
	var inserted bool
	curr := ll.head
	for curr != nil {
		if curr.key == key {
			curr.val = val
			break
		}
		curr = curr.next
	}
	if curr == nil {
		// not found
		inserted = true
		ll.head = &node{val: val, key: key, next: ll.head}
	}
	return inserted
}

func (ll *linkedList) find(key int) int {
	val := -1
	curr := ll.head
	for curr != nil {
		if curr.key == key {
			val = curr.val
			break
		}
		curr = curr.next
	}
	return val
}

func (ll *linkedList) remove(key int) bool {
	if ll.head == nil {
		return false
	}
	curr := ll.head
	var prev *node
	for curr != nil {
		if curr.key == key {
			break
		}
		prev = curr
		curr = curr.next
	}
	if curr == nil {
		// not found
		return false
	}
	if prev == nil {
		// found (head)
		ll.head = curr.next
	} else {
		// in the middle
		prev.next = curr.next
	}
	return true
}

func isPrime(num int) bool {
	if num <= 1 {
		return false
	}
	if num <= 3 {
		return true
	}
	if num%2 == 0 || num%3 == 0 {
		return false
	}
	for i := 5; int(math.Sqrt(float64(num))) >= i; i = i + 6 {
		if num%i == 0 || num%(i+2) == 0 {
			return false
		}
	}
	return true
}

func findNextPrime(n int) int {
	for {
		if isPrime(n) {
			return n
		}
		n++
	}
}
