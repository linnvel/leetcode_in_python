#
# @lc app=leetcode id=86 lang=python
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return head
        small_dummy = ListNode(0)
        sm = small_dummy
        large_dummy = ListNode(0)
        lg = large_dummy
        while head is not None:
            if head.val < x:
                sm.next = ListNode(head.val)
                sm = sm.next
            else:
                lg.next = ListNode(head.val)
                lg = lg.next
            head = head.next
        sm.next = large_dummy.next
        return small_dummy.next





        
# @lc code=end

