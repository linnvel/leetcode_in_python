#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums, i, j, target):
            results = []
            while i < j:
                curSum = nums[i] + nums[j]
                if curSum == target:
                    results.append([nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                elif curSum < target:
                    i += 1
                else:
                    j -= 1
            return results
        
        nums.sort()
        n = len(nums)
        results = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            pairs = twoSum(nums, i + 1, n - 1, -nums[i])
            for pair in pairs:
                results.append([nums[i]] + pair)
        return results

        
# @lc code=end

