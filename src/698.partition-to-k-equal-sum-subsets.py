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

        def helper(curSum, seen):
            print(curSum, seen)
            if curSum == 0:
                return True
            for i in range(len(nums)):
                if seen[i] == 1 or curSum < nums[i]:
                    continue
                seen[i] = 1
                if helper(curSum - nums[i], seen):
                    if sum(seen) == len(nums):
                        return True
                    else:
                        return helper(targetSum, seen)
                else:
                    seen[i] = 0
                    return False
        
        seen = [0 for _ in range(len(nums))]
        return helper(targetSum, seen)     
        
# @lc code=end

