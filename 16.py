







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
