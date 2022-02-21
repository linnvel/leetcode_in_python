#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:

        sums = {}

        def helper(root, sums):
            if root is None:
                return 0
            left = helper(root.left, sums)
            right = helper(root.right, sums)
            curSum = root.val + left + right
            if curSum in sums:
                sums[curSum] += 1
            else:
                sums[curSum] = 1
            # sums.append(curSum)
            return curSum

        helper(root, sums)
        most_count = 0
        results = []
        for sum_value, cnt in sums.items():
            if cnt > most_count:
                results = [sum_value]
                most_count = cnt
            elif cnt == most_count:
                results.append(sum_value)
        return results
        
# @lc code=end

