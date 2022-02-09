#
# @lc app=leetcode id=126 lang=python
#
# [126] Word Ladder II
#

# @lc code=start

from collections import defaultdict, deque


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
    
        L = len(beginWord)
        intermediates = defaultdict(list)

        # preprocessing
        for word in wordList + ['hit']:
            for i in range(L):
                state = word[:i] + "*" + word[i+1:]
                intermediates[state].append(word)

        # bfs to find distance to endWord
        queue = deque([endWord])
        distance = {endWord: 0}
        count = 0
        while queue:
            # if len(distance) == len(wordList):
            #     break
            size = len(queue)
            count += 1
            for i in range(size):
                word = queue.popleft()
                for nextWord in self.findNeighbor(word, intermediates):
                    if nextWord not in distance:
                        queue.append(nextWord)
                        distance[nextWord] = count
        
        # dfs: to find all shortest paths
        results = []
        if beginWord not in distance:
            return results
        path = [beginWord]
        self.dfs(intermediates, distance, endWord, path, results)
        return results
    
    def dfs(self, intermediates, distance, endWord, path, results):
        # print(path, results)
        currentWord = path[-1]
        currentDist = distance[currentWord]
        if currentWord == endWord:
            results.append(path[:])
            return
        for word in self.findNeighbor(currentWord, intermediates):
            dist = distance.get(word, float('inf'))
            if dist == currentDist - 1:
                path.append(word)
                self.dfs(intermediates, distance, endWord, path, results)
                path.pop()
    
    def findNeighbor(self, word, intermediates):
        neighbors = []
        for j in range(len(word)):
            state = word[:j] + "*" + word[j+1:]
            if state in intermediates:
                neighbors += [w for w in intermediates[state] if w != word]
        return neighbors
        
# @lc code=end

