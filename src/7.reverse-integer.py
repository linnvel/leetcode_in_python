#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
from math import ceil

class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        # # solution 1
        # sign = 1 if x >= 0 else -1
        # x = abs(x)
        # ans = 0
        # while x != 0:
        #     x, pop = x // 10, x % 10
        #     ans = 10 * ans + pop
        # ans = sign * ans
        # return ans if MIN_INT <= ans <= MAX_INT else 0

        # # solution 2: overflow check before storing new int
        # # Note: // and % work differently for negative int in python
        # ans = 0
        # while x != 0:
        #     if x > 0:
        #         x, pop = x // 10, x % 10
        #         if ans > MAX_INT // 10 or (ans == MAX_INT // 10 and pop > 7):
        #             return 0
        #     else:   
        #         x, pop = ceil(x / 10), -(-x % 10)
        #         if ans < ceil(MIN_INT / 10) or (ans == MIN_INT // 10 and pop < -8 ):
        #             return 0
        #     ans = ans * 10 + pop
        # return ans
        
        # Solution 3: str
        sign = 1 if x >= 0 else -1
        x = str(abs(x))
        ans = int(x[::-1]) * sign
        return ans if MIN_INT <= ans <= MAX_INT else 0

# @lc code=end

