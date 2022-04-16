#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from dbm import dumb
from multiprocessing import dummy


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # def mergeTwoList(list1, list2):
        #     dummy = ListNode(0)
        #     node = dummy
        #     while list1 is not None and list2 is not None:
        #         if list1.val <= list2.val:
        #             node.next = list1
        #             list1 = list1.next
        #         else:
        #             node.next = list2
        #             list2 = list2.next
        #         node = node.next
        #     node.next = list1 if list1 is not None else list2
        #     return dummy.next


        # # Solution 1: Top-down
        # Time complexity:
        # k lists, n - average length of a list
        # Time = n
        #
        # k = len(lists)
        # if k == 0:
        #     return None
        # elif k == 1:
        #     return lists[0]
        # if k == 2:
        #     list1, list2 = lists
        #     return mergeTwoList(list1, list2) 
        # else:
        #     list1 = self.mergeKLists(lists[:k//2])
        #     list2 = self.mergeKLists(lists[k//2 :])
        #     return self.mergeKLists([list1, list2])

        # Solution 2: Bottom up
        # while len(lists) > 1:
        #     j = 0
        #     while j < len(lists) and j + 1 < len(lists):
        #         lists[j] = mergeTwoList(lists[j], lists[j + 1])
        #         lists.pop(j + 1)
        #         j += 1
        # if len(lists) == 1:
        #     return lists[0]

        # Solution 3: priority queue   
        import heapq
        pq = []
        for i, ls in enumerate(lists):
            if ls is not None:
                heapq.heappush(pq, (ls.val, i, ls))

        dummy = ListNode(0)
        cur = dummy
        while pq:
            _, i, node = heapq.heappop(pq)
            cur.next = node
            cur = cur.next
            if not pq:
                break
            if node.next is not None:
                node = node.next
                heapq.heappush(pq, (node.val, i, node))
        return dummy.next


# @lc code=end

