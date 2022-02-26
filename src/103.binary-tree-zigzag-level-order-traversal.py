#
# @lc app=leetcode id=103 lang=python
#
# [103] Binary Tree Zigzag Level Order Traversal
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        results = []
        q = deque([root])
        flag = 1
        while q:
            qsize = len(q)
            result = []
            for i in range(qsize):
                node = q.popleft()
                if flag > 0:
                    result.append(node.val)
                else:
                    result = [node.val] + result
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            results.append(result)
            flag = -flag
        return results
        
# @lc code=end

