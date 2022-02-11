#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:        
        
        # First implementation
        def helper1(candidates, results, cur, curIndex, curSum):
            if curSum == target:
                results.append(cur[:])
                return
            if curSum > target:
                return
            for i in range(curIndex, len(candidates)):
                # if curSum + candidates[i] > target:
                #     break
                helper1(candidates, results, cur + [candidates[i]], 
                i,
                curSum + candidates[i])
        
        # Second implementation (faster)
        # 1. sort + break <-- return
        # 2. remainingTarget <-- curSum
        def helper2(candidates, results, candidate, startIndex, remainingTarget):
            if remainingTarget == 0:
                results.append(candidate[:])
                return
            for i in range(startIndex, len(candidates)):
                if remainingTarget < candidates[i]:
                    break
                helper2(candidates, results, candidate + [candidates[i]], 
                i,
                remainingTarget - candidates[i]) 

        results = []
        candidate = []
        candidates.sort()
        helper2(candidates, results, candidate, 0, target)
        return results
# @lc code=end

