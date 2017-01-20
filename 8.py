import numpy as np

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

# 8.6
# uses that (6 - start - end) yields the extra peg, assuming they're labeled (1,2,3)
def tower(n, start=1, end=3):
    if n == 1:
        return [(start, end)]
    else:
        return tower(n-1, start, 6-start-end) + \
               [(start,end)] + \
               tower(n-1, 6-start-end, end)

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

# print perm("ab")
# print perm("abc")
# print perm("aac")
