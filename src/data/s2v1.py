#!/usr/local/bin/python2.7

import csv

# open data fie using csv module
def open_with_csv(filename):
    # create a list
    data = []
    # open a file with utf encoding
    with open(filename, encoding='utf-8') as tsvin:
        # read line with csv reader
        tie_reader = csv.reader(tsvin, delimiter = '\t')
        # for each line in data file upend to a list
        for line in tie_reader:
            data.append(line)
    # return a list
    return data

# open file with csv
data_from_csv = open_with_csv('data.csv')
# print the header
print data_from_csv[0]