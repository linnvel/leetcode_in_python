from typing import (
    List,
)

class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequence_reconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # write your code here
        
        if not org:
            for seq in seqs:
                if seq:
                    return False
            return True

        # get indegree dict
        indegree = {}
        for seq in seqs:
            if not seq:
                continue
            for node in seq[1:]:
                if node in indegree:
                    indegree[node] += 1
                else:
                    indegree[node] = 1
        
        # get graph dict
        graph = {}
        for seq in seqs:
            for i in range(len(seq)):
                if seq[i] not in graph:
                    graph[seq[i]] = []
                if i < len(seq) - 1:
                    graph[seq[i]].append(seq[i + 1])

        # get start nodes
        startnodes = list(set([seq[0] for seq in seqs if seq and seq[0] not in indegree]))
        if len(startnodes) != 1 or startnodes[0] != org[0]:
            return False
        
        from collections import deque
        queue = deque(startnodes)
        order = startnodes
        while queue:
            if len(queue) > 1:
                return False
            node = queue.popleft()
            for neighbor in graph.get(node, []):
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    order.append(neighbor)

        return org == order


