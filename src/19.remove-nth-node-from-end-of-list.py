#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # i = 0
        # fast = head
        # while fast and i < n:
        #     fast = fast.next
        #     i += 1
        # if i < n:
        #     return head
        # dummy = ListNode(0, head)
        # slow = dummy
        # while fast:
        #     fast = fast.next
        #     slow = slow.next
        # slow.next = slow.next.next
        # return dummy.next

        # cleaner implementation
        fast = head
        slow = dummy = ListNode(0, head)
        while fast:
            fast = fast.next
            n -= 1
            if n < 0:
                slow = slow.next
        slow.next = slow.next.next
        return dummy.next
# @lc code=end

