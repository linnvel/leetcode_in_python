#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(n):
            result = 0
            while n > 0:
                result += (n % 10) ** 2
                n = n // 10
            return result
        # # Solution 1: hashmap        
        # res_set = set()
        
        # while 1:
        #     result = helper(n)    
        #     if result == 1:
        #         return True
        #     elif result in res_set:
        #         return False
        #     else:
        #         res_set.add(result)
        #         n = result

        # Solution 2: find circle in the link
        next_result = helper(n)
        next_next_result = helper(next_result)
        while next_next_result != 1 and next_result != next_next_result:
            next_result = helper(next_result)
            next_next_result = helper(helper(next_next_result))
        return next_next_result == 1

        
# @lc code=end

