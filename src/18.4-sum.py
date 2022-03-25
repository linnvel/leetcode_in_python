#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # # Solution 1
        # nums.sort()
        # results = []
        # for i in range(len(nums) - 3):
        #     if i > 0 and nums[i - 1] == nums[i]:
        #         continue
        #     for j in range(i + 1, len(nums) - 2):
        #         if j > i + 1 and nums[j - 1] == nums[j]:
        #             continue
        #         l, r = j + 1, len(nums) - 1
        #         while l < r:
        #             curSum = nums[i] + nums[j] + nums[l] + nums[r]
        #             if curSum == target:
        #                 results.append([nums[i], nums[j], nums[l], nums[r]])
        #                 l += 1
        #                 r -= 1
        #                 while l < r and nums[l] == nums[l - 1]:
        #                     l += 1
        #                 while l < r and nums[r] == nums[r + 1]:
        #                     r -= 1
        #             elif curSum < target:
        #                 l += 1
        #             else:
        #                 r -= 1
        # return results

        # # Solution 2: general KSum solution
        # def kSum(nums, start, k, target):
        #     ans = []
        #     if k == 2:
        #         l, r = start, len(nums) - 1
        #         while l < r:
        #             curSum = nums[l] + nums[r]
        #             if curSum == target:
        #                 ans.append([nums[l], nums[r]])
        #                 l += 1
        #                 r -= 1
        #                 while l < r and nums[l] == nums[l - 1]:
        #                     l += 1
        #                 while l < r and nums[r] == nums[r + 1]:
        #                     r -= 1
        #             elif curSum < target:
        #                 l += 1
        #             else:
        #                 r -= 1
        #     else:
        #         for i in range(start, len(nums) - k + 1):
        #             if i > start and nums[i - 1] == nums[i]:
        #                 continue
        #             results = kSum(nums, i + 1, k - 1, target - nums[i])
        #             for result in results:
        #                 ans.append([nums[i]] + result)
        #     return ans
        
        # nums.sort()
        # return kSum(nums, 0, 4, target)                
    
        # Solution 2: time and space optimization
        def kSum(nums, start, k, target, result, results):
            if k == 2:
                l, r = start, len(nums) - 1
                while l < r:
                    curSum = nums[l] + nums[r]
                    if curSum == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif curSum < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(start, len(nums) - k + 1):
                    if nums[i] * k > target or nums[-1] * k < target: # take advantage of sorted list
                        break
                    if i ==0 or nums[i - 1] != nums[i]:
                        kSum(nums, i + 1, k - 1, target - nums[i], result + [nums[i]], results)
        
        nums.sort()
        results = []
        kSum(nums, 0, 4, target, [], results)                
        return results                
        
# @lc code=end

