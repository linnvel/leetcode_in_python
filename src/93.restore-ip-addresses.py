#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def isValidIP(ss):
            return ss.isdigit() and (len(ss) == 1 or (1 < len(ss) <=3 and ss[0] != "0" and int(ss) < 256))

        def helper(s, results, cur, startIndex):
            if len(cur) == 4: 
                if startIndex == len(s):
                    results.append(".".join(cur))
                return
            for i in range(startIndex, len(s)):
                ss = s[startIndex: i + 1]
                if not isValidIP(ss):
                    continue
                helper(s, results, cur + [ss], i + 1)
        
        results = []
        cur = []
        helper(s, results, cur, 0)
        return results

# @lc code=end

