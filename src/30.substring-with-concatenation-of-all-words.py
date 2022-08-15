#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        l = len(words[0])
        i, j = 0, 0
        ans = []
        word_dict = {}
        for word in words:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
        cur_dict = word_dict.copy()
        while j < len(s):
            cur = s[j : j + l]
            if cur in cur_dict:
                cur_dict[cur] -= 1
                if cur_dict[cur] == 0:
                    del cur_dict[cur]
                j = j + l
            else:
                cur_dict = word_dict.copy()
                i, j = i + 1, i + 1
            if not cur_dict:
                cur_dict = word_dict.copy()
                if i != j:
                    ans.append(i)
                    i, j = i + 1, i + 1
        return ans
        
# @lc code=end

