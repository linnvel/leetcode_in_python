#
# @lc app=leetcode id=145 lang=python
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # # Iterative solution 1
        # if root is None:
        #     return []
        # stack = [root]
        # cnt = {}
        # results = []
        # while stack:
        #     cur = stack[-1]

        #     # left branch
        #     while cur.left is not None and cnt.get(cur, 0) < 1:
        #         stack.append(cur.left)
        #         cnt[cur] = 1
        #         cur = cur.left
        #     if cur not in cnt:
        #         cnt[cur] = 1

        #     # right node
        #     if cnt[cur] < 2:
        #         if cur.right is not None: 
        #             stack.append(cur.right)
        #         cnt[cur] += 1

        #     # root node
        #     else:
        #         cur = stack.pop()
        #         results.append(cur.val)

        # iterative solution 2:
        if root is None:
            return []
        stack = [root]
        cur = root
        lastvisited = None
        results = []

        while stack:
            cur = stack[-1]
            # mask sure that the left branch haven't been visited
            if lastvisited is None or lastvisited.left == cur or lastvisited.right == cur:
                while cur.left is not None:
                    stack.append(cur.left)
                    cur = cur.left
            if cur.right is None or cur.right == lastvisited:
                stack.pop()
                results.append(cur.val)
            elif cur.right is not None:
                stack.append(cur.right)
            lastvisited = cur
                
        return results
            



        
# @lc code=end

