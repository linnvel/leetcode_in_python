#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValidSudoku(value, r, c):
            for i in range(m): # scan by col
                if board[i][c] == value:
                    return False
            for j in range(n): # scan by row
                if board[r][j] == value:
                    return False
            for i in range(r // 3 * 3, r //3 * 3 + 3):
                for j in range(c // 3 * 3, c //3 * 3 + 3):
                    if board[i][j] == value:
                        return False
            return True

        def helper(startIndex):
            for i in range(startIndex, len(holes)):
                r, c = holes[i]
                for num in range(9):
                    value = str(num + 1)
                    if not isValidSudoku(value, r, c):
                        continue
                    board[r][c] = value
                    if helper(i + 1):
                        return True
                    else:
                        board[r][c] = "."
                return False
            return True
            
        if len(board) == 0:
            return board
        
        m, n = len(board), len(board[0])
        holes = [(i, j) for i in range(m) for j in range(n) if board[i][j] == "."]
        print(holes)
        helper(0)
        return board
# @lc code=end

