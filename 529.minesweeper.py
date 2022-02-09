#
# @lc app=leetcode id=529 lang=python
#
# [529] Minesweeper
#

# @lc code=start
class Solution(object):
    # Solution 1: DFS
    # def updateBoard(self, board, click):
    #     """
    #     :type board: List[List[str]]
    #     :type click: List[int]
    #     :rtype: List[List[str]]
    #     """
    #     if len(board) == 0:
    #         return board
    #     row, col = click
    #     m, n = len(board), len(board[0])
    #     self.deltaX = [-1, 0, 1, -1, 1, -1, 0, 1]
    #     self.deltaY = [-1, -1, -1, 0, 0, 1, 1, 1]
    #     self.helper(board, row, col, m, n)
    #     return board
    
    # def helper(self, board, row, col, m, n):
    #     if row < 0 or col < 0 or row >= m or col >= n:
    #         return
    #     if board[row][col] == "M":
    #         board[row][col] = "X"            
    #     elif board[row][col] == "E":
    #         mines = self.countNeighbors(board, row, col, m, n)
    #         if mines > 0:
    #             board[row][col] = str(mines)
    #         else:
    #             board[row][col] = "B"
    #             for i in range(8):
    #                 nrow = row + self.deltaX[i]
    #                 ncol = col + self.deltaY[i]
    #                 self.helper(board, nrow, ncol, m, n)
    
    # def countNeighbors(self, board, row, col, m, n):
    #     count = 0
    #     for i in range(8):
    #         nrow = row + self.deltaX[i]
    #         ncol = col + self.deltaY[i]
    #         if nrow < 0 or ncol < 0 or nrow >= m or ncol >= n:
    #             continue
    #         if board[nrow][ncol] == "M":
    #             count += 1
    #     return count

    # Solution 2: BFS
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if len(board) == 0:
            return board
        m, n = len(board), len(board[0])
        row, col = click
        if board[row][col] == "M":
            board[row][col] = "X"
            return board
        if board[row][col] != "E":
            return board
        
        queue = [click]
        deltaX = [-1, 0, 1, -1, 1, -1, 0, 1]
        deltaY = [-1, -1, -1, 0, 0, 1, 1, 1]
        while queue:
            row, col = queue.pop()
            count = 0
            neighbors = []
            for i in range(8):
                nrow = row + deltaX[i]
                ncol = col + deltaY[i]
                if 0 <= nrow < m and 0 <= ncol < n:
                    if board[nrow][ncol] == "M":
                        count += 1
                    elif board[nrow][ncol] == "E":
                        neighbors.append([nrow, ncol])
            if count == 0:
                board[row][col] = 'B'
                queue += neighbors
            else:
                board[row][col] = str(count)
        return board



# @lc code=end

