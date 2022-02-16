#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(results, cur, nl, nr):
            if len(cur) == 2 * n:
                results.append(cur[:])
                return
            if nl < n:
                helper(results, cur + '(', nl + 1, nr)
            if nr < nl:
                helper(results, cur + ')', nl, nr + 1)
        
        results = []
        cur = ""
        helper(results, cur, 0, 0)
        return results

        
# @lc code=end

