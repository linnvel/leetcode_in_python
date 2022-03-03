#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start

from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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

        if len(order) == numCourses:
            return order
        else:
            return []
# @lc code=end

