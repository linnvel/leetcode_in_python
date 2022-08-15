#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start

from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # get indegree and adjacent list
        indegree = {i:0 for i in range(numCourses)}
        adj_list = {i:[] for i in range(numCourses)}
        for course, precourse in prerequisites:
            indegree[course] += 1
            adj_list[precourse].append(course)
        
        # find start nodes and push to queue
        startNodes = [i for i in indegree if indegree[i] == 0]
        queue = deque(startNodes)

        # bfs
        # results = []
        # while queue:
        #     node = queue.popleft()
        #     if indegree[node] == 0:
        #         for neighbor in adj_list[node]:
        #             indegree[neighbor] -= 1
        #             if neighbor not in queue:
        #                 queue.appendleft(neighbor)
        #         results.append(node)

        results = startNodes
        while queue:
            node = queue.pop()
            for neighbor in adj_list[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    results.append(neighbor)
        return len(results) == numCourses       
            

# @lc code=end