#!/usr/bin/env python2.7
# coding=utf-8

from multiprocessing import Pool


def f(x):
    """ Worker thread logic.

    :param x:   Input parameter, value, etc...
    :return:    Result.
    """
    if x[1] in 'int':
        return x[0] * x[0]
    else:
        return None


if __name__ == '__main__':
    # specify number of pools
    p = Pool(processes=2)
    print(p.map(f, [[2, 'string'], [3, 'int'], [4, 'int']]))
