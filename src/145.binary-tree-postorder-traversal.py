#
# @lc app=leetcode id=145 lang=python
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import re


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # # Solution 1: recursion
        # results = []
        # if root is None:
        #     return results
        # if root.left is not None:
        #     results += self.postorderTraversal(root.left)
        # if root.right is not None:
        #     results += self.postorderTraversal(root.right)
        # results.append(root.val)
        # return results

        # Solution 2: iteration
        from collections import deque
        results = []
        stack = deque()
        lastVisited = None
        while root is not None:
            stack.append(root)
            root = root.left
        
        while stack:
            node = stack.pop()
            if node.right is not None and lastVisited != node.right:
                stack.append(node)
                node = node.right
                stack.append(node)
                while node.left is not None:
                    stack.append(node.left)
                    node = node.left
            else:
                results.append(node.val)
                lastVisited = node
        return results



        
# @lc code=end

