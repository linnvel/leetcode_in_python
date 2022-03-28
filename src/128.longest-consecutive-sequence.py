#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        maxLen = 0
        for num in nums:
            if num - 1 not in hashset:
                curNum = num
                count = 1
                while curNum + 1 in hashset:
                    count += 1
                    curNum += 1
                maxLen = max(maxLen, count)
        return maxLen

        
# @lc code=end

