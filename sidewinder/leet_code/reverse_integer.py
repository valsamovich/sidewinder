#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/reverse-integer/

inputs = [123, -123, 120, 1534236469]


def reverse(x):
    """ Given a 32-bit signed integer, reverse digits of an integer.

    Assume we are dealing with an environment which could only store integers
    within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose
    of this problem, assume that your function returns 0 when the reversed
    integer overflows. """

    '''# By converting to string.
    if x < 0:
        s = str(x).strip('-')
        return int('-' + s[::-1])
    else:
        return int(str(x)[::-1])'''

    # O(n).
    num = 0
    # Convert to absolute value.
    a = abs(x)

    while a != 0:
        temp = a % 10
        num = num * 10 + temp
        a = a // 10

    if x > 0 and num < 2147483647:
        return num
    elif x < 0 and num <= 2147483647:
        return -num
    else:
        return 0


for i in inputs:
    print(reverse(i))
