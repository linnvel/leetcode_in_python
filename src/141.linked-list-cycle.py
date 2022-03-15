#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # if head is None:
        #     return False
        # slow = head
        # fast = head.next
        # while head is not None and head.next is not None:
        #     slow = slow.next
        #     head = head.next.next
        #     if slow == head:
        #         return True
        # return False
        
        #  second implentation
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
# @lc code=end

