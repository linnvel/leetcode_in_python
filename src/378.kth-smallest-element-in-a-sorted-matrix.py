#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
from heapq import heapify, heappop, heappush
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        if n == 0:
            return
        
        # Solution 1: heap + set
        # cnt = 0
        # h = [(matrix[0][0], 0, 0)]
        # visited = {(0, 0)}
        # while cnt < k and h:
        #     value, i, j = heappop(h)
        #     if i + 1 < n and (i + 1, j) not in visited:
        #         heappush(h, (matrix[i + 1][j], i + 1, j))
        #         visited.add((i + 1, j))
        #     if j + 1 < n and (i, j + 1) not in visited:
        #         heappush(h, (matrix[i][j + 1], i, j + 1))
        #         visited.add((i, j + 1))
        #     cnt += 1
        # if cnt == k:
        #     return value

        # Solution 2: heap
        cnt = 0
        h = [(matrix[i][0], i, 0) for i in range(n)]  
        # here we don't have to heapify because matrix[:][0] is already sorted
        while cnt < k and h:
            value, i, j = heappop(h)
            if j + 1 < n:
                heappush(h, (matrix[i][j + 1], i, j + 1))
            cnt += 1
        if cnt == k:
            return value    
# @lc code=end

