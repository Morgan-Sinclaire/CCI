import numpy as np
import sys

# recursion warm-up
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# my first memoized function, shamelessly taken from the chapter
def fib(n, memo=[]):
    if memo == []:
        memo=[0]*(n+1)

    if n == 0 or n == 1:
        return n
    elif memo[n] == 0:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)

    return memo[n]

def fib(n, last=1, penult=0):
    if n == 1:
        return last + penult
    return fib(n-1, last + penult, last)

# sys.setrecursionlimit(1000000)
# print fib(10000)

# bottom-up methods
def fib(n):
    memo = [0]*(n+1)
    for i in range(n + 1):
        if i <= 2:
            memo[i] = 1
        else:
            memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

def fib(n):
    if n in [1,2]:
        return 1
    a,b = 1,1
    for i in range(n-2):
        a,b = a+b,a
    return a

# 8.1
# top-down
def stair(n, prev_1=1, prev_2=0, prev_3=0):
    if n == 1:
        return prev_1 + prev_2 + prev_3
    return stair(n - 1, prev_1 + prev_2 + prev_3, prev_1, prev_2)

# bottom-up
def stair(n):
    if n in [1,2]:
        return n
    if n == 3:
        return 4
    a,b,c = 4,2,1
    for i in range(n-3):
        a,b,c = a+b+c,a,b
    return a

# print(stair(100000))

# 8.2
# assumes grid is a numpy array of 0's and 1's, with 1's being forbidden cells

# as a warm-up, grid() will simply return whether or not a path exists
def grid(m):
    r,c = m.shape
    if r == 1 or c == 1:
        return np.sum(m) == 0
    elif m[0,0] == 1:
        return False
    else:
        return grid(m[1:]) or grid(m[:,1:])

# grid_path() will return a matrix with 0's representing a specific path
# if none exists, returns false
def grid_path(m):
    r,c = m.shape
    if np.sum(m) == 0:
        a = np.ones(m.shape)
        a[0] = 0
        a[:,-1] = 0
        return a
    elif m[0,0] == 1:
        return False
    elif grid_path(m[1:]) is not False:
        a = np.ones((1,c))
        a[0,0] = 0
        return np.concatenate((a, grid_path(m[1:])), axis=0)
    elif grid_path(m[:,1:]) is not False:
        a = np.ones((r,1))
        a[0,0] = 0
        return np.concatenate((a, grid_path(m[:,1:])), axis=1)
    else:
        return False

# m = np.array([[0, 1],
#               [1, 0]])
# print grid(m)
# print grid_path(m)
# m = np.array([[0, 1],
#               [0, 0]])
# print grid(m)
# print grid_path(m)
# m = np.array([[0, 0, 1],
#               [0, 0, 0],
#               [1, 0, 0]])
# print grid(m)
# print grid_path(m)

# 8.3
# iterative O(n) solution
def magic(a):
    for i in xrange(len(a)):
        if a[i] == i:
            return i
    return False

# O(log n) solution, assuming ascending distinct values
def magic(a, index=0):
    mid = len(a) / 2
    split = a[mid]
    if split == mid + index:
        return split
    elif len(a) == 1:
        return False
    elif split > mid + index:
        return magic(a[:mid], index)
    elif split < mid + index:
        index += mid+1
        return magic(a[mid+1:], index)

print magic([-1,0,1,3,6])
print magic([-1,0,1,4,6])

# O(log n) solution, assuming ascending but possibly repeated values
def magic2(a):
    return magic(list(set(a)))

print magic([0,0,1,4,6])

# 8.4
def power(s):
    if len(s) == 1:
        return [s, set([])]
    else:
        m = s.pop()
        p = power(s)
        l = [list(sub) for sub in p]
        return map(set, l + [sub + [m] for sub in l])

# print power(set([1]))
# print power(set([1,2]))
# print power(set([1,2,3]))

# 8.5
def mult(a,b):
    if a == 0 or b == 0:
        return 0
    else:
        return a + mult(a, b-1)

# print mult(3,5)

# 8.6
# uses that (6 - start - end) yields the extra peg, assuming they're labeled (1,2,3)
def tower(n, start=1, end=3):
    if n == 1:
        return [(start, end)]
    else:
        return tower(n-1, start, 6-start-end) + \
               [(start,end)] + \
               tower(n-1, 6-start-end, end)

# 8.7
def perm(s):
    if len(s) == 1:
        return [s]
    else:
        f = s[0]
        l = []
        for p in perm(s[1:]):
            for i in xrange(len(p) + 1):
                l.append(p[:i] + f + p[i:])
        return l

# print perm("ab")
# print perm("abc")

# 8.8
def perm(s):
    if len(s) == 1:
        return [s]
    else:
        f = s[0]
        l = []
        for p in perm(s[1:]):
            for i in xrange(len(p) + 1):
                l.append(p[:i] + f + p[i:])
        return list(set(l))

# print(perm("ab"))
# print(perm("abc"))
# print(perm("aac"))

# 8.9
def parens(n):
    s = set()
    if n == 1:
        s.add("()")
    else:
        for i in parens(n-1):
            s.add("()" + i)
            s.add(i + "()")
            s.add("(" + i + ")")
    return s

# print(parens(3))

# 8.10
def fill(a, p, color, old=None):
    i,j = p[0], p[1]
    if old is None:
        old = a[i,j]
    if a[i,j] != color and a[i,j] == old:
        a[i,j] = color
        if i > 0:
            fill(a, [i-1,j], color, old)
        if i < a.shape[0] - 1:
            fill(a, [i+1,j], color, old)
        if j > 0:
            fill(a, [i,j-1], color, old)
        if j < a.shape[0] - 1:
            fill(a, [i,j+1], color, old)
    return a

# a = np.chararray((5, 5))
# print(fill(a, (2,2), 'y'))

# 8.11
# assumes we only have pennies, nickels, and dimes
def dimes(n):
    return n // 10 + 1

# breaks it down into simpler problem
def quarters(n):
    total = 0
    for i in range(n // 25 + 1):
        total += dimes(n - 25 * i)
    return total
