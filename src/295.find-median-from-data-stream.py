#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
from heapq import heappush, heappushpop

class MedianFinder:

    # # Solution 1: array + binary search
    # def __init__(self):
    #     self.data = []
    #     self.length = 0        

    # def addNum(self, num: int) -> None:
    #     if self.length == 0:
    #         self.data.append(num)
    #     else:
    #         left, right = 0, self.length - 1
    #         while left < right - 1:
    #             mid = left + (right - left) // 2
    #             if self.data[mid] < num:
    #                 left = mid
    #             else:
    #                 right = mid
    #         if self.data[right] < num:
    #             index = right
    #         elif self.data[left] < num:
    #             index = left
    #         else:
    #             index = left - 1
    #         self.data.insert(index + 1, num)
    #     self.length += 1        

    # def findMedian(self) -> float:
    #     if self.length == 0:
    #         return
    #     if self.length % 2 == 0:
    #         return (self.data[self.length // 2 - 1] + self.data[self.length // 2]) / 2
    #     else:
    #         return self.data[self.length // 2]

    # # Solution 2: two heaps
    # def __init__(self):
    #     self.small = []  # max heap, negative values
    #     self.large = []  # min heap
    #     heapq.heapify(self.small)
    #     heapq.heapify(self.large)
    #     self.length = 0

    # def addNum(self, num:int) -> None:
    #     heapq.heappush(self.small, -num)
    #     ns, nl = len(self.small), len(self.large)
    #     if ns > nl + 1:
    #         value = -heapq.heappop(self.small)
    #         heapq.heappush(self.large, value)
    #     elif nl != 0 and ns == nl + 1 and -self.small[0] > self.large[0]:
    #         sm = -heapq.heappop(self.small)
    #         lg = heapq.heappop(self.large)
    #         heapq.heappush(self.small, -lg)
    #         heapq.heappush(self.large, sm)
    #     self.length += 1

    # def findMedian(self) -> float:
    #     if self.length == 0:
    #         return
    #     if self.length % 2 == 0:
    #         sm = -self.small[0]
    #         lg = self.large[0]
    #         return (sm + lg) / 2
    #     else:
    #         return -self.small[0]

    # Solution 2 cleaner and faster implementation
    def __init__(self):
        self.small = []  # max heap, negative values
        self.large = []  # min heap

    def addNum(self, num:int) -> None:
        if len(self.small) == len(self.large):
            heappush(self.small, -heappushpop(self.large, num))
        else:  # len(self.small) == len(self.large) + 1
            heappush(self.large, -heappushpop(self.small, -num))

    def findMedian(self) -> float:
        if len(self.small) == 0:
            return
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            return -self.small[0]
    

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

