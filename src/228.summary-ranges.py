#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return nums
        ranges = []
        start = nums[0]
        for i in range(1, len(nums) + 1):
            if i < len(nums) and nums[i] == nums[i-1] + 1:
                continue
            else:
                res = str(start)
                if nums[i-1] == start:
                    ranges.append(res)
                else:
                    ranges.append(res + "->" + str(nums[i-1]))
                if i < len(nums): 
                    start = nums[i]
        return ranges
        
# @lc code=end

