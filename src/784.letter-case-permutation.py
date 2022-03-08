#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        results = []
        cur = list(s)

        def helper(s, results, cur, startIndex):
            for i in range(startIndex, len(s)):
                character = s[i]
                if not character.isalpha():
                    continue
                cur[i] = character.swapcase()
                helper(s, results, cur, i + 1)
                cur[i] = character
            results.append("".join(cur))
        
        helper(s, results, cur, 0)
        return results

        # Another implementation
        # def dfs(sub, i):
        #     if len(sub) == len(s):
        #         res.append(sub)
        #         return
        #     if s[i].isalpha():
        #         dfs(sub + s[i].swapcase(), i + 1)
        #     dfs(sub + s[i], i + 1)
        
        # res = []
        # dfs("", 0)
        # return res

                
        
# @lc code=end

