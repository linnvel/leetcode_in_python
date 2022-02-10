#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return nums
        nums.sort()
        def helper(nums, results, curIndex, cur):
            results.append(cur[:])
            for i in range(curIndex, len(nums)):
                if i > curIndex and nums[i - 1] == nums[i]:
                    continue
                helper(nums, results, i + 1, cur + [nums[i]])
        
        results = []
        cur = []
        helper(nums, results, 0, cur)
        return results
        
# @lc code=end

