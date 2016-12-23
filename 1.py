






# 1.1
# sort the list, then go through it, taking O(nlogn) time

# 1.2
# sort both lists, check for equality

# 1.3
def URLify(s, n):
    end = 0
    for i in xrange(n):
        if s[i] != ' ':
            end = i
    s = s[:end+1]
    s = s.replace(' ', '%20')
    return s

# 1.4
# runs in O(mn), where n is the string length and m is the number of unique letters
def permpal(s):
    t = set(s)
    n = 0
    for c in t:
        if s.count(c) % 2 == 1:
            n += 1
    return n <= 1

# alternatively, this runs in O(nlogn) instead
def permpal(s):
    a = sorted("".join(s.split()))
    lengths = []
    count = 1

    for i in range(len(a) - 1):
        if a[i] != a[i+1]:
            lengths.append(count)
            count = 1
        else:
            count += 1
    lengths.append(count)

    return sum([i % 2 for i in lengths]) <= 1

# 1.5
# tests the cases of replacements separately from insertions/deletions
def one_away(a,b):
    d = len(a) - len(b)
    if d < 0:
        a,b = b,a

    if d == 0:
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
        return count <= 1

    elif d == 1:
        for i in range(len(a)):
            if b == a[:i] + a[i+1:]:
                return True
        return False

    else:
        return False

# 1.6
# reused the for-loop from my second solution of 1.4
def compress(s):
    lengths = []
    count = 1

    for i in range(len(s) - 1):
        if s[i] != s[i+1]:
            lengths.append(s[i] + str(count))
            count = 1
        else:
            count += 1
    lengths.append(s[-1] + str(count))

    compr = "".join(lengths)

    if len(compr) < len(s):
        return compr
    else:
        return s

# 1.7
# for each entry in the upper left quadrant, swaps it with the 3 corresponding entries
# could have also transposed and reflected but I thought of this first
import numpy as np
def rotate(A):
    n = A.shape[0]
    for i in range((n+1) / 2):
        for j in range(n / 2):
            w,x,y,z = A[i,j], A[j,n-i-1], A[n-i-1,n-j-1], A[n-j-1,i]
            A[i,j], A[j,n-i-1], A[n-i-1,n-j-1], A[n-j-1,i] = z,w,x,y

    return A
