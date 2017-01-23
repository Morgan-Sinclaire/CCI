# 1.1
# with sets, O(n) is easy
def is_unique(s):
    return list(s) == list(set(s))

# without sets or anything else, sort the list and go through it in O(nlogn)
def is_unique(s):
    s = sorted(s)
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            return False
    return True

# 1.2
# sort both lists and check for equality in O(nlogn + mlogm)
def is_perm(a,b):
    return sorted(a) == sorted(b)

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

# 1.8
def set_zero(A):
    m,n = A.shape
    rows,cols = [],[]
    for i in range(m):
        for j in range(n):
            if A[i,j] == 0:
                rows.append(i)
                cols.append(j)

    for i in rows:
        A[i] = np.zeros(n)
    for j in cols:
        A[:,j] = np.zeros(m)

    return A

# 1.9
# can't think of a way to use isSubstring effectively, but this just seemed
# like the way I'd do it, running in O(n) where n is the length of each string
def is_rotation(s1,s2):
    if len(s1 != len(s2)):
        return False
    for i in range(len(s1)):
        if s1 == s2[-i:] + s2[:-i]:
            return True
    return False
