#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return nums
        
        # backtracking implemtation
        # nums = [1, 2, 3]
        # output = [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]
        
        def helper(nums, results, curIndex, cur):
            results.append(cur[:])
            for i in range(curIndex, len(nums)):
                helper(nums, results, i + 1, cur + [nums[i]])
        
        results = []
        cur = []
        helper(nums, results, 0, cur)
        return results

        # # dfs implementation
        # nums = [1, 2, 3]
        # output = [[1,2,3],[1,2],[1,3],[1],[2,3],[2],[3],[]]

        # def dfs(nums, index, cur, results):
        #     if index == len(nums):
        #         results.append(cur[:])
        #         return
        #     # two possible decisions in each node index
        #     dfs(nums, index + 1, cur + [nums[index]], results)
        #     dfs(nums, index + 1, cur, results)
        
        # results = []
        # dfs(nums, 0, [], results)
        # return results

        
# @lc code=end

