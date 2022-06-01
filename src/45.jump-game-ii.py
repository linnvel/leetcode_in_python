#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        # # Solution 1: DP (TLE)
        # # dp[i]: minimum jumps to reach index i
        # dp = [0] + [float('inf')] * (len(nums) - 1)
        # for j in range(1, len(nums)):
        #     for i in range(j):
        #         if nums[i] >= j - i:
        #             dp[j] = min(dp[j], 1 + dp[i])
        # return dp[len(nums) - 1] 

        # # Solution 2: BFS (TLE)
        # adjacent = {}
        # for i in range(len(nums) - 1):
        #     adjacent[i] = [j for j in range(i + 1, i + nums[i] + 1)]
        
        # from queue import Queue
        # queue = Queue()
        # queue.put(0)
        # minLen = 0
        # while queue.qsize():
        #     qsize = queue.qsize()
        #     for i in range(qsize):
        #         cur = queue.get()
        #         if cur == len(nums) - 1:
        #             return minLen
        #         for neighbor in adjacent[cur]:
        #             queue.put(neighbor)
        #     minLen += 1
        # return -1

        # Solution 3: BFS -> Greedy
        end = 0
        step = 0
        maxend = end
        for i in range(len(nums)):
            if end >= len(nums) - 1:
                return step
            maxend = max(maxend, i + nums[i])
            if i >= end:
                step += 1
                end = maxend
        return -1



# @lc code=end

