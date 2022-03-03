#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start

from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # get indegree dict
        indegree = {}
        for course, _ in prerequisites:
            if course in indegree:
                indegree[course] += 1
            else:
                indegree[course] = 1
        
        # find start nodes
        q = deque()
        order = []
        for course in range(numCourses):
            if course not in indegree:
                q.append(course)
                order.append(course)

        while q:
            pre = q.popleft()
            for course, precourse in prerequisites:
                if pre != precourse:
                    continue
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
                    order.append(course)

        return len(order) == numCourses

# @lc code=end