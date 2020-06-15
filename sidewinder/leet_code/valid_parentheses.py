#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/valid-parentheses/


def is_valid(s):
    parentheses = {'(': ')', '[': ']', '{': '}'}
    stack = []

    for bracket in s:
        if bracket in parentheses:
            stack.append(parentheses[bracket])
        elif not stack or bracket != stack.pop():
            return False
    return not stack


is_valid('()[]')
