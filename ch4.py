from ch2 import Node,LL

# ll = LL()
# ll.insert(5)
# print ll

class BinaryTree(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, n):
        if self.value == None:
            self.value = n
        elif n <= self.value:
            if self.left == None:
                self.left = BinaryTree(n)
            else:
                self.left.insert(n)
        elif n > self.value:
            if self.right == None:
                self.right = BinaryTree(n)
            else:
                self.right.insert(n)

    def find(self, n):
        if self.value == n:
            return True
        elif n < self.value:
            if self.left == None:
                return False
            return self.left.find(n)
        elif n > self.value:
            if self.right == None:
                return False
            return self.right.find(n)



t = BinaryTree(4, None, None)


# 4.2
def minimal(a):
    t = binary_tree(None, None, None)
    i = 0
    while i < len(a):
        if t.value == None:
            t.value = a[i]
        elif t.left != None and t.right == None:
            t.right = a[i]
        else:
            t.left = t
            t.value = a[i]

        i += 1

    return t

# 4.3
def linked(t):
    l = []
    while t != None:
        l.append(linked_layer(t))

def linked_layer(t, depth=0, l=[]):
    if t == None:
        return
    if str(type(t)) != "<type 'list'>":
        t = [t]
    sub = []
    for i in t:
        sub.append(t.value)
    l.append(sub)


# def linked(t, depth=0, l=[]):
#     if t != None:
#         l.append([t.value])
#         l.append(linked(t.left) + linked(t.right))
#         return l

def linked(t):
    tag(t)

def tag(t, depth=0):
    if t != None:
        t.value = (t.value, depth)
        tag(t.left, depth+1)
        tag(t.right, depth+1)


# 4.4
def max_depth(t):
    if t == None:
        return 0
    else:
        return 1 + max(max_depth(t.left), max_depth(t.right))

def min_depth(t):
    if t == None:
        return 0
    else:
        return 1 + min(min_depth(t.left), min_depth(t.right))

def balanced(t):
    return max_depth(t) - min_depth(t) <= 1

# t = binary_tree(5, binary_tree(3, binary_tree(4)))
# print min_depth(t)
# print max_depth(t)

# 4.5
def validate(t, lower=None, upper=None):
    if t != None:
        if lower != None and t.value < lower:
            return False
        if upper != None and t.value > upper:
            return False
        return validate(t.left, lower, t.value) \
           and validate(t.right, t.value, upper)
    return True

# t = binary_tree(5, binary_tree(8), binary_tree(6))
# print validate(t)
