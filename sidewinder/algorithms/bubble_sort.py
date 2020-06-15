#!/usr/bin/env python2.7
# coding=utf-8


def bubble_sort(lst):
    """ Bubble Sort algorithm."""
    for i in range(0, len(lst) - 1):
        print('i = {}'.format(i))
        for j in range(0, len(lst) - 1 - i):
            print('j = {}'.format(j))
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def bubble_sort_2(lst):
    for j in range(len(lst)):
        check = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                swap = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = swap
                check = True
        if check is False:
            break
    return j, lst


nums = [3, 5, 4, 1, 2, 6, 8, 7]

# print(bubble_sort(nums))
print(bubble_sort_2(nums))


