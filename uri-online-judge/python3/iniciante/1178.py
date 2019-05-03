# -*- coding: utf-8 -*-

x = float(input())

for i in range(100):
    print('N[%i] = %.4f' % (i, x))
    x = x/2
