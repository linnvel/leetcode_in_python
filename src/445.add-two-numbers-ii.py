#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # # Solution 1: Reverse + add
        def reverse(node):
            prev = None
            cur = node
            while node is not None:
                cur = cur.next
                node.next = prev
                prev, node = node, cur
            return prev
        # l1 = reverse(l1)
        # l2 = reverse(l2)
        # dummy = ListNode()
        # cur = dummy
        # carry = 0
        # while l1 is not None or l2 is not None:
        #     x = l1.val if l1 is not None else 0
        #     y = l2.val if l2 is not None else 0
        #     result = x + y + carry
        #     result, carry = result % 10, result // 10
        #     cur.next = ListNode(result)
        #     l1 = l1.next if l1 is not None else l1
        #     l2 = l2.next if l2 is not None else l2
        #     cur = cur.next
        # if carry != 0:
        #     cur.next = ListNode(carry)
        # return reverse(dummy.next)

        # Solution 2: 
        def countLength(node):
            n = 1
            cur = node
            while cur is not None:
                n += 1
                cur = cur.next
            return n

        n1 = countLength(l1)
        n2 = countLength(l2)

        dummy = ListNode()
        if n1 > n2:
            dummy.next = l1
            cur = dummy.next
            while n1 > n2:
                cur = cur.next
                l1 = l1.next
                n1 -= 1
        else:
            dummy.next = l2
            cur = dummy.next
            while n1 < n2:
                cur = cur.next
                l2 = l2.next
                n2 -= 1
        while cur is not None:
            cur.val = l1.val + l2.val
            l1 = l1.next
            l2 = l2.next
            cur = cur.next

        cur = reverse(dummy.next)
        dummy = ListNode(0, cur)
        prev = dummy
        carry = 0
        while cur is not None:
            result = cur.val + carry
            carry = result // 10
            cur.val = result % 10
            cur = cur.next
            prev = prev.next
        if carry != 0:
            prev.next = ListNode(carry)
        return reverse(dummy.next)        


# @lc code=end

