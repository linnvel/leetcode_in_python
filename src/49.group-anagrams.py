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
            key = tuple(sorted(word)) # tuple is faster than "".join()
            word_map[key] = word_map.get(key, []) + [word]
        return list(word_map.values())
        
# @lc code=end

