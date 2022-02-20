#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        cur = root
        while cur is not None:
            if val < cur.val:
                if cur.left is not None:    
                    cur = cur.left
                else:
                    cur.left = TreeNode(val)
                    break
            else:
                if cur.right is not None:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    break
        return root
        
# @lc code=end

