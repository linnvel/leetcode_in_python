#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(candidates, results, candidate, startIndex, remainingTarget):
            if remainingTarget == 0:
                results.append(candidate[:])
                return
            for i in range(startIndex, len(candidates)):
                if remainingTarget < candidates[i]:
                    break
                if i != startIndex and candidates[i - 1] == candidates[i]:
                    continue
                helper(candidates, results, candidate + [candidates[i]], 
                i + 1,
                remainingTarget - candidates[i]) 

        results = []
        candidate = []
        candidates.sort()
        helper(candidates, results, candidate, 0, target)
        return results
# @lc code=end

