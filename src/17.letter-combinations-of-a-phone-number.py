#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_alphabet = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def helper(digits, cur, results):
            if len(digits) == 0:
                return
            if len(cur) == len(digits):
                results.append(cur[:])
                return
            candidates = digit_to_alphabet[digits[len(cur)]]
            for i in range(len(candidates)):
                helper(digits, cur+candidates[i], results)

        cur = ""
        results = []
        helper(digits, cur, results)
        return results
        
# @lc code=end

