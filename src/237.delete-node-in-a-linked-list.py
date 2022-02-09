#
# @lc app=leetcode id=237 lang=python
#
# [237] Delete Node in a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Solution 1
        # nxt = node.next
        # while nxt is not None:
        #     node.val = nxt.val
        #     if nxt.next is None:
        #         node.next = None
        #     else:
        #         node = node.next
        #     nxt = nxt.next

        # Solution 2
        node.val = node.next.val
        tmp = node.next
        node.next = node.next.next
        # del tmp
        
# @lc code=end

