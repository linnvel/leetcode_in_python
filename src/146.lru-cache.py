#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class ListNode:
    def __init__(self, val=[], next=None):
        self.val = val
        self.next = next

class LRUCache:
    """
    set: key: pointer -> previous list node
    linked list: [key, value] (head: least recent, tail: most recent)
    """
    def __init__(self, capacity):
        self.set = {}
        self.head = ListNode()
        self.tail = self.head
        self.capacity = capacity
        self.count = 0

    def get(self, key):
        if key in self.set:
            self._move_node_to_tail(self.set[key])
            return self.set[key].next.val[1]
        else:
            return -1

    def put(self, key, value):
        if key in self.set:
            _ = self.get(key)
            self.set[key].next.val[1] = value
        else:
            if self.count == self.capacity:
                self._remove_head()
            else:
                self.count += 1
            self.tail.next = ListNode([key, value])
            self.set[key] = self.tail
            self.tail = self.tail.next
    
    def _move_node_to_tail(self, prev):
        cur = prev.next
        if cur.next is None:
            return
        prev.next = cur.next
        self.tail.next = cur
        self.set[cur.val[0]] = self.tail
        self.set[cur.next.val[0]] = prev
        cur.next = None
        self.tail = cur
    
    def _remove_head(self):
        if self.head.next is None:
            return
        cur = self.head.next
        self.head.next = cur.next
        del self.set[cur.val[0]]
        if cur.next is not None:
            self.set[cur.next.val[0]] = self.head
        else:
            self.tail = self.head
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

