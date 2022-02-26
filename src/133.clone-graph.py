#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Solution 1 (faster)
        if node is None:
            return None
        q = deque([node])
        gmap = {}
        while q:
            cur = q.popleft()
            if gmap.get(cur, None) is None:
                newNode = Node(cur.val)
                gmap[cur] = newNode
            for neighbor in cur.neighbors:
                if gmap.get(neighbor, None) is not None:
                    gmap[neighbor].neighbors.append(newNode)
                    newNode.neighbors.append(gmap[neighbor])
                elif neighbor not in gmap:
                    q.append(neighbor)
                    gmap[neighbor] = None
            print('\n')
        return gmap[node]

    #     # Solution 2
    #     if node is None:
    #         return None
        
    #     # 1. get all nodes by bfs
    #     nodes = self.getAllNodes(node)

    #     # 2. create new nodes
    #     mapping = {}
    #     for old in nodes:
    #         new = Node(old.val)
    #         mapping[old] = new
        
    #     # 3. copy edge
    #     for old in nodes:
    #         for neighbor in old.neighbors:
    #             mapping[old].neighbors.append(mapping[neighbor])
        
    #     return mapping[node]
    
    # def getAllNodes(self, node):
    #     q = deque([node])
    #     hashset = {node}
    #     nodes = []
    #     while q:
    #         cur = q.popleft()
    #         nodes.append(cur)
    #         hashset.add(cur)
    #         for neighbor in cur.neighbors:
    #             if neighbor not in hashset:
    #                 q.append(neighbor)
    #                 hashset.add(neighbor)
    #     return nodes

        
# @lc code=end

