#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        results = []
        queue = deque()
        if root is not None:
            queue.append(root)
        while queue:
            qsize = len(queue)
            level = []
            for i in range(qsize):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
            results.append(level)
        return results

        
        
# @lc code=end

