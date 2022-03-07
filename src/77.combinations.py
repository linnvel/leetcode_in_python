#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        cur = []

        def helper(n, k, cur, results, startNum):
            if len(cur) == k:
                results.append(cur[:])
                return
            for i in range(startNum, n + 1):
                helper(n, k, cur + [i], results, i + 1)
        
        helper(n, k , cur, results, 1)
        return results
        
# @lc code=end

