# @lintcode
#
# 587. Two Sum - Unique Pairs
#
# https://www.lintcode.com/problem/587/
#

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        nums.sort()
        l, r = 0, len(nums) - 1
        ans = 0
        while l < r:
            curSum = nums[l] + nums[r]
            if curSum == target:
                ans += 1
                l += 1
                r -= 1
                # 注意：先two pointers再去重
                # 反例：[1,2,2,3] target=4
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
                while nums[r] == nums[r + 1] and l < r:
                    r -= 1
            elif curSum < target:
                l += 1
            else:
                r -= 1
        return ans