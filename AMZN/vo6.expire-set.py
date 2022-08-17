import time
from queue import PriorityQueue
class ExpireSet:
    def __init__(self, time_limit):
        self.time_limit = time_limit
        self.set = {}
        self.pq = PriorityQueue()
    
    def add(self, value):
        current = time.time()
        self.set[value] = current
        self.pq.put((current, value))
    
    def delete(self, value):
        if value not in self.set:
            raise ValueError("Cannot find value.")
        del self.set[value]

    def contains(self, value):
        self.expire()
        return value in self.set
    
    def expire(self):
        while self.pq:
            (t, value) = self.pq.get()
            if time.time() - t >= self.time_limit:
                if value in self.set and t == self.set[value]:
                    del self.set[value]
            else:
                self.pq.put((t, value))
                break
