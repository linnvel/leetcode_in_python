#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_LIMIT = 2 ** 31 - 1
        MIN_LIMIT = -2 ** 31
        if divisor == 1:
            return dividend
        if divisor == -1:
            return MAX_LIMIT if dividend == MIN_LIMIT else -dividend
        
        # sign = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        sign = (dividend > 0) is (divisor > 0)
        dividend = - dividend if dividend > 0 else dividend
        divisor = -divisor if divisor > 0 else divisor
        i = 0
        while dividend <= divisor:
            cusum = divisor
            j = 1
            while cusum >= dividend - cusum:
                cusum += cusum
                if j >= MAX_LIMIT - j:
                    j = MAX_LIMIT
                    break
                j += j
            if i >= MAX_LIMIT - j:
                i = MAX_LIMIT
                break
            i += j
            dividend -= cusum
        return i if sign else -i
        
# @lc code=end

