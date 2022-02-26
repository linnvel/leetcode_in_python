#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "X"
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return  str(root.val) + "," + left + "," + right
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def deserializeQueue(q):
            if len(q) == 0:
                return None
            val = q.popleft()
            if val == "X":
                return None
            root = TreeNode(val)
            root.left = deserializeQueue(q)
            root.right = deserializeQueue(q)
            return root
        q = deque(data.split(","))
        return deserializeQueue(q)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

