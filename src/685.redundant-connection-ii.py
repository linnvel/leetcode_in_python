#
# @lc app=leetcode id=685 lang=python3
#
# [685] Redundant Connection II
#

# @lc code=start
from queue import deque

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:        
        # Solution 1: BFS
        # def isValid(adjacent, indegree):
        #     roots = [k for k, v in indegree.items() if v == 0]
        #     if len(roots) != 1:
        #         return False
        #     start = roots[0]
        #     visited = set()
        #     queue = deque()
        #     queue.append(start)
        #     visited.add(start)
        #     while queue:
        #         cur = queue.pop()
        #         for neighbor in adjacent[cur]:
        #             if neighbor in visited:
        #                 return False
        #             queue.append(neighbor)
        #             visited.add(neighbor)
        #     return len(visited) == len(adjacent)

        # n = max([max(edge)for edge in edges])
        # adjacent = {i + 1: [] for i in range(n)}
        # indegree = {i + 1: 0 for i in range(n)}
        # for edge in edges:
        #     start, end = edge
        #     adjacent[start].append(end)
        #     indegree[end] += 1
        
        # for edge in edges[::-1]:
        #     start, end = edge
        #     adjacent[start].remove(end)
        #     indegree[end] -= 1
        #     if isValid(adjacent, indegree):
        #         return edge
        #     adjacent[start].append(end)
        #     indegree[end] += 1

        # Solution 2: Union Find
        n = max([max(edge)for edge in edges])
        parents = [-1 for _ in range(n)]

        def find(node):
            parent = node
            while parents[parent - 1] > 0:
                parent = parents[parent - 1]
            return parent

        candidates = []
        for edge in edges:
            print(parents)
            start, end = edge
            pstart, pend = find(start), find(end)
            print(pstart, pend, start, end)
            if pstart == pend:
                return edge
            if parents[end - 1] > 0 and parents[end - 1] != start:
                candidates.append(edge)
                candidates.append([parents[end - 1], end])
                parents[end - 1] = -1
                continue
            parents[end - 1] = start
        print(parents, candidates)
        
        for edge in candidates:
            start, end = edge
            pstart, pend = find(start), find(end)
            if pstart == pend:
                return edge
        return candidates[0]
        # roots = [p for p in parents if p < 0]
        # return len(roots)  == 1
            

# @lc code=end

