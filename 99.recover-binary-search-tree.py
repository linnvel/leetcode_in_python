#
# @lc app=leetcode id=99 lang=python
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        # Solution 1: three steps
        # if root is None:
        #     return

        # # inorder traversal
        # results = []
        # self.inorder(root, results)
        # if len(results) < 2:
        #     return

        # # find the start and end of descending nodes
        # prev = results[0]
        # start, end = None, None
        # for curr in results[1:]:
        #     if curr.val < prev.val:
        #         if start is None:
        #             start = prev
        #         end = curr
        #     prev = curr
        
        # # swap val between start and end nodes
        # start.val, end.val = end.val, start.val

        # Solution 2: iterative inorder with two steps
        # stack = []
        # x, y, pred = None, None, None
        # while stack or root:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     root = stack.pop()
        #     if pred and root.val < pred.val:
        #         if x is None:
        #             x = pred
        #         y = root
        #     pred = root
        #     root = root.right
        
        # x.val, y.val = y.val, x.val

        # Solution 3: recursive inorder with two steps
        global x, y, pred 
        x, y, pred = None, None, None

        def find_two_swapped(root):
            global pred, x, y 
            if root is None:
                return
            find_two_swapped(root.left)
            if pred is not None and pred.val > root.val:
                if x is None:
                    x = pred
                y = root
            pred = root
            find_two_swapped(root.right)
        
        find_two_swapped(root)
        x.val, y.val = y.val, x.val
        
        
    def inorder(self, root, results):
        if root.left is not None:
            self.inorder(root.left, results)
        results.append(root)
        if root.right is not None:
            self.inorder(root.right, results)

# @lc code=end

