package ds

import (
	"fmt"
	"testing"
)

func TestNewSinglyLinkedList(t *testing.T) {
	ll := NewLinkedList()
	fmt.Println(ll.GetValues())
	ll.InsertHead(3)
	fmt.Println(ll.GetValues())
	ll.InsertHead(2)
	fmt.Println(ll.GetValues())
	ll.InsertTail(0)
	fmt.Println(ll.GetValues())
	fmt.Println("Remove(0)", ll.Remove(0))
	fmt.Println(ll.GetValues())
	fmt.Println("Remove(1)", ll.Remove(1))
	fmt.Println(ll.GetValues())
	ll.InsertHead(5)
	ll.InsertTail(10)
	fmt.Println(ll.GetValues())
}
