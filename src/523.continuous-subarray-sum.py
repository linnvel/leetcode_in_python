#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # # Solution 1: Time Limit Exceeded
        # prefix = [0]
        # for num in nums:
        #     cur = prefix[-1] + num
        #     prefix.append(cur)
        #     for pre in prefix[:-2]:
        #         if (cur - pre) % k == 0:
        #             return True
        # return False

        # Solution 2: prefixSum --> prefixRemainder
        # if the current prefixRemainder already exists, return True
        # Time: O(n), Space: O(k)
        prefix = {0: -1}
        remainder = 0
        for i, num in enumerate(nums):
            remainder = (remainder + num) % k
            if remainder in prefix:
                if prefix[remainder] < i - 1:
                    return True
            else:
                prefix[remainder] = i
        return False
        
# @lc code=end

