#
# @lc app=leetcode id=127 lang=python
#
# [127] Word Ladder
#

# @lc code=start

from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def getPattern(word, i):
            return word[:i] + "*" + word[i + 1:]
            
        # Get adjList = {pattern: [words]}
        wordLen = len(beginWord)
        adjList = {}
        for word in wordList:
            for i in range(wordLen):
                pattern = getPattern(word, i)
                if pattern in adjList:
                    adjList[pattern].append(word)
                else:
                    adjList[pattern] = [word]
        
        queue = deque([beginWord])
        seen = {beginWord}
        count = 1
        while queue:
            qsize = len(queue)
            count += 1
            for _ in range(qsize):
                word = queue.popleft()
                for i in range(wordLen):
                    pattern = getPattern(word, i)
                    if pattern not in adjList:
                        continue
                    for neighbor in adjList[pattern]:
                        if neighbor == endWord:
                            return count
                        if neighbor in seen:
                            continue
                        queue.append(neighbor)
                        seen.add(neighbor)
        return 0


        
# @lc code=end

