class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
   
    def validTree(self, n, edges):
        # write your code here
        # if not edges:
        #     return n <= 1
        # if n == 0:
        #     return True

        # from collections import deque
     
        # adjList = {}
        # for start, end in edges:
        #     if start in adjList:
        #         adjList[start].append(end)
        #     else:
        #         adjList[start] = [end]
        #     if end in adjList:
        #         adjList[end].append(start)
        #     else:
        #         adjList[end] = [start]

        # level = 0
        # queue = deque([0])
        # seen = {0: level}
        # while queue:
        #     qsize = len(queue)
        #     level += 1
        #     for _ in range(qsize):
        #         node = queue.popleft()
        #         if node not in adjList:
        #             continue
        #         for neighbor in adjList[node]:
        #             if neighbor in seen:
        #                 if seen[neighbor] != seen[node] - 1:
        #                     return False
        #                 else:
        #                     continue
        #             queue.append(neighbor)
        #             seen[neighbor] = level
        # return len(seen) == n

        # Cleaner version
        # Necessary and sufficient conditions of valid tree:
        # 1. len(nodes) = len(edges) + 1
        # 2. All nodes are connected

        if n == 0:
            return False
        if len(edges) != n - 1:
            return False

        # initialize graph
        graph = {i: set() for i in range(n)}
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # use bfs to find connected area
        from collections import deque
        queue = deque([0])
        seen = {0}
        while queue:
            node = queue.popleft()
            for neighbor in graph.get(node, []):
                if neighbor in seen:
                    continue
                queue.append(neighbor)
                seen.add(neighbor)
        return len(seen) == n