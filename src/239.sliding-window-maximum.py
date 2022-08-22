#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from queue import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # # Solution 1: Brute force (TLE)
        # results = []
        # for i in range(len(nums) - k + 1):
        #     results.append(max(nums[i:i+k]))
        # return results

        # # Solution 2: deque
        # def clean_queue(i):           
        #     if deq and deq[0] <= i - k:
        #         deq.popleft()
        #     while deq and nums[deq[-1]] < nums[i]:
        #         deq.pop()

        # results = []
        # deq = deque()
        # max_index = 0
        # for i in range(k):
        #     clean_queue(i)
        #     deq.append(i)
        #     if nums[i] > nums[max_index]:
        #         max_index = i
        # results.append(nums[max_index])

        # for i in range(k, len(nums)):
        #     clean_queue(i)
        #     deq.append(i)
        #     results.append(nums[deq[0]])
        # return results

        # Solution 3: DP
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        left = [0] * n
        right = [0] * n
        for i in range(n):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
        for i in range(n - 1, -1, -1):
            if i == n - 1 or (i + 1) % k == 0:
                right[i] = nums[i]
            else:
                right[i] = max(right[i + 1], nums[i])
        results = []
        for i in range(n - k + 1):
            results.append(max(right[i], left[i + k - 1]))
        
        return results


# @lc code=end

