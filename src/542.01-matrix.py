#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start

from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if len(mat) == 0:
            return []
        m, n = len(mat), len(mat[0])

        # Solution 1: Time Limit Exceeded
        # result = [[0 for _ in range(n)] for _ in range(m)]
        # dx = [1, 0, -1, 0]
        # dy = [0, 1, 0, -1]
        # for i in range(m):
        #     for j in range(n):
        #         if mat[i][j] == 0:
        #             continue
        #         q = deque([(i, j)])
        #         dist = 0
        #         while q:
        #             dist += 1
        #             qsize = len(q)
        #             k = 0
        #             # print(q, dist)
        #             while k < qsize:
        #                 x0, y0 = q.popleft()
        #                 for kk in range(4):
        #                     x = x0 + dx[kk]
        #                     y = y0 + dy[kk]
        #                     if 0 <= x <= m - 1 and 0 <= y <= n - 1:
        #                         if mat[x][y] == 0:
        #                             q = deque()
        #                             k = qsize
        #                             break
        #                         q.append((x, y))
        #                 k += 1             
        #         result[i][j] = dist
        # return result

        result = [[None for _ in range(n)] for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    queue.append((i, j))
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        while queue:
            x0, y0 = queue.popleft()
            for k in range(4):
                x = x0 + dx[k]
                y = y0 + dy[k]
                if x < 0 or x >= m or y < 0 or y >= n or result[x][y] is not None:
                    continue
                result[x][y] = result[x0][y0] + 1
                queue.append((x, y))
        return result
                              
        
# @lc code=end

