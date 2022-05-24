#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # # Solution 1: DFS (Time Limit Exceeded)
        # # Time: O(2^n), n = len(s), break or not
        # # Space: O(n), n decisions
        # def helper(s, wordDict, startIndex):
        #     if startIndex == len(s):
        #         return True
        #     for i in range(startIndex, len(s)):
        #         if s[startIndex: i + 1] in wordDict and helper(s, wordDict, i + 1):
        #             return True
        #     return False

        # return helper(s, wordDict, 0)

        # # Solution 2: DFS with memorization
        # # key: startIndex, value: T/F
        # def helper(s, wordDict, startIndex):
        #     if startIndex == len(s):
        #         return True
        #     global memo
        #     if startIndex not in memo:
        #         for i in range(startIndex, len(s)):
        #             if s[startIndex: i + 1] in wordDict and helper(s, wordDict, i + 1):
        #                 memo[startIndex] = True
        #                 break
        #         if startIndex not in memo:
        #             memo[startIndex] = False
        #     return memo[startIndex]
        
        # global memo
        # memo = {}
        # return helper(s, wordDict, 0)

        # Solution 3: DP
        # dp[j] = True if s[:j] can be segmented into words in wordDict
        n = len(s)
        dp = [True] + [False] * n

        # words = set(wordDict) # speed up search        
        # maxLen = max([len(w) for w in words])
        # for i in range(n + 1):
        #     for j in range(i + 1, min(i + maxLen + 1, n + 1)):
        #         dp[j] = dp[j] or (dp[i] and (s[i: j] in words))

        # This is faster:
        # for j in range(n + 1):
        #     for i in range(max(j - maxLen, 0), j):
        #         dp[j] = dp[i] and (s[i: j] in words)
        #         if dp[j]:
        #             break

        # Even faster:
        for j in range(n + 1):
            for word in wordDict:
                if( j >= len(word) and dp[j - len(word)] and s[j - len(word): j] == word):
                    dp[j] = True
                    break

        return dp[n]


# @lc code=end

