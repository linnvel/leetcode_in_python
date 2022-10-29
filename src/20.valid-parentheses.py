#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_dict = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for c in s:
            # if c in map_dict.keys(): - O(n) lookup
            # this would be faster - O(1)
            if c in map_dict:
                stack.append(c)
            elif not stack or map_dict[stack.pop()] != c:
                return False
        return not stack
        
# @lc code=end

