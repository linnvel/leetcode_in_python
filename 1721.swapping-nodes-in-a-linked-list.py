#
# @lc app=leetcode id=1721 lang=python
#
# [1721] Swapping Nodes in a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        l = 0
        curt = head
        while curt is not None:
            l += 1
            curt = curt.next
        
        left = k
        right = l - k + 1
        left, right = min(left, right), max(left, right)
        # print(left, right)

        i = 1
        curt = head
        while i < left:
            i += 1
            curt = curt.next
        nl = curt
        while i < right:
            i += 1
            curt = curt.next
        nr = curt

        nl.val, nr.val = nr.val, nl.val
        return head
        
# @lc code=end

