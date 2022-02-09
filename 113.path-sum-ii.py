#
# @lc app=leetcode id=113 lang=python
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        paths = []
        if root is None:
            return paths
        path = []
        self.helper(root, targetSum, path, paths)
        return paths
    
    def helper(self, root, targetSum, path, paths):
        if root is None:
            return
        path.append(root.val)
        newSum = targetSum-root.val
        # if root.left is None and root.right is None:
        #     if newSum == 0:
        #         paths.append(path[:])
        #     return
        
        # self.helper(root.left, newSum, path, paths)
        # if root.left is not None:
        #     path.pop()
        # self.helper(root.right, newSum, path, paths)
        # if root.right is not None:
        #     path.pop()
        if root.left is None and root.right is None and newSum == 0:
            paths.append(path[:])
        else:
            self.helper(root.left, newSum, path, paths)
            self.helper(root.right, newSum, path, paths)
        path.pop()

    # @lc code=end

