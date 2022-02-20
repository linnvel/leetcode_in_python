#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.pointer = TreeNode(-float('inf'))
        self.stack = deque()
        if root is not None:
            self.stack.append(root)
            while root.left is not None:
                self.stack.append(root.left)
                root = root.left

    def next(self) -> int:
        self.pointer = self.stack.pop()
        cur = self.pointer
        if cur.right is not None:
            cur = cur.right
            self.stack.append(cur)
            while cur.left is not None:
                self.stack.append(cur.left)
                cur = cur.left
        return self.pointer.val

    def hasNext(self) -> bool:
        return bool(self.stack)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

