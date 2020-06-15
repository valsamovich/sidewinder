#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import numpy

x = numpy.array([345, 457, 120, 458, 400, 300, 451, 200])

normalized = (x - min(x))/(max(x)-min(x))
print('normalized: {}'.format(normalized))

denormalized = (normalized * (max(x)-min(x))) + min(x)
print('denormalized: {}'.format(denormalized))