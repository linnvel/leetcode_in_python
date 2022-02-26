#
# @lc app=leetcode id=107 lang=python
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        results = []
        q = deque([root])
        while q:
            qsize = len(q)
            result = []
            for i in range(qsize):
                node = q.popleft()
                result.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            results.append(result)
        return results[::-1]

# @lc code=end

