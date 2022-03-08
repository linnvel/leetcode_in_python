#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def helper(n, results, cur, attack_sum, attack_diff):
            if len(cur) == n:
                results.append(cur[:])
            ind = len(cur)
            for i in range(n):
                if i in cur or i + ind in attack_sum or i - ind in attack_diff:
                    continue
                helper(n, results, cur + [i], attack_sum + [i + ind], attack_diff + [i - ind])
        
        def convert_list_to_chess(nums, n):
            chess = [["." for _ in range(n)] for _ in range(n)]
            for i, num in enumerate(nums):
                chess[i][num] = "Q"
            return ["".join(row) for row in chess]
    
        results = []
        helper(n, results, [], [], [])
        return [convert_list_to_chess(result, n) for result in results]
        

        
# @lc code=end

