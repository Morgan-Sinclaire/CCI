# 16.1
# I have no idea what this is asking :(

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

print(min_dif([1,3,15,11,2], [23,127,235,19,8]))

# 16.7
# this problem is dumb and hilarious
def bigger(a,b):
    return (a,b)[str(a-b)[0] in ['-']]
