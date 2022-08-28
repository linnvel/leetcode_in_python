#
# @lc app=leetcode id=472 lang=python3
#
# [472] Concatenated Words
#

# @lc code=start

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def dfs(word, wordIndex, startIndex, isprint=0):
            if isprint:
                print(word, wordIndex, startIndex)
            if not word:
                return True
            for i in range(startIndex, len(words)):
                if i == wordIndex or words[i] not in word:
                    continue
                if not dfs(word, wordIndex, i + 1):
                    new_words = word.split(words[i])
                    for new_word in new_words:
                        if not dfs(new_word, wordIndex, i + 1):
                            return False
                return True   
                         
            return False
        results = []
        for i, word in enumerate(words):
            isprint = int(word == "glafbwzdd")
            if dfs(word, i, 0, isprint=isprint):
                results.append(word)
        return results              
        
# @lc code=end

