#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = {}
        for word in strs:
            key = "".join(sorted(list(word)))
            if key not in word_map:
                word_map[key] = [word]
            else:
                word_map[key].append(word)
        return word_map.values()
# @lc code=end

