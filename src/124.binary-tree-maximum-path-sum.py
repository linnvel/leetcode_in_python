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
        # Solution 1: Time Limit Exceed
        # def getAdjList(root, adjList):
        #     if root not in adjList:
        #         adjList[root] = []
        #     if root.left is not None:
        #         adjList[root].append(root.left)
        #         adjList[root.left] = [root]
        #         getAdjList(root.left, adjList)
        #     if root.right is not None:
        #         adjList[root].append(root.right)
        #         adjList[root.right] = [root]
        #         getAdjList(root.right, adjList)
        
        # def helper(root, seen, adjList, curSum):
        #     seen.add(root)
        #     curSum += root.val
        #     maxSum = curSum
        #     # print(maxSum)
        #     # print([s.val for s in seen])
        #     for node in adjList[root]:
        #         if node in seen:
        #             continue
        #         maxSum = max(helper(node, seen, adjList, curSum), maxSum)
        #     seen.remove(root)
        #     curSum -= root.val
        #     return maxSum
        
        # if root is None:
        #     return
        # adjList = {}
        # seen = set()
        # getAdjList(root, adjList)
        # # for node, adjNodes in adjList.items():
        # #     print(node.val, " : ", [n.val for n in adjNodes])
        # result = -float('inf')
        # for node in adjList.keys():
        #     result = max(result, helper(node, seen, adjList, 0))
        # return result

        # Solution 2: Post Tranverse
        global maxSum
        maxSum = -float('inf')
        def maxPath(root):
            if root is None:
                return 0
            global maxSum
            left = max(maxPath(root.left), 0)
            right = max(maxPath(root.right), 0)
            curPrice = root.val + left + right
            maxSum = max(curPrice, maxSum)
            return root.val + max(left, right)
    
        maxPath(root)
        return maxSum
# @lc code=end