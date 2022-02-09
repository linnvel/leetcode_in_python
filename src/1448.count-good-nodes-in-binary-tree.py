#
# @lc app=leetcode id=1448 lang=python
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        results = []
        if root is None:
            return results
        path = []
        self.helper(root, path, results, -float('inf'))
        return len(results)
    
    def helper(self, node, path, results, curMax):
        path.append(node.val)
        if node.val >= curMax:
            results.append(node.val)
            curMax = max(curMax, node.val)
        if node.left is not None:
            self.helper(node.left, path, results, curMax)
            path.pop()
        if node.right is not None:
            self.helper(node.right, path, results, curMax)
            path.pop()
        
# @lc code=end

