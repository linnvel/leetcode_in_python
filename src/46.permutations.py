#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return nums
        
        def helper(nums, results, seen, cur):
            if len(cur) == len(nums):
                results.append(cur[:])
                return
            for i in range(len(nums)):
                if seen[i]:
                    continue
                seen[i] = True
                cur.append(nums[i])
                helper(nums, results, seen, cur)
                seen[i] = False
                cur.pop()
        
        results = []
        cur = []
        seen = [False for _ in range(len(nums))]
        helper(nums, results, seen, cur)
        return results

# @lc code=end

