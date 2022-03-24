#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Solution 1: two pointers
        l, r = 0, len(numbers) - 1
        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum == target:
                return [l + 1, r + 1]
            elif curSum < target:
                l += 1
            else:
                r -= 1

        # Solution 2: hashset
        hashset = {}
        for i, num in enumerate(numbers): 
            value = target - num
            if value in hashset:
                return [hashset[value] + 1, i + 1]
            elif value < numbers[0]:
                break
            else:
                hashset[num] = i
        return []

        
# @lc code=end

