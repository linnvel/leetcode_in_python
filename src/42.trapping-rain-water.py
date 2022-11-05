#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # # Solution 1: brute force(TLE)
        # n = len(height)
        # ans = 0
        # for i in range(n):
        #     left_max = max(height[:i + 1])
        #     right_max = max(height[i:])
        #     ans += (min(left_max, right_max) - height[i])
        # return ans

        # # Solution 2: DP
        # left_max = height.copy()
        # right_max = height.copy()
        # n = len(height)
        # ans = 0
        # for i in range(1, n):
        #     left_max[i] = max(left_max[i - 1], left_max[i])
        #     right_max[n - i - 1] = max(right_max[n - i], right_max[n - i - 1])

        # for i in range(n):
        #     ans += (min(left_max[i], right_max[i]) - height[i])
        # return ans
        
        # Solution 3: DP space optimization with sliding array
        # left_max: left to right iterate => l
        # right_max: right to left iterate => r
        # min(left_max[i], right_max[i]) => 
        # two pointers: if left_max < right_max: l += 1 else: r -= 1
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        ans = 0
        while l < r:
            if left_max < right_max:
                ans += (left_max - height[l])
                l += 1
                left_max = max(left_max, height[l])
            else:
                ans += (right_max - height[r])
                r -= 1
                right_max = max(right_max, height[r])
        return ans
            
# @lc code=end

