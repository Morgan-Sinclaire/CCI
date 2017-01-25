import math

def select_sort(a):
    for i in xrange(len(a) - 1):
        m = a.index(min(a[i:]))
        a[i], a[m] = a[m], a[i]

    return a

def bubble_sort(a):
    for i in xrange(len(a)):
        c = 0
        for j in xrange(len(a) - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                c += 1
        if c == 0:
            return a

def insertion_sort(a):
    for i in xrange(1, len(a)):
        j = i
        while j >= 1:
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                j -= 1
            else:
                break

def bucket_sort(a, b=5):
    lower,upper = min(a),max(a)
    partitions = [lower + i*(upper-lower)/b for i in range(1, b+1)]
    buckets = [[] for i in xrange(b)]
    for num in a:
        for i in xrange(len(partitions)):
            if num < p[i]:
                b[i].append(num)
                break

    for bucket in buckets:
        bucket = bucket_sort(bucket, b)

    return [x for x in bucket for bucket in buckets]

def radix_sort(a):
    digits = int(math.log10(max(a))) + 1
    for i in xrange(digits):
        for num in a:
            buckets = [[] for j in xrange(10)]
            buckets[num % 10 ** i].append(num)
            a = [x for x in bucket for bucket in buckets]

    return a

def merge(left, right):
    i = j = 0
    l = len(left)
    r = len(right)
    result = left + right
    while i < l and j < r:
        if left[i] <= right[j]:
            result[i+j] = left[i]
            i += 1
        else:
            result[i+j] = right[j]
            j += 1

    for k in xrange(i, l):
        result[k+j] = left[k]

    return result

def merge_sort(a):
    if len(a) == 1:
        return a

    mid = len(a) / 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)

def ackermann(m,n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n-1))

def worst_sort(a):
    n = len(a)
    ackermann(n,n)
    return quick_sort(a)


a = [170, 45, 75, 90, 802, 2, 24, 66]
# print select_sort(a)
# print merge_sort(a)

# searches for a number n in a sorted list a
def binary_search(a, n):
    mid = len(a) / 2
    if a[mid] == n:
        return mid
    if a[mid] > n:
        return binary_search(a[:mid], n)
    if a[mid] < n:
        return mid + 1 + binary_search(a[mid + 1:], n)

# print binary_search(sorted(a), 170)

# 10.1
# already implemented this above
def sorted_merge(left, right):
    return merge(left, right)

# 10.2
def sort_anagrams(a):
    b = [''.join(sorted(x)) for x in a]
    b = [(b[i], i) for i in xrange(len(b))]
    b = sorted(b, key=lambda x: x[0])
    b = [(b[i][1], i) for i in xrange(len(b))]

    c = []
    for pair in b:
        c.append(a[pair[0]])

    return c

# 10.3
# finds the index where the lowest number is in O(log(n))
def find_rotation_point(a):
    l = len(a)
    if l == 2:
        return a[0] < a[1]
    lower = a[0]
    upper = a[l/2]
    if upper < lower:
        return find_rotation_point(a[l/2 + 1])
    if upper > lower:
        return l/2 + find_rotation_point(a[l/2:])

# splits the list into the two sorted lists
def rotated_search(a, n):
    r = find_rotation_point(a)
    if a[-1] == n:
        return len(a) - 1
    if a[-1] < n:
        return binary_search(a[:r], n)
    if a[-1] > n:
        return r + binary_search(a[r:], n)

# 10.4
# finds the last index of listy, runs in O((log(n))^2) time
def find_end(a, l=0):
    i = 1
    x = a[i-1]
    if x == -1:
        return l
    while x != -1:
        i *= 2
        x = a[i-1]
    l += i
    return find_end(a[i/2], l)

def search_listy(a, n):
    size = find_end(a)
    # we can now effectively treat listy as an actual list
    return binary_search(a,n)
