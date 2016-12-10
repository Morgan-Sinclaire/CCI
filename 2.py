# implementation of a Linked List
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LL(object):
    def __init__(self):
        self.next = None

    def append(self, value):
        cur = self
        while cur.next != None:
            cur = cur.next
        cur.next = Node(value)
        return self

    def insert(self, value):
        new = Node(value)
        new.next = self.next
        self.next = new
        return self

    def __iter__(self):
        cur = self
        while cur.next != None:
            cur = cur.next
            yield cur.value

    def __str__(self):
        return str(list(self))

    # 2.1
    def remove_dups(self):
        cur = self.next
        temp = self.next.next
        while temp != None:
            if cur.value == temp.value:

        # out = ""
        # cur = self
        # while cur.next != None:
        #     cur = cur.next
        #     out += str(cur.value) + " "
        # return out
        return str(list(self))
