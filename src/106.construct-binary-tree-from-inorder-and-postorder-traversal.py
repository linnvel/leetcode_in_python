#
# @lc app=leetcode id=106 lang=python
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        global postorderIndex
        postorderIndex = len(postorder) - 1

        def helper(inorder, postorder):
            global postorderIndex
            if not inorder:
                return None

            # global postorderIndex
            root = TreeNode(postorder[postorderIndex])
            idx = inorder.index(postorder[postorderIndex])
            postorderIndex -= 1
            root.right = helper(inorder[idx+1:], postorder)
            root.left = helper(inorder[:idx], postorder)
            return root

        return helper(inorder, postorder)
        
# @lc code=end

