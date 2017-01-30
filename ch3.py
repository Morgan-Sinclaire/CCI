# implementation of a Stack
class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.next = pointer

class Stack(object):
    def __init__(self, head=None):
        self.head = head

    def push(self, n):
        cur = self.head
        new = Node(n, cur)
        cur = new

    def peek(self):
        cur = self.head
        if cur is not None:
            return cur.value

    def pop(self):
        cur = self.head
        if cur is not None:
            v = cur.value
            if cur.next is not None:
                cur.value = cur.next.value
                cur.next = cur.next.next
            else:
                cur = None
            return v
