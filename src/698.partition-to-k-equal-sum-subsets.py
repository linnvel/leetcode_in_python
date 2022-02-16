#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#

# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        targetSum = sum(nums) // k

        def helper(indices, curSum):
            if len(indices) == 0:
                return True
            for i in indices:
                if curSum < nums[i]:
                    return False
                indices.pop(i)
                if curSum == nums[i]:
                    result = helper(indices, targetSum)
                else:
                    result = helper(indices, curSum - nums[i])
                



                

            
        
# @lc code=end

