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


if __name__ == '__main__':
    functions()


