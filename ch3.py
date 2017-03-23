class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.next = pointer

# implementation of a Stack
class Stack(object):
    def __init__(self, head=None):
        self.head = head
        if self.head is not None:
            self.min = self.head.value
        else:
            self.min = None
        self.count = 0
        if self.head is not None:
            self.count += 1

    def push(self, n):
        self.head = Node(n, self.head)
        if self.min is None or self.min > n:
            self.min = n
        self.count += 1


    def peek(self):
        cur = self.head
        if cur is not None:
            return cur.value

    def pop(self):
        self.min = None

        cur = self.head
        if cur is None:
            return "empty"

        v = cur.value
        if cur.next is not None:
            cur.value = cur.next.value
            cur.next = cur.next.next
        else:
            self.head = None
        self.count -= 1
        return v


def merge(left, right):
    s = Stack()
    cur = s.head
    if left.peek() < right.peek():





class MyQueue(object):
    def __init__(self):
        pass



# class SetOfStacks(dict):
#     def __init__(self):
#         self.length = 0
#
#     def push(self, n):
#         s = self[]

# not a set, but a list seems to work just as well
class SetOfStacks(list):
    def __init__(self, h=10):
        self.height = h

    def push(self, n):
        if len(self) == 0:
            self.append(Stack(Node(n)))
        else:
            last = self[len(self) - 1]
            if last.count < h:
                last.push(n)
            else:
                self.append(Stack(Node(n)))

    def pop(self):
        if len(self) == 0:
            return "empty"

        last = self[len(self) - 1]
        v = last.pop()
        if last is None:
            self.pop()

        return v

    def popAt(self, i):
        s = self[i]
        if s is None:
            return "empty"
        else:
            return s.pop()



class Queue(object):
    def __init__(self, head=None):
        self.head = head
        self.end = head

    def push(self, n):
        self.end.next = Node(n)
        self.end = self.end.next

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

class DoubleQueue(list):
    def __init__(self):
        self = [Queue(), Queue(), Queue()]

    def enqueue(self, n, species):
        self[2].push(n)
        self[species == "cat"].push(n)

    def dequeueAny(self):
        p = self[2].pop()
        return self[p == self[1].peek()].pop()

    def dequeueSpecies(self, species="cat"):
        p = self[species == "cat"].pop()
        cur = self[2].head
        if p == cur.value:
            if cur.next is None:
                self[2].head = None
            else:
                cur.value = cur.next.value
                cur.next = cur.next.next
            return p
        while p != cur.next.value:
            cur = cur.next

        cur.next = cur.next.next
        return p






        if p == cur.value:
            if cur.next is not None:
                cur.value = cur.next.value
                cur.next = cur.next.next
            else:
                self[2].head = None
            return p
        while cur.next is not None:
            if cur.next.value



# 3.1


# 3.2
# this was implemented in the stack above

# 3.3
# also implemented above

# 3.4
