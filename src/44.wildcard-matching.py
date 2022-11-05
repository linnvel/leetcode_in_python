#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # # Solution 1: DFS (TLE)
        # if not p:
        #     return not s
        
        # if p[0] == "*":
        #     return self.isMatch(s, p[1:]) or (s and self.isMatch(s[1:], p))
        # else:
        #     return s and (p[0] == "?" or p[0] == s[0]) and self.isMatch(s[1:], p[1:])

        # # Solution 2: DFS with memorization
        # memo = {}
        # m = len(s)
        # n = len(p)
        # def dfs(i, j):
        #     if j == n:
        #         return i == m
        #     if (i, j) not in memo:
        #         if p[j] == "*":
        #             memo[(i, j)] = dfs(i, j + 1) or (i < m and dfs(i + 1, j))
        #         else:
        #             memo[(i, j)] = i < m and p[j] in ("?", s[i]) and dfs(i + 1, j + 1)
        #     return memo[(i, j)]
        
        # return dfs(0, 0)

        # # Solution 2: cleaner code
        # m = len(s)
        # n = len(p)

        # # https://www.geeksforgeeks.org/python-functools-lru_cache/
        # # def _lru_cache_wrapper(user_function, maxsize, typed, _CacheInfo)
        # @lru_cache(None) 
        # def dfs(i, j):
        #     if j == n:
        #         return i == m
        #     if p[j] == "*":
        #         return dfs(i, j + 1) or (i < m and dfs(i + 1, j))
        #     elif i < m and p[j] in ("?", s[i]):
        #         return dfs(i + 1, j + 1)
        #     return False
        
        # return dfs(0, 0)

        # # Solution 3: DP
        # # dp[i][j] = s[n - i : ] match with p[m - j: ]
        # # initialization:
        # # dp[0][0] = 1, dp[i][0] = 0
        # # dp[i][j] = dp[i - 1][j] or dp[i][j - 1] = max(dp[i - 1][j], dp[i][j - 1]) if dp[j] == "*"
        # #            first_match and dp[i - 1][j - 1] otherwise
        # # first_match = p[j] == '?' or s[i] == p[j]

        # m, n = len(s), len(p)
        # dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        # dp[0][0] = True
        # for j in range(1, n + 1):
        #     if p[j - 1] == "*":
        #         dp[0][j] = True
        #     else:
        #         break
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         if p[j - 1] == "*":
        #             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        #         else:
        #             dp[i][j] = p[j - 1] in (s[i - 1], "?") and dp[i - 1][j - 1]
        # return dp[m][n]

        # Solution 4: DP space optimization
        m, n = len(s), len(p)
        dp = [False for _ in range(n + 1)]
        dp[0] = True
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[j] = True
            else:
                break
        for i in range(1, m + 1):
            prev = i == 1
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[j] = max(dp[j], dp[j - 1])
                else:
                    dp[j] = p[j - 1] in (s[i - 1], "?") and prev
                prev = dp[j]
        return dp[n]


# @lc code=end

