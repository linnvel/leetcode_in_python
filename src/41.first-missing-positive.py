#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # # Solution 1:
        # n = len(nums)
        # for i in range(n):
        #     if nums[i] > n or nums[i] <= 0:
        #         continue
        #     while nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
        #         tmp = nums[i]
        #         nums[i], nums[tmp - 1] = nums[tmp - 1], nums[i]
        #         if nums[i] > n or nums[i] <= 0:
        #             break
        # for i in range(n):
        #     if nums[i] != i + 1:
        #         return i + 1
        # return n + 1

        # Smarter and cleaner solution:
        nums.append(0)  # trick 1: append 0
        n = len(nums)
        
        # note n is one larger than actual length of nums
        # the first missing positive must be in range [1,...,n-1]
        # so remove useless values 
        for i in range(n):
            if nums[i] >= n or nums[i] < 0:  # trick 2: >= n, not > n
                nums[i] = 0
        
        # use the index as the hash to record the frequency of each number
        for i in range(n):
            nums[nums[i] % n] += n
        print(nums)
        for i in range(1, n):  # trick 3: start from 1
            if nums[i] // n == 0:
                return i
        return n
        
# @lc code=end

