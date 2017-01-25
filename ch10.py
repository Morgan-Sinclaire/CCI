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
