#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # count_dict = {}
        # for c in s:
        #     if c in count_dict:
        #         count_dict[c] += 1
        #     else:
        #         count_dict[c] = 1
        # for c in t:
        #     if c not in count_dict or count_dict[c] == 0:
        #         return False
        #     count_dict[c] -= 1
        # return True
        
        # faster implementation
        map_s = {}
        map_t = {}
        for c in s:
            map_s[c] = map_s.get(c, 0) + 1
        for c in t:
            map_t[c] = map_t.get(c, 0) + 1
        return map_s == map_t
# @lc code=end

