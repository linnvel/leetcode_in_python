#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        num = 0
        prev = roman_dict[s[0]]
        for c in s[1:]:
            cur = roman_dict[c]
            if prev < cur:
                num -= prev
            else:
                num += prev
            prev = cur
        num += prev
        return num

        
# @lc code=end

