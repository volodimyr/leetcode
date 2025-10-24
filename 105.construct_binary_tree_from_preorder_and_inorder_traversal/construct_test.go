package construct

import (
	"reflect"
	"testing"
)

func TestBuildTreeExample1(t *testing.T) {
	preorder := []int{3, 9, 2, 11, 20, 15, 7}
	inorder := []int{2, 9, 11, 3, 15, 20, 7}

	root := buildTree(preorder, inorder)

	/*
		      3
		    /   \
		  9      20
		 / \    /  \
		2  11 15   7
	*/

	var result []int
	traverse(root, &result)

	if !reflect.DeepEqual(result, inorder) {
		t.Fatalf("expected inorder %v, got %v", inorder, result)
	}
}

func TestBuildTreeSingleNode(t *testing.T) {
	preorder := []int{-1}
	inorder := []int{-1}

	root := buildTree(preorder, inorder)

	/*
	   -1
	*/

	var result []int
	traverse(root, &result)

	if !reflect.DeepEqual(result, inorder) {
		t.Fatalf("expected inorder %v, got %v", inorder, result)
	}
}

func TestBuildTreeEmpty(t *testing.T) {
	var preorder []int
	var inorder []int

	root := buildTree(preorder, inorder)

	/*
	   nil
	*/

	var result []int
	traverse(root, &result)

	if len(result) != 0 {
		t.Fatalf("expected empty inorder, got %v", result)
	}
}
