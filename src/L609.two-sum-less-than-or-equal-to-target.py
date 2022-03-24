# @lintcode
#
# 609. Two Sum - Less than or equal to target
#
# https://www.lintcode.com/problem/609/
#

class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        nums.sort()
        l, r = 0, len(nums) - 1
        ans = 0
        while l < r:
            curSum = nums[l] + nums[r]
            if curSum > target:
                r -= 1
            else:
                ans += r - l
                l += 1
        return ans
