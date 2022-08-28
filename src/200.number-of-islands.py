#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        m, n = len(grid), len(grid[0])

#         # Solution 1: DFS
#         def dfs(x, y):
#             for i in range(4):
#                 newx = x + dx[i]
#                 newy = y + dy[i]
#                 if 0 <= newx < m and 0 <= newy < n and grid[newx][newy] == "1":
#                     grid[newx][newy] = "0"
#                     dfs(newx, newy)
                    
#         number = 0
#         for x in range(m):
#             for y in range(n):
#                 if grid[x][y] == "1":
#                     grid[x][y] = "0"
#                     dfs(x, y)
#                     number += 1
#         return number

#         # Solution 2: BFS
#         def bfs(x, y):
#             dq = deque()
#             dq.append((x, y))
#             while dq:
#                 curx, cury = dq.popleft()
#                 for i in range(4):
#                     newx = curx + dx[i]
#                     newy = cury + dy[i]
#                     if 0 <= newx < m and 0 <= newy < n and grid[newx][newy] == "1":
#                         grid[newx][newy] = "0"
#                         dq.append((newx, newy))
                        
#         number = 0
#         for x in range(m):
#             for y in range(n):
#                 if grid[x][y] == "1":
#                     grid[x][y] = "0"
#                     bfs(x, y)
#                     number += 1
#         return number

        # Solution 3: DFU
        parents = [[-1 for i in range(n)] for j in range(m)]
        number = m * n
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    parents[i][j] = ()
                    number -= 1
                    
        def make_set(number):
            for x in range(m):
                for y in range(n):
                    if grid[x][y] == "1":
                        grid[x][y] = "0"
                        
                        for i in range(4):
                            nx = x + dx[i]
                            ny = y + dy[i]
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                                # grid[nx][ny] = "0"
                                number -= union(x, y, nx, ny)
            return number
            
        def union(xa, ya, xb, yb):
            parenta = find((xa, ya))
            parentb = find((xb, yb))
            if parenta != parentb:
                if parents[parenta[0]][parenta[1]] <= parents[parentb[0]][parentb[1]]:
                    parent, child = parenta, parentb
                else:
                    parent, child = parentb, parenta
                parents[parent[0]][parent[1]] += parents[child[0]][child[1]]
                parents[child[0]][child[1]] = parent
                return 1
            else:
                return 0
        
        def find(node):
            parent = node
            while isinstance(parents[parent[0]][parent[1]], tuple):
                parent = parents[parent[0]][parent[1]]
            if isinstance(parents[node[0]][node[1]], tuple):
                parents[node[0]][node[1]] = parent
            return parent
        
        return make_set(number)
               
# @lc code=end

