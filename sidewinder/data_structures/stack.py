#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

"""
Stack Data Structure.
Source: https://www.youtube.com/watch?v=lVFnq4zbs-g&t=478s

Books example.
Input -> A B C D
Result as stack:
D
C
B
A
"""


class Stack(object):
    def __init__(self):
        """ Constructor."""
        self.items = []

    def push(self, item):
        """ Push (add) function. """
        self.items.append(item)

    def pop(self):
        """ Pop (remove) function. """
        return self.items.pop()

    def is_empty(self):
        """ Check is stack empty (boolean). """
        return self.items == []

    def peek(self):
        if not self.items == []:
            return self.items[-1]

    def get_stack(self):
        """ Get all stack. """
        return self.items


stack = Stack()
print(stack.is_empty())
stack.push('A')
stack.push('B')
print(stack.get_stack())
stack.push('C')
print(stack.get_stack())
stack.pop()
print(stack.get_stack())
print(stack.is_empty())
print(stack.peek())
