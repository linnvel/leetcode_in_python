#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def update_grid_bfs(grid, x0, y0, m, n):
            grid[x0][y0] = "0"
            queue = deque([(x0, y0)])
            dx = [-1, 0, 0, 1]
            dy = [0, -1, 1, 0]
            while queue:
                x0, y0 = queue.popleft()
                for i in range(4):
                    x = x0 + dx[i]
                    y = y0 + dy[i]
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                        grid[x][y] = "0"
                        queue.append((x, y))
                    
        if len(grid) == 0:
            return 0
        
        count = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    update_grid_bfs(grid, i, j, m, n)
                    count += 1
        return count


        
# @lc code=end

