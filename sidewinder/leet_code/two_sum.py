#!/usr/bin/env python7.7
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/two-sum/

def two_sum(nums, target):
    """ Given an array of integers, return indices of the two numbers such
    that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you
    may not use the same element twice."""

    '''# Brute force O(n^2).
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]'''

    # O(n).
    seen = {}
    for i, j in enumerate(nums):
        if target - j in seen:
            return [seen[target - j], i]
        elif j is not seen:
            seen[j] = i


two_sum([1, 2, 12, 7], 9)
