#
# @lc app=leetcode id=61 lang=python
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        fast = head
        nList = 0
        while k > 0:
            fast = fast.next
            nList += 1
            k -= 1
            if fast is None:
                fast = head
                k = k % nList
        slow = head
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        if slow.next is not None:
            newHead = slow.next 
            slow.next = None
            fast.next = head
            return newHead
        else:
            return head

        
# @lc code=end

