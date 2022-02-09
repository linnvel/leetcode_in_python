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
class Solution(object):
    # # Solution 1: merge sort
    # def sortList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     if head is None or head.next is None:
    #         return head
        
    #     mid = self.findMid(head)
    #     right = self.sortList(mid.next)
    #     mid.next = None
    #     left = self.sortList(head)
    #     return self.mergeSortedList(left, right)

    # def findMid(self, head):
    #     if head is None or head.next is None:
    #         return head
    #     slow = head
    #     fast = head.next
    #     while fast is not None and fast.next is not None:
    #         slow = slow.next
    #         fast = fast.next.next
    #     return slow
    
    # def mergeSortedList(self, head1, head2):
    #     dummy = ListNode(0)
    #     cur = dummy
    #     while head1 is not None and head2 is not None:
    #         if head1.val <= head2.val:
    #             cur.next = head1
    #             cur = cur.next
    #             head1 = head1.next
    #         else:
    #             cur.next = head2
    #             cur = cur.next
    #             head2 = head2.next
    #     if head1 is not None:
    #         cur.next = head1
    #     if head2 is not None:
    #         cur.next = head2
    #     return dummy.next

    # Solution 2: quick sort
    def sortList(self, head):
        head, _ = self.quickSortList(head)
        return head
    
    def quickSortList(self, head):
        if head is None or head.next is None:
            return head, head

        # split
        pivot = self.findMid(head).val
        dummy_sm, dummy_eq, dummy_lg = ListNode(0), ListNode(0), ListNode(0)
        small, equal, large = dummy_sm, dummy_eq, dummy_lg
        while head is not None:
            if head.val > pivot:
                large.next = head
                large = large.next
            elif head.val < pivot:
                small.next = head
                small = small.next
            else:
                equal.next = head
                equal = equal.next
            head = head.next
        
        small.next, equal.next, large.next = None, None, None

        small_head, small_tail = self.quickSortList(dummy_sm.next)
        large_head, large_tail = self.quickSortList(dummy_lg.next)

        # print("small", small_head, small_tail)
        # print("large", large_head, large_tail)
        # merge
        if small_tail is None:
            small_head = dummy_eq.next
        else:
            small_tail.next = dummy_eq.next
        equal.next = large_head
        large_tail = equal if large_tail is None else large_tail
        return small_head, large_tail
    
    def findMid(self, head):
        if head is None or head.next is None:
            return head
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow


# @lc code=end

