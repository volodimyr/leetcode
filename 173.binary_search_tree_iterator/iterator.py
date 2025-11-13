from typing import List, Optional

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.root = root
        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left

    def next(self) -> int:
        pop = self.stack.pop()
        cur = pop.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return pop.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
    
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def inorder(self) -> List[int]:
        cur = self
        stack = []
        result = []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                pop = stack.pop()
                result.append(pop.val)
                cur = pop.right
        return result

    def preorder(self) -> List[int]:
        cur = self
        stack = []
        result = []
        while cur or stack:
            if cur:
                result.append(cur.val)
                stack.append(cur)
                cur = cur.left
            else:
                pop = stack.pop()
                cur = pop.right
        return result

    def postorder(self) -> List[int]:
        stack = []
        stack.append((self, False))
        result = []
        while stack:
            cur = stack.pop()
            if cur[0]:
                if cur[1]:
                    result.append(cur[0].val)
                else:
                    stack.append((cur[0], True))
                    stack.append((cur[0].right, False))
                    stack.append((cur[0].left, False))
        return result