#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#

# @lc code=start

import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:

        # Solution 1: heap + hashset
        # pq = []
        # seen = set()
        # count = 0
        # heapq.heappush(pq, (1, (0, 0, 0)))
        # seen.add((0, 0, 0))
        # while count < n:
        #     value, (i, j, k) = heapq.heappop(pq)
        #     if (i + 1, j, k) not in seen:
        #         seen.add((i + 1, j, k))
        #         heapq.heappush(pq, (2 ** (i + 1) * 3 ** j * 5 ** k, (i + 1, j, k)))
        #     if (i, j + 1, k) not in seen:
        #         seen.add((i, j + 1, k))
        #         heapq.heappush(pq, (2 ** i * 3 ** (j + 1) * 5 ** k, (i, j + 1, k)))
        #     if (i, j, k + 1) not in seen:
        #         seen.add((i, j, k + 1))
        #         heapq.heappush(pq, (2 ** i * 3 ** j * 5 ** (k + 1), (i, j, k + 1)))
        #     count += 1
        # return value

        # cleaner implementation
        pq = []
        seen = set()
        heapq.heappush(pq, 1) # heap is much faster than priority queue
        seen.add(1)
        while n > 1:
            value = heapq.heappop(pq)
            for factor in [2, 3, 5]:
                num = value * factor
                if num not in seen:
                    seen.add(num)
                    heapq.heappush(pq, num)
            n -= 1
        value = heapq.heappop(pq)
        return value

        # Solution 2
        # todo

# @lc code=end

