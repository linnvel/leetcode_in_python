#
# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#

# @lc code=start
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        m = 10 ** 9 + 7
        n = len(arr)
        left = [1] * n
        right = [1] * n
        stack = []  # monotonous stack which saves (arr[i], left/right[i])
        for i in range(n):
            while stack and arr[i] <= stack[-1][0]:
                left[i] += stack.pop()[1]
            stack.append((arr[i], left[i]))
        print(left)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[i] < stack[-1][0]:
                right[i] += stack.pop()[1]
            stack.append((arr[i], right[i]))
        print(right)
        result = sum( a * l * r for a, l, r in zip(arr, left, right)) 
        return result % m


# @lc code=end

