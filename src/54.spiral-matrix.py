#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Solution 0: Initial recursion solution
        # def helper(result):
        #     n = len(matrix)
        #     if n == 0:
        #         return
        #     m = len(matrix[0])
        #     if m == 0:
        #         return
        #     result += matrix.pop(0)
        #     if n > 1:
        #         for i in range(len(matrix) - 1):
        #             result.append(matrix[i].pop())
        #         result += matrix[-1][::-1]
        #         matrix.pop()
        #         if m > 1:
        #             for i in range(len(matrix) - 1, -1, -1):
        #                 result.append(matrix[i].pop(0))
        #     helper(result)
        # result = []
        # helper(result)
        # return result

        # Solution 1: rotation and recursion (cleaner implementation)
        if not matrix:
            return[]
        
        # return the first row and rotate the remaining matrix

        result = list(matrix.pop(0))
        # or result = [*matrix.pop(0)]

        # rotation explanation: 
        # https://leetcode.com/problems/spiral-matrix/discuss/999388/95.41-faster-solution
        rotate_matrix = list(zip(*matrix))[::-1]
        # or rotate_matrix = [*zip(*matrix)][::-1]

        return result + self.spiralOrder(rotate_matrix)

        # # Solution 2: rotation and iteration
        # result = []
        # while matrix:
        #    result += list(matrix.pop(0))
        #    matrix = list(zip(*matrix))[::-1]
        # return result

        # Solution 3: simulation by yielding subscripts in spiral order
        # https://leetcode.com/submissions/detail/317296712/

# @lc code=end

