#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # # Solution 1: DFS (TLE)
        # def dfs(board, candidates, visited, x, y, m, n, word, results):
        #     new_word = word + board[x][y]
        #     new_candidates = [wd for wd in candidates if wd[len(word)] == board[x][y]]
        #     visited[x][y] = 1
        #     if new_word in new_candidates:
        #         results.append(new_word)
        #         new_candidates.remove(new_word)
        #     if new_candidates:
        #         dx = [0, -1, 0, 1]
        #         dy = [-1, 0, 1, 0]        
        #         for i in range(4):
        #             nx = x + dx[i]
        #             ny = y + dy[i]
        #             if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
        #                 dfs(board, new_candidates, visited, nx, ny, m, n, new_word, results)
        #     visited[x][y] = 0

        # m, n = len(board), len(board[0])
        # results = []
        # visited = [[0 for _ in range(n)] for _ in range(m)]

        # for i in range(m):
        #     for j in range(n):
        #         dfs(board, words, visited, i, j, m, n, "", results)
        # return list(set(results))
        
        # # Solution 2: DFS + Trie
        # def dfs(board, trie, visited, x, y, m, n, results):
        #     if not trie or board[x][y] not in trie:
        #         return
        #     if "$" in trie[board[x][y]]:
        #         results.append(trie[board[x][y]]["$"])
        #         del trie[board[x][y]]["$"]
        #         if not trie[board[x][y]] and len(trie) == 1:
        #             del trie[board[x][y]]
        #             return
        #     visited[x][y] = 1
            
        #     dx = [0, -1, 0, 1]
        #     dy = [-1, 0, 1, 0]        
        #     for i in range(4):
        #         nx = x + dx[i]
        #         ny = y + dy[i]
        #         if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
        #             dfs(board, trie[board[x][y]], visited, nx, ny, m, n, results)
        #     visited[x][y] = 0

        # m, n = len(board), len(board[0])
        # results = []
        # visited = [[0 for _ in range(n)] for _ in range(m)]
        # trie = {}
        # for word in words:
        #     cur = trie
        #     for c in word:
        #         if c not in cur:
        #             cur[c] = {}
        #         cur = cur[c]
        #     cur["$"] = word

        # for i in range(m):
        #     for j in range(n):
        #         dfs(board, trie, visited, i, j, m, n, results)
        # return list(set(results))

        # Cleaner code (avoid visited)
        def dfs(board, trie, x, y, m, n, results):
            cur = board[x][y]
            if not trie or not cur in trie:
                return
            if "$" in trie[cur]:
                results.append(trie[cur]["$"])
                del trie[cur]["$"]
                if not trie[cur]:
                    del trie[cur]
                    return
            board[x][y] = "#"
            
            dx = [0, -1, 0, 1]
            dy = [-1, 0, 1, 0]        
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    dfs(board, trie[cur], nx, ny, m, n, results)
            board[x][y] = cur

        m, n = len(board), len(board[0])
        results = []
        trie = {}
        for word in words:
            cur = trie
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur["$"] = word

        for i in range(m):
            for j in range(n):
                dfs(board, trie, i, j, m, n, results)
        return list(set(results))
        
# @lc code=end

