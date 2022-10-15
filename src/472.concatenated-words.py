#
# @lc app=leetcode id=472 lang=python3
#
# [472] Concatenated Words
#

# @lc code=start

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # Solution 1: DFS search by words (TLE)
        """
        This method doesn't work for a long words list
        because it has to tranverse the whole words list from beginning for each dfs call.
        Why not set a startIndex? Because when find a substr exists, we are not sure the 
        remaining substr is before or after. That's because word.split
        will remove all substr. But that might not be the case.
        Sometimes we only use the substr once even though it appears multiple times.
        E.g. words = ["d", "zd", "zdd"]
        For the two "d"s in words, one is from "d", the other is from "zd"
        it's hard to handle this case by word.split(substr)
        """
        # def dfs(word, wordIndex, seen, isprint):
        #     if isprint:
        #         print(word, wordIndex, seen)
        #     if not word:
        #         return True
        #     for i in range(len(words)):
        #         if i == wordIndex or words[i] not in word or words[i] in seen:
        #             continue
        #         new_words = word.split(words[i])
        #         result = True
        #         for new_word in new_words:
        #             if not dfs(new_word, wordIndex, seen + [words[i]], isprint):
        #                 result = False
        #                 break
        #         if result:
        #             return True                    
        #     return False
        # results = []
        # for i, word in enumerate(words):
        #     isprint = (word == "glafbwzdd")
        #     if dfs(word, i, [], isprint):
        #         results.append(word)
        # return results              

        # Solution 2: DFS search by word split
        # words = set(words)
        # def dfs(word):
        #     # start from 1 because the word itself must exist in words 
        #     # and all words are unique.
        #     # Going forward, if word exists in words, dfs will not be called.
        #     for i in range(1, len(word)):
        #         prefix = word[:i]
        #         suffix = word[i:]
        #         if prefix in words and suffix in words:
        #             return True
        #         elif prefix in words and dfs(suffix):
        #             return True
        #         # The following case has already been handled in previous call.
        #         # If this is true, there must be a shorter prefix that satisfies
        #         # the first/second condition.
        #         # elif suffix in words and dfs(prefix):  
        #         #     return True
        #     return False

        # results = []
        # for word in words:
        #     if dfs(word):
        #         results.append(word)
        # return results
    
        # # Solution 3: DFS with memorization
        # memo = {}
        # words = set(words)

        # def dfs(word):
        #     if word in memo:
        #         return memo[word]
        #     memo[word] = False
        #     for i in range(1, len(word)):
        #         prefix = word[:i]
        #         suffix = word[i:]
        #         if prefix in words and suffix in words:
        #             memo[word] = True
        #             break
        #         elif prefix in words and dfs(suffix):
        #             memo[word] = True
        #             break
        #     return memo[word]

        # return[word for word in words if dfs(word)]

        # Solution 4: DP
        def helper(word, words):
            dp = [ word[: i + 1] in words for i in range(len(word))]
            dp[-1] = False
            for i in range(len(word)):
                if not dp[i]:
                    for j in range(1, i + 1):
                        dp[i] = dp[j - 1] and word[j : i + 1] in words
                        if dp[i]:
                            break
            return dp[-1]
    
        # words = set(words)
        # return[word for word in words if helper(word, words)]

        # Faster DP (Theoretically, actually not TT)
        words.sort(key = len)
        candidates = set()
        results = []
        for word in words:
            if candidates and helper(word, candidates):
                results.append(word)
            candidates.add(word)
        return results

        # Todo: DP is not faster here
    
# @lc code=end

