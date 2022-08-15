#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # def checkValid(value, curSet):
        #     if value != ".":
        #         if value in curSet:
        #             return False
        #         else:
        #             curSet.add(value)
        #     return True
        
        # m, n = len(board), len(board[0])
        # # check rows
        # for i in range(m):
        #     row = set()
        #     for j in range(n):
        #         print(i, j, row)
        #         if not checkValid(board[i][j], row):
        #             return False

        # # check columns
        # for j in range(n):
        #     col = set()
        #     for i in range(m):
        #         if not checkValid(board[i][j], col):
        #             return False

        # # check subboxes
        # iter = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        # for i in range(m):
        #     box = set()
        #     for j in range(n):
        #         ix = iter[i // 3][j // 3]
        #         iy = iter[i % 3][j % 3]
        #         if not checkValid(board[ix][iy], box):
        #             return False

        # return True 
        
        # Cleanr and faster implementation
        # row_map = [set() for _ in range(9)]
        # col_map = [set() for _ in range(9)]
        # box_map = [set() for _ in range(9)]
        # m, n = len(board), len(board[0])
        # for i in range(m):
        #     for j in range(n):
        #         cur = board[i][j]
        #         bi = 3 * (i // 3) + j // 3
        #         if cur != ".":
        #             if cur in row_map[i] or cur in col_map[j] or cur in box_map[bi]:
        #                 return False
        #             row_map[i].add(cur)
        #             col_map[j].add(cur)
        #             box_map[bi].add(cur)
        # return True                  

        return (self.is_row_valid(board) and
                self.is_col_valid(board) and
                self.is_square_valid(board))

    # More readable
    def is_row_valid(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True

    def is_col_valid(self, board):
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False
        return True
        
    def is_square_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_unit_valid(square):
                    return False
        return True
        
    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)
# @lc code=end

