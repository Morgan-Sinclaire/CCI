# 16.1
# I assume this is asking to reverse the digits of the number
def swap(n):
    if n / 10 == 0:
        return n
    else:
        return int(str(n % 10) + str(swap(n / 10)))


# 16.2
# we assume the book is given as a string, so we can just use count
# if this were run multiple times for different words, we could just use
# collections.Counter (I recognize splitting on whitespace isn't perfect,
# but it would be hard to cover commas, periods, etc. comprehensively)
def freq(word, book):
    c = book.count(word)
    text = book.split()
    return float(c/len(text))

# 16.3
# we assume the lines are of the form ((x1, y1), (x2, y2)) and do algebra
def intersect(a,b):
    m1 = float(a[1][1] - a[0][1]) / (a[1][0] - a[0][0])
    m2 = float(b[1][1] - b[0][1]) / (b[1][0] - b[0][0])

    if m1 == m2:
        return "No intersection: lines are parallel"

    x = (b[0][1] - a[0][1] + m1*a[0][0] - m2*b[0][0]) / (m1 - m2)

    if x >= a[0][0] and x >= b[0][0] and x <= a[1][0] and x <= b[1][0]:
        return (x, m1*(x - a[0][0]) + a[0][1])
    else:
        return "No intersection"

# 16.4
# assume a 3x3 numpy array with 1 for X, 2 for O, 0 for blank
import numpy as np
def ttt_win(m):
    for i in range(3):
        if sum(m[i]) % 3 == 0 or sum(m[:,i]) % 3 == 0:
            return True

    if sum([m[i,i] for i in range(3)]) % 3 == 0:
        return True

    if sum([m[3-i-1,i] for i in range(3)]) % 3 == 0:
        return True

    return False

# 16.5
# the number of trailing zeros is just the number of times we multiply 2 and 5
# since there's always more 2's than 5's in a factorial, we just count the latter
def trailing(n):
    return n / 5

# just kidding! that last solution fails for n >= 25, but this generalizes
def trailing(n):
    count = 0
    p = 1
    while n / (5**p):
        count += n / (5**p)
        p += 1
    return count

# this is the simplest solution I could come up with
def trailing(n):
    if n / 5:
        return n / 5 + trailing(n / 5)
    else:
        return 0

# 16.6
# sorts each list, then simply compares the closest values in each list
# runs in O(mlogm + nlogn + m + n) = O(mlogm + nlogn)
def min_dif(a,b):
    a,b = sorted(a),sorted(b)
    m = abs(a[0] - b[0])
    while a != [] and b != []:
        d = abs(a[0] - b[0])
        if d < m:
            m = d
        if a[0] < b[0]:
            a = a[1:]
        elif a[0] > b[0]:
            b = b[1:]
        else:
            return 0
    return m

# print(min_dif([1,3,15,11,2], [23,127,235,19,8]))

# 16.7
# this problem is dumb and hilarious
def bigger(a,b):
    return (a,b)[str(a-b)[0] in ['-']]

# 16.8
# I don't think there's an elegant way to do this; to be accurate, we would have to
# hard code in words like this: https://en.wikipedia.org/wiki/Names_of_large_numbers

# 16.9
# not sure if "+= -1" is cheating, but not sure how else to do subtraction
def multiply(a,b):
    p = 0
    for i in range(b):
        p += a
    return p

def subtract(a,b):
    for i in range(b):
        a += -1
    return a

def divide(a,b):
    q = 0
    while a > b:
        q += 1
        a = subtract(a,b)
    return q

# 16.10
# if the current year never grows, runs in O(n), where n is the number of people
def alive(people):
    y = 1900
    m = 0
    for i in xrange(1900,2017):
        n = 0
        for p in people:
            if i >= p[0] and i <= p[1]:
                n += 1
        if n > m:
            y,m = i,n
    return y

# 16.11
# straightforward
def length(shorter, longer, k):
    return range(shorter*k, longer*k, longer - shorter) + [longer*k]

# 16.12


# 16.13
# assumes a square is given as ((x,y), l), the center coordinates and side length
# note we just need the centers, since any line through there bisects the square
def split(s1, s2):
    m = float(s2[0][1] - s1[0][1]) / (s2[0][0] - s1[0][0])
    return "y = {:.2f}(x - {}) + {}".format(m, s1[0][0], s1[0][1])

# print split(((-2,4), 3), ((4,9), 5))

# 16.14
# def best_line(points):
#     m = 1
#     best = (points[0][0], points[0][1], 0)
#     for i in points:
#         for j in points:
#             line = points
#             pass

# 16.15

# 16.16
def gl(a):
    g,l = [], []
    x = a[0]
    for n in a:
        if n > x:
            x = n
        g.append(x)
    x = a[-1]
    for n in a[::-1]:
        if n < x:
            x = n
        l.append(x)
    return g, l[::-1]

def sub_sort(a):
    g,l = gl(a)
    for i in range(len(a)):
        if a[i] != l[i]: break
    left = i
    for i in range(len(a) - 1, -1, -1):
        if a[i] != g[i]: break
    right = i
    return left,right

# a = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
# print sub_sort(a)

# # 16.17
# def contiguous(a):
#     m = max(a)



# 16.20
def t9(n, words):
    """
    Maintain a list of viable words, filter them out at each digit.
    Also, make sure word lengths are appropriate.
    """
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(str(n))):
        d = int(str(n)[i])
        if d == 1:
            return []
        elif d <= 6:
            words = [w for w in words if w[i] in alpha[(d-2)*3:(d-1)*3]]
        elif d == 7:
            words = [w for w in words if w[i] in "pqrs"]
        elif d == 8:
            words = [w for w in words if w[i] in "tuv"]
        elif d == 9:
            words = [w for w in words if w[i] in "wxyz"]

    return [w for w in words if len(w) == len(str(n))]

print(t9(8733, ["tree", "trees", "used", "note", "wall", "rain"]))

# 16.24
# def pairs(l, n):
#     p = []
#     for i in l:
#         m = n - i
#         for j in l:
#             if j == m:
#                 p.append((i,j))
#     return p
