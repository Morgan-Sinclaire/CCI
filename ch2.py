# implementation of a Linked List
class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.next = pointer

class LL(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, n):
        new = Node(n, self.head)
        self.head = new

    def size(self):
        cur = self.head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count


# class Node(object):
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class LL(object):
#     def __init__(self):
#         self.next = None
#
#     def append(self, value):
#         cur = self
#         while cur.next != None:
#             cur = cur.next
#         cur.next = Node(value)
#
#     def insert(self, value):
#         new = Node(value)
#         new.next = self.next
#         self.next = new
#         return self
#
#     def insert_list(self, l):
#         for i in l:
#             self.insert(i)
#
#     def __iter__(self):
#         cur = self
#         while cur.next != None:
#             cur = cur.next
#             yield cur.value
#
#     def __str__(self):
#         return str(list(self))

# class LL(object):
#     def __init__(self, value=None, pointer=None):
#         self.value = value
#         self.next = pointer
#
#     def insert(self, n):
#         return LL(n, self)
#
#     def insert_list(self, l):
#         cur = self
#         for i in l:
#             cur = LL(i, cur)
#         return cur
#
#     def __iter__(self):
#         cur = self
#         while cur != None:
#             yield cur.value
#             cur = cur.next
#
#     def __str__(self):
#         return str(list(self))


# ll = LL()
# ll = ll.insert(1)
# ll = ll.insert(2)
# ll = ll.insert(3)
# ll = ll.insert(4)
# ll = ll.insert(5)
# print ll
# print ll.value, ll.next
# print ll.next.value
# print ll.next.next
# print ""

# ll = ll.insert(3)

# ll = ll.insert_list(range(5,8))
# print ll.value, ll.next
# print ll.next.value
# print ll.next.next.value
# print ll.next.next.next.value
# print ll.next.next.next.next.value


# print ll


# ll = LL()
# print ll.value, ll.next
# ll.insert(1)
# print ll.value, ll.next
# print ll.next.value
# print ll.next.next.value

# ll.insert(2)
# ll.insert(3)
# ll.insert_list(range(10))
# print ll.next.value
# cur = ll
# while cur.next != None:
#     print cur.value
#     cur = cur.next

    # 2.1
    def remove_dups(ll):
        s = set([])
        cur = ll.head
        while cur != None:
            s.add(cur.value)
        ll.head = None
        while len(s) > 0:
            ll.insert(s.pop())
        return ll

    def remove_dups(ll):
        cur = ll.head.next
        while cur != None:
            temp = ll.head
            while temp is not cur:
                if temp.value == cur.value:
                    temp.value = temp.next.value
                    temp.next = temp.next.next
                temp = temp.next
            cur = cur.next
        return(ll)


    # 2.2
    def kth_last(ll):
        s = size(ll):
        count = s
        cur = ll.head:
        while count > k:
            cur = cur.next
            count -= 1
        return cur.value

    # 2.3
    def delete_middle(node):
        node.value = node.next.value
        node.next = node.next.next

    # 2.4
    def partition(ll, n):
        left = right = LL()
        cur = ll.head
        while cur != None:
            if cur.value < n:
                left.insert(n)
            else:
                right.insert(n)
            cur = cur.next
        cur = left.head
        while cur.next != None:
            cur = cur.next
        cur.next = right.head
        ll.head = left.head
        return ll

# 2.5
def sum_backward(ll):
    cur = ll.head
    total = 0
    index = 0
    while cur != None:
        total += cur.value * 10 ** index
        index += 1
        cur = cur.next
    return total

def sum_forward(ll):
    cur = ll.head
    total = 0
    index = -1
    while cur != None:
        total += cur.value * 10 ** index
        index -= 1
        cur = cur.next

    total *= 10 ** index
    return total

def sum_lists(left, right, backward=True):
    if backward:
        return sum_backward(left) + sum_backward(right)
    else:
        return sum_forward(left) + sum_forward(right)

# 2.6
def palindrome(ll):
    s = ""
    cur = ll.head
    while cur != None:
        s += cur.value
        cur = cur.next

    m = len(s)
    return s[:m/2] == s[(m+1)/2::-1]

# 2.7
def intersection(left, right):
    l_cur = left.head
    r_cur = right.head
    while l_cur.next != None:
        l_cur = l_cur.next
    while r_cur.next != None:
        r_cur = r_cur.next
    return l_cur is r_cur

# 2.8
def loop(ll):
    slow = ll.head
    if slow.next is None:
        return False
    fast = ll.head.next
    while fast.next is not None:
        if slow is fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False
