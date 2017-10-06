#!/usr/bin/env python2.7
# coding=utf-8

"""
Script contain example how to use n NumPy & NumPy Array(s) - ndarray. It
contains a collection of tools and techniques that can be used to solve on a
computer mathematical models of problems in Science and Engineering.
"""

import numpy as np


def to_string(val):
    """
    Convert value to string and return.
    :param val: Input value.
    :return:    string
    """
    return str(val)


def create_array():
    """
    Print different types of arrays.
    """
    # one dimension array.
    print 'One dimension array.'
    print np.array([1, 2, 3])
    # two dimension array.
    print 'Two dimension array.'
    print np.array([[1, 2], [3, 4]])


def array_attributes():
    """
    Print attributes of the array.
    """
    # 2 dimension array
    array_2d = np.array([[1, 2], [3, 4]])
    print 'Raw 2d array:'
    print array_2d
    print 'Out of memory address ... {}'.format(to_string(array_2d.data))
    print 'Data type of array ...... {}'.format(to_string(array_2d.dtype))
    print 'Size of the array ....... {}'.format(to_string(array_2d.shape))
    print 'Stride of the array ..... {}'.format(to_string(array_2d.strides))


def empty_array():
    """
    Empty NumPy Array.
    :return:
    """
    # create array of ones: 3 rows, 4 columns
    print np.ones((3, 4))
    # create array of zeros
    print np.zeros((2, 3, 4), dtype=np.float16)
    # create array with random values
    print np.random.random((2, 2))
    # create a full array
    print np.full((2, 2), 122, dtype=np.int16)


def read_file():
    """
    Read files.
    """
    # Import your data
    # TODO: not working, need a fix.
    data = np.loadtxt('np_data.txt', skiprows=1)
    print data


def slicing():
    """
    Slicing & Indexing.
    :return:
    """
    print 'Slicing for 1 dimensional array.'
    arr = np.arange(10)
    print arr
    print arr[2:]
    print arr[2:5]
    print 'Slicing multi-dimensional ndarray'
    arr = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
    print arr
    print arr[1:]
    # print values in 2nd column
    print arr[..., 1]
    # print values in 2nd row
    print arr[1, ...]


if __name__ == '__main__':
    slicing()
