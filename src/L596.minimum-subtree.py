"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        self.minSum = float('inf')
        self.minSumRoot = None

        def getSubtreeSum(root):    
            if root is None:
                return 0
            
            left_sum = getSubtreeSum(root.left)
            right_sum = getSubtreeSum(root.right)
            curSum = root.val + left_sum + right_sum
            if curSum < self.minSum:
                self.minSum = curSum
                self.minSumRoot = root
            return curSum
        
        result = getSubtreeSum(root)
        return self.minSumRoot
