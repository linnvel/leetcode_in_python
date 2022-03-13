#
# @lc app=leetcode id=92 lang=python
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        i = 1
        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        while i < left:
            node = node.next
            head = head.next
            i += 1
        prev = head
        cur = head.next
        while i < right:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            i += 1
        head.next = cur
        node.next = prev
        return dummy.next
        
# @lc code=end

