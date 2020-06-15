#!/usr/bin/env bash

# Executables
# Type          CMD             Location                    Version
# Mac           which python    /usr/bin/python
# IntelliJIDEA  NA              /usr/bin/python2.7          2.7
# IntelliJIDEA  NA              /usr/local/bin/python3.7    3.7
# Homebrew      which pythno2   /usr/local/bin/python2      NA
# Homebrew      which pythno2   /usr/local/bin/python3      NA
# PYTHON_HOME   NA              /usr/bin/python2.7          2.7
# https://docs.python-guide.org/starting/install/osx/

They will install into the site-package directory
  /usr/local/lib/python2.7/site-packages

Python has been installed as
  /usr/local/bin/python3
They will install into the site-package directory
  /usr/local/lib/python3.7/site-packages


# check python process on linux.
ps -elf | grep python
pgrep -lf python

# delete all python processes.
pkill -9 python

# create virtual environment
virtualenv <process-name>

# list divide on list
# coverage = [30441]
# mfc = [2173]
# [mfc[i]/ coverage[i] for i in range(len(mfc))]
# [a / b for a, b in zip(mfc, coverage)]
# [float(a) / b for a, b in zip([2173,1], [30441,10])]

# logging.
# log severity: DEBUG INFO WARNING ERROR CRITICAL
import logging
# basic configuration.
logging.basicConfig(level=logging.INFO)
# custom format.
logging.basicConfig(filename='logging.out', format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Info')




