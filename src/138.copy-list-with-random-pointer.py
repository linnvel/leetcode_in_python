#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # # Solution 1: with extra space
        # old = head
        # nodeMap = {}
        # dummy = Node(0)
        # new = dummy
        # while old is not None:
        #     new.next = Node(old.val)
        #     new = new.next
        #     nodeMap[old] = new
        #     old = old.next
        
        # old = head
        # while old is not None:
        #     if old.random is not None:
        #         nodeMap[old].random = nodeMap[old.random]
        #     old = old.next
        # return dummy.next

        # Solution 2: without extra space
        # 1. Copy next
        if head is None:
            return
        cur = head
        while cur is not None:
            newNode = Node(cur.val)
            tmp = cur.next
            cur.next = newNode
            newNode.next = tmp
            cur = tmp
        
        # 2. Copy random
        cur = head
        while cur is not None:
            if cur.random is not None:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        # 3. Split
        cur1 = head
        newhead = head.next
        cur2 = newhead
        while cur1 is not None and cur2 is not None:
            cur1.next = cur1.next.next
            cur2.next = cur2.next.next if cur2.next is not None else None
            cur1 = cur1.next
            cur2 = cur2.next
        return newhead

        
# @lc code=end

