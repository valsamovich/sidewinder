#!/usr/bin/env python2.7
# coding=utf-8

import pandas as pd
import matplotlib.pyplot as plt


def read_file():
    """
    Read files.
    """
    # plot
    df = pd.read_csv('data.csv', index_col=0)
    df.plot(title='Example using pandas', style='o')
    plt.show()


if __name__ == '__main__':
    read_file()


