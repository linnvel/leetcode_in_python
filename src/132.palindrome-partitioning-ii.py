#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#

# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        def getPalindrome(s):
            n = len(s)
            isPalindrome = [[False for _ in range(n)] for _ in range(n)]
            for i in range(n):
                isPalindrome[i][i] = True
                if i < n - 1:
                    isPalindrome[i][i + 1] = (s[i] == s[i + 1])
            for j in range(2, n):
                for i in range(j - 1):
                    isPalindrome[i][j] = isPalindrome[i + 1][j - 1] and (s[i] == s[j])
            return isPalindrome

        global isPalindrome
        isPalindrome = getPalindrome(s)

        # Solution 1: DFS
        # def dfs(s, startIndex, curCut):
        #     global isPalindrome
        #     if startIndex == len(s):
        #         return curCut
        #     minCut = float('inf')
        #     for i in range(startIndex, len(s)):
        #         if isPalindrome[startIndex][i]:
        #             minCut = min(minCut, dfs(s, i + 1, curCut + 1 if i < len(s) - 1 else curCut))
        #     return minCut

        # return dfs(s, 0, 0)

        # Solution 2: DP
        dp = [float('inf')] * len(s)
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome[i][j]:
                    dp[i] = dp[i - 1]




        
        
        
# @lc code=end

