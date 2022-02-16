#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        m = len(board)
        n = len(board[0])
        deltaX = [-1, 0, 0, 1]
        deltaY = [0, 1, -1, 0]

        # def helper(cur, seen, x, y):
        #     if x < 0 or y < 0 or x >= m or y >=n or seen[x][y] or board[x][y] != word[len(cur)]:
        #         return False
        #     cur += board[x][y]
        #     seen[x][y] = True
        #     if len(cur) == len(word):
        #         return True   
        #     for k in range(4):
        #         newx = x + deltaX[k]
        #         newy = y + deltaY[k]
        #         if helper(cur, seen, newx, newy):
        #             return True
        #     cur = cur[:-1]
        #     seen[x][y] = False
        #     return False
        
        # for i in range(m):
        #     for j in range(n):
        #         cur = ""
        #         seen = [[False for _ in range(n)] for _ in range(m)]
        #         if helper(cur, seen, i, j):
        #             return True

        # optimize memory
        def helper(count, x, y):
            if x < 0 or y < 0 or x >= m or y >=n or board[x][y] != word[count]:
                return False
            tmp = board[x][y]
            board[x][y] = ""
            if count == len(word) - 1:
                return True   
            for k in range(4):
                newx = x + deltaX[k]
                newy = y + deltaY[k]
                if helper(count + 1, newx, newy):
                    return True
            board[x][y] = tmp
            return False
        
        for i in range(m):
            for j in range(n):
                if helper(0, i, j):
                    return True

        return False

        
# @lc code=end

