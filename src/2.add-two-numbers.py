#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Solution 1:
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 is not None or l2 is not None:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            result = x + y + carry
            carry, result = result // 10, result % 10
            cur.next = ListNode(result)
            l1 = l1.next if l1 is not None else l1
            l2 = l2.next if l2 is not None else l2
            cur = cur.next
        if carry != 0:
            cur.next = ListNode(carry)
        return dummy.next

        # # Solution 2: less memory
        # dummy = ListNode(0, l1)
        # prev = dummy
        # carry = 0
        # while l1 is not None and l2 is not None:
        #     result = l1.val + l2.val + carry
        #     carry, result = result // 10, result % 10
        #     l1.val = result
        #     l1 = l1.next
        #     l2 = l2.next
        #     prev = prev.next
        # if l2 is not None:
        #     prev.next = l2
        #     l1 = prev.next
        # while l1 is not None:
        #     result = l1.val + carry
        #     carry, result = result // 10, result % 10
        #     l1.val = result
        #     l1 = l1.next
        #     prev = prev.next
        # if carry != 0:
        #     prev.next = ListNode(carry)
        # return dummy.next
        
# @lc code=end

