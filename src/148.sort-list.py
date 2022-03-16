#
# @lc app=leetcode id=148 lang=python
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from subprocess import list2cmdline


class Solution(object):
    # Solution 1: merge sort
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        # 1. Find mid
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        # 2. sort left and right
        right = self.sortList(slow.next)
        slow.next = None
        left = self.sortList(head)
        
        # 3. merge two sorted list
        return self.merge(left, right)

    def merge(self, list1, list2):
        dummy = ListNode(0)
        node = dummy
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 if list1 is not None else list2 
        return dummy.next


# @lc code=end

