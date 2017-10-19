#!/usr/bin/env python2.7
# coding=utf-8

""" Collection of the string, date and other utilities.
"""

import datetime
import os
import subprocess


def today_date(date_format):
    """ Return today's date in YYYY-MM-DD format.
    :param date_format: Date format as String. For example '%Y-%m-%d'.
    :return:            Date as date object
    """
    return datetime.datetime.today().strftime(date_format)


def remove_file(src_file):
    """ Remove file.
    :param src_file:    Source file.
    :return:            None
    """
    os.remove(src_file)


def simple_cmd(cmd):
    """ Run simple shell command.
    :param cmd: Command
    :return:    None
    """
    subprocess.call(cmd, shell=True, stdout=subprocess.PIPE)


def simple_cmd_2(cmd):
    """ Run simple shell command.
    :param cmd: Command
    :return:    None
    """
    subprocess.call(cmd, shell=True)


def date_range(start_date, end_date):
    """ Return the list of all dates based on passed dates.
    :param start_date:  The exclusive start date to use. YYYY-MM-DD format.
    :param end_date:    The exclusive end date to use. YYYY-MM-DD format.
    :return:            List of dates.
    """
    date_list = []
    for single_date in range(int((end_date - start_date).days + 1)):
        date_list.append(start_date + datetime.timedelta(days=single_date))
    return date_list

simple_cmd_2('ls')
print
simple_cmd_2('touch tmp.txt')
print
simple_cmd_2('ls')