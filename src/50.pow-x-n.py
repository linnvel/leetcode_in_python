#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # # Solution 0: dirty iteration
        # if n < 0:
        #     x = 1/x
        #     n = -n
        # i = 1
        # ans = 1
        # tmp = x
        # while n > 0:
        #     if i * 2 < n - 1:
        #         tmp *= tmp
        #         i *= 2
        #     else:
        #         n -= i
        #         i = 1
        #         ans *= tmp
        #         tmp = x
        # return ans

        # # Solution 1: brute force
        # if n < 0:
        #     x = 1/x
        #     n = -n
        # ans = 1
        # while n > 0:
        #     ans *= x
        #     n -= 1
        # return ans

        # # Solution 2: recursion
        # if n == 0:
        #     return 1
        # if n < 0:
        #     n = -n
        #     x = 1/x
        # n, res = n // 2, n % 2
        # tmp = self.myPow(x, n)
        # return tmp * tmp if res == 0 else tmp * tmp * x

        # Solution 3: iteration
        if n < 0:
            x = 1/x
            n = -n
        i = 1
        ans = 1
        cur = x
        while n > 0:
            if n % 2 == 1:
                ans *= cur
            cur *= cur
            n = n // 2
        return ans

        
# @lc code=end

