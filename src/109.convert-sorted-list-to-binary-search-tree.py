#
# @lc app=leetcode id=109 lang=python
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return
        if head.next is None:
            return TreeNode(head.val)
        dummy = ListNode(0, head)
        prev = dummy
        slow = fast = head
        # fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            prev = prev.next
        root = TreeNode(slow.val)
        prev.next = None
        root.left = self.sortedListToBST(dummy.next) 
        root.right = self.sortedListToBST(slow.next)
        return root     
# @lc code=end

