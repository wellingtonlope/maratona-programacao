# -*- coding: utf-8 -*-

n = int(input())

[print('%i^%i = %i' % (i, 2, i**2)) for i in range(2, n + 1 if n % 2 == 0 else n, 2)]
