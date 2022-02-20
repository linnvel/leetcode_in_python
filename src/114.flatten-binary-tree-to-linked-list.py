#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # def helper(root):
        #     if root is None:
        #         return None, None
        #     if root.left is None and root.right is None:
        #         return root, root
        #     left = helper(root.left)
        #     right = helper(root.right)
        #     if root.left is None:
        #         return root, right[1]
        #     elif root.right is None:
        #         root.right = left[0]
        #         root.left = None
        #         return root, left[1]
        #     else:
        #         root.right = left[0]
        #         left[1].right = right[0]
        #         root.left = None
        #         return root, right[1]

        def helper(root):
            if root is None:
                return None
            leftLast = helper(root.left)
            rightLast = helper(root.right)
            if root.left is not None:
                leftLast.right = root.right
                root.right = root.left
                root.left = None
            if rightLast is not None:
                return rightLast
            if leftLast is not None:
                return leftLast
            return root

        helper(root)

        
# @lc code=end

