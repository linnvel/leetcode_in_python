#
# @lc app=leetcode id=611 lang=python3
#
# [611] Valid Triangle Number
#

# @lc code=start
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ans = 0
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                curSum = nums[l] + nums[r]
                if curSum > nums[i]:
                    ans += r - l
                    l += 1
                else:
                    r -= 1
        return ans
        
# @lc code=end

