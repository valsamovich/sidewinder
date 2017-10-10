#!/usr/bin/env python2.7
# coding=utf-8

import numpy as np
import pandas as pd


def q1():
    df = pd.DataFrame([52, 46, 50, 51], columns=['AAPL'], index=['01-01', '01-02', '01-03', '01-04'])
    df = df.join(pd.DataFrame([83, 88, 86, 90], columns=['SPY'], index=['01-01', '01-02', '01-04', '01-05']))
    print df


def q2():
    d = {"SPY": [86.80, 86.70, 87.28, 84.67, 85.01],
         "AAPL": [90.36, 94.18, 92.62, 90.62, 92.30],
         "HNZ": [33.95, 33.82, 33.38, 32.59, 31.99],
         "XOM": [74.48, 74.47, 73.26, 71.39, 85.13],
         "GLD": [86.23, 84.48, 85.13, 82.75, 84.46]}
    df = pd.DataFrame(d)
    normed = df/df.ix[0]
    normed['AAPL'] = np.nan
    normed.fillna(value='0')
    print normed[0:2]


def q3():
    array = np.ones((2,3,4))
    print array
    array = array * 2
    print array
    print array.sum(axis=None)


if __name__ == '__main__':
    q3()
