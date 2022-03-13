#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        node0 = head
        while prev.next is not None and prev.next.next is not None:
            node1 = node0.next
            nextNode = node1.next
            node1.next = node0
            node0.next = nextNode
            prev.next = node1
            prev = node0
            node0 = nextNode
        return dummy.next

        
# @lc code=end

