#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if len(board) == 0:
            return
        m, n = len(board), len(board[0])
        def getNeighborLiveCount(i, j):
            nx = [-1, 0, 1]
            ny = [-1, 0, 1]
            live_count = 0
            for x in nx:
                newi = i + x
                if 0 <= newi < m:
                    for y in ny:
                        newj = j + y
                        if (x == 0 and y == 0) or newj < 0 or newj >= n:
                            continue 
                        if board[newi][newj] == 1 or board[newi][newj] == -1:
                            live_count += 1
            return live_count
        
        for i in range(m):
            for j in range(n):
                live_count = getNeighborLiveCount(i, j) 
                if board[i][j] == 1:
                    if live_count < 2 or live_count > 3:
                        board[i][j] = -1
                elif live_count == 3:
                    board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1


# @lc code=end

