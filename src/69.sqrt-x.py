#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:

        # Solution 1: Binary search
        if x < 0:
            return None
        lo, hi = 0, int(x)
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if mid ** 2 <= x:
                lo = mid
            else:
                hi = mid
        return hi if hi ** 2 <= x else lo

        # 
        
# @lc code=end

