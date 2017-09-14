#!/usr/local/bin/python2.7

import csv
import codecs


# open data fie using csv module
def open_with_csv(input_file):
    # create a list
    data = []
    # open a file with utf encoding
    with codecs.open(input_file, 'r', 'utf-8') as utf8_file:
        # read line with csv reader
        tie_reader = csv.reader(utf8_file, delimiter='\t')
        # for each line in data file upend to a list
        for line in tie_reader:
            data.append(line)
    # return a list
    return data


# open file with csv
data_from_csv = open_with_csv('sample_data.csv')
# print the header
print data_from_csv[0]