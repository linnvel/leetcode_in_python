#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # if not obstacleGrid:
        #     return 0
        # m, n = len(obstacleGrid), len(obstacleGrid[0])
        # # dp = [1 - obstacleGrid[0][j] for j in range(n)]
        # # for j in range(1, n):
        # #     dp[j] = (1 - obstacleGrid[0][j]) * dp[j - 1]

        # dp = [0 for _ in range(n)]
        # for j in range(n):
        #     if obstacleGrid[0][j] == 1:
        #         break
        #     dp[j] = 1

        # for i in range(1, m):
        #     for j in range(n):
        #         if j == 0:
        #             dp[j] = dp[j] * (1 - obstacleGrid[i][0])
        #         else:
        #             if obstacleGrid[i][j] == 0:
        #                 dp[j] += dp[j - 1]
        #             else:
        #                 dp[j] = 0
        # return dp[n - 1]

        # Another implementation: update in-place
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid[0][0] = 1
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j - 1] != 0 and obstacleGrid[0][j] != 1)
        for i in range(1, m):
            obstacleGrid[i][0] = int(obstacleGrid[i - 1][0] != 0 and obstacleGrid[i][0] != 1)
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        return obstacleGrid[m - 1][n - 1]

# @lc code=end

