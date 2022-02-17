#
# @lc app=leetcode id=94 lang=python
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from unittest import result


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # # Solution 1: recursion
        # results = []

        # if root is None:
        #     return results
        # if root.left is not None:
        #     results += self.inorderTraversal(root.left)
        # results.append(root.val)
        # if root.right is not None:
        #     results += self.inorderTraversal(root.right)
        # return results

        # # def inorder(root):
        # #     if root is None:
        # #         return
        # #     if root.left is not None:
        # #         inorder(root.left)
        # #     results.append(root.val)
        # #     if root.right is not None:
        # #         inorder(root.right)

        # inorder(root)
        # return results
        
        # Solution 2: iteration
        from collections import deque
        results = []
        stack = deque()

        while root is not None:
            stack.append(root)
            root = root.left
        while stack:
            node = stack.pop()
            results.append(node.val)
            if node.right is not None:
                node = node.right
                stack.append(node)
                while node.left is not None:
                    node = node.left
                    stack.append(node)
        return results            

        
# @lc code=end

