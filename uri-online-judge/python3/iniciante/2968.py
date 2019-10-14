# -*- coding: utf-8 -*-

from math import ceil

v, n = map(int, input().split())

total = v * n
print('%i %i %i %i %i %i %i %i %i' % (ceil(total * 0.1), ceil(total * 0.2), ceil(total * 0.3), ceil(total * 0.4),
      ceil(total * 0.5), ceil(total * 0.6), ceil(total * 0.7), ceil(total * 0.8), ceil(total * 0.9)))
