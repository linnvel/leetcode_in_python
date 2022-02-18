#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        # # Solution 1: backtracking
        # def helper(root, results, curPath):
        #     curPath.append(str(root.val))
        #     if root.left is None and root.right is None:
        #         results.append("->".join(curPath))
        #         return
        #     if root.left is not None:
        #         helper(root.left, results, curPath)
        #         curPath.pop()
        #     if root.right is not None:
        #         helper(root.right, results, curPath)
        #         curPath.pop()
        
        # results = []
        # if root is None:
        #     return results
        # curPath = []
        # helper(root, results, curPath)
        # return results

        # Solution 2: recursion
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]

        left_paths = self.binaryTreePaths(root.left)
        right_paths = self.binaryTreePaths(root.right)
        return [str(root.val) + "->" + path for path in left_paths] + [str(root.val) + "->" + path for path in right_paths]

# @lc code=end

