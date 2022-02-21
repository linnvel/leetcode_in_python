#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # def findPath(root):
        #     if root.left is None and root.right is None:
        #         return [str(root.val)]
        #     paths = []
        #     if root.left is not None:
        #         paths += [str(root.val) + p for p in findPath(root.left)] 
        #     if root.right is not None:
        #         paths += [str(root.val) + p for p in findPath(root.right)]
        #     return paths

        # return sum([int(p) for p in findPath(root)])

        # Solution 2:
        global sumValue
        sumValue = 0
        def helper(root, num):
            global sumValue
            if root is None:
                return
            if root.left is None and root.right is None:
                num = num * 10 + root.val
                sumValue += num
                return
            num = num * 10 + root.val
            helper(root.left, num)
            helper(root.right, num)
        helper(root, 0)
        return sumValue
            

        
# @lc code=end

