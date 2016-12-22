






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

print permpal("tacocat")
print permpal("permpal")
