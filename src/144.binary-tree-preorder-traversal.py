#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # # Solution 1: recursion
        # results = []
        # if root is None:
        #     return results
        # results.append(root.val)
        # if root.left is not None:
        #     results += self.preorderTraversal(root.left)
        # if root.right is not None:
        #     results += self.preorderTraversal(root.right)
        # return results

        # Solution 2: iteration
        from collections import deque
        results = []
        stack = deque()

        if root is not None:
            stack.append(root)
        
        while stack:
            node = stack.pop()
            results.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return results

# @lc code=end

