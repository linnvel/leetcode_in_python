#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start

class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31        
        # s = s.strip()
        # s = list(s)
        # if not s or (s[0] not in ["+", "-"] and not s[0].isdigit()):
        #     return 0
        # sign = -1 if s[0] == "-" else 1
        # if not s[0].isdigit():
        #     s = s[1:]
        # # ans = ""
        # # for c in s:
        # #     if not c.isdigit():
        # #         break
        # #     ans += c
        # # if not ans:
        # #     return 0
        # # ans = sign * int(ans)
        # # return min(max(ans, MIN_INT), MAX_INT)
        
        # i = 0
        # while i < len(s):
        #     if not s[i].isdigit():
        #         break
        #     i += 1
        # if i == 0:
        #     return 0
        # ans = sign * int("".join(s[:i]))
        # return min(max(ans, MIN_INT), MAX_INT)

        #  Solution 2
        # s = list(s)
        # i = 0
        # while i < len(s) and s[i] == " ": i += 1  # equivalent to s.strip()
        # if i >= len(s):
        #     return 0
        s = list(s.strip())
        if not s :
            return 0
        sign = 1
        ans = 0
        i = 0
        if s[i] in ["+", "-"]:
            sign = -1 if s[i] == "-" else 1
            i += 1
        while i < len(s) and s[i].isdigit():
            d = int(s[i])  # or d = ord(s[i]) - ord('0')
            if ans > MAX_INT // 10 or (ans == MAX_INT // 10 and d > 7):
                return MAX_INT if sign == 1 else MIN_INT
            ans = ans * 10 + d
            i += 1
        return ans * sign

# @lc code=end

