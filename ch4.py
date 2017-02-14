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


class Operation(object):
    """Evaluates an operation given its string representation."""
    def __init__(self, o):
        self.o = o

    def operate(self, left, right):
        if self.o == '+':
            return left + right
        if self.o == '-':
            return left - right
        if self.o == '*':
            return left * right

class AST(object):
    """Implementation of an Abstract Syntax Tree."""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, n):
        """Take in a tuple of the form (op, num)."""
        self.left = AST(self.value,self.left,self.right)
        self.value = n[0]
        self.right = AST(n[1])

    def evaluate(self):
        """Uses Operation class to recursively evaluate."""
        if type(self.value) == int:
            return int(self.value)
        return Operation(self.value).operate(self.left.evaluate(),
                                             self.right.evaluate())

# a = AST(5)
# print(a.evaluate())
# a.insert(('+', 3))
# print(a.evaluate())
# a.insert(('*', 2))
# print(a.evaluate())
# a.insert(('-', 9))
# print(a.evaluate())



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

# 4.6
def successor(t, i=0):
    if not i:
        t = t.right
        return successor(t.right, 1)

    if t.left is not None:
        return successor(t.left, 1)
    return t.value

# 4.7
def order(projects, dependencies):
    o = []
    t = set(projects)
    for d in dependencies:
        t.remove(d[1])

    while len(t) > 0:
        p = t.pop()
        o.append(p)
        for d in dependencies:
            if d[0] == p:
                t.add(d[1])

    if len(o) < len(projects):
        return "Error"
    return o

# 4.8
def common(t, a, b, a_below=False, b_below=False):
    if t.value == a:
        a_below = True
    if t.value == b:
        b_below = True

    for branch in [t.left, t.right]:
        if branch is not None:
            s = common(branch, a, b, a_below, b_below)
            if type(s) == int:
                return s
            a_below += s[0]
            b_below += s[1]

    if (a_below, b_below) == (1,1):
        return t.value
    return (a_below, b_below)


# 4.9
def merge(a,b):
    if len(a) == 0:
        return [b]
    if len(b) == 0:
        return [a]

    return [[a[0]] + x for x in merge(a[1:],b)] + \
           [[b[0]] + x for x in merge(a,b[1:])]

def sequence(t):
    if t.left is None and t.right is None:
        return [t.value]
    if t.left is None:
        return [t.value + x for x in sequence(t.right)]
    if t.right is None:
        return [t.value + x for x in sequence(t.left)]

    l = []
    for i in sequence(t.left):
        for j in sequence(t.right):
            l += merge(i,j)
    return [t.value + x for x in l]

# 4.10
def same(t1, t2):
    if t1 is None or t2 is None:
        return t1 is None + t2 is None - 1

    if t1.value != t2.value:
        return False

    return same(t1.left, t2.left) and same(t1.right, t2.right)

def subtree(t1, t2):
    if t1.value == t2.value:
        if same(t1, t2):
            return True

    if t1.left is None and t2.left is None:
        return False

    if t1.left is None:
        return subtree(t1.right, t2)

    if t1.right is None:
        return subtree(t1.left, t2)

    return subtree(t1.left, t2) or subtree(t1.right, t2)


# 4.12
def path(t, n):
    num = 0
    if t.value == n:
        num += 1

    if t.left is not None:
        num += path(t.left, n - t.value)

    if t.right is not None:
        num += path(t.right, n - t.value)

    return num
