#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/longest-common-prefix/


def longest_common_prefix(strs):
    """ Write a function to find the longest common prefix string amongst
    an array of strings. If there is no common prefix, return an empty
    string ''. """

    # Corner cases/basic cases.
    if len(strs) == 0:
        return ''
    if len(strs) == 1:
        return strs[0]

    # Add core logic.
    prefix = strs[0]
    prefix_len = len(prefix)

    # Loop over words, but not 1st one.
    for s in strs[1:]:
        while prefix != s[0:prefix_len]:
            prefix = prefix[0:(prefix_len - 1)]
            prefix_len -= 1
            if prefix_len == 0:
                return ''

    return prefix


for i in [[], ['rocket'], ['flower', 'flow', 'flight'], ["dog","racecar","car"]]:
    print(longest_common_prefix(i))
