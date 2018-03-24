#!/usr/bin/env python2.7
# coding=utf-8

LST = [4, 2, 3, 2, 1, 1, 5]


def map_reduce(lst):
    """
    Map values and reduce based on key.

    :param lst: list of values.
    :return: map of values.
    """

    dct = {}
    for num in lst:
        if num in dct:
            print '{} key exists. updating value'.format(num)
            dct[num] += 1
        else:
            print 'new key {}'.format(num)
            dct[num] = 1
    return dct


print map_reduce(LST)