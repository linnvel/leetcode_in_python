#
# @lc app=leetcode id=126 lang=python
#
# [126] Word Ladder II
#

# @lc code=start

from collections import defaultdict, deque
from webbrowser import get


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        def getPattern(word, i):
            return word[:i] + "*" + word[i + 1 :]
        
        adjList = {}
        wordLen = len(beginWord)
        for word in wordList + [beginWord]:
            for i in range(wordLen):
                pattern = getPattern(word, i)
                if pattern in adjList:
                    adjList[pattern].append(word)
                else:
                    adjList[pattern] = [word]
        
        # # Solution 1: DFS (Time Limit Exceed)
        # def helper(paths, path, seen, count):
        #     global minCount
        #     if count > minCount:
        #         return
        #     word = path[-1]
        #     if word == endWord:
        #         paths.append(path[:])
        #         minCount = min(minCount, count)
        #         return
        #     for i in range(wordLen):
        #         pattern = getPattern(word, i)
        #         for neighbor in adjList.get(pattern, []):
        #             if neighbor in seen:
        #                 continue
        #             seen.add(neighbor)
        #             helper(paths, path + [neighbor], seen, count + 1)
        #             seen.remove(neighbor)
                 
        # paths = []
        # global minCount
        # minCount = len(wordList)
        # helper(paths, [beginWord], set(), 1)
        # return [path for path in paths if len(path) == minCount]

        # Solution 2: BFS + DFS
        queue = deque([endWord])
        distance = {endWord: 0}
        count = 0
        while queue:
            count += 1
            qsize = len(queue)
            for _ in range(qsize):
                word = queue.popleft()
                for i in range(wordLen):
                    pattern = getPattern(word, i)
                    for neighbor in adjList.get(pattern, []):
                        if neighbor in distance:
                            continue
                        if neighbor == beginWord:
                            distance[beginWord] = count
                        queue.append(neighbor)
                        distance[neighbor] = count
        if beginWord not in distance:
            return []
        
        def dfs(paths, path, remainCount, seen):
            if remainCount < 0:
                return
            word = path[-1]
            if distance[word] != remainCount:
                return
            if word == endWord:
                paths.append(path[:])
                return
            for i in range(wordLen):
                pattern = getPattern(word, i)
                for neighbor in adjList.get(pattern, []):
                    if neighbor in seen:
                        continue
                    seen.add(neighbor)
                    dfs(paths, path + [neighbor], remainCount - 1, seen)
                    seen.remove(neighbor)
        
        paths = []
        dfs(paths, [beginWord], distance[beginWord], {beginWord})
        return paths                   
        
# @lc code=end

