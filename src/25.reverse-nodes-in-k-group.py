#
# @lc app=leetcode id=25 lang=python
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # def reverse(start, end):
        #     dummy = ListNode(0)
        #     dummy.next = start
        #     prev = start
        #     start = start.next
        #     stop = end.next
        #     while start != stop:
        #         tmp = start.next
        #         start.next = prev
        #         prev = start
        #         start = tmp
        #     return dummy.next, stop
        
        # dummy = ListNode(0)
        # dummy.next = head
        # start, end = head, head
        # cur = dummy
        # while end is not None:
        #     idx = k
        #     while idx > 1 and end is not None:
        #         idx -= 1
        #         end = end.next
        #     if end is not None:
        #         cur.next = end
        #         cur, nextNode = reverse(start, end)
        #         start = nextNode
        #         end = nextNode
        #         if end is None:
        #             cur.next = None
        #     else:
        #         cur.next = start
        # return dummy.next

        # Cleaner implementation
        if head is None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while prev is not None:
            prev = self.reverseNextNodes(prev, k)
        return dummy.next
    
    def reverseNextNodes(self, head, k):
        curt = head
        n1 = head.next
        for i in range(k):
            curt = curt.next
            if curt is None:
                return None
        
        nk = curt
        nkplus = nk.next

        # reverse
        # head -> 0 -> 1 -> 2 -> 3 ->4 
        prev = head
        curt = head.next
        while curt != nkplus:
            temp = curt.next
            curt.next = prev
            prev = curt
            curt = temp
        
        # head -> 0 <- 1 <- 2 <- 3 4 <- nkplus
        head.next = nk
        n1.next = nkplus
        print(nkplus.val, n1.val)
        return n1


# @lc code=end

