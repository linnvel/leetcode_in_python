#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Solution 0: brute force
        # Time:O(nk)
        
        # # Solution 1: heap (TLE)
        # import heapq
        # result = []
        # l = 0
        # nums = [-num for num in nums]
        # for r in range(k, len(nums) + 1):
        #     heap = nums[l:r]
        #     heapq.heapify(heap)    
        #     result.append(-heap[0])
        #     l += 1
        # return result

        # Solution 2: optimized heap
        # time: O(nlogk)
        # space: O(k)
        # worst case: nums = [1, 2, 3, 4, 5, 6]
        import heapq
        result = []
        l = 0
        nums = [(-num, i) for i, num in enumerate(nums)]
        heap = nums[:k]
        heapq.heapify(heap)    
        result.append(-heap[0][0])
        for i in range(k, len(nums)):
            heapq.heappush(heap, nums[i])  # heap push -> O(log(n))
            while heap[0][1] <= i - k:
                heapq.heappop(heap)  # heap pop -> O(log(n))    
            result.append(-heap[0][0])
        return result


# @lc code=end

