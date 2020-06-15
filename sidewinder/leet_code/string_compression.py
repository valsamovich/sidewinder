#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/string-compression/


def run_length_encoding(chars):
    """ Run-length encoding (RLE) """
    # Corner & edge cases.
    if chars == 0:
        return []

    encoding = []
    prev_char = ''
    count = 0

    # Core logic.
    for char_ in chars:
        if char_ != prev_char:
            if prev_char:
                encoding.extend([prev_char, str(count)])
            prev_char = char_
            count = 1
        else:
            count += 1
    else:
        encoding.extend([prev_char, str(count)])
        return encoding


# output data: '3a2b1c
print(run_length_encoding(['a', 'a', 'b', 'b', 'c', 'c', 'c']))
