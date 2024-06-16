#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        ans = 0
        while r < len(nums):
            cur = nums[r]
            if cur == 0 and k > 0:
                k -= 1
            elif cur == 0:
                while nums[l] == 1:
                    l += 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1    
        return ans


        
# @lc code=end

