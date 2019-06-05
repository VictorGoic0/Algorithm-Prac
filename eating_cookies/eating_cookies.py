#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
# Can eat 3, 2, or 1 cookie(s) at a time

def eating_cookies(n, cache={0: 1, 1: 1, 2: 2, 3: 4}):
  if n in cache:
    return cache[n]
  else:
    cache[n] = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    return cache[n]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')

# 2 cookies:
# 2
# 1 1

# 3 cookies:
# 3
# 1 2
# 2 1
# 1 1 1
# 4 ways

# 4 cookies:
# 3 1
# 1 3
# 1 1 1 1
# 2 1 1
# 1 1 2
# 1 2 1
# 6 ways

# 5 cookies:
# 3 1 1
# 1 3 1
# 1 1 3
# 1 1 1 1 1
# 2 1 1 1
# 1 2 1 1
# 1 1 2 1
# 1 1 1 2
# 3 2
# 2 3
# 13 ways

# 6 cookies:
# 3 3
# 3 2 1
# 3 1 2
# 2 3 1
# 2 1 3
# 1 2 3
# 1 3 2
# 1 1 1 1 1 1
# 2 2 1 1
# 2 1 2 1
# 2 1 1 2
# 1 1 2 2
# 1 2 1 2
# 1 2 2 1
# 2 1 1 1 1
# 1 2 1 1 1
# 1 1 2 1 1
# 1 1 1 2 1
# 1 1 1 1 2
# 19 ways ? ?