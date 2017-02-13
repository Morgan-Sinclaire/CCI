# 1.1
def is_unique(s):
    """With sets, O(n) is easy."""
    return len(list(s)) == len(set(s))

# print(is_unique("abcdef"))
# print(is_unique("abcdea"))

def is_unique(s):
    """
    Without sets or anything else, sort the list and go through it in
    O(nlogn).
    """

    s = sorted(s)
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            return False
    return True

# print(is_unique("abcdef"))
# print(is_unique("abcdea"))

# 1.2
def is_perm(a,b):
    """Sort both lists and check for equality in O(nlogn + mlogm)."""
    return sorted(a) == sorted(b)

# print(is_perm("tommarvoloriddle", "iamlordvoldemort"))
# print(is_perm("tom marvolo riddle", "i am lordVoldemort"))

# 1.3
def urlify(s, n):
    """Iterate through string and replace spaces."""
    end = 0
    for i in range(n):
        if s[i] != ' ':
            end = i
    s = s[:end+1]
    s = s.replace(' ', '%20')
    return s

# print(urlify("Mr John Smith    ", 13))

# 1.4
def permpal(s):
    """
    Run in O(mn), where n is the string length and m is the number of
    unique letters.
    """
    s = s.lower().replace(" ","")
    t = set(s)
    n = 0
    for c in t:
        if s.count(c) % 2 == 1:
            n += 1
    return n <= 1

# print(permpal("Tact Coe"))
# print(permpal("Tact Coa"))

def permpal(s):
    """Alternatively, run in O(nlogn) instead."""
    s = s.lower().replace(" ","")
    a = sorted(s)
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

# print(permpal("Tact Coe"))
# print(permpal("Tact Coa"))

# 1.5
def one_away(a,b):
    """
    Test the cases of replacements separately from
    insertions/deletions.
    """

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

# print(one_away("pale","ple"))
# print(one_away("pales","pale"))
# print(one_away("pale","bale"))
# print(one_away("pale","bake"))

# 1.6
def compress(s):
    """
    Iterate over string, making compressed list that becomes a string.
    Would have been simpler to create string directly,
    but runtime would be higher.
    """
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

# print(compress("aabcccccaaa"))

# 1.7
import numpy as np
def rotate(A):
    """
    For each entry in the upper left quadrant, swap it with the 3
    corresponding entries.
    """
    n = A.shape[0]
    for i in range((n+1) // 2):
        for j in range(n // 2):
            w,x,y,z = A[i,j], A[j,n-i-1], A[n-i-1,n-j-1], A[n-j-1,i]
            A[i,j], A[j,n-i-1], A[n-i-1,n-j-1], A[n-j-1,i] = z,w,x,y

    return A

# m = np.array([range(x,x+3) for x in [1,4,7]])
# print(rotate(m))
# m = np.array([range(x,x+4) for x in [1,5,9,13]])
# print(rotate(m))

def rotate(A):
    """Transpose, then reflect across vertical middle."""
    A = A.T
    n = A.shape[0]
    for i in range(n):
        for j in range(n // 2):
            A[i,j],A[i,n-j-1] = A[i,n-j-1],A[i,j]
    return A

# m = np.array([range(x,x+3) for x in [1,4,7]])
# print(rotate(m))
# m = np.array([range(x,x+4) for x in [1,5,9,13]])
# print(rotate(m))

# 1.8
def set_zero(A):
    """Marks rows and columns, then zeros them out."""
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

# m = np.array([range(x,x+3) for x in [1,4,7]])
# m[1,1] = 0
# print(set_zero(m))
# m = np.array([range(x,x+4) for x in [1,5,9,13]])
# m[1,1] = 0
# m[3,1] = 0
# print(set_zero(m))

# 1.9
def is_rotation(s1,s2):
    """
    Can't think of a way to use isSubstring effectively, but this just
    seemed like the way I'd do it, running in O(n) where n is the
    length of each string.
    """
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1 == s2[-i:] + s2[:-i]:
            return True
    return False

# print(is_rotation("waterbottle", "erbottlewat"))
# print(is_rotation("waterbottle", "erbattlewat"))
