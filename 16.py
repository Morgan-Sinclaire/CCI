







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

# 16.7
def bigger(a,b):
    pass
