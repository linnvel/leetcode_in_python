#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        q = deque([root])
        results = []
        while q:
            qsize = len(q)
            result = []
            for i in range(qsize):
                node = q.popleft()
                result.append(node.val)
                if node.children is not None:
                    for child in node.children:
                        q.append(child)
            results.append(result)
        return results
        
# @lc code=end

