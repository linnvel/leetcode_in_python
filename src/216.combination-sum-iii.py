#
# @lc app=leetcode id=216 lang=python
#
# [216] Combination Sum III
#

# @lc code=start
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def helper(results, result, startNumber, remainSum):
            if remainSum == 0 and len(result) == k:
                results.append(result[:])
                return
            if len(result) > k:
                return
            for num in range(startNumber, 10):
                if remainSum < num:
                    break
                helper(results, result + [num], num + 1, remainSum - num)
        
        if n > (19 - k) * k /2:
            return []
        result = []
        results = []
        helper(results, result, 1, n)
        return results
        
# @lc code=end

