#
# @lc app=leetcode id=111 lang=python
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cnt = 0
        if root is None:
            return cnt
        queue = [root]
        while queue:
            size = len(queue)
            cnt += 1
            for i in range(size):
                node = queue.pop(0)
                if node.left is None and node.right is None:
                    return cnt
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                    

        
# @lc code=end

