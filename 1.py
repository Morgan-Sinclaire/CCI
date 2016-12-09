






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
