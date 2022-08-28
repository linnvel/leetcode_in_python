#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start
from collections import deque

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Solution 1: BFS
        # def hasCircle(adj_list):
        #     for startNode in adj_list.keys():
        #         nodes = {startNode: None}
        #         queue = deque()
        #         queue.append(startNode)
        #         while queue:
        #             node = queue.popleft()
        #             for neighbor in adj_list[node]:
        #                 if nodes[node] == neighbor:
        #                     continue
        #                 if neighbor in nodes:
        #                     return True
        #                 queue.append(neighbor)
        #                 nodes[neighbor] = node
        #     return False

        # all_nodes = list({node for edge in edges for node in edge})
        # adj_list = {node:[] for node in all_nodes}
        # for start, end in edges:
        #     adj_list[start].append(end)
        #     adj_list[end].append(start)

        # for edge in edges[::-1]:
        #     start, end = edge
        #     adj_list[start].remove(end)
        #     adj_list[end].remove(start)
        #     if not hasCircle(adj_list):
        #         return edge
        #     adj_list[start].append(end)
        #     adj_list[end].append(start)

        # Solution 2: DFU
        def find(parents, node):
            parent = node
            while parents[parent] >= 0:
                parent = parents[parent]
            if parents[node] >= 0:
                parents[node] = parent
            return parent
        
        def union_circle(parents, nodea, nodeb):
            parenta = find(parents, nodea)
            parentb = find(parents, nodeb)
            if parenta != parentb:
                if parents[parenta] <= parents[parentb]:
                    parent, child = parenta, parentb
                else:
                    parent, child = parentb, parenta
                parents[parent] += parents[child]
                parents[child] = parent
                return False
            else:
                return True
            
        nodes = set([node for edge in edges for node in edge])
        parents = [-1 for _ in range(len(nodes))]
        for edge in edges:
            nodea, nodeb = edge
            if union_circle(parents, nodea - 1, nodeb - 1):
                return edge
        
# @lc code=end

