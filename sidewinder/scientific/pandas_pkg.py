#!/usr/bin/env python2.7
# coding=utf-8

import pandas as pd
import matplotlib.pyplot as plt


def read_file():
    # plot
    df = pd.read_csv('GOOG.csv')
    df.plot(title='Example using pandas', style='o')
    plt.show()


def functions():
    df = pd.read_csv('data_1.csv')
    print 'Print 5 rows:'
    print df.head(3)
    print ''

    print 'Print tail:'
    print df.tail(1)
    print ''

    print 'Print max value per column:'
    print df.max()
    print ''

    # drop na
    print 'Print max value per column:'
    print df.dropna()
    print ''


def merges():
    print '1st DataFrame'
    df1 = pd.DataFrame({
        'city': ['new york', 'chicago', 'orlando'],
        'temperature': [21, 14, 35]
    })
    print df1
    print ''

    print '2nd DataFrame'
    df2 = pd.DataFrame({
        'city': ['new york', 'chicago', 'orlando'],
        'humidity': [65, 68, 75]
    })
    print df2
    print ''

    # Inner merge
    print 'Inner join'
    print pd.merge(df1, df2, on='city')


if __name__ == '__main__':
    merges()


