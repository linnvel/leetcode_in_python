#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#

# @lc code=start
from queue import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacent list
        adjacent = {i:[] for i in range(n)}
        for edge in edges:
            start, end = edge
            adjacent[start].append(end)
            adjacent[end].append(start)
        
        # # Solution 1: BFS
        # nodes = {i for i in range(n)}
        # result = 0
        # while nodes:    
        #     queue = deque()
        #     node = nodes.pop()
        #     queue.append(node)
        #     while queue:
        #         cur = queue.popleft()
        #         for neighbor in adjacent[cur]:
        #             if neighbor in nodes:
        #                 nodes.remove(neighbor)
        #                 queue.append(neighbor)
        #     result += 1
        # return result
                        
        # Solution 2: DFS
        nodes = {i for i in range(n)}
        
        def dfs(cur):
            for neighbor in adjacent[cur]:
                if neighbor in nodes:
                    nodes.remove(neighbor)
                    dfs(neighbor)
        
        result = 0
        while nodes:
            node = nodes.pop()
            dfs(node)
            result += 1
        return result

# @lc code=end