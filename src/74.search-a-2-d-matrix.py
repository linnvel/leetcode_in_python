#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None or len(matrix) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid
            else:
                left = mid
        if matrix[left // n][left % n] == target or matrix[right // n][right % n] == target:
            return True
        return False

        # while left <= right:
        #     mid = left + (right - left) // 2
        #     row = mid // n
        #     col = mid % n
        #     if matrix[row][col] == target:
        #         return True
        #     elif matrix[row][col] > target:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return False


        
# @lc code=end

