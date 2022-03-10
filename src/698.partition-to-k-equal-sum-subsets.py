#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#

# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        ## todo: not accepted
        if sum(nums) % k != 0:
            return False
        targetSum = sum(nums) // k
        nums.sort(reverse=True)
        if nums[0] > targetSum:
            return False
    
        # # Solution 1: dfs (Time Limit Exceeded)
        # seen = [0 for _ in range(len(nums))]
        # def helper(i, k, curSum):
        #     if k == 0:
        #         return True
        #     elif curSum == 0:
        #         return helper(0, k - 1, targetSum) # already find a subset: k -= 1, start from begining
        #     for j in range(i, len(nums)):
        #         if seen[j] == 1 or curSum < nums[j]:
        #             continue
        #         seen[j] = 1
        #         if helper(j + 1, k, curSum - nums[j]): # not complete current subset: k keeps same, start from j + 1
        #             return True
        #         else:
        #             seen[j] = 0 # can't find valid subset, backtracking
        #     return False
        
        # return helper(0, k, targetSum)     

        dp = [0 for _ in range(k)]

        def helper(i):
            # print(i, dp)
            if i == len(nums):
                return len(set(dp)) == 1
            for j in range(k):
                dp[j] += nums[i]
                if dp[j] <= targetSum and helper(i + 1):
                    return True
                dp[j] -= nums[i]
                if dp[j] == 0:
                    # print("break", i, j, dp)
                    break  # soul of the solution: while trackbacking, if dp[j] == 0, will not try other buckets
            return False

        return helper(0) 
# @lc code=end

