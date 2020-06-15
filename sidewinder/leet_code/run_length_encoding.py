#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/string-compression/


def run_length_encoding(chars):
    """ Run-length encoding (RLE) """
    # Corner & edge cases.
    if chars == 0:
        return ''

    encoding = ''
    prev_char = ''
    count = 0

    # Core logic.
    for char in chars:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            prev_char = char
            count = 1
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding


# output data: '3a2b1c
print(run_length_encoding('aaabbc'))
