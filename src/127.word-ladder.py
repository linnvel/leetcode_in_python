#
# @lc app=leetcode id=127 lang=python
#
# [127] Word Ladder
#

# @lc code=start

from collections import defaultdict, deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        queue = deque([beginWord])
        visited = {}
        L = len(beginWord)
        intermediates = defaultdict(list)

        # preprocessing
        for word in wordList:
            for i in range(L):
                state = word[:i] + "*" + word[i+1:]
                intermediates[state].append(word)

        cnt = 0
        while queue:
            if len(visited) == len(wordList):
                break
            size = len(queue)
            cnt += 1
            for i in range(size):
                word = queue.popleft()
                for j in range(len(word)):
                    state = word[:j] + "*" + word[j+1:]
                    if state in intermediates:
                        for nextWord in intermediates[state]:
                            if nextWord == endWord:
                                return cnt + 1
                            if nextWord not in visited:
                                queue.append(nextWord)
                                visited[nextWord] = True
                
        return 0
    
    # Time Limit Exceeded
    # def isSingleDiff(self, word1, word2):
    #     if len(word1) != len(word2):
    #         return False
    #     cnt = 0
    #     for i in range(len(word1)):
    #         if word1[i] != word2[i]:
    #             cnt += 1
    #     return cnt == 1


        
# @lc code=end

