#
# @lc app=leetcode id=103 lang=python
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        queue = [root]
        left = True
        order = []

        while queue:
            level = []
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if left:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            order.append(level)
            left = not left
        return order


        
        
# @lc code=end

