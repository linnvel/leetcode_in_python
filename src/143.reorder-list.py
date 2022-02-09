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
        if head is None or head.next is None or head.next.next is None:
            return head

        # split
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        front = head
        rear = slow.next
        slow.next = None

        # reverse
        prev = rear
        cur = rear.next
        while cur is not None:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        rear.next = None
        rear = prev

        # merge
        dummy = ListNode(0)
        cur = dummy
        while front is not None and rear is not None:
            print(front.val, rear.val)
            cur.next = front
            tmp = front.next
            cur.next.next = rear
            cur = cur.next.next
            front = tmp
            rear = rear.next
        while front is not None:
            cur.next = front
            cur = cur.next
            front = front.next
        while rear is not None:
            cur.next = rear
            cur = cur.next
            rear = rear.next
        return dummy.next

        
# @lc code=end

