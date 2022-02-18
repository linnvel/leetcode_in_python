#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanceHelper(root):
            if root is None:
                return True, 0
            left_balance, left_height = balanceHelper(root.left)
            right_balance, right_height = balanceHelper(root.right)
            balance = left_balance and right_balance and abs(left_height - right_height) <= 1
            height = max(left_height, right_height) + 1
            return balance, height

        return balanceHelper(root)[0]
        
# @lc code=end

