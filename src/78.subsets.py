#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return nums
        
        def helper(nums, results, curIndex, cur):
            results.append(cur[:])
            for i in range(curIndex, len(nums)):
                helper(nums, results, i + 1, cur + [nums[i]])
        
        results = []
        cur = []
        helper(nums, results, 0, cur)
        return results
        
# @lc code=end

