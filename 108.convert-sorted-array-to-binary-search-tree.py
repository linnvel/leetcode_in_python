#
# @lc app=leetcode id=108 lang=python
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(node, nums):
            # if not nums:
            #     return None
            mid = len(nums) // 2
            # print(mid, nums)
            node.val = nums[mid]
            if mid <= 0:
                node.left = None
            else:
                left = TreeNode()
                node.left = helper(left, nums[:mid])
            if mid >= len(nums) - 1:
                node.right = None
            else:
                right = TreeNode()
                node.right = helper(right, nums[mid+1:])
            return node

        if not nums:
            return None
        root = TreeNode()
        helper(root, nums)
        return root

        
# @lc code=end

