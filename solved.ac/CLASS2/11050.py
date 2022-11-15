import math

A,B = map(int, input().split())

print(math.comb(A,B))


# import scipy.special
# print(scipy.special.binom(10,5))

# import scipy.special
# print(scipy.special.comb(10,5))

# import math
# import operator
# from functools import reduce
# product = lambda m,n: reduce(operator.mul, range(m, n+1), 1)
# x = 10
# y = 5
# product(y+1, x) / product(1, x-y)

# from math import factorial as fact

# def binomial(n, r):
#     return fac(n) // fac(r) // fac(n - r)

# print(binomial(10,5))