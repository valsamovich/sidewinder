#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import random

bars = ['COCONUT SEA SALT', 'PIKE PLACE ESPRESSO', 'WHOLE MILK']

while bars:
    print(bars)
    bar = random.choice(bars)
    print(bar)
    bars.remove(bar)
    if bars:
        input("Press Enter to pick a bar...")
    else:
        print('No more bars!')
        break