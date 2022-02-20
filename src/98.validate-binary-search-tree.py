#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Result:
    def __init__(self, isValid, minValue, maxValue):
        self.isValid = isValid
        self.minValue = minValue
        self.maxValue = maxValue

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if root is None:
                return Result(True, float('inf'), -float('inf'))
            left = helper(root.left)
            right = helper(root.right)
            isValid = left.isValid and right.isValid and right.minValue > root.val > left.maxValue
            minValue = min(left.minValue, root.val, right.minValue)
            maxValue = max(left.maxValue, root.val, right.maxValue)
            return Result(isValid, minValue, maxValue)
        
        return helper(root).isValid

# @lc code=end

