#
# @lc app=leetcode id=94 lang=python
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        results = []
        stack = []
        while root is not None:
            stack.append(root)
            root = root.left
        
        while stack:
            node = stack.pop()
            results.append(node.val)
            if node.right is not None:
                node = node.right
                stack.append(node)
                while node.left is not None:
                    node = node.left
                    stack.append(node)
        return results

        

        
# @lc code=end

