#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Solution 1
        # output = 0
        # curMin = prices[0]
        # for price in prices[1:]:
        #     output = max(output, price - curMin)
        #     curMin = min(curMin, price)
        # return output
        
        # Solution 2
        l, r = 0, 1
        output = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                output = max(output, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return output
# @lc code=end

