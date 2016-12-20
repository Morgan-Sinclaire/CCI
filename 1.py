






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
def permpal(s):
    t = set(s)
    n = 0
    for c in t:
        if s.count(c) % 2 == 1:
            n += 1
    return n <= 1

print permpal("tacocat")
print permpal("permpal")
