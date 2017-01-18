# 6.1
# Take 1 pill from the first bottle, 2 from the second, and so on, and weigh
# the 210 pills. For the resulting weight w, (w - 210) / .1 gives the number of
# pills with weight 1.1 grams, and thus the bottle with those pills.

# 6.2
# The chance of winning each game is:
# 1: p
# 2: p^3 + 3(1-p)p^2
# We need to find what values of p make (2) > (1). After doing some algebra, we
# see that this is true iff 3p - 2p^2 > 1, and solving this quadratic, we get
# .5 < p < 1 (with .5 being where they're equal).
# Intuitively, it should be clear that if p > .5, then it should make sense to
# play more games, since you're less likely to get multiple fluke results than
# one fluke.

# 6.3
# If we have a black-and-white checkered board, then the two diagonally opposite
# squares are the same color, leaving e.g. 30 white and 32 black squares. But
# each domino would itself cover one white and one black, so we cannot cover
# two black squares no matter the arrangement.

# 6.4
# The only situation where they don't collide is when they all pick the same
# direction, since otherwise at least two ants will collide eventually. The
# first ant's choice is arbitray, but all other must conform, so the probability
# of collision is 1 - .5^(n-1).

# 6.5
# Fill 3-quart, pour into 5-squart. Fill 3-squart again, pouring into 5-squart
# until it is full, leaving 1 quart left in 3-quart. Dump out 5-quart, pour
# available 1 quart into it. Fill 3-quart again, dump into 5-quart, leaving 4
# quarts in there.
