#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
from unittest import result


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Solution 1: DFS (Accepted?! LOL)
        # wordDict = set(wordDict)
        # def dfs(startIndex, current, results):
        #     if startIndex == len(s):
        #         results.append(" ".join(current))
        #     for i in range(startIndex, len(s)):
        #         if s[startIndex:i + 1] in wordDict:
        #             dfs(i + 1, current + [s[startIndex:i + 1]], results )
        
        # results = []
        # dfs(0, [], results)
        # return results

        # Solution 2: DFS + memorization???
        memo = {}
        wordDict = set(wordDict)
        def dfs(startIndex, current, results):
            if startIndex == len(s):
                results.append(" ".join(current))
            for i in range(startIndex, len(s)):
                if s[startIndex:i + 1] in wordDict:
                    dfs(i + 1, current + [s[startIndex:i + 1]], results )
        
        results = []
        dfs(0, [], results)
        return results
        
# @lc code=end

