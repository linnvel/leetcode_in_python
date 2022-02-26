#
# @lc app=leetcode id=449 lang=python3
#
# [449] Serialize and Deserialize BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    # # Solution 1: Iterative BFS (Level traversal)
    # def serialize(self, root: Optional[TreeNode]) -> str:
    #     """Encodes a tree to a single string.
    #     """
    #     if root is None:
    #         return ""
    #     nodes = []
    #     q = deque([root])
    #     while q:
    #         qsize = len(q)
    #         for i in range(qsize):
    #             node = q.popleft()
    #             if node is None:
    #                 nodes.append(node)
    #             else:
    #                 nodes.append(node.val)
    #                 q.append(node.left)
    #                 q.append(node.right)
    #     return ",".join([str(node) for node in nodes])

    # def deserialize(self, data: str) -> Optional[TreeNode]:
    #     """Decodes your encoded data to tree.
    #     """
    #     if not data:
    #         return None
    #     nodes = data.split(",")
    #     i = 1
    #     root = TreeNode(nodes[0])
    #     q = deque([root])
    #     while i < len(nodes) and q:
    #         node = q.popleft()
    #         left, right = nodes[i], nodes[i + 1]
    #         if left != "None":
    #             node.left = TreeNode(int(left))
    #             q.append(node.left)
    #         if right != "None":
    #             node.right = TreeNode(int(right))
    #             q.append(node.right)
    #         i += 2
    #     return root
    
    # Solution 2: DFS Recursion (Preorder traversal)
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if root is None:
            return "X"
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return  str(root.val) + "," + left + "," + right
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
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
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# @lc code=end

