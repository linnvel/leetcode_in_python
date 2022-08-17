# VO-4 Adding Two Numbers
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createList(values):
    dummy = ListNode()
    cur = dummy
    for value in values:
        cur.next = ListNode(value)
        cur = cur.next
    return dummy.next

def reverse(node):
    prev = None
    cur = node
    while node is not None:
        cur = cur.next
        node.next = prev
        prev, node = node, cur
    return prev

def addMultiList(lists):
    reverses = []
    maxLen = -1
    for ls in lists:
        if ls.val == "-":
            sign = -1
            ls = ls.next            
        else:
            sign = 1
            if ls.val == "+":
                ls = ls.next

        cur = ls
        prev = None
        n = 0
        while ls is not None:
            ls.val = int(ls.val) * sign
            cur = cur.next
            ls.next = prev
            prev = ls
            ls = cur
            n += 1
        reverses.append(prev)
        maxLen = max(maxLen, n)
    
    carry = 0
    dummy = ListNode()
    cur = dummy
    for i in range(maxLen):
        result = carry
        for ls in reverses:
            if ls is not None:
                result += ls.val
                ls = ls.next
        result, carry = result % 10, result // 10
        cur.next = ListNode(str(result))
        cur = cur.next
    if carry != 0:
        cur.next = ListNode(str(abs(carry)))
        if carry < 0:
            cur.next = ListNode("-")
    return reverse(dummy.next)
    

