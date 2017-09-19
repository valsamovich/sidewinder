#!/usr/bin/env python2.7
# coding=utf-8

from datetime import datetime

now = datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day

if __name__ == '__main__':
    print current_year
    print current_month
    print current_day
