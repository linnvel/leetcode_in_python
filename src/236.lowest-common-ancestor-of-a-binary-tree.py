#
# @lc app=leetcode id=236 lang=python
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is not None and right is None:
            return left
        elif left is None and right is not None:
            return right
        elif left is not None and right is not None:
            return root
        else:
            return None
        
# @lc code=end
