#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
from collections import OrderedDict


class ListNode:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class LRUCache:

    # # Solution 1: dict + list 
    # def __init__(self, capacity: int):
    #     self.size = 0
    #     self.capacity = capacity
    #     self.dict = {}
    #     self.dummy = ListNode(0)
    #     self.tail = self.dummy

    # def get(self, key: int) -> int:
    #     if key in self.dict:
    #         tmp = self._del_list_node(key)
    #         node = ListNode(tmp)
    #         self.tail.next = node
    #         self.dict[key] = self.tail
    #         self.tail = node
    #         return tmp[1]
    #     else:
    #         return -1
        
    # def put(self, key: int, value: int) -> None:
    #     if key in self.dict:
    #         self._del_list_node(key)
    #         self.size -= 1
    #     elif self.size == self.capacity:
    #         tmp = self._del_list_node(-1, self.dummy)
    #         del self.dict[tmp[0]]
    #         self.size -= 1
    #     node = ListNode((key, value))
    #     self.tail.next = node
    #     self.dict[key] = self.tail
    #     self.tail = node
    #     self.size += 1
    #     # print(self.dict)
    
    # def _del_list_node(self, key, prev=None):
    #     prev = self.dict[key] if prev is None else prev
    #     value = prev.next.val
    #     prev.next = prev.next.next
    #     if prev.next is None:
    #         self.tail = prev
    #     else:
    #         self.dict[prev.next.val[0]] = prev
    #     del prev
    #     return value

    # Solution 2: OrderedDict
    from collections import OrderedDict
    def __init__(self, capacity):
        self.remain = capacity
        self.dict = OrderedDict()
    
    def get(self, key):
        if key not in self.dict:
            return -1
        value = self.dict[key]
        self.dict.pop(key)
        self.dict[key] = value
        return value

    def put(self, key, value):
        if key in self.dict:
            self.dict.pop(key)
        elif self.remain == 0:
            # self.dict.pop(self.dict.keys[0]) wrong
            self.dict.popitem(last=False)
        else:
            self.remain -= 1
        self.dict[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

