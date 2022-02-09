#
# @lc app=leetcode id=105 lang=python
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        global preorderIndex
        preorderIndex = 0
        def helper(preoorder, inorder):
            if not inorder:
                return None
            global preorderIndex
            root = TreeNode(preorder[preorderIndex])
            idx = inorder.index(preorder[preorderIndex])
            preorderIndex += 1
            root.left = helper(preorder, inorder[:idx])
            root.right = helper(preorder, inorder[idx+1:])
            return root
        return helper(preorder, inorder)
# @lc code=end

