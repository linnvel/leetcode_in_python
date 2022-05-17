#
# @lc app=leetcode id=1049 lang=python3
#
# [1049] Last Stone Weight II
#

# @lc code=start
from tracemalloc import start


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Optimum case: divide stones into two parts so that both parts have the same sum of weights
        
        # # Solution 0: Brute force
        # # global mindiff
        # # mindiff = float('inf')
        # # def dfs(stones, startIndex, set1, set2):
        # #     global mindiff
        # #     if startIndex == len(stones):
        # #         mindiff = min(mindiff, abs(sum(set1) - sum(set2)))
        # #         return
        # #     dfs(stones, startIndex + 1, set1 + [stones[startIndex]], set2)
        # #     dfs(stones, startIndex + 1, set1, set2 + [stones[startIndex]])

        # # set1, set2 = [], []
        # # dfs(stones, 0, set1, set2)
        # # return mindiff
            
        # # Better implementation
        # def dfs(stones, index, sum1, sum2):
        #     if index == len(stones):
        #         return abs(sum1 - sum2)
        #     diff1 = dfs(stones, index + 1, sum1 + stones[index], sum2)
        #     diff2 = dfs(stones, index + 1, sum1, sum2 + stones[index])
        #     return min(diff1, diff2)

        # return dfs(stones, 0, 0, 0)
        
        # # Solution 1: DFS + memorization
        # def dfs(stones, index, sum1, sum2):
        #     global cache
        #     if index == len(stones):
        #         return abs(sum1 - sum2)
        #     key = min(sum1, sum2)
        #     if key not in cache[index]:
        #         diff1 = dfs(stones, index + 1, sum1 + stones[index], sum2)
        #         diff2 = dfs(stones, index + 1, sum1, sum2 + stones[index])
        #         cache[index][key] = min(diff1, diff2)
        #     return cache[index][key]
        
        # global cache
        # cache = [{} for _ in range(len(stones))]
        # return dfs(stones, 0, 0, 0)

        # Solution 2: DP (0-1 Knapsack)
        # bag capacity = sum(stones) // 2
        # weights = stones, values = stones
        # dp[j]: the maximum possible sum of values in the bag with capacity of j

        capacity = sum(stones) // 2
        dp = [0] * (capacity + 1)
        for i in range(len(stones)):
            for j in range(capacity, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i] )
        return abs(sum(stones) - 2 * dp[capacity] )

        

        
# @lc code=end

