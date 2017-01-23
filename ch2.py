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

    def insert_list(self, l):
        for i in l:
            self.insert(i)

    def __iter__(self):
        cur = self
        while cur.next != None:
            cur = cur.next
            yield cur.value

    def __str__(self):
        return str(list(self))

ll = LL()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert_list(range(10))
print ll

    # 2.1
    # def remove_dups(self):
    #     cur = self.next
    #     temp = self.next.next
    #     while temp != None:
    #         if cur.value == temp.value:
