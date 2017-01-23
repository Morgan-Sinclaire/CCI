# from 2 import Node,LL
#
from stuff import Node,LL

ll = LL()
ll.insert(5)
print ll

class binary_tree(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def stuff(self):
        if self.value != None:
            print self.value
            self.left.stuff()
            # stuff(self.right)

    # def stuff(self, l=[]):
    #     while self.value != None:
    #         l.append(self.value)
    #         stuff(self.left, l)
    #         stuff(self.right, l)

# t = binary_tree(4, None, None)
# t.stuff()


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
def linked(t, list=False):
    ll = LL()




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
def validate(t, lower=[], upper=[]):
    if t != None:
        if lower != [] and t.value < lower:
            return False
        if upper != [] and t.value > upper:
            return False
        return validate(t.left, lower, t.value) \
           and validate(t.right, t.value, upper)
    return True

# t = binary_tree(5, binary_tree(3), binary_tree(6))
# print validate(t)
