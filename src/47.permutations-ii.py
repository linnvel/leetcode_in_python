#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return nums
        
        def helper(nums, results, seen, cur):
            if len(cur) == len(nums):
                results.append(cur[:])
                return
            for i in range(len(nums)):
                if seen[i] or (i > 0 and nums[i] == nums[i - 1] and not seen[i - 1]):
                    continue
                seen[i] = True
                cur.append(nums[i])
                helper(nums, results, seen, cur)
                seen[i] = False
                cur.pop()
        
        nums.sort()
        results = []
        cur = []
        seen = [False for _ in range(len(nums))]
        helper(nums, results, seen, cur)
        return results

        
# @lc code=end

