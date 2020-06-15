#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/palindrome-number/

import time


def is_palindrome(x):
    """ Determine whether an integer is a palindrome. An integer is a
    palindrome when it reads the same backward as forward. """

    # By string conversion.
    return str(x) == str(x)[::-1]

    ''' if x < 0:
        return False

    rev_num = 0
    digit = 0
    while x // (10**digit) != 0:
        rev_num = (rev_num * 10) + (x // (10**digit) % 10)
        digit += 1

    return x == rev_num '''


if __name__ == "__main__":
    for i in [121, -121, 10]:
        start_time = time.time()
        print(is_palindrome(i))
        print("--- %s seconds ---" % (time.time() - start_time))
