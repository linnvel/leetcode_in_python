#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # c = Counter(p)
        # window_dict = Counter()
        # l, r = 0, 0
        # results = []
        # while r < len(s):
        #     character = s[r]
        #     if character in c:
        #         window_dict.update(character)
        #         while window_dict[character] > c[character]:
        #             window_dict[s[l]] -= 1
        #             l += 1
        #         if r - l + 1 == len(p):
        #             results.append(l)
        #     else:
        #         l = r + 1
        #         window_dict.clear()
        #     r += 1
        # return results

        # another implementation
        result = []
        if len(s) < len(p):
            return result
        dictS = Counter(s[:len(p)])
        dictP = Counter(p)
        l = 0
        for r in range(len(p), len(s) + 1):
            if dictS == dictP:  # O(1)???
                result.append(l)
            if r < len(s):
                dictS[s[l]] -= 1
                if dictS[s[l]] <= 0:
                    dictS.pop(s[l])
                l += 1
                dictS.update(s[r])
        return result

# @lc code=end

