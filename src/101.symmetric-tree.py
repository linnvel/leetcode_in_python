#
# @lc app=leetcode id=101 lang=python
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def isMirror(self, node1, node2):
    #     if node1 is None and node2 is None:
    #         return True
    #     if node1 is None or node2 is None:
    #         return False
    #     return node1.val == node2.val and \
    #         self.isMirror(node1.left, node2.right) and \
    #         self.isMirror(node1.right, node2.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # # Solution 1: recursion
        # return self.isMirror(root, root)

        # Solution 2: iteration BFS
        if root is None:
            return True
        
        queue = [root, root]
        while queue:
            node1 = queue.pop(0)
            node2 = queue.pop(0)
            if node1 is None and node2 is None:
                continue
            elif node1 is None or node2 is None:
                return False
            elif node1.val != node2.val:
                return False
            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)
        return True

        
# @lc code=end

