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
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        l = 1
        while cur.next is not None:
            cur = cur.next
            l += 1
        if k % l == 0:
            return head
        cur.next = head
        
        prev = dummy
        for _ in range(l - k%l):
            prev = prev.next

        tmp = prev.next
        dummy.next = tmp
        prev.next = None

        return dummy.next
        

        
# @lc code=end

