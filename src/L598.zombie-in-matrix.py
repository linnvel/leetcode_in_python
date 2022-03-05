from typing import (
    List,
)

from collections import deque

class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid: List[List[int]]) -> int:
        # write your code here
        if len(grid) == 0:
            return 0
        
        m, n = len(grid), len(grid[0])

        queue = deque()
        humans = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                elif grid[i][j] == 0:
                    humans.add((i, j))
        days = 0
        if len(humans) == 0:
            return days
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        while queue:
            qsize = len(queue)
            days += 1
            for _ in range(qsize):
                x0, y0 = queue.popleft()
                for i in range(4):
                    x = x0 + dx[i]
                    y = y0 + dy[i]
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                        grid[x][y] = 1
                        queue.append((x, y))
                        humans.remove((x, y))
                        if len(humans) == 0:
                            return days
        return -1