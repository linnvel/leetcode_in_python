#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Solution 1
        # carry = 1
        # n = len(digits)
        # for i in range(n - 1, -1, -1):
        #     value = digits[i] + carry
        #     digits[i], carry = value % 10, value // 10
        #     if carry == 0:
        #         break
        # if carry > 0:
        #     digits.insert(0, carry)
        # return digits
        
        # Solution 2
        return list(str(int("".join([str(d) for d in digits])) + 1 ))
        
# @lc code=end

