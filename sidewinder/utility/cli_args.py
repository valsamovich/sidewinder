#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--argument_x', default=True, action='store_false')
parser.add_argument('--argument_y', default=False, action='store_true')
args = parser.parse_args()

x = args.argument_x
y = args.argument_y
if not y:
    print('argument_x is {}'.format(args.argument_x))
    print('argument_y is {}'.format(args.argument_y))
