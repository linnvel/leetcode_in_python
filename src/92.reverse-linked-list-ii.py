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
        if head is None:
            return None
        if right - left < 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        curt = head
        i = 1
        while i < left:
            curt = curt.next
            start = start.next
            i += 1
        nl = curt
        while i < right:
            curt = curt.next
            i += 1
        nr = curt
        nrplus = nr.next

        prev = nl
        curt = nl.next
        while curt != nrplus:
            temp = curt.next
            curt.next = prev
            prev = curt
            curt = temp

        
        start.next = nr
        nl.next = nrplus
        return dummy.next


        
# @lc code=end

