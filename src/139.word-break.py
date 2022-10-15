#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # # Solution 1: DFS (TLE)
        # wordDict = set(wordDict)
        # def dfs(word):
        #     if word in wordDict:
        #         return True
        #     for i in range(1, len(word)):
        #         prefix = word[:i]
        #         suffix = word[i:]
        #         if prefix in wordDict and suffix in wordDict:
        #             return True
        #         elif prefix in wordDict and dfs(suffix):
        #             return True
        #     return False
        
        # return dfs(s)

        # # Solution 2: DFS with memorization
        # wordDict = set(wordDict)
        # memo = {}
        # def dfs(word):
        #     if word in memo:
        #         return memo[word]

        #     if word in wordDict:
        #         memo[word] = True
        #         return True
            
        #     memo[word] = False
        #     for i in range(1, len(word)):
        #         prefix = word[:i]
        #         suffix = word[i:]
        #         if prefix in wordDict and suffix in wordDict:
        #             memo[word] = True
        #             break
        #         elif prefix in wordDict and dfs(suffix):
        #             memo[word] = True
        #             break
        #     return memo[word]  
        # return dfs(s)

        # Solution 3: DP
        # dp[i] = s[:i+1] exists in wordDict or not
        wordDict = set(wordDict)
        dp = [False] * len(s)
        for i in range(len(s)):
            if s[: i + 1] in wordDict:
                dp[i] = True
                continue
            for j in range(i):
                dp[i] = dp[j] and s[j + 1 : i + 1] in wordDict
                if dp[i]:
                    break
        return dp[-1]    


# @lc code=end

