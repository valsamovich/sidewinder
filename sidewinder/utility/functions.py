#!/usr/bin/env python2.7
# coding=utf-8

n = [1, 2, 3, 4, 5]


# traditional function
def double(x):
    return x * 2

# lambda function
lambda x: 2 * x

# map & lambda example
print list(map(lambda x: x * 2, n))

# filter & lambda example
print list(filter(lambda x: x > 2, n))

# reduce & lambda example
print reduce(lambda x, y: x * y, n)
