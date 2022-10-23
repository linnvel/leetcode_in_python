#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_amount = 0
        while l < r:
            amount = (r - l) * min(height[l], height[r])
            max_amount = max(max_amount, amount)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_amount
        
# @lc code=end

