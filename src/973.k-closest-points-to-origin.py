#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
from random import randint
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            x, y = point
            return x ** 2 + y ** 2

        def quickSelect(points, start, end, k):
            i = randint(start, end)
            left, right = start, end - 1
            points[i], points[end] = points[end], points[i]
            pivot = distance(points[end]) 
            while left <= right:
                while left <= right and distance(points[left]) <= pivot:
                    left += 1
                while left <= right and distance(points[right]) >= pivot:
                    right -= 1
                if left <= right:
                    points[left], points[right] = points[right], points[left]
                    left += 1
                    right -= 1
            points[left], points[end] = points[end], points[left]
            if left == k - 1:
                return
            if left < k - 1:
                quickSelect(points, left + 1, end, k)
            else:
                quickSelect(points, start, left - 1, k)

        quickSelect(points, 0, len(points) - 1, k)     
        return points[:k]

        
# @lc code=end

