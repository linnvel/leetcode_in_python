#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        minDiff = float('inf')
        ans = None
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                diff = abs(curSum - target)
                if diff < minDiff:
                    minDiff = diff
                    ans = curSum
                if curSum == target:
                    return ans
                elif curSum > target:
                    r -= 1
                else:
                    l += 1
        return ans
        
# @lc code=end

