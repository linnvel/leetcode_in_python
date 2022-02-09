#
# @lc app=leetcode id=124 lang=python
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Solution 1: Time exceeded limit
        # adjList = {}
        # self.getAdjList(root, adjList)
        # print([(k.val, [vv.val for vv in v]) for k, v in adjList.items()])
        
        # seen = {node: False for node in adjList.keys()}
        # maxSum = [-float('inf'), 0]
        # self.helper(adjList, seen, [], maxSum)
        # return maxSum[0]
        global maxSum 
        maxSum = -float('inf')
        
        def maxPath(node):
            global maxSum
            if node is None:
                return 0
            leftGain = max(maxPath(node.left), 0)
            rightGain = max(maxPath(node.right), 0)
            newPrice = node.val + leftGain + rightGain
            maxSum = max(maxSum, newPrice)
            return node.val + max(leftGain, rightGain)
        
        maxPath(root)
        return maxSum


    def getAdjList(self, root, adjList):
        if root is None:
            return 
        if root not in adjList:
            adjList[root] = []
        if root.left is not None:
            adjList[root].append(root.left)
            adjList[root.left] = [root]
        if root.right is not None:
            adjList[root].append(root.right)
            adjList[root.right] = [root]
        self.getAdjList(root.left, adjList)
        self.getAdjList(root.right, adjList)

    def helper(self, adjList, seen, path, maxSum):
        for node in adjList:
            if seen[node]:
                continue
            if len(path) >= 1 and node not in adjList[path[-1]]:
                continue
            path.append(node)
            seen[node] = True
            maxSum[1] += node.val
            maxSum[0] = max(maxSum[0], maxSum[1])
            self.helper(adjList, seen, path, maxSum)
            path.pop()
            seen[node] = False
            maxSum[1] -= node.val

    
        
# @lc code=end

