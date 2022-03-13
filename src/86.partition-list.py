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
        small_dummy = ListNode(0)
        large_dummy = ListNode(0)
        small = small_dummy
        large = large_dummy
        while head is not None:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next
        small.next = large_dummy.next
        large.next = None
        return small_dummy.next

        
# @lc code=end

