# 8.6
# uses that 6-start-end yields the extra peg, assuming they're labeled (1,2,3)
def tower(n, start=1, end=3):
    if n == 1:
        return [(start, end)]
    else:
        return tower(n-1, start, 6-start-end) +
               [(start,end)] +
               tower(n-1, 6-start-end, end)
