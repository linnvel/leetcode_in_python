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
        # # Solution 1
        # dummy = ListNode(0, node)
        # prev = dummy
        # while node.next is not None:
        #     node.val = node.next.val
        #     prev = prev.next
        #     node = node.next
        # prev.next = None

        # # Solution 2
        # while node.next is not None:
        #     node.val = node.next.val
        #     if node.next.next is not None:
        #         node = node.next
        #     else:
        #         node.next = None

        # Solution 3
        node.val = node.next.val
        node.next = node.next.next
        
# @lc code=end

