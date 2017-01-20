import numpy as np

# 8.2
# assumes grid is a numpy array of 0's and 1's, with 1's being forbidden cells
def grid(m):
    r,c = m.shape
    if r == 1 or c == 1:
        return np.sum(m) == 0
    elif m[0,0] == 1:
        return False
    else:
        return grid(m[1:]) or grid(m[:,1:])

# m = np.array([[0, 1],
#               [1, 0]])
# print grid(m)
# m = np.array([[0, 1],
#               [0, 0]])
# print grid(m)
#
# def grid_path(m):
#     r,c = m.shape
#     if r == 1 or c == 1:
#         if np.sum(m) == 0:
#             return m
#         else:
#             pass
#     elif m[0,0] == 1:
#         pass
#     else:
#         return grid(m[1:]) or grid(m[:,1:])


# 8.4
def power(s):
    if len(s) == 1:
        return [s, set([])]
    else:
        m = s.pop()
        p = power(s)
        l = [list(sub) for sub in p]
        print p
        print m
        return set(l + [sub + [m] for sub in l])

# print power(set([1]))
print power(set([1,2]))
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
