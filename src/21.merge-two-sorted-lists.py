#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # # Solution 1: dummy node
        # dummy = ListNode(0)
        # node = dummy
        # while list1 is not None and list2 is not None:
        #     if list1.val <= list2.val:
        #         node.next = list1
        #         list1 = list1.next
        #     else:
        #         node.next = list2
        #         list2 = list2.next
        #     node = node.next
        # if list1 is not None:
        #     node.next = list1
        # elif list2 is not None:
        #     node.next = list2
        # return dummy.next

        # Solution 2: without dummy node
        if not list1 or not list2:
            return list1 if not list2 else list2
        
        seek, target = (list1, list2) if list1.val <= list2.val else (list2, list1)
        head = seek
        while target and seek:
            while seek.next and seek.next.val <= target.val:
                seek = seek.next
            seek.next, target = target, seek.next
            seek = seek.next
        return head
        
# @lc code=end

