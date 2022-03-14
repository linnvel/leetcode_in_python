#
# @lc app=leetcode id=143 lang=python
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
            
        # 1. find mid point
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # 2. Split first list and second list
        first = head
        second = slow.next
        slow.next = None
        
        # 3. Reverse second list
        prev = None
        cur = second
        while cur is not None:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        second = prev

        # 4. Merge
        dummy = ListNode(0)
        node = dummy
        isFirst = 1
        while first is not None and second is not None:
            if isFirst == 1:
                node.next = first
                node = node.next
                first = first.next
            else:
                node.next = second
                node = node.next
                second = second.next
            isFirst = -isFirst
        if first is not None:
            node.next = first
        elif second is not None:
            node.next = second
        
        return dummy.next


# @lc code=end

